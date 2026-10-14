#!/usr/bin/env node

/**
 * Validate the public WordPress SEO launch baseline with no third-party packages.
 * Requires Node 18+ (global fetch).
 *
 * Usage:
 *   node scripts/validate-baseline.mjs https://example.com
 *   node scripts/validate-baseline.mjs https://example.com \
 *     --expect-schema=Organization,WebSite,WebPage,Service,FAQPage \
 *     --json=.claude/evidence/norml-seo-basics/{run-id}/live-validation.json
 */

import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const STATUS_ORDER = { FAIL: 0, WARN: 1, PASS: 2 };

function usage(message = '') {
  if (message) process.stderr.write(`${message}\n\n`);
  process.stderr.write(`Usage:
  node scripts/validate-baseline.mjs <url> [options]

Options:
  --expect-schema=<types>  Comma-separated types. Use A|B for alternatives.
                           Default: Organization|Person,WebSite,WebPage
  --expect-icon-sha256=<hashes>
                           Comma-separated SHA-256 digests of approved favicon files.
  --expect-social-sha256=<hashes>
                           Comma-separated SHA-256 digests of approved social cards.
  --allow-site-icon-as-logo Permit identical Site Icon and Organization-logo bytes.
                           Use only when that dual role is explicitly approved.
  --sitemap=<path-or-url>  Canonical XML sitemap index. Default: /sitemap_index.xml
  --max-sitemaps=<number>  Child sitemap URLs to sample. Default: 20
  --timeout=<milliseconds> Per-request timeout. Default: 15000
  --json=<path>            Write the full machine-readable result.
  --help                   Show this help.
`);
}

function parseArgs(argv) {
  const options = {
    target: '',
    expectSchema: ['Organization|Person', 'WebSite', 'WebPage'],
    sitemap: '/sitemap_index.xml',
    maxSitemaps: 20,
    timeout: 15000,
    jsonPath: '',
    expectIconSha256: [],
    expectSocialSha256: [],
    allowSiteIconAsLogo: false,
  };

  for (let index = 0; index < argv.length; index += 1) {
    const argument = argv[index];

    if (argument === '--help' || argument === '-h') {
      usage();
      process.exit(0);
    }

    if (!argument.startsWith('--') && !options.target) {
      options.target = argument;
      continue;
    }

    if (argument === '--allow-site-icon-as-logo') {
      options.allowSiteIconAsLogo = true;
      continue;
    }

    const readValue = (name) => {
      if (argument.startsWith(`${name}=`)) return argument.slice(name.length + 1);
      if (argument === name && argv[index + 1] && !argv[index + 1].startsWith('--')) {
        index += 1;
        return argv[index];
      }
      return null;
    };

    let value = readValue('--expect-schema');
    if (value !== null) {
      options.expectSchema = value.split(',').map((item) => item.trim()).filter(Boolean);
      continue;
    }

    value = readValue('--sitemap');
    if (value !== null) {
      options.sitemap = value;
      continue;
    }

    value = readValue('--expect-icon-sha256');
    if (value !== null) {
      options.expectIconSha256 = value.split(',').map((item) => item.trim().toLowerCase()).filter(Boolean);
      continue;
    }

    value = readValue('--expect-social-sha256');
    if (value !== null) {
      options.expectSocialSha256 = value.split(',').map((item) => item.trim().toLowerCase()).filter(Boolean);
      continue;
    }

    value = readValue('--max-sitemaps');
    if (value !== null) {
      options.maxSitemaps = Number.parseInt(value, 10);
      continue;
    }

    value = readValue('--timeout');
    if (value !== null) {
      options.timeout = Number.parseInt(value, 10);
      continue;
    }

    value = readValue('--json');
    if (value !== null) {
      options.jsonPath = value;
      continue;
    }

    throw new Error(`Unknown or incomplete argument: ${argument}`);
  }

  if (!options.target) throw new Error('A target URL is required.');
  if (!Number.isInteger(options.timeout) || options.timeout < 1000 || options.timeout > 120000) {
    throw new Error('--timeout must be an integer between 1000 and 120000.');
  }
  if (!Number.isInteger(options.maxSitemaps) || options.maxSitemaps < 0 || options.maxSitemaps > 100) {
    throw new Error('--max-sitemaps must be an integer between 0 and 100.');
  }
  for (const digest of [...options.expectIconSha256, ...options.expectSocialSha256]) {
    if (!/^[a-f0-9]{64}$/.test(digest)) {
      throw new Error('Expected asset SHA-256 values must contain exactly 64 hexadecimal characters.');
    }
  }

  return options;
}

function normalizeInputUrl(input) {
  const withScheme = /^[a-z][a-z0-9+.-]*:\/\//i.test(input) ? input : `https://${input}`;
  const url = new URL(withScheme);
  url.hash = '';
  return url;
}

function normalizeComparable(input) {
  try {
    const url = new URL(input);
    url.hash = '';
    url.hostname = url.hostname.toLowerCase();
    if ((url.protocol === 'https:' && url.port === '443') || (url.protocol === 'http:' && url.port === '80')) {
      url.port = '';
    }
    if (url.pathname === '') url.pathname = '/';
    return url.toString();
  } catch {
    return String(input || '');
  }
}

function decodeHtml(value) {
  return String(value || '')
    .replace(/&amp;/gi, '&')
    .replace(/&quot;/gi, '"')
    .replace(/&#39;|&apos;/gi, "'")
    .replace(/&lt;/gi, '<')
    .replace(/&gt;/gi, '>')
    .replace(/&#(\d+);/g, (_, number) => String.fromCodePoint(Number(number)))
    .replace(/&#x([0-9a-f]+);/gi, (_, number) => String.fromCodePoint(Number.parseInt(number, 16)));
}

function parseAttributes(tag) {
  const attributes = {};
  const source = tag.replace(/^<\/?\s*[a-z0-9:-]+/i, '').replace(/\/?\s*>$/, '');
  const pattern = /([^\s=/>]+)(?:\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s"'=<>`]+)))?/g;
  let match;

  while ((match = pattern.exec(source)) !== null) {
    const name = match[1].toLowerCase();
    const value = match[2] ?? match[3] ?? match[4] ?? '';
    attributes[name] = decodeHtml(value);
  }

  return attributes;
}

function extractTags(html, tagName) {
  return html.match(new RegExp(`<${tagName}\\b[^>]*>`, 'gi')) || [];
}

function metasBy(metaTags, attribute, expected) {
  const needle = expected.toLowerCase();
  return metaTags
    .map(parseAttributes)
    .filter((attrs) => String(attrs[attribute] || '').toLowerCase() === needle);
}

function linksWithRel(linkTags, relation) {
  const needle = relation.toLowerCase();
  return linkTags
    .map(parseAttributes)
    .filter((attrs) => String(attrs.rel || '').toLowerCase().split(/\s+/).includes(needle));
}

function resolveUrl(value, base) {
  try {
    return new URL(decodeHtml(value), base).toString();
  } catch {
    return '';
  }
}

function isAbsoluteHttps(value) {
  try {
    return new URL(value).protocol === 'https:';
  } catch {
    return false;
  }
}

function looksLikeXml(body) {
  return /^\s*<\?xml\b/i.test(body) || /<(sitemapindex|urlset)\b/i.test(body);
}

function extractLocs(xml) {
  return [...xml.matchAll(/<loc\b[^>]*>([\s\S]*?)<\/loc>/gi)]
    .map((match) => decodeHtml(match[1].trim()))
    .filter(Boolean);
}

function sha256(body) {
  return crypto.createHash('sha256').update(body).digest('hex');
}

function imageDimensions(body, contentType = '') {
  if (!Buffer.isBuffer(body) || body.length < 10) return null;

  if (body.length >= 24 && body.subarray(0, 8).equals(Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]))) {
    return { width: body.readUInt32BE(16), height: body.readUInt32BE(20) };
  }

  if (body.subarray(0, 3).toString('ascii') === 'GIF' && body.length >= 10) {
    return { width: body.readUInt16LE(6), height: body.readUInt16LE(8) };
  }

  if (body[0] === 0xff && body[1] === 0xd8) {
    let offset = 2;
    const startOfFrame = new Set([0xc0, 0xc1, 0xc2, 0xc3, 0xc5, 0xc6, 0xc7, 0xc9, 0xca, 0xcb, 0xcd, 0xce, 0xcf]);
    while (offset + 8 < body.length) {
      if (body[offset] !== 0xff) {
        offset += 1;
        continue;
      }
      const marker = body[offset + 1];
      if (marker === 0xd8 || marker === 0xd9 || marker === 0x01 || (marker >= 0xd0 && marker <= 0xd7)) {
        offset += 2;
        continue;
      }
      if (offset + 4 > body.length) break;
      const segmentLength = body.readUInt16BE(offset + 2);
      if (segmentLength < 2 || offset + 2 + segmentLength > body.length) break;
      if (startOfFrame.has(marker) && segmentLength >= 7) {
        return { width: body.readUInt16BE(offset + 7), height: body.readUInt16BE(offset + 5) };
      }
      offset += 2 + segmentLength;
    }
  }

  if (body[0] === 0x00 && body[1] === 0x00 && body[2] === 0x01 && body[3] === 0x00 && body.length >= 8) {
    return { width: body[6] || 256, height: body[7] || 256 };
  }

  if (/image\/svg\+xml/i.test(contentType)) {
    const source = body.toString('utf8', 0, Math.min(body.length, 32768));
    const viewBox = source.match(/\bviewBox\s*=\s*["']\s*[-\d.]+[ ,]+[-\d.]+[ ,]+([\d.]+)[ ,]+([\d.]+)\s*["']/i);
    if (viewBox) return { width: Number(viewBox[1]), height: Number(viewBox[2]) };
    const width = source.match(/\bwidth\s*=\s*["']([\d.]+)/i);
    const height = source.match(/\bheight\s*=\s*["']([\d.]+)/i);
    if (width && height) return { width: Number(width[1]), height: Number(height[1]) };
  }

  return null;
}

async function fetchResource(url, { timeout, binary = false, redirect = 'follow' }) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeout);

  try {
    const response = await fetch(url, {
      redirect,
      signal: controller.signal,
      headers: {
        'user-agent': 'Norml-seo-basics/2.1 (+wordpress-baseline-validator)',
        accept: binary ? '*/*' : 'text/html,application/xhtml+xml,application/xml,text/plain,*/*;q=0.8',
      },
    });

    const body = binary
      ? Buffer.from(await response.arrayBuffer())
      : await response.text();

    return {
      ok: response.ok,
      status: response.status,
      url: response.url || url,
      headers: Object.fromEntries(response.headers.entries()),
      body,
      error: '',
    };
  } catch (error) {
    return {
      ok: false,
      status: 0,
      url,
      headers: {},
      body: binary ? Buffer.alloc(0) : '',
      error: error instanceof Error ? error.message : String(error),
    };
  } finally {
    clearTimeout(timer);
  }
}

function collectSchema(value, state) {
  if (Array.isArray(value)) {
    value.forEach((item) => collectSchema(item, state));
    return;
  }

  if (!value || typeof value !== 'object') return;

  const rawTypes = value['@type'] ?? [];
  const types = Array.isArray(rawTypes) ? rawTypes : [rawTypes];
  const normalizedTypes = types.filter((type) => typeof type === 'string' && type !== '');

  if (normalizedTypes.length > 0) {
    normalizedTypes.forEach((type) => state.types.add(type));
    state.definitions.push({
      types: normalizedTypes,
      id: typeof value['@id'] === 'string' ? value['@id'] : '',
      value,
    });
  }

  Object.values(value).forEach((child) => collectSchema(child, state));
}

function createRecorder() {
  const results = [];
  const record = (id, status, label, actual, expected = '') => {
    results.push({ id, status, label, actual: String(actual ?? ''), expected: String(expected ?? '') });
  };
  return { results, record };
}

function countSummary(results) {
  return results.reduce((summary, result) => {
    summary[result.status] += 1;
    return summary;
  }, { PASS: 0, WARN: 0, FAIL: 0 });
}

function printResults(report) {
  const icons = { PASS: 'PASS', WARN: 'WARN', FAIL: 'FAIL' };
  process.stdout.write(`SEO basics — WordPress profile: ${report.target}\n`);
  process.stdout.write(`Final URL: ${report.final_url || 'unavailable'}\n\n`);

  for (const result of report.results) {
    process.stdout.write(`[${icons[result.status]}] ${result.id} ${result.label}\n`);
    if (result.actual) process.stdout.write(`       actual: ${result.actual}\n`);
    if (result.expected && result.status !== 'PASS') process.stdout.write(`       expect: ${result.expected}\n`);
  }

  process.stdout.write(`\nSummary: PASS=${report.summary.PASS} WARN=${report.summary.WARN} FAIL=${report.summary.FAIL}\n`);
  process.stdout.write(`Result: ${report.result}\n`);
}

let options;
try {
  options = parseArgs(process.argv.slice(2));
} catch (error) {
  usage(error instanceof Error ? error.message : String(error));
  process.exit(2);
}

if (typeof fetch !== 'function') {
  process.stderr.write('This validator requires Node 18+ with global fetch.\n');
  process.exit(2);
}

const targetUrl = normalizeInputUrl(options.target);
const { results, record } = createRecorder();
const page = await fetchResource(targetUrl.toString(), { timeout: options.timeout });
const finalUrl = page.url || targetUrl.toString();
const finalOrigin = (() => {
  try {
    return new URL(finalUrl).origin;
  } catch {
    return targetUrl.origin;
  }
})();

record(
  'http.homepage',
  page.ok && page.status >= 200 && page.status < 300 ? 'PASS' : 'FAIL',
  'Homepage returns successful HTTP',
  page.error || `${page.status} ${page.headers['content-type'] || 'no content-type'}`,
  '2xx HTML response'
);

record(
  'http.https',
  (() => { try { return new URL(finalUrl).protocol === 'https:' ? 'PASS' : 'FAIL'; } catch { return 'FAIL'; } })(),
  'Final URL uses HTTPS',
  finalUrl,
  'https://...'
);

const contentType = page.headers['content-type'] || '';
record(
  'http.content_type',
  /text\/html|application\/xhtml\+xml/i.test(contentType) ? 'PASS' : 'FAIL',
  'Homepage is HTML',
  contentType || 'missing',
  'text/html or application/xhtml+xml'
);

const xRobots = page.headers['x-robots-tag'] || '';
record(
  'http.x_robots',
  /noindex/i.test(xRobots) ? 'FAIL' : 'PASS',
  'HTTP robots header permits indexing',
  xRobots || 'not set',
  'No noindex directive'
);

const html = typeof page.body === 'string' ? page.body : '';
const metaTags = extractTags(html, 'meta');
const linkTags = extractTags(html, 'link');

const titleMatches = [...html.matchAll(/<title\b[^>]*>([\s\S]*?)<\/title>/gi)];
const titles = titleMatches.map((match) => decodeHtml(match[1].replace(/<[^>]+>/g, '').trim()));
record(
  'head.title_count',
  titles.length === 1 && titles[0] !== '' ? 'PASS' : 'FAIL',
  'Exactly one non-empty title',
  `${titles.length} — ${titles.join(' | ') || 'empty'}`,
  '1 non-empty <title>'
);
if (titles.length === 1 && titles[0] !== '') {
  record(
    'head.title_length',
    titles[0].length >= 30 && titles[0].length <= 60 ? 'PASS' : 'WARN',
    'Title length is SERP-readable',
    `${titles[0].length} characters`,
    'Approximately 30–60 characters; intentional exceptions allowed'
  );
}

const descriptions = metasBy(metaTags, 'name', 'description');
record(
  'head.description_count',
  descriptions.length === 1 && String(descriptions[0]?.content || '').trim() !== '' ? 'PASS' : 'FAIL',
  'Exactly one non-empty meta description',
  `${descriptions.length} — ${descriptions.map((item) => item.content || '').join(' | ') || 'empty'}`,
  '1 non-empty description'
);
if (descriptions.length === 1 && descriptions[0].content) {
  record(
    'head.description_length',
    descriptions[0].content.length >= 120 && descriptions[0].content.length <= 165 ? 'PASS' : 'WARN',
    'Description length is SERP-readable',
    `${descriptions[0].content.length} characters`,
    'Approximately 120–165 characters; intentional exceptions allowed'
  );
}

const robotsMetas = metasBy(metaTags, 'name', 'robots');
const robotsContent = robotsMetas.map((item) => item.content || '').join(' | ');
record(
  'head.robots_count',
  robotsMetas.length === 1 ? 'PASS' : 'FAIL',
  'Exactly one robots meta',
  `${robotsMetas.length} — ${robotsContent || 'empty'}`,
  '1 robots meta'
);
record(
  'head.robots_indexable',
  robotsMetas.length === 1 && !/\b(noindex|nofollow)\b/i.test(robotsContent) ? 'PASS' : 'FAIL',
  'Robots meta permits homepage indexing',
  robotsContent || 'missing',
  'No noindex or nofollow'
);

const canonicals = linksWithRel(linkTags, 'canonical');
const canonicalUrls = canonicals.map((item) => resolveUrl(item.href || '', finalUrl)).filter(Boolean);
record(
  'head.canonical_count',
  canonicals.length === 1 && canonicalUrls.length === 1 ? 'PASS' : 'FAIL',
  'Exactly one valid canonical',
  `${canonicals.length} — ${canonicalUrls.join(' | ') || 'invalid/missing'}`,
  '1 absolute canonical URL'
);
if (canonicalUrls.length === 1) {
  record(
    'head.canonical_self',
    normalizeComparable(canonicalUrls[0]) === normalizeComparable(finalUrl) && isAbsoluteHttps(canonicalUrls[0]) ? 'PASS' : 'FAIL',
    'Canonical matches final HTTPS page URL',
    canonicalUrls[0],
    normalizeComparable(finalUrl)
  );
}

const h1Count = (html.match(/<h1\b[^>]*>/gi) || []).length;
record('html.h1_count', h1Count === 1 ? 'PASS' : 'FAIL', 'Exactly one homepage H1 in HTML', h1Count, '1');

const htmlTag = (html.match(/<html\b[^>]*>/i) || [])[0] || '';
const htmlAttributes = htmlTag ? parseAttributes(htmlTag) : {};
record(
  'html.language',
  /^[a-z]{2,3}(?:-[a-z0-9]{2,8})*$/i.test(htmlAttributes.lang || '') ? 'PASS' : 'FAIL',
  'HTML language is declared',
  htmlAttributes.lang || 'missing',
  'Valid BCP 47-like lang value'
);

const viewports = metasBy(metaTags, 'name', 'viewport');
record(
  'head.viewport',
  viewports.length === 1 && /width\s*=\s*device-width/i.test(viewports[0].content || '') ? 'PASS' : 'FAIL',
  'One responsive viewport meta',
  `${viewports.length} — ${viewports.map((item) => item.content || '').join(' | ') || 'missing'}`,
  '1 viewport containing width=device-width'
);

const socialRequirements = [
  ['og:type', 'property'],
  ['og:site_name', 'property'],
  ['og:title', 'property'],
  ['og:description', 'property'],
  ['og:url', 'property'],
  ['og:image', 'property'],
  ['og:image:width', 'property'],
  ['og:image:height', 'property'],
  ['og:image:type', 'property'],
  ['og:image:alt', 'property'],
  ['twitter:card', 'name'],
  ['twitter:title', 'name'],
  ['twitter:description', 'name'],
  ['twitter:image', 'name'],
];
const socialValues = {};

for (const [key, attribute] of socialRequirements) {
  const matches = metasBy(metaTags, attribute, key);
  const values = matches.map((item) => item.content || '').filter(Boolean);
  socialValues[key] = values[0] || '';
  record(
    `social.${key.replace(':', '_')}`,
    matches.length === 1 && values.length === 1 ? 'PASS' : 'FAIL',
    `Exactly one ${key}`,
    `${matches.length} — ${values.join(' | ') || 'empty'}`,
    `1 non-empty ${key}`
  );
}

if (socialValues['og:url']) {
  const resolvedOgUrl = resolveUrl(socialValues['og:url'], finalUrl);
  record(
    'social.og_url_canonical',
    normalizeComparable(resolvedOgUrl) === normalizeComparable(finalUrl) ? 'PASS' : 'FAIL',
    'Open Graph URL matches canonical page',
    resolvedOgUrl || socialValues['og:url'],
    normalizeComparable(finalUrl)
  );
}

record(
  'social.twitter_card_type',
  socialValues['twitter:card'] === 'summary_large_image' ? 'PASS' : 'WARN',
  'Twitter card uses a large image',
  socialValues['twitter:card'] || 'missing',
  'summary_large_image unless intentionally different'
);

const verifyImage = async (id, label, rawUrl) => {
  const url = resolveUrl(rawUrl, finalUrl);
  if (!url) {
    record(id, 'FAIL', label, rawUrl || 'missing/invalid', 'Absolute or resolvable image URL');
    return null;
  }
  const response = await fetchResource(url, { timeout: options.timeout, binary: true });
  const type = response.headers['content-type'] || '';
  record(
    id,
    response.ok && /^image\//i.test(type) && response.body.length > 0 ? 'PASS' : 'FAIL',
    label,
    `${response.status} ${type || 'no content-type'} ${response.body.length} bytes — ${response.url}`,
    '2xx non-empty image/* response'
  );
  return response;
};

const openGraphImage = await verifyImage(
  'social.og_image_response',
  'Open Graph image resolves as an image',
  socialValues['og:image']
);
let twitterImage = openGraphImage;
if (socialValues['twitter:image'] && socialValues['twitter:image'] !== socialValues['og:image']) {
  twitterImage = await verifyImage(
    'social.twitter_image_response',
    'Twitter image resolves as an image',
    socialValues['twitter:image']
  );
} else {
  record(
    'social.twitter_image_response',
    socialValues['twitter:image'] ? 'PASS' : 'FAIL',
    'Twitter image resolves as an image',
    socialValues['twitter:image'] ? 'Same URL as verified Open Graph image' : 'missing',
    'Verified image URL'
  );
}

const openGraphDimensions = openGraphImage
  ? imageDimensions(openGraphImage.body, openGraphImage.headers['content-type'] || '')
  : null;
const declaredSocialDimensions = {
  width: Number.parseInt(socialValues['og:image:width'], 10),
  height: Number.parseInt(socialValues['og:image:height'], 10),
};
record(
  'social.og_image_dimensions',
  openGraphDimensions
    && openGraphDimensions.width === 1200
    && openGraphDimensions.height === 630
    && declaredSocialDimensions.width === openGraphDimensions.width
    && declaredSocialDimensions.height === openGraphDimensions.height ? 'PASS' : 'FAIL',
  'Open Graph image is the declared 1200x630 social card',
  openGraphDimensions
    ? `actual=${openGraphDimensions.width}x${openGraphDimensions.height} declared=${declaredSocialDimensions.width || '?'}x${declaredSocialDimensions.height || '?'}`
    : 'dimensions unavailable',
  'actual=1200x630 and declarations match'
);

const socialDigest = openGraphImage ? sha256(openGraphImage.body) : '';
record(
  'social.approved_digest',
  options.expectSocialSha256.length === 0
    ? 'WARN'
    : options.expectSocialSha256.includes(socialDigest) ? 'PASS' : 'FAIL',
  'Social card matches an approved source digest',
  socialDigest || 'unavailable',
  options.expectSocialSha256.join(', ') || 'Pass --expect-social-sha256 during a fix run'
);

if (twitterImage && openGraphImage && socialValues['twitter:image'] !== socialValues['og:image']) {
  record(
    'social.twitter_image_dimensions',
    (() => {
      const dimensions = imageDimensions(twitterImage.body, twitterImage.headers['content-type'] || '');
      return dimensions && dimensions.width === 1200 && dimensions.height === 630 ? 'PASS' : 'FAIL';
    })(),
    'Distinct Twitter image is 1200x630',
    (() => {
      const dimensions = imageDimensions(twitterImage.body, twitterImage.headers['content-type'] || '');
      return dimensions ? `${dimensions.width}x${dimensions.height}` : 'dimensions unavailable';
    })(),
    '1200x630'
  );
}

const iconLinks = linksWithRel(linkTags, 'icon');
const appleLinks = linksWithRel(linkTags, 'apple-touch-icon');
const manifestLinks = linksWithRel(linkTags, 'manifest');
record('icons.icon_links', iconLinks.length >= 1 ? 'PASS' : 'FAIL', 'At least one favicon link exists', iconLinks.length, '>= 1');
record(
  'icons.legacy_ico',
  iconLinks.some((item) => /\.ico(?:$|[?#])/i.test(item.href || '') || /x-icon|vnd\.microsoft\.icon/i.test(item.type || '')) ? 'PASS' : 'FAIL',
  'Legacy ICO favicon is linked',
  iconLinks.map((item) => item.href || '').filter(Boolean).join(' | ') || 'none',
  'An .ico or image/x-icon link'
);
record('icons.apple_touch', appleLinks.length >= 1 ? 'PASS' : 'FAIL', 'Apple touch icon is linked', appleLinks.length, '>= 1');
record('icons.manifest_count', manifestLinks.length === 1 ? 'PASS' : 'FAIL', 'Exactly one web manifest is linked', manifestLinks.length, '1');

const uniqueIconUrls = [...new Set([...iconLinks, ...appleLinks]
  .map((item) => resolveUrl(item.href || '', finalUrl))
  .filter(Boolean))];
let brokenIconAssets = 0;
const iconEvidence = [];
const iconDigests = [];
for (const iconUrl of uniqueIconUrls.slice(0, 12)) {
  const response = await fetchResource(iconUrl, { timeout: options.timeout, binary: true });
  const type = response.headers['content-type'] || '';
  const good = response.ok && /^image\//i.test(type) && response.body.length > 0;
  if (!good) brokenIconAssets += 1;
  const digest = good ? sha256(response.body) : '';
  const dimensions = good ? imageDimensions(response.body, type) : null;
  if (digest) iconDigests.push(digest);
  iconEvidence.push(
    `${response.status}/${type || 'no-type'} ${dimensions ? `${dimensions.width}x${dimensions.height}` : '?x?'} sha256=${digest || 'n/a'} ${response.url}`
  );
}

const rootFaviconUrl = new URL('/favicon.ico', `${finalOrigin}/`).toString();
const rootFavicon = await fetchResource(rootFaviconUrl, { timeout: options.timeout, binary: true });
const rootFaviconType = rootFavicon.headers['content-type'] || '';
const rootFaviconDigest = rootFavicon.ok && /^image\//i.test(rootFaviconType) && rootFavicon.body.length > 0
  ? sha256(rootFavicon.body)
  : '';
const rootFaviconApproved = options.expectIconSha256.length === 0
  || options.expectIconSha256.includes(rootFaviconDigest);
if (rootFaviconDigest) iconDigests.push(rootFaviconDigest);
record(
  'icons.root_ico',
  rootFaviconDigest && rootFaviconApproved ? 'PASS' : 'FAIL',
  'Conventional root favicon returns approved image bytes',
  `${rootFavicon.status} ${rootFaviconType || 'no content-type'} ${rootFavicon.body.length} bytes sha256=${rootFaviconDigest || 'n/a'} — ${rootFavicon.url}`,
  options.expectIconSha256.length > 0
    ? '2xx non-empty image/* response matching an approved favicon SHA-256'
    : '2xx non-empty image/* response (pass --expect-icon-sha256 during a fix run)'
);
record(
  'icons.asset_responses',
  uniqueIconUrls.length > 0 && brokenIconAssets === 0 ? 'PASS' : 'FAIL',
  'Linked favicon/touch assets resolve as images',
  iconEvidence.join(' | ') || 'no resolvable icon URLs',
  'All sampled icon URLs return non-empty image/* responses'
);

const wordpressDefaultIconUrls = uniqueIconUrls.filter(
  (url) => /\/(?:wp-admin|wp-includes)\/images\/(?:wordpress-logo|w-logo-blue-white-bg)/i.test(url)
);
record(
  'icons.no_wordpress_default_url',
  wordpressDefaultIconUrls.length === 0 ? 'PASS' : 'FAIL',
  'Favicon URLs do not point at WordPress default artwork',
  wordpressDefaultIconUrls.join(' | ') || 'none',
  'No WordPress core logo URL'
);

const matchingIconDigest = iconDigests.find((digest) => options.expectIconSha256.includes(digest)) || '';
record(
  'icons.approved_digest',
  options.expectIconSha256.length === 0 ? 'WARN' : matchingIconDigest ? 'PASS' : 'FAIL',
  'At least one live favicon matches an approved source digest',
  matchingIconDigest || iconDigests.join(', ') || 'unavailable',
  options.expectIconSha256.join(', ') || 'Pass --expect-icon-sha256 during a fix run'
);

let manifestJson = null;
let manifestUrl = '';
const manifestIconDigests = [];
if (manifestLinks.length === 1) {
  manifestUrl = resolveUrl(manifestLinks[0].href || '', finalUrl);
  const manifestResponse = manifestUrl
    ? await fetchResource(manifestUrl, { timeout: options.timeout })
    : { ok: false, status: 0, headers: {}, body: '', url: manifestUrl, error: 'invalid URL' };
  try {
    manifestJson = JSON.parse(manifestResponse.body);
  } catch {
    manifestJson = null;
  }
  record(
    'icons.manifest_response',
    manifestResponse.ok && manifestJson ? 'PASS' : 'FAIL',
    'Manifest resolves and parses as JSON',
    `${manifestResponse.status} ${manifestResponse.headers['content-type'] || 'no content-type'} — ${manifestResponse.error || manifestResponse.url}`,
    '2xx parseable JSON'
  );
}

if (manifestJson) {
  const manifestIcons = Array.isArray(manifestJson.icons) ? manifestJson.icons : [];
  const has192 = manifestIcons.some((icon) => String(icon.sizes || '').split(/\s+/).includes('192x192'));
  const has512 = manifestIcons.some((icon) => String(icon.sizes || '').split(/\s+/).includes('512x512'));
  record(
    'icons.manifest_identity',
    manifestJson.name && manifestJson.short_name ? 'PASS' : 'FAIL',
    'Manifest has name and short_name',
    `name=${manifestJson.name || 'missing'} short_name=${manifestJson.short_name || 'missing'}`,
    'Both values present'
  );
  record(
    'icons.manifest_sizes',
    has192 && has512 ? 'PASS' : 'FAIL',
    'Manifest declares 192x192 and 512x512 icons',
    manifestIcons.map((icon) => `${icon.sizes || '?'} ${icon.src || '?'}`).join(' | ') || 'none',
    '192x192 and 512x512'
  );

  let badManifestIcons = 0;
  const manifestIconEvidence = [];
  for (const icon of manifestIcons) {
    const iconUrl = resolveUrl(icon.src || '', manifestUrl);
    if (!iconUrl) {
      badManifestIcons += 1;
      manifestIconEvidence.push(`invalid ${icon.src || 'missing'}`);
      continue;
    }
    const response = await fetchResource(iconUrl, { timeout: options.timeout, binary: true });
    const type = response.headers['content-type'] || '';
    const good = response.ok && /^image\//i.test(type) && response.body.length > 0;
    if (!good) badManifestIcons += 1;
    const digest = good ? sha256(response.body) : '';
    if (digest) manifestIconDigests.push(digest);
    manifestIconEvidence.push(
      `${icon.sizes || '?'} ${response.status}/${type || 'no-type'} sha256=${digest || 'n/a'} ${response.url}`
    );
  }
  record(
    'icons.manifest_icon_responses',
    manifestIcons.length >= 2 && badManifestIcons === 0 ? 'PASS' : 'FAIL',
    'Manifest icon URLs resolve as images',
    manifestIconEvidence.join(' | ') || 'none',
    'All declared icons return non-empty image/* responses'
  );
}

const schemaScripts = [...html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)]
  .map((match) => ({ attributes: parseAttributes(`<script ${match[1]}>`), body: match[2].trim() }))
  .filter((script) => String(script.attributes.type || '').toLowerCase() === 'application/ld+json');

const schemaState = { types: new Set(), definitions: [], parseErrors: [] };
for (const [index, script] of schemaScripts.entries()) {
  try {
    const parsed = JSON.parse(script.body);
    collectSchema(parsed, schemaState);
  } catch (error) {
    schemaState.parseErrors.push(`block ${index + 1}: ${error instanceof Error ? error.message : String(error)}`);
  }
}

record(
  'schema.blocks',
  schemaScripts.length >= 1 ? 'PASS' : 'FAIL',
  'At least one JSON-LD block exists',
  schemaScripts.length,
  '>= 1'
);
record(
  'schema.parse',
  schemaScripts.length >= 1 && schemaState.parseErrors.length === 0 ? 'PASS' : 'FAIL',
  'Every JSON-LD block parses',
  schemaState.parseErrors.join(' | ') || `${schemaScripts.length} valid block(s)`,
  '0 parse errors'
);

for (const expectedGroup of options.expectSchema) {
  const alternatives = expectedGroup.split('|').map((item) => item.trim()).filter(Boolean);
  const found = alternatives.find((type) => schemaState.types.has(type));
  record(
    `schema.type_${expectedGroup.replace(/[^a-z0-9]+/gi, '_').toLowerCase()}`,
    found ? 'PASS' : 'FAIL',
    `Expected schema type ${expectedGroup}`,
    found || `available: ${[...schemaState.types].sort().join(', ') || 'none'}`,
    alternatives.join(' or ')
  );
}

const idCounts = new Map();
const invalidDefinitionIds = [];
for (const definition of schemaState.definitions) {
  if (!definition.id) {
    if (definition.types.some((type) => ['Organization', 'Person', 'WebSite', 'WebPage'].includes(type))) {
      invalidDefinitionIds.push(`${definition.types.join('+')}: missing @id`);
    }
    continue;
  }
  idCounts.set(definition.id, (idCounts.get(definition.id) || 0) + 1);
  if (!/^https:\/\//i.test(definition.id)) {
    invalidDefinitionIds.push(`${definition.types.join('+')}: ${definition.id}`);
  }
}
const duplicateIds = [...idCounts.entries()].filter(([, count]) => count > 1);
record(
  'schema.definition_ids',
  invalidDefinitionIds.length === 0 ? 'PASS' : 'FAIL',
  'Base schema definitions use absolute HTTPS @id values',
  invalidDefinitionIds.join(' | ') || `${idCounts.size} stable definition ID(s)`,
  'No missing/relative/non-HTTPS base IDs'
);
record(
  'schema.duplicate_ids',
  duplicateIds.length === 0 ? 'PASS' : 'FAIL',
  'Schema definitions have no duplicate @id values',
  duplicateIds.map(([id, count]) => `${id} ×${count}`).join(' | ') || 'none',
  '0 duplicate definition IDs'
);

const definitionsById = new Map(
  schemaState.definitions
    .filter((definition) => definition.id)
    .map((definition) => [definition.id, definition.value])
);

const collectSchemaAssetUrls = (value, urls = new Set(), visitedIds = new Set()) => {
  if (typeof value === 'string') {
    try {
      const url = new URL(value);
      if (url.protocol === 'http:' || url.protocol === 'https:') urls.add(url.toString());
    } catch {
      // A schema label or unresolved fragment is not an asset URL.
    }
    return urls;
  }

  if (Array.isArray(value)) {
    value.forEach((item) => collectSchemaAssetUrls(item, urls, visitedIds));
    return urls;
  }

  if (!value || typeof value !== 'object') return urls;

  const referenceId = typeof value['@id'] === 'string' ? value['@id'] : '';
  if (referenceId && definitionsById.has(referenceId) && !visitedIds.has(referenceId)) {
    visitedIds.add(referenceId);
    collectSchemaAssetUrls(definitionsById.get(referenceId), urls, visitedIds);
  }

  for (const [key, child] of Object.entries(value)) {
    if (key === '@id') continue;
    collectSchemaAssetUrls(child, urls, visitedIds);
  }

  return urls;
};

const organizationLogoUrls = new Set();
for (const definition of schemaState.definitions) {
  if (!definition.types.includes('Organization') || !Object.hasOwn(definition.value, 'logo')) continue;
  collectSchemaAssetUrls(definition.value.logo, organizationLogoUrls);
}

const iconRoleDigests = new Set([...iconDigests, ...manifestIconDigests]);
const organizationLogoEvidence = [];
const reusedIconLogoUrls = [];
let brokenOrganizationLogos = 0;
for (const logoUrl of organizationLogoUrls) {
  const response = await fetchResource(logoUrl, { timeout: options.timeout, binary: true });
  const type = response.headers['content-type'] || '';
  const good = response.ok && /^image\//i.test(type) && response.body.length > 0;
  const digest = good ? sha256(response.body) : '';
  if (!good) brokenOrganizationLogos += 1;
  if (digest && iconRoleDigests.has(digest)) reusedIconLogoUrls.push(response.url);
  organizationLogoEvidence.push(
    `${response.status}/${type || 'no-type'} sha256=${digest || 'n/a'} ${response.url}`
  );
}

const organizationLogoStatus = organizationLogoUrls.size === 0
  ? 'PASS'
  : brokenOrganizationLogos > 0
    ? 'FAIL'
    : reusedIconLogoUrls.length > 0 && !options.allowSiteIconAsLogo
      ? 'FAIL'
      : 'PASS';
record(
  'schema.organization_logo_role',
  organizationLogoStatus,
  'Organization logo is valid and distinct from Site Icon artwork by default',
  organizationLogoUrls.size === 0
    ? 'No Organization logo declared'
    : `${organizationLogoEvidence.join(' | ')}${reusedIconLogoUrls.length > 0 ? ' — matches Site Icon bytes' : ' — distinct bytes'}`,
  'No logo, a distinct approved logo, or --allow-site-icon-as-logo with documented dual-role approval'
);

let canonicalSitemapUrl;
try {
  canonicalSitemapUrl = new URL(options.sitemap, `${finalOrigin}/`).toString();
} catch {
  canonicalSitemapUrl = '';
}

const sitemap = canonicalSitemapUrl
  ? await fetchResource(canonicalSitemapUrl, { timeout: options.timeout })
  : { ok: false, status: 0, body: '', headers: {}, url: '', error: 'invalid sitemap URL' };
const sitemapLocs = typeof sitemap.body === 'string' ? extractLocs(sitemap.body) : [];
record(
  'sitemap.index',
  sitemap.ok && looksLikeXml(sitemap.body) && /<sitemapindex\b/i.test(sitemap.body) && sitemapLocs.length > 0 ? 'PASS' : 'FAIL',
  'Canonical sitemap index returns valid sitemap-index XML',
  `${sitemap.status} ${sitemap.headers['content-type'] || 'no content-type'} locs=${sitemapLocs.length} — ${sitemap.error || sitemap.url}`,
  '2xx <sitemapindex> XML with at least one <loc>'
);

let failedChildSitemaps = 0;
const sampledSitemaps = [];
for (const childUrl of sitemapLocs.slice(0, options.maxSitemaps)) {
  const child = await fetchResource(childUrl, { timeout: options.timeout });
  const good = child.ok && looksLikeXml(child.body);
  if (!good) failedChildSitemaps += 1;
  sampledSitemaps.push(`${child.status}/${child.headers['content-type'] || 'no-type'} ${child.url}`);
}
record(
  'sitemap.children',
  sitemapLocs.length > 0 && failedChildSitemaps === 0 ? 'PASS' : 'FAIL',
  'Sampled child sitemaps return XML',
  sampledSitemaps.join(' | ') || 'no child sitemap sampled',
  `0 failures among up to ${options.maxSitemaps} child maps`
);

const coreSitemapUrl = new URL('/wp-sitemap.xml', `${finalOrigin}/`).toString();
if (normalizeComparable(coreSitemapUrl) === normalizeComparable(canonicalSitemapUrl)) {
  record('sitemap.core_duplicate', 'PASS', 'WordPress core sitemap ownership is intentional', coreSitemapUrl, 'Canonical sitemap');
} else {
  const coreSitemap = await fetchResource(coreSitemapUrl, { timeout: options.timeout });
  const redirectedToCanonical = normalizeComparable(coreSitemap.url) === normalizeComparable(canonicalSitemapUrl);
  const independentlyActive = coreSitemap.ok && looksLikeXml(coreSitemap.body) && !redirectedToCanonical;
  record(
    'sitemap.core_duplicate',
    independentlyActive ? 'FAIL' : 'PASS',
    'WordPress core sitemap is not a second independent index',
    `${coreSitemap.status} final=${coreSitemap.url} xml=${looksLikeXml(coreSitemap.body)}`,
    'Disabled/404/410 or redirected to canonical sitemap'
  );
}

const robotsUrl = new URL('/robots.txt', `${finalOrigin}/`).toString();
const robots = await fetchResource(robotsUrl, { timeout: options.timeout });
const robotsBody = typeof robots.body === 'string' ? robots.body : '';
record(
  'robots.response',
  robots.ok && robotsBody.trim() !== '' ? 'PASS' : 'FAIL',
  'robots.txt returns non-empty text',
  `${robots.status} ${robots.headers['content-type'] || 'no content-type'} — ${robots.error || robots.url}`,
  '2xx non-empty response'
);

const blanketDisallow = /(?:^|\n)\s*user-agent\s*:\s*\*\s*(?:\r?\n)+\s*disallow\s*:\s*\/\s*(?:\r?\n|$)/i.test(robotsBody);
record(
  'robots.public_access',
  !blanketDisallow ? 'PASS' : 'FAIL',
  'robots.txt does not blanket-disallow the public site',
  blanketDisallow ? 'User-agent: * with Disallow: /' : 'no blanket disallow',
  'No public Disallow: /'
);

const robotSitemaps = robotsBody
  .split(/\r?\n/)
  .map((line) => line.match(/^\s*sitemap\s*:\s*(\S+)\s*$/i)?.[1] || '')
  .filter(Boolean);
const canonicalRobotMatch = robotSitemaps.some(
  (url) => normalizeComparable(url) === normalizeComparable(canonicalSitemapUrl)
);
record(
  'robots.sitemap_pointer',
  canonicalRobotMatch && robotSitemaps.length === 1 ? 'PASS' : 'FAIL',
  'robots.txt has one canonical sitemap pointer',
  robotSitemaps.join(' | ') || 'none',
  canonicalSitemapUrl
);

const summary = countSummary(results);
const report = {
  skill: 'norml-seo-basics@1.0.0',
  checked_at: new Date().toISOString(),
  target: targetUrl.toString(),
  final_url: finalUrl,
  canonical_sitemap: canonicalSitemapUrl,
  expected_schema: options.expectSchema,
  site_icon_as_logo_allowed: options.allowSiteIconAsLogo,
  result: summary.FAIL === 0 ? 'PASS' : 'FAIL',
  summary,
  results: results.sort((a, b) => {
    const statusDelta = STATUS_ORDER[a.status] - STATUS_ORDER[b.status];
    return statusDelta === 0 ? a.id.localeCompare(b.id) : statusDelta;
  }),
};

if (options.jsonPath) {
  const outputPath = path.resolve(options.jsonPath);
  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  fs.writeFileSync(outputPath, `${JSON.stringify(report, null, 2)}\n`, 'utf8');
}

printResults(report);
process.exitCode = summary.FAIL === 0 ? 0 : 1;
