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
    fetch: (url) => Promise.resolve({ json: () => Promise.resolve(url === "ontology.json" ? dataPath : readData(path.join(path.dirname(relativePath), url))) }),
  };
  vm.runInNewContext(script, context, { filename: relativePath });
  await new Promise((resolve) => setImmediate(resolve));
  return { elements, source, context };
}

function encodedId(id) {
  return encodeURIComponent(id);
}

async function testBrowser(relativePath, dataPath, presetSearch, presetTarget) {
  const data = assertDataIntegrity(dataPath);
  const { elements, source, context } = await loadBrowser(relativePath, data);
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
  assert(tree.innerHTML.includes("class=\"meta node-stats\""), `${relativePath}: child counts missing`);
  const counts = readData(path.join(path.dirname(relativePath), "species-counts.json"));
  for (const [id, value] of Object.entries(counts)) {
    assert(data.nodes.some(node => node.id === id), `${relativePath}: taxon mapping references missing node ${id}`);
    const start = tree.innerHTML.indexOf(`id="${encodedId(id)}"`);
    const row = tree.innerHTML.slice(start, tree.innerHTML.indexOf("</div>", start));
    assert(row.includes('class="species-count"'), `${relativePath}: species count missing on ${id}`);
    assert(!row.includes("?"), `${relativePath}: unavailable count rendered on ${id}`);
    assert(!row.includes("†"), `${relativePath}: species dagger clutter on ${id}`);
    assert(row.includes(value.url), `${relativePath}: evidence link missing on ${id}`);
  }
  for (const [count, expected] of [[230000,"230K"],[30040,"30.0K"],[1000,"1.00K"],[999500,"1.00M"],[999499,"999K"],[2030000,"2.03M"],[0,"0"],[1,"1"],[null,""]]) {
    assert.equal(context.formatSpeciesCount(count), expected);
  }
  const sample = { taxon: "Sample", scope: "Test", url: "evidence.html", retrieved: "2026.10.10" };
  const renderedCount = values => (context.speciesStats({speciesCount: {...sample, ...values}}).match(/>([^<]*)<\/a>/) || [null, ""])[1];
  assert.equal(renderedCount({total:30040, extinct:null, extant:null}), "30.0K");
  assert.equal(renderedCount({total:30040, extinct:40, extant:30000}), "40☠︎+30.0K♥︎");
  assert.equal(renderedCount({total:null, extinct:40, extant:null}), "40☠︎");
  assert.equal(renderedCount({total:null, extinct:null, extant:30000}), "30.0K♥︎");
  assert.equal(renderedCount({total:null, extinct:null, extant:null}), "");
  assert.equal(renderedCount({total:30040, extinct:40, extant:null}), "40☠︎");
  assert.equal(renderedCount({total:1, extinct:0, extant:1}), "0☠︎+1♥︎");
  assert.equal(context.speciesStats({}), "");
  if (counts.Animal) {
    assert.equal(renderedCount(counts.Animal), "169K☠︎+1.48M♥︎");
  }
  const entityCounts = readData(path.join(path.dirname(relativePath), "entity-counts.json"));
  for (const [id, annotations] of Object.entries(entityCounts)) {
    assert(data.nodes.some(node => node.id === id), `${relativePath}: entity count maps to missing node ${id}`);
    const start = tree.innerHTML.indexOf(`id="${encodedId(id)}"`);
    const row = tree.innerHTML.slice(start, tree.innerHTML.indexOf("</div>", start));
    for (const annotation of annotations) {
      assert(row.includes(annotation.url), `${relativePath}: entity evidence missing on ${id}`);
      assert(row.replaceAll("&gt;", ">").includes(context.formatEntityCount(annotation)), `${relativePath}: scoped entity count missing on ${id}`);
      assert(row.includes('class="entity-count"'), `${relativePath}: entity annotation missing on ${id}`);
      assert(row.includes('title="'), `${relativePath}: entity scope tooltip missing on ${id}`);
    }
  }
  assert.equal(context.formatEntityCount({display:"ℵ₀"}), "ℵ₀");
  assert.equal(context.formatEntityCount({display:"𝔠 uncountable"}), "𝔠 uncountable");
  assert.equal(context.formatEntityCount({extinctDisplay:"40", extantDisplay:"30.0K"}), "40☠︎+30.0K♥︎");
  assert.equal(context.formatEntityCount({extantDisplay:"7.17K", countLabel:"living languages"}), "7.17K♥︎ living languages");
  assert.equal(context.formatEntityCount({extinctDisplay:"0", extantDisplay:"1"}), "0☠︎+1♥︎");
  assert.equal(context.entityStats({}), "");
  assert(context.entityStats({label:'<name>', entityCounts:[{display:'<count>', scope:'"scope"', url:'evidence.html'}]}).includes('&lt;count&gt;'));
  if (relativePath === "GPT/index.html") {
    for (const id of ["NaturalNumber", "Integer", "RationalNumber"]) {
      assert.equal(entityCounts[id].find(s => s.record === "countable-numbers").display, "ℵ₀");
    }
    for (const id of ["RealNumber", "ComplexNumber"]) {
      assert.equal(entityCounts[id].find(s => s.record === "uncountable-numbers").display, "𝔠 uncountable");
    }
    assert.equal(entityCounts.Function[0].display, "𝔠 ℕ→ℕ");
    assert.equal(entityCounts.Graph[0].display, "ℵ₀ finite graphs");
    assert(!entityCounts.Bone, "anatomical bone count incorrectly attached to tissue portions");
    assert(!entityCounts.Muscle, "anatomical muscle count incorrectly attached to tissue portions");
    assert.equal(entityCounts.Human[0].extantDisplay, "≈8.30B");
    assert.equal(entityCounts.HumanLanguage[0].extantDisplay, "7.17K");
    assert(!entityCounts.Particle, "elementary-particle count incorrectly attached to grammatical particles");
  }
  assert(!tree.innerHTML.includes(" &#8595;"), `${relativePath}: space before down arrow`);
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

  elements.get("#expand").onclick();
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
      tree.innerHTML.slice(branchStart, childrenStart).includes(`+${otherDescendants}&#8595;`),
      `${relativePath}: descendant count missing`,
    );
  }

  // Parse nested list visibility: hidden descendants still exist in the HTML.
  const rows = () => {
    const result = new Map(), lists = [], nodes = [];
    const tokens = tree.innerHTML.matchAll(/<li id="([^"]+)">|<ul([^>]*)>|<\/ul>|<\/li>/g);
    for (const token of tokens) {
      if (token[1] !== undefined) {
        const id = decodeURIComponent(token[1]);
        result.set(id, {visible: lists.every(Boolean), open: false}); nodes.push(id);
      } else if (token[2] !== undefined) {
        const open = !/\bhidden\b/.test(token[2]);
        if (/class="children"/.test(token[2])) result.get(nodes.at(-1)).open = open;
        lists.push(open);
      } else if (token[0] === "</ul>") lists.pop();
      else nodes.pop();
    }
    return result;
  };
  const nodes = new Map(data.nodes.map(n => [n.id, n]));
  const parents = new Map(data.nodes.flatMap(n => n.children.map(child => [child, n.id])));
  const title = id => tree.onclick({target: eventTarget("a[data-node]", {node:id}), preventDefault() {}});
  const triangle = id => tree.onclick({target: eventTarget("button.expander[data-node]", {node:id})});
  const assertLineage = id => {
    const expected = new Set(nodes.get(id).children);
    for (let current=id; current; current=parents.get(current)) expected.add(current);
    assert.deepEqual([...rows()].filter(([,r]) => r.visible).map(([id]) => id).sort(),
      [...expected].sort(), `${relativePath}: title must show only lineage and direct children of ${id}`);
  };
  const assertTriangleIsolation = id => {
    const before = rows(); triangle(id); const after = rows();
    assert.deepEqual([...after.keys()], [...before.keys()], `${relativePath}: triangle changed the projection`);
    for (const [other, state] of before) {
      assert.equal(after.get(other).open, other === id ? !state.open : state.open,
        `${relativePath}: triangle changed another node's expansion: ${other}`);
    }
  };
  const focus = nodes.has("Primate") ? "Primate" : data.nodes.find(n => parents.has(n.id) && n.children.length)?.id || branch.id;
  const second = nodes.get(focus).children[0] || parents.get(focus);
  for (const initial of ["#expand", "#collapse"]) {
    elements.get(initial).onclick();
    assertTriangleIsolation(branch.id);
    const original = tree.innerHTML;
    title(focus); assertLineage(focus);
    title(focus);
    assert.equal(tree.innerHTML, original, `${relativePath}: repeated title did not restore the prior view`);
    title(focus); assertLineage(focus);
    const focused = tree.innerHTML;
    title(second); assertLineage(second);
    title(second);
    assert.equal(tree.innerHTML, focused, `${relativePath}: repeated different title did not restore earlier lineage`);
    // Test every title exposed in the lineage, including ancestors and children.
    for (const id of [...rows()].filter(([id,r]) => r.visible && id !== focus).map(([id]) => id)) {
      elements.get(initial).onclick(); title(focus); title(id); assertLineage(id);
    }
    elements.get(initial).onclick(); title(focus);
    const beforeToggle = tree.innerHTML;
    assertTriangleIsolation(focus); assertTriangleIsolation(focus);
    assert.equal(tree.innerHTML, beforeToggle, `${relativePath}: triangle pair did not restore lineage`);
    const ancestor = parents.get(focus);
    if (ancestor) { assertTriangleIsolation(ancestor); assertTriangleIsolation(ancestor); }
    const childBranch = nodes.get(focus).children.find(id => nodes.get(id).children.length);
    if (childBranch) { assertTriangleIsolation(childBranch); assertTriangleIsolation(childBranch); }
    // Undo must preserve custom expansion inside an earlier lineage as well.
    if (childBranch) triangle(childBranch);
    const customized = tree.innerHTML;
    title(second); assertLineage(second); title(second);
    assert.equal(tree.innerHTML, customized, `${relativePath}: undo lost prior lineage expansion states`);
    // A triangle breaks consecutive title clicks: the next title focuses afresh.
    triangle(focus); title(focus); assertLineage(focus);
    title(focus);
    assert.equal(rows().get(focus).open, false, `${relativePath}: restore lost a triangle change`);
  }
  title(leaf.id); assertLineage(leaf.id);

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
  const gpt = readData("GPT/ontology.json");
  const gptNodes = new Map(gpt.nodes.map(n => [n.id, n]));
  assert(gptNodes.get("Eukaryote").children.includes("Animal"), "GPT Animal must be displayed under Eukaryote");
  assert(!gptNodes.get("Organism").children.includes("Animal"), "GPT Animal must not be Eukaryote's sibling");
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
