#!/usr/bin/env node

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = __dirname;
const browsers = [
  ["index.html", "ontology.json", "flowering plant", "FloweringPlant"],
  ["SUMO/index.html", "SUMO/ontology.json", "flowering plant", "FloweringPlant"],
  ["HumanKnowledge/index.html", "HumanKnowledge/ontology.json", "philosophy", "hk-1"],
  ["Propaedia/index.html", "Propaedia/ontology.json", "life", "part-3"],
  ["Rogets/index.html", "Rogets/ontology.json", "number", "roget-node-23"],
  ["Wikipedia/index.html", "Wikipedia/ontology.json", "geography", "Category:Geography"],
  ["GPT/index.html", "GPT/ontology.json", "organism", "Organism"],
];

function readData(relativePath) {
  return JSON.parse(fs.readFileSync(path.join(root, relativePath), "utf8"));
}

function assertDataIntegrity(relativePath) {
  const data = readData(relativePath);
  const ids = new Set(data.nodes.map((node) => node.id));
  assert.equal(ids.size, data.nodes.length, `${relativePath}: duplicate node id`);
  for (const node of data.nodes) {
    for (const child of node.children) {
      assert(ids.has(child), `${relativePath}: ${node.id} references missing child ${child}`);
    }
    for (const parent of node.alternateParents || []) {
      assert(ids.has(parent), `${relativePath}: ${node.id} references missing parent ${parent}`);
    }
  }
  for (const rootNode of data.rootNodes) {
    assert(ids.has(rootNode), `${relativePath}: missing root ${rootNode}`);
  }
  return data;
}

function eventTarget(selector, dataset) {
  return {
    closest(requested) {
      return requested === selector ? { dataset } : null;
    },
  };
}

function scriptOf(source) {
  return source.match(/<script>([\s\S]*)<\/script>/)[1];
}

async function loadBrowser(relativePath, dataPath) {
  const source = fs.readFileSync(path.join(root, relativePath), "utf8");
  if (relativePath === "index.html") {
    assert(!/\bsumo\b/i.test(source), "canonical browser contains a SUMO reference");
  }
  const script = scriptOf(source);
  const elements = new Map(
    ["#tree", "#summary", "#expand", "#collapse", "#search", "#results", ".search-presets"]
      .map((selector) => [selector, { innerHTML: "", textContent: "", value: "" }]),
  );
  const document = {
    querySelector(selector) {
      assert(elements.has(selector), `${relativePath}: unexpected selector ${selector}`);
      return elements.get(selector);
    },
    getElementById() {
      return { scrollIntoView() {} };
    },
  };
  const context = {
    console,
    document,
    encodeURIComponent,
    fetch: () => Promise.resolve({ json: () => Promise.resolve(dataPath) }),
  };
  vm.runInNewContext(script, context, { filename: relativePath });
  await new Promise((resolve) => setImmediate(resolve));
  return { elements, source };
}

function encodedId(id) {
  return encodeURIComponent(id);
}

async function testBrowser(relativePath, dataPath, presetSearch, presetTarget) {
  const data = assertDataIntegrity(dataPath);
  const { elements, source } = await loadBrowser(relativePath, data);
  const tree = elements.get("#tree");
  const search = elements.get("#search");
  const results = elements.get("#results");
  const presets = elements.get(".search-presets");
  const branch = data.nodes.find((node) => node.children.length > 0);
  const leaf = data.nodes.find((node) => node.children.length === 0);
  assert(branch && leaf, `${relativePath}: normalized data needs branches and leaves`);
  assert(tree.innerHTML.includes(`data-node="${branch.id}"`), `${relativePath}: target is not rendered`);
  assert(!tree.innerHTML.includes(">undefined<"), `${relativePath}: dangling child rendered`);
  assert(!tree.innerHTML.includes("lineage-toggle"), `${relativePath}: obsolete lineage arrow rendered`);
  assert(tree.innerHTML.includes("class=\"meta\""), `${relativePath}: child counts missing`);
  assert.equal((source.match(/data-search="/g) || []).length, 5, `${relativePath}: search presets are missing`);
  const searchRow = source.match(/<div class="search-row">([\s\S]*?)<\/div>/)?.[1] || "";
  assert(searchRow.includes('<input id="search"'), `${relativePath}: search input is missing`);
  assert(
    searchRow.indexOf('id="search"') < searchRow.indexOf('class="search-presets"'),
    `${relativePath}: search presets are not to the right of the search input`,
  );
  assert.equal(typeof presets.onclick, "function", `${relativePath}: search presets are not wired`);
  presets.onclick({ target: eventTarget("button[data-target]", { search: presetSearch, target: presetTarget }) });
  assert.equal(search.value, presetSearch, `${relativePath}: preset did not populate search`);
  assert(tree.innerHTML.includes(`id="${encodedId(presetTarget)}"`), `${relativePath}: preset did not navigate`);
  assert(!source.includes("search-example"), `${relativePath}: duplicate search-example controls remain`);
  assert(!tree.innerHTML.includes("Suggested question:"), `${relativePath}: generated question text rendered`);
  assert(!tree.innerHTML.match(/data-node="[^"]+"><\/a>/), `${relativePath}: blank node rendered`);
  const childIds = new Set(data.nodes.flatMap((node) => node.children));
  for (const rootNode of data.rootNodes) {
    assert(!childIds.has(rootNode), `${relativePath}: child node incorrectly listed as a root`);
  }
  if (relativePath === "Rogets/index.html") {
    assert(tree.innerHTML.includes("Words Expressing Abstract Relations"), "Roget titles are not mixed case");
    assert(!tree.innerHTML.includes("WORDS EXPRESSING"), "Roget boilerplate definition rendered");
    assert(!tree.innerHTML.includes(" / 0001. Existence"), "Roget repeated path definition rendered");
  }
  if (data.nodes.some((node) => node.sourceUrl)) {
    assert(tree.innerHTML.includes("class=\"source-link\""), `${relativePath}: source links missing`);
  }
  assert(!tree.innerHTML.includes("Alternate Parents:"), `${relativePath}: alternate parents rendered`);
  assert(!tree.innerHTML.includes("Alternate Children:"), `${relativePath}: alternate children rendered`);

  const definitionNode = data.nodes.find((node) => node.definition && node.children.length > 0);
  if (definitionNode) {
    const definitionButton = eventTarget("button.expander[data-node]", { node: definitionNode.id });
    tree.onclick({ target: definitionButton });
    const definitionStart = tree.innerHTML.indexOf(`id="${encodedId(definitionNode.id)}"`);
    const definitionEnd = tree.innerHTML.indexOf("</div>", definitionStart);
    if (!tree.innerHTML.slice(definitionStart, definitionEnd).includes('class="definition expanded"')) {
      tree.onclick({ target: definitionButton });
    }
    assert(
      tree.innerHTML.slice(definitionStart, definitionEnd).includes('class="definition expanded"'),
      `${relativePath}: definition did not expand`,
    );
    tree.onclick({ target: definitionButton });
    assert(
      !tree.innerHTML.slice(definitionStart, definitionEnd).includes('class="definition expanded"'),
      `${relativePath}: definition did not collapse`,
    );
  }

  elements.get("#expand").onclick();
  assert(tree.innerHTML.includes(`data-node="${leaf.id}"`), `${relativePath}: leaf is not reachable`);
  const branchButton = eventTarget("button.expander[data-node]", { node: branch.id });
  tree.onclick({ target: branchButton });
  const branchStart = tree.innerHTML.indexOf(`id="${encodedId(branch.id)}"`);
  const childrenStart = tree.innerHTML.indexOf('<ul class="children"', branchStart);
  assert(tree.innerHTML.slice(childrenStart, childrenStart + 80).includes("hidden"), `${relativePath}: chevron did not collapse`);
  assert(
    tree.innerHTML.slice(branchStart, childrenStart).includes(`${branch.children.length}`),
    `${relativePath}: direct-child count missing`,
  );
  const descendants = new Map();
  const countDescendants = (id) => {
    if (descendants.has(id)) return descendants.get(id);
    const node = data.nodes.find((candidate) => candidate.id === id);
    const count = node.children.reduce((total, child) => total + 1 + countDescendants(child), 0);
    descendants.set(id, count);
    return count;
  };
  const otherDescendants = countDescendants(branch.id) - branch.children.length;
  if (otherDescendants) {
    assert(
      tree.innerHTML.slice(branchStart, childrenStart).includes(`+${otherDescendants} &#8595;`),
      `${relativePath}: descendant count missing`,
    );
  }

  const nodeLink = eventTarget("a[data-node]", { node: leaf.id });
  tree.onclick({ target: nodeLink, preventDefault() {} });
  assert(tree.innerHTML.includes(`id="${encodedId(leaf.id)}"`), `${relativePath}: node name did not open lineage view`);

  search.value = leaf.label.split(/\s+/).slice(0, 2).join(" ");
  search.oninput({ target: search });
  assert(results.innerHTML.includes(`data-node="${leaf.id}"`), `${relativePath}: search failed`);
  results.onclick({
    target: eventTarget("a[data-node]", { node: leaf.id }),
    preventDefault() {},
  });
  assert(tree.innerHTML.includes(`id="${encodedId(leaf.id)}"`), `${relativePath}: search result did not open lineage view`);

  return source;
}

async function main() {
  const canonicalSource = fs.readFileSync(path.join(root, "index.html"), "utf8");
  const canonicalScript = scriptOf(canonicalSource);
  const canonicalStyle = canonicalSource.match(/<style>([\s\S]*)<\/style>/)[1];
  assert(!canonicalSource.includes("Canonical upper ontology with historical physical projection"));
  const sources = [];
  for (const [page, data, query, expected] of browsers) {
    assert(!/historical physical projection/i.test(data.source?.overlayPolicy || ""), `${page}: stale overlay title remains`);
    if (data.source?.upperOntology) {
      assert.equal(data.source.upperOntology, "Ontology/Ontology.md#upper-ontologies", `${page}: stale upper-ontology link`);
    }
    if (page === "index.html") {
      const canonical = assertDataIntegrity(data);
      assert.equal(canonical.source.name, "My Ontology");
      const nodes = new Map(canonical.nodes.map((node) => [node.id, node]));
      assert.deepEqual(nodes.get("Object").children, ["Item", "Collection", "Region", "Agent", "SelfConnectedObject"]);
      assert.deepEqual(nodes.get("Item").children, ["AbioticObject", "BiologicalObject", "Artifact"]);
      assert.equal(nodes.get("Item").definition, "An object distinguished as a single unit.");
      assert.equal(nodes.get("AbioticObject").definition, "An item of nonbiological, nonartificial origin.");
      assert.equal(nodes.get("BiologicalObject").definition, "An item constituted by or originating from biological activity.");
      assert.equal(nodes.get("Artifact").definition, "An item intentionally produced or modified for a purpose.");
      assert.equal(nodes.get("Collection").definition, "An object constituted by multiple members.");
      assert.equal(nodes.get("Region").definition, "An object defined by spatial extent or boundaries.");
      assert.match(nodes.get("Agent").definition, /^To be moved —/);
      assert.match(nodes.get("SelfConnectedObject").definition, /^To be moved —/);
    }
    sources.push(await testBrowser(page, data, query, expected));
  }
  for (const [index, source] of sources.entries()) {
    assert.equal(scriptOf(source), canonicalScript, `${browsers[index][0]}: renderer differs from canonical browser`);
    assert.equal(source.match(/<style>([\s\S]*)<\/style>/)[1], canonicalStyle, `${browsers[index][0]}: layout differs from canonical browser`);
  }
  console.log("Ontology browser tests passed for all seven browsers.");
}

main().catch((error) => {
  console.error(error.stack || error);
  process.exitCode = 1;
});
