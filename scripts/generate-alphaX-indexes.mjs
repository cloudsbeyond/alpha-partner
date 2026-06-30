#!/usr/bin/env node

import { existsSync, readFileSync, unlinkSync, writeFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { basename, dirname, join, relative, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const args = new Set(process.argv.slice(2));
const modeWrite = args.has('--write');
const modeCheck = args.has('--check');

if (modeWrite === modeCheck) {
  console.error('Usage: node scripts/generate-alphaX-indexes.mjs --write|--check');
  process.exit(2);
}

const requiredFields = ['type', 'title', 'description'];
const generatedIndexes = new Map();
const conceptDocs = [];
const indexableDirs = new Set();
const collapsedEntriesByDir = new Map();
let failed = false;

function rel(path, from = root) {
  return relative(from, path).split(sep).join('/');
}

function gitVisibleMarkdownFiles() {
  const output = execFileSync(
    'git',
    ['-C', root, 'ls-files', '--cached', '--others', '--exclude-standard', '--', '*.md'],
    { encoding: 'utf8' },
  );
  return output
    .split('\n')
    .map((line) => line.trim())
    .filter(Boolean)
    .filter((path) => existsSync(join(root, path)))
    .filter((path) => basename(path) !== 'index.md')
    .sort();
}

function gitVisibleIndexFiles() {
  const output = execFileSync(
    'git',
    ['-C', root, 'ls-files', '--cached', '--others', '--exclude-standard', '--', '*.md'],
    { encoding: 'utf8' },
  );
  return output
    .split('\n')
    .map((line) => line.trim())
    .filter(Boolean)
    .filter((path) => existsSync(join(root, path)))
    .filter((path) => basename(path) === 'index.md')
    .map((path) => join(root, path))
    .sort();
}

function parseFrontmatter(path, text) {
  if (!text.startsWith('---\n')) {
    return { error: 'missing YAML frontmatter' };
  }
  const end = text.indexOf('\n---\n', 4);
  if (end === -1) {
    return { error: 'unterminated YAML frontmatter' };
  }
  const raw = text.slice(4, end).trim();
  const frontmatter = {};
  for (const line of raw.split('\n')) {
    if (!line.trim() || line.startsWith('#')) continue;
    const idx = line.indexOf(':');
    if (idx === -1) {
      return { error: `invalid frontmatter line: ${line}` };
    }
    const key = line.slice(0, idx).trim();
    let value = line.slice(idx + 1).trim();
    if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }
    frontmatter[key] = value;
  }
  for (const field of requiredFields) {
    if (!frontmatter[field]) {
      return { error: `missing frontmatter field: ${field}` };
    }
  }
  return { frontmatter };
}

function loadConceptDocs() {
  for (const sourcePath of gitVisibleMarkdownFiles()) {
    const fullPath = join(root, sourcePath);
    const text = readFileSync(fullPath, 'utf8');
    const parsed = parseFrontmatter(fullPath, text);
    if (parsed.error) {
      console.error(`${sourcePath}: ${parsed.error}`);
      failed = true;
      continue;
    }
    conceptDocs.push({ path: fullPath, dir: dirname(fullPath), ...parsed.frontmatter });
  }
}

function docsForDir(dir) {
  return conceptDocs.filter((doc) => doc.dir === dir);
}

function collectDirs() {
  const dirs = new Set([root]);
  for (const doc of conceptDocs) {
    let cur = doc.dir;
    while (cur.startsWith(root)) {
      dirs.add(cur);
      if (cur === root) break;
      cur = dirname(cur);
    }
  }
  return Array.from(dirs).sort((a, b) => b.length - a.length);
}

function childDirs(dir, dirs) {
  return dirs
    .filter((candidate) => candidate !== dir && dirname(candidate) === dir)
    .sort((a, b) => basename(a).localeCompare(basename(b)));
}

function addEntry(groups, type, title, link, description) {
  if (!groups.has(type)) groups.set(type, []);
  groups.get(type).push({ title, link, description });
}

function buildEntries(dir, dirs) {
  const entries = [];

  for (const child of childDirs(dir, dirs)) {
    const childEntries = buildEntries(child, dirs);
    const childHasIndex = child === root || childEntries.length > 1;
    if (childHasIndex) {
      indexableDirs.add(child);
      entries.push({
        type: 'Subdirectory',
        title: basename(child),
        link: rel(join(child, 'index.md'), dir),
        description: 'Directory index for related alphaX source documents.',
      });
      continue;
    }
    entries.push(...childEntries.map((entry) => ({
      ...entry,
      link: rel(join(child, entry.link), dir),
    })));
  }

  for (const doc of docsForDir(dir)) {
    entries.push({
      type: doc.type,
      title: doc.title,
      link: basename(doc.path),
      description: doc.description,
    });
  }

  collapsedEntriesByDir.set(dir, entries);
  return entries;
}

function buildIndex(dir) {
  const groups = new Map();

  for (const entry of collapsedEntriesByDir.get(dir) || []) {
    addEntry(groups, entry.type, entry.title, entry.link, entry.description);
  }

  if (groups.size === 0) return null;

  const sections = [];
  for (const type of Array.from(groups.keys()).sort()) {
    const entries = groups.get(type).sort((a, b) => a.title.localeCompare(b.title));
    sections.push(`# ${type}`);
    sections.push('');
    for (const entry of entries) {
      const desc = entry.description ? ` - ${entry.description}` : '';
      sections.push(`- [${entry.title}](${entry.link})${desc}`);
    }
    sections.push('');
  }
  return `${sections.join('\n').trim()}\n`;
}

loadConceptDocs();

if (failed) process.exit(1);

const dirs = collectDirs();
buildEntries(root, dirs);
indexableDirs.add(root);

for (const dir of Array.from(indexableDirs).sort()) {
  const content = buildIndex(dir);
  if (content) generatedIndexes.set(join(dir, 'index.md'), content);
}

const obsoleteIndexes = gitVisibleIndexFiles().filter((path) => !generatedIndexes.has(path));

for (const [path, content] of generatedIndexes) {
  if (modeWrite) {
    writeFileSync(path, content, 'utf8');
    continue;
  }
  let actual = '';
  try {
    actual = readFileSync(path, 'utf8');
  } catch {
    console.error(`${rel(path)}: missing generated index`);
    failed = true;
    continue;
  }
  if (actual !== content) {
      console.error(`${rel(path)}: generated index is stale`);
    failed = true;
  }
}

for (const path of obsoleteIndexes) {
  if (modeWrite) {
    if (existsSync(path)) unlinkSync(path);
    continue;
  }
  console.error(`${rel(path)}: obsolete generated index`);
  failed = true;
}

if (failed) process.exit(1);

const action = modeWrite ? 'Generated' : 'Checked';
console.log(`${action} ${generatedIndexes.size} index file(s).`);
