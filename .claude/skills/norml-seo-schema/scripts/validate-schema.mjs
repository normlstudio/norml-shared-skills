#!/usr/bin/env node
/** Local advisory JSON-LD checks. Node 20+, no npm deps. Not a full schema/RRT validator. */
import { readFile } from 'node:fs/promises';
const args = process.argv.slice(2), flags = { json: false, type: null }, targets = [];
for (let i = 0; i < args.length; i++) {
  if (args[i] === '--json') flags.json = true;
  else if (args[i] === '--type') flags.type = args[++i];
  else if (args[i].startsWith('--')) { console.error('Unknown flag'); process.exit(2); }
  else targets.push(args[i]);
}
if (targets.length !== 1 || flags.type === undefined) {
  console.error('Usage: node validate-schema.mjs [--json] [--type Product] <URL or HTML file>');
  process.exit(2);
}
const report = { target: targets[0], block_count: 0, validations: [],
  summary: { errors: 0, warnings: 0, info: 0 },
  scope: 'Local advisory checks; visible parity, complete vocabulary and Google eligibility require separate review.' };
function finding(level, message, node = null) {
  report.validations.push({ level, type: node?.['@type'] ?? null, id: node?.['@id'] ?? null, message });
  report.summary[level]++;
}
let html;
try {
  if (/^https?:\/\//.test(targets[0])) {
    const response = await fetch(targets[0], { redirect: 'follow', signal: AbortSignal.timeout(30000),
      headers: { 'user-agent': 'norml-seo-schema/1.0' } });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    html = await response.text();
  } else html = await readFile(targets[0], 'utf8');
} catch (error) { console.error(`Input unavailable: ${error.message}`); process.exit(2); }
const nodes = [];
function walk(value, context) {
  if (Array.isArray(value)) { for (const item of value) walk(item, context); return; }
  if (!value || typeof value !== 'object') { finding('errors', 'JSON-LD root must be object/array'); return; }
  const effective = value['@context'] ?? context;
  if (Array.isArray(value['@graph'])) { for (const item of value['@graph']) walk(item, effective); return; }
  nodes.push({ ...value, '@context': effective });
}
for (const match of html.matchAll(/<script\b[^>]*\btype\s*=\s*["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi)) {
  report.block_count++;
  try { walk(JSON.parse(match[1])); }
  catch { finding('errors', `Block ${report.block_count}: invalid JSON`); }
}
if (!report.block_count) finding('errors', 'No JSON-LD script blocks found');
const present = (value) => value !== undefined && value !== null && value !== '' && value !== false;
const typesOf = node => Array.isArray(node['@type']) ? node['@type'] : [node['@type']];
const required = {
  Organization: ['name'], WebSite: ['url', 'name'], WebPage: ['url'], Person: ['name'],
  Service: ['name', 'provider'], LocalBusiness: ['name', 'address'], Product: ['name'],
  MerchantReturnPolicy: ['applicableCountry', 'returnPolicyCategory'],
};
const recommended = { Article: ['headline', 'image', 'author', 'datePublished'],
  BlogPosting: ['headline', 'image', 'author', 'datePublished'],
  NewsArticle: ['headline', 'image', 'author', 'datePublished'] };
const ids = new Set(); let matched = 0;
for (const node of nodes) {
  const types = typesOf(node);
  if (!node['@context']) finding('errors', 'Missing effective @context', node);
  if (!types[0] || types.some(t => typeof t !== 'string')) finding('errors', 'Missing/invalid @type', node);
  if (node['@id'] && Object.keys(node).some(k => !['@context', '@id'].includes(k))) {
    if (ids.has(node['@id'])) finding('warnings', 'Repeated entity definition; review identity/owner', node);
    ids.add(node['@id']);
  }
  if (flags.type && !types.includes(flags.type)) continue;
  matched++;
  for (const type of types) {
    for (const key of required[type] ?? []) if (!present(node[key])) finding('errors', `${type}: missing ${key}`, node);
    for (const key of recommended[type] ?? []) if (!present(node[key])) finding('warnings', `${type}: recommended ${key} missing`, node);
    if (type === 'Product') {
      if (!node.offers && !node.review && !node.aggregateRating) finding('warnings', 'Product snippet: needs offers, review or aggregateRating for eligibility', node);
      for (const offer of node.offers ? (Array.isArray(node.offers) ? node.offers : [node.offers]) : []) {
        if (!present(offer.price) && !present(offer.priceSpecification?.price) && !present(offer.lowPrice)) finding('warnings', 'Product offer lacks price; review chosen Google result requirements', node);
        if (!present(offer.priceCurrency)) finding('warnings', 'Product offer lacks currency; review chosen result requirements', node);
      }
    }
    if (['BreadcrumbList', 'ItemList'].includes(type)) {
      if (!Array.isArray(node.itemListElement) || !node.itemListElement.length) finding('errors', `${type}: empty/non-array itemListElement`, node);
      else node.itemListElement.forEach((item, index) => {
        if (!item || typeof item !== 'object') { finding('errors', `${type}: invalid list item`, node); return; }
        if (item.position !== index + 1) finding('warnings', `${type}: non-sequential position`, node);
        if (type === 'BreadcrumbList' && !item.name) finding('errors', 'Breadcrumb: name missing', node);
        if (type === 'BreadcrumbList' && index < node.itemListElement.length - 1 && !item.item) finding('errors', 'Breadcrumb: nonfinal item URL missing', node);
      });
    }
    if (type === 'FAQPage') {
      if (!Array.isArray(node.mainEntity) || !node.mainEntity.length) finding('errors', 'FAQPage: empty/non-array mainEntity', node);
      else for (const q of node.mainEntity) if (!q?.name || !q?.acceptedAnswer?.text) finding('errors', 'FAQPage: question or answer text missing', node);
      finding('info', 'Google FAQ rich results retired May 2026; Schema.org Q&A semantics only', node);
    }
    if (type === 'MerchantReturnPolicy' && String(node.returnPolicyCategory).endsWith('MerchantReturnFiniteReturnWindow') && !present(node.merchantReturnDays)) finding('errors', 'Finite return policy lacks merchantReturnDays', node);
  }
  for (const key of ['url', '@id']) if (node[key] && !/^https?:\/\//.test(node[key])) finding('warnings', `${key} is not an absolute HTTP(S) URL; check canonical identity`, node);
  for (const key of ['datePublished', 'dateModified']) if (node[key] && (!/^\d{4}-\d{2}-\d{2}(?:T.*)?$/.test(node[key]) || Number.isNaN(Date.parse(node[key])))) finding('errors', `${key} has invalid date format`, node);
}
if (flags.type && !matched) finding('errors', `Requested type ${flags.type} not found`);
if (flags.json) console.log(JSON.stringify(report, null, 2));
else { for (const item of report.validations) console.log(`${item.level.toUpperCase()}: ${item.message}`); console.log(JSON.stringify(report.summary)); }
process.exit(report.summary.errors ? 2 : report.summary.warnings ? 1 : 0);
