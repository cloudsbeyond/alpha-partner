#!/usr/bin/env node

import { readFile } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const scriptDir = dirname(fileURLToPath(import.meta.url));
const sourceRoot = dirname(scriptDir);
const defaultConfigPath = join(sourceRoot, '.alphaX', 'local', 'agent-runtime-services.json');
const memoryMethods = new Set([
  'memory.event.append',
  'memory.event.get',
  'memory.event.list',
  'memory.claim.upsert',
  'memory.claim.get',
  'memory.claim.query',
  'memory.relation.upsert',
  'memory.relation.query',
  'memory.context.retrieve',
]);

const inspectionMethods = new Set([
  'version',
  'capabilities.describe',
  'resources.status',
]);

const [command, firstArg, secondArg] = process.argv.slice(2);
let endpoint = '<not resolved>';

if (!command || command === '-h' || command === '--help') {
  usage(0);
}

endpoint = await resolveEndpoint();

if (command === 'describe') {
  const result = await rpcCall('capabilities.describe', {});
  result.capabilities = Array.isArray(result.capabilities)
    ? result.capabilities.filter((capability) => memoryMethods.has(capability.id))
    : [];
  printJson(result);
} else if (command === 'call') {
  if (!firstArg) fail('missing method');
  assertAllowedMethod(firstArg);
  printJson(await rpcCall(firstArg, await readParams(secondArg)));
} else {
  assertAllowedMethod(command);
  printJson(await rpcCall(command, await readParams(firstArg)));
}

function assertAllowedMethod(method) {
  if (memoryMethods.has(method) || inspectionMethods.has(method)) return;
  fail(`unsupported method: ${method}`);
}

async function readParams(input) {
  if (!input) return {};
  if (input === '-') return parseJson(await readStdin(), 'stdin');
  if (input.trim().startsWith('{')) return parseJson(input, 'argument');
  return parseJson(await readFile(input, 'utf8'), input);
}

async function resolveEndpoint() {
  const envEndpoint = process.env.RUNTIME_SERVICES_RPC_URL;
  if (envEndpoint) return normalizeRpcEndpoint(envEndpoint);

  const configPath = process.env.ALPHAX_MEMORY_CONFIG ?? defaultConfigPath;
  const config = await readEndpointConfig(configPath);
  const configuredEndpoint = endpointFromConfig(config);
  if (configuredEndpoint) return normalizeRpcEndpoint(configuredEndpoint);

  return normalizeRpcEndpoint('http://127.0.0.1:8765/');
}

async function readEndpointConfig(configPath) {
  try {
    return parseJson(await readFile(configPath, 'utf8'), configPath);
  } catch (error) {
    if (error?.code === 'ENOENT') return {};
    fail(`failed to read config ${configPath}: ${error instanceof Error ? error.message : String(error)}`);
  }
}

function endpointFromConfig(config) {
  return stringValue(config.rpcUrl)
    ?? stringValue(config.baseUrl)
    ?? stringValue(config.agentRuntimeServices?.rpcUrl)
    ?? stringValue(config.agentRuntimeServices?.baseUrl)
    ?? stringValue(config.runtimeServices?.rpcUrl)
    ?? stringValue(config.runtimeServices?.baseUrl);
}

function stringValue(value) {
  return typeof value === 'string' && value.trim() ? value.trim() : undefined;
}

function normalizeRpcEndpoint(value) {
  try {
    const url = new URL(value);
    const pathname = url.pathname.replace(/\/+$/, '');
    url.pathname = pathname.endsWith('/rpc') ? pathname : `${pathname}/rpc`;
    url.search = '';
    url.hash = '';
    return url.toString();
  } catch {
    fail(`invalid runtime services endpoint: ${value}`);
  }
}

async function readStdin() {
  const chunks = [];
  for await (const chunk of process.stdin) {
    chunks.push(Buffer.isBuffer(chunk) ? chunk : Buffer.from(chunk));
  }
  return Buffer.concat(chunks).toString('utf8');
}

function parseJson(text, label) {
  try {
    const parsed = JSON.parse(text);
    if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) {
      fail(`${label} must be a JSON object`);
    }
    return parsed;
  } catch (error) {
    fail(`${label} is not valid JSON: ${error instanceof Error ? error.message : String(error)}`);
  }
}

async function rpcCall(method, params) {
  const response = await fetch(endpoint, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      jsonrpc: '2.0',
      id: 1,
      method,
      params,
    }),
  });
  if (!response.ok) fail(`runtime services rpc failed (${response.status})`);
  const payload = await response.json();
  if (payload.error) fail(payload.error.message ?? 'runtime services rpc error');
  return payload.result;
}

function printJson(value) {
  process.stdout.write(`${JSON.stringify(value, null, 2)}\n`);
}

function fail(message) {
  process.stderr.write(`FAIL: ${message}\n`);
  usage(1);
}

function usage(exitCode) {
  const methods = [...memoryMethods].join('|');
  process.stderr.write(`Usage:
  node scripts/alphaX-memory-family-rpc.mjs describe
  node scripts/alphaX-memory-family-rpc.mjs version
  node scripts/alphaX-memory-family-rpc.mjs resources.status
  node scripts/alphaX-memory-family-rpc.mjs call <memory-method> [params.json|-|'{...}']
  node scripts/alphaX-memory-family-rpc.mjs <memory-method> [params.json|-|'{...}']

Memory methods:
  ${methods}

Environment:
  ALPHAX_MEMORY_CONFIG defaults to ${defaultConfigPath}
  RUNTIME_SERVICES_RPC_URL overrides config when set.
  Resolved resident endpoint: ${endpoint}
  This helper calls an existing compatible service; it does not start one.
`);
  process.exit(exitCode);
}
