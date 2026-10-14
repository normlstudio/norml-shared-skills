#!/usr/bin/env node

import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';
import { fileURLToPath } from 'node:url';

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const skillRoot = path.resolve(scriptDir, '..');
const recipesDir = path.join(skillRoot, 'recipes');
const skillPath = path.join(skillRoot, 'SKILL.md');
const reportPath = path.join(skillRoot, 'templates', 'baseline-report.md');
const currentSummaryPath = path.join(
  skillRoot,
  'templates',
  'current-summary.md',
);
const jsonOutput = process.argv.includes('--json');

const requiredKeys = [
  'recipe',
  'version',
  'scope',
  'baseline',
  'depends_on',
  'applies_when',
];

const requiredSections = [
  'Outcome',
  'Inputs',
  'Ownership rules',
  'Procedure',
  'Verification',
  'Rollback',
  'Evidence to record',
  'Hard stops',
  'Sources',
];

const allowedScopes = new Set(['universal', 'wordpress']);
const allowedBaselines = new Set(['required', 'recommended', 'conditional']);
const errors = [];

function fail(file, message) {
  errors.push(`${path.relative(skillRoot, file)}: ${message}`);
}

function unquote(value) {
  if (
    value.length >= 2 &&
    ((value.startsWith('"') && value.endsWith('"')) ||
      (value.startsWith("'") && value.endsWith("'")))
  ) {
    return value.slice(1, -1);
  }
  return value;
}

function parseFrontmatter(file, text) {
  const lines = text.replaceAll('\r\n', '\n').split('\n');
  if (lines[0] !== '---') {
    fail(file, 'frontmatter must start on line 1');
    return { data: {}, body: text };
  }

  const end = lines.indexOf('---', 1);
  if (end === -1) {
    fail(file, 'frontmatter closing delimiter is missing');
    return { data: {}, body: text };
  }

  const data = {};
  let listKey = null;
  for (const line of lines.slice(1, end)) {
    const listMatch = line.match(/^\s+-\s+(.+?)\s*$/);
    if (listMatch && listKey) {
      data[listKey].push(unquote(listMatch[1]));
      continue;
    }

    const keyMatch = line.match(/^([a-z_]+):\s*(.*?)\s*$/);
    if (!keyMatch) {
      if (line.trim()) {
        fail(file, `unsupported frontmatter line: ${line.trim()}`);
      }
      continue;
    }

    const [, key, rawValue] = keyMatch;
    listKey = null;
    if (rawValue === '[]' || rawValue === '') {
      data[key] = [];
      if (rawValue === '') listKey = key;
    } else {
      data[key] = unquote(rawValue);
    }
  }

  return { data, body: lines.slice(end + 1).join('\n') };
}

function extractMarked(text, startMarker, endMarker, file) {
  const start = text.indexOf(startMarker);
  const end = text.indexOf(endMarker);
  if (start === -1 || end === -1 || end <= start) {
    fail(file, `missing or invalid ${startMarker} / ${endMarker} markers`);
    return '';
  }
  return text.slice(start + startMarker.length, end);
}

function uniqueSorted(values) {
  return [...new Set(values)].sort();
}

function compareCatalog(label, actual, expected, file) {
  const duplicateValues = actual.filter(
    (value, index) => actual.indexOf(value) !== index,
  );
  for (const duplicate of uniqueSorted(duplicateValues)) {
    fail(file, `${label} contains duplicate recipe ${duplicate}`);
  }

  const actualSet = new Set(actual);
  const expectedSet = new Set(expected);
  for (const slug of expected) {
    if (!actualSet.has(slug)) fail(file, `${label} is missing ${slug}`);
  }
  for (const slug of actual) {
    if (!expectedSet.has(slug)) fail(file, `${label} has unknown ${slug}`);
  }
}

if (!fs.existsSync(recipesDir)) {
  console.error(`Recipe directory not found: ${recipesDir}`);
  process.exit(2);
}

const recipeFiles = fs
  .readdirSync(recipesDir, { withFileTypes: true })
  .filter((entry) => entry.isFile() && entry.name.endsWith('.md'))
  .map((entry) => path.join(recipesDir, entry.name))
  .sort();

const recipes = new Map();
for (const file of recipeFiles) {
  const text = fs.readFileSync(file, 'utf8');
  const { data, body } = parseFrontmatter(file, text);
  const filenameSlug = path.basename(file, '.md');

  for (const key of requiredKeys) {
    if (!(key in data)) fail(file, `missing frontmatter key ${key}`);
  }

  if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(filenameSlug)) {
    fail(file, 'filename must be lowercase kebab-case');
  }
  if (data.recipe !== filenameSlug) {
    fail(file, `recipe must equal filename slug ${filenameSlug}`);
  }
  if (!/^\d+\.\d+\.\d+$/.test(data.version ?? '')) {
    fail(file, 'version must be semantic x.y.z');
  }
  if (!allowedScopes.has(data.scope)) {
    fail(file, `scope must be one of ${[...allowedScopes].join(', ')}`);
  }
  if (!allowedBaselines.has(data.baseline)) {
    fail(file, `baseline must be one of ${[...allowedBaselines].join(', ')}`);
  }
  if (!Array.isArray(data.depends_on)) {
    fail(file, 'depends_on must be a YAML list or []');
    data.depends_on = [];
  }
  if (!data.applies_when || Array.isArray(data.applies_when)) {
    fail(file, 'applies_when must be a non-empty string');
  }

  const headings = [...body.matchAll(/^##\s+(.+?)\s*$/gm)].map(
    (match) => match[1],
  );
  let previousIndex = -1;
  for (const section of requiredSections) {
    const index = headings.indexOf(section);
    if (index === -1) {
      fail(file, `missing required section ## ${section}`);
    } else if (index <= previousIndex) {
      fail(file, `required section ## ${section} is out of order`);
    } else {
      previousIndex = index;
    }
  }

  if (recipes.has(filenameSlug)) {
    fail(file, `duplicate recipe slug ${filenameSlug}`);
  }
  recipes.set(filenameSlug, { file, data });
}

for (const [slug, recipe] of recipes) {
  const dependencies = recipe.data.depends_on;
  const duplicateDependencies = dependencies.filter(
    (value, index) => dependencies.indexOf(value) !== index,
  );
  for (const duplicate of uniqueSorted(duplicateDependencies)) {
    fail(recipe.file, `duplicate dependency ${duplicate}`);
  }
  for (const dependency of dependencies) {
    if (dependency === slug) fail(recipe.file, 'recipe cannot depend on itself');
    if (!recipes.has(dependency)) {
      fail(recipe.file, `missing dependency recipe ${dependency}`);
    }
  }
}

const visitState = new Map();
const visitStack = [];
function visit(slug) {
  const state = visitState.get(slug) ?? 0;
  if (state === 2) return;
  if (state === 1) {
    const cycleStart = visitStack.indexOf(slug);
    const cycle = [...visitStack.slice(cycleStart), slug].join(' -> ');
    fail(recipes.get(slug).file, `circular dependency: ${cycle}`);
    return;
  }

  visitState.set(slug, 1);
  visitStack.push(slug);
  for (const dependency of recipes.get(slug).data.depends_on) {
    if (recipes.has(dependency)) visit(dependency);
  }
  visitStack.pop();
  visitState.set(slug, 2);
}
for (const slug of recipes.keys()) visit(slug);

const googleAnalytics = recipes.get('google-analytics');
if (googleAnalytics) {
  if (googleAnalytics.data.depends_on.length !== 0) {
    fail(
      googleAnalytics.file,
      'Google Analytics must remain an independent presence-only check',
    );
  }
  const analyticsText = fs.readFileSync(googleAnalytics.file, 'utf8');
  for (const requiredPhrase of [
    'presence',
    'never creates or changes',
    'check-only recipe',
  ]) {
    if (!analyticsText.includes(requiredPhrase)) {
      fail(
        googleAnalytics.file,
        `missing presence-only boundary phrase: ${requiredPhrase}`,
      );
    }
  }
}

const issues404 = recipes.get('404-issues');
if (issues404) {
  const issuesText = fs.readFileSync(issues404.file, 'utf8');
  for (const requiredPhrase of [
    '500-URL',
    'no API key',
    'ScreamingFrogSEOSpiderLauncher',
    'human review',
  ]) {
    if (!issuesText.includes(requiredPhrase)) {
      fail(issues404.file, `missing 404 safety phrase: ${requiredPhrase}`);
    }
  }
  if (issuesText.includes('ScreamingFrogSEOSpiderCli')) {
    fail(issues404.file, 'macOS must use ScreamingFrogSEOSpiderLauncher');
  }
}

const expectedSlugs = [...recipes.keys()].sort();
const skillText = fs.readFileSync(skillPath, 'utf8');
const catalogText = extractMarked(
  skillText,
  '<!-- recipe-catalog:start -->',
  '<!-- recipe-catalog:end -->',
  skillPath,
);
const catalogSlugs = catalogText
  .split('\n')
  .map((line) => line.match(/^\|\s*`([a-z0-9-]+)\.md`\s*\|/)?.[1])
  .filter(Boolean);
compareCatalog('recipe catalog', catalogSlugs, expectedSlugs, skillPath);

const reportText = fs.readFileSync(reportPath, 'utf8');
const matrixText = extractMarked(
  reportText,
  '<!-- recipe-matrix:start -->',
  '<!-- recipe-matrix:end -->',
  reportPath,
);
const reportSlugs = matrixText
  .split('\n')
  .map((line) => line.match(/^\|\s*`([a-z0-9-]+)`\s*\|/)?.[1])
  .filter(Boolean);
compareCatalog('report recipe matrix', reportSlugs, expectedSlugs, reportPath);

const currentSummaryText = fs.readFileSync(currentSummaryPath, 'utf8');
const currentMatrixText = extractMarked(
  currentSummaryText,
  '<!-- current-recipe-matrix:start -->',
  '<!-- current-recipe-matrix:end -->',
  currentSummaryPath,
);
const currentRows = currentMatrixText
  .split('\n')
  .map((line) => {
    const match = line.match(
      /^\|\s*(SEO-\d+)\s*\|\s*`([a-z0-9-]+)`\s*\|/,
    );
    return match ? { ref: match[1], recipe: match[2] } : null;
  })
  .filter(Boolean);
const currentSlugs = currentRows.map((row) => row.recipe);
compareCatalog(
  'current summary recipe matrix',
  currentSlugs,
  expectedSlugs,
  currentSummaryPath,
);

const skillVersion = skillText.match(/^version:\s*(\d+\.\d+\.\d+)\s*$/m)?.[1];
const reportSkillVersion = reportText.match(
  /^skill:\s*["']norml-seo-basics@(\d+\.\d+\.\d+)["']\s*$/m,
)?.[1];
if (reportSkillVersion !== skillVersion) {
  fail(
    reportPath,
    `report skill version ${reportSkillVersion ?? 'missing'} does not match ` +
      `SKILL.md ${skillVersion ?? 'missing'}`,
  );
}
const currentSkillVersion = currentSummaryText.match(
  /^skill:\s*["']norml-seo-basics@(\d+\.\d+\.\d+)["']\s*$/m,
)?.[1];
if (currentSkillVersion !== skillVersion) {
  fail(
    currentSummaryPath,
    `current summary skill version ${currentSkillVersion ?? 'missing'} does not ` +
      `match SKILL.md ${skillVersion ?? 'missing'}`,
  );
}

const result = {
  ok: errors.length === 0,
  recipes: expectedSlugs.length,
  dependencies: [...recipes.values()].reduce(
    (count, recipe) => count + recipe.data.depends_on.length,
    0,
  ),
  errors,
};

if (jsonOutput) {
  console.log(JSON.stringify(result, null, 2));
} else if (result.ok) {
  console.log(
    `PASS norml-seo-basics recipes=${result.recipes} dependencies=${result.dependencies} ` +
      'catalog=sync report=sync current=sync',
  );
} else {
  console.error(`FAIL norml-seo-basics recipe validation (${errors.length} errors)`);
  for (const error of errors) console.error(`- ${error}`);
}

if (!result.ok) process.exitCode = 1;
