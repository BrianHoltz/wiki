#!/usr/bin/env node

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = __dirname;

function readData(relativePath) {
  return JSON.parse(fs.readFileSync(path.join(root, relativePath), "utf8"));
}

function assertDataIntegrity(relativePath) {
  const data = readData(relativePath);
  const ids = new Set(data.nodes.map((node) => node.id));
  for (const node of data.nodes) {
    for (const child of node.children) {
      assert(ids.has(child), `${relativePath}: ${node.id} references missing child ${child}`);
    }
    for (const parent of node.alternateParents) {
      assert(ids.has(parent), `${relativePath}: ${node.id} references missing parent ${parent}`);
    }
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

async function loadBrowser(relativePath, dataPath) {
  const source = fs.readFileSync(path.join(root, relativePath), "utf8");
  if (relativePath === "index.html") {
    assert(!/\bsumo\b/i.test(source), "canonical browser contains a SUMO reference");
  }
  const script = source.match(/<script>([\s\S]*)<\/script>/)[1];
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
  return elements;
}

async function testBrowser(relativePath, dataPath) {
  const elements = await loadBrowser(relativePath, dataPath);
  const tree = elements.get("#tree");
  const search = elements.get("#search");
  const results = elements.get("#results");
  const presets = elements.get(".search-presets");

  if (relativePath === "index.html") {
    assert.equal(dataPath.root, "Entity", "canonical ontology root must be Entity");
    assert.deepEqual(
      dataPath.nodes.find((node) => node.id === "Entity").children,
      ["RealizedEntity", "AbstractEntity", "Property", "Relation"],
      "canonical Entity children must be RealizedEntity, AbstractEntity, Property, and Relation",
    );
    assert.deepEqual(
      dataPath.nodes.find((node) => node.id === "Collection").children,
      ["Group"],
      "Collection must retain its Group child",
    );
  }
  assert(tree.innerHTML.includes("Geopolitical Area"), `${relativePath}: target is not rendered`);
  assert(!tree.innerHTML.includes(">undefined<"), `${relativePath}: dangling child rendered`);

  if (relativePath === "index.html") {
    const objectDefinition = dataPath.nodes.find((node) => node.id === "Object").definition;
    const realizedEntityButton = eventTarget("button.expander[data-node]", { node: "RealizedEntity" });
    tree.onclick({ target: realizedEntityButton });
    const objectStart = () => tree.innerHTML.indexOf('id="Object"');
    const objectEnd = () => tree.innerHTML.indexOf("</div>", objectStart());
    const objectButton = eventTarget("button.expander[data-node]", { node: "Object" });
    tree.onclick({ target: objectButton });
    assert(
      tree.innerHTML.slice(objectStart(), objectEnd()).includes('class="definition expanded"'),
      `${relativePath}: expanded Object definition is not marked expanded`,
    );
    tree.onclick({ target: objectButton });
    assert(
      !tree.innerHTML.slice(objectStart(), objectEnd()).includes('class="definition expanded"'),
      `${relativePath}: collapsed Object definition remains expanded`,
    );
    tree.onclick({ target: objectButton });
    const expandedObject = tree.innerHTML.slice(objectStart(), objectEnd());
    assert(
      expandedObject.includes('class="definition expanded"') && expandedObject.includes(objectDefinition.slice(0, 24)),
      `${relativePath}: Object definition did not expand fully`,
    );
  }

  elements.get("#expand").onclick();
  assert(tree.innerHTML.includes('data-node="GeopoliticalArea"'), `${relativePath}: target child is not reachable`);
  assert(!tree.innerHTML.includes("Alternate Parents:"), `${relativePath}: alternate parents rendered`);
  assert(!tree.innerHTML.includes("Alternate Children:"), `${relativePath}: alternate children rendered`);

  const geographicArea = eventTarget("button.expander[data-node]", { node: "GeographicArea" });
  tree.onclick({ target: geographicArea });
  const geographicStart = tree.innerHTML.indexOf('id="GeographicArea"');
  assert(geographicStart >= 0, `${relativePath}: Geographic Area is missing`);
  const geographicChildrenStart = tree.innerHTML.indexOf('<ul class="children"', geographicStart);
  assert(
    tree.innerHTML.slice(geographicChildrenStart, geographicChildrenStart + 80).includes("hidden"),
    `${relativePath}: Geographic Area did not collapse`,
  );

  const geopoliticalStart = tree.innerHTML.indexOf('id="GeopoliticalArea"');
  const geopoliticalEnd = tree.innerHTML.indexOf("</div>", geopoliticalStart);
  assert(
    !tree.innerHTML.slice(geopoliticalStart, geopoliticalEnd).includes('class="expander"'),
    `${relativePath}: leaf has an expandable triangle`,
  );

  search.value = "Geopolitical Area";
  search.oninput({ target: search });
  assert(results.innerHTML.includes('data-node="GeopoliticalArea"'), `${relativePath}: search failed`);
  results.onclick({
    target: eventTarget("a[data-node]", { node: "GeopoliticalArea" }),
    preventDefault() {},
  });
  assert(
    tree.innerHTML.includes('id="GeopoliticalArea"'),
    `${relativePath}: search result did not open lineage view`,
  );

  presets.onclick({
    target: eventTarget("button[data-target]", { search: "primate", target: dataPath.root === "Entity" ? "Primate" : "BioPrimates" }),
  });
  assert(tree.innerHTML.includes("primate") || tree.innerHTML.includes("Primate"), `${relativePath}: preset did not navigate`);
}

async function main() {
  const canonical = assertDataIntegrity("ontology.json");
  const historical = assertDataIntegrity("SUMO/sumo.json");
  await testBrowser("index.html", canonical);
  await testBrowser("SUMO/index.html", historical);
  console.log("Ontology browser tests passed.");
}

main().catch((error) => {
  console.error(error.stack || error);
  process.exitCode = 1;
});
