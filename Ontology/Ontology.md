# 20 Questions Ontology

## Current tree and provenance

The published tree currently contains 678 nodes: 50 semantic branches and 628
terminal noun categories. It is a curated, embedded baseline in
`generate_20q_hierarchy.py`, not an import from WordNet, Wikidata, or another
external ontology. The branch structure, leaf selection, and suggested
questions were authored for this prototype.

The generated `index.html` is intentionally a single-page browser: branches
are collapsible, suggested questions are shown at each branch, and search and
expand/collapse controls work without a server or JavaScript dependency. That
UI is a useful constraint for the next version.

## Scope target

A reasonable target is **5,000–20,000 displayed nodes**, with a preferred
operating point around **10,000–12,000**:

- Below 5,000, familiar game answers will remain conspicuously missing.
- Around 10,000, WordNet-derived common nouns plus selected named entities and
  food/place coverage should fit comfortably in one browser page while
  remaining searchable and expandable.
- Near 20,000, the HTML will still be practical as a static file, but the
  initial collapsed view, search index, and DOM size need measurement on the
  target browsers.
- Above 20,000, a single fully expandable page becomes a poor primary
  interface even if it remains technically possible. The generator should
  then produce the same one-page profile plus optional filtered views rather
  than grow the default page indefinitely.

“Node” should be defined before comparing versions. The count may include
source concepts, displayed branches, terminal categories, aliases, or
questions. The published count should use one declared convention and report
source concepts separately from display nodes.

## Standards-based options

### WordNet as the lexical backbone

[Princeton WordNet](https://wordnet.princeton.edu/) is the strongest first
candidate for ordinary noun gameplay. A pinned WordNet release provides noun
synset IDs, lemmas, glosses, frequencies, and hypernym/hyponym relations.
The generator can import its noun graph, retain source IDs, and filter to
familiar terms without changing WordNet.

The resulting display should be a deterministic projection of the WordNet
DAG, not a new ontology. For each displayed node, retain its synset ID and
source edges; choose one presentation path with reproducible tie-breakers
when the source has multiple hypernym paths. Alternate source paths should be
metadata, not duplicated visible branches.

### Wikidata for entities and contemporary vocabulary

[Wikidata](https://www.wikidata.org/) is a strong supplement for people,
places, organizations, fictional characters, brands, historical events, and
current concepts. It is broader than WordNet but has a noisier and more
cyclic subclass graph. It should initially be a separately labeled enrichment
layer, with QIDs and source claims retained, rather than the replacement for a
clean noun backbone.

### Specialized sources

Use specialized standards only where a coverage report demonstrates a gap:

- [FoodOn](https://foodon.org/) for foods, ingredients, preparations, and
  dishes such as steak and salad;
- [GeoNames](https://www.geonames.org/) for geographic entities;
- [Schema.org](https://schema.org/) for practical web-facing categories; and
- [NLTK WordNet](https://www.nltk.org/howto/wordnet.html) as a convenient
  programmatic interface to the pinned WordNet data.

Each source should remain source-labeled. Exact source concepts may be linked
across sources, but the project should not silently invent a replacement
classification when two standards disagree.

## Adapting a standard ontology to 20 Questions

The generator can turn a source graph into the current UI through this
pipeline:

- Import source nodes, stable identifiers, labels, definitions, frequencies,
  and authoritative edges.
- Select a game profile: common nouns, familiar entities, language, region,
  proper-name policy, and an explicit node budget.
- Choose candidate roots and estimate the candidate mass beneath each source
  node.
- At each displayed branch, select a source-supported split that most nearly
  balances the remaining candidate mass.
- Generate a suggested yes/no question from the selected distinction or from
  a declared source attribute.
- Apply deterministic tie-breakers so the same source release and profile
  reproduce the same page.
- Preserve every displayed node’s source ID and provenance in a sidecar data
  file or HTML attributes.

This separates **source semantics** from **game presentation**. Pruning,
ranking, and choosing one visible path are reversible build decisions; they
are not edits to WordNet, Wikidata, or another upstream ontology.

The generator should also measure:

- leaf and branch counts under the declared node-count convention;
- maximum and median visible depth;
- candidate balance at every question;
- duplicate labels and polysemous lemmas;
- source coverage of common game-answer lists; and
- browser load, search, expansion, and rendering time.

## Using the Human Knowledge outline

The likely source outline is the original
`Human Knowledge 2000/Old Text/Thoughts 1-8.html`, with the later
`Thoughts 2009.html` as a related revision. It is valuable because it contains
Brian’s conceptual organization of knowledge, but it is not a standard lexical
ontology and should not be treated as one.

There are several useful experiments:

### Overlay only

Parse headings, numbered sections, anchors, and explicit links from the HTML
into a separate outline graph. Use it as a navigational overlay on the
WordNet-derived game tree. This preserves the personal outline and reveals
where familiar game concepts land within it without changing the game tree.

### Graft as a separate profile

Import the outline’s headings as source-labeled branches and attach matching
WordNet synsets beneath them when the mapping is explicit or high-confidence.
Publish a second generated page such as `Human Knowledge × WordNet`, while
leaving the 20 Questions page unchanged. This is the safest way to explore how
the outline expands.

### Use the outline as a root hierarchy

Treat the personal outline as the visible root and graft WordNet subtrees under
its sections. This may be intellectually interesting and could expose a rich
conceptual map, but it will probably be less efficient for 20 Questions:
philosophical, scientific, and disciplinary divisions are not generally
balanced game discriminators. It should therefore be a separate view, not the
default game profile.

### Use the outline as a ranking prior

Keep WordNet as the canonical graph but give concepts that map to prominent
Human Knowledge sections a display boost or preferred root path. This combines
the standard ontology’s lexical coverage with the personal outline’s
interests, without making the personal classification authoritative.

The parser should preserve the original HTML filename, heading anchor, source
text, and extraction rules. Ambiguous matches should be reported for review,
not silently attached to an invented branch.

## Recommended next build

Build a comparison tool before replacing the current tree:

- import a pinned WordNet release;
- normalize the current 628 terminal labels;
- report WordNet matches, missing labels, and candidate additions;
- test food and prepared-dish coverage, including steak and salad;
- construct one or more 5K, 10K, and 20K game profiles;
- benchmark the existing single-page UI in the target browser; and
- separately parse the Human Knowledge outline and generate an overlay
  profile.

The default published page should remain the smallest profile that provides
good everyday coverage and stays pleasant to search and expand. The larger
profiles should be reproducible build artifacts, not hand-edited branches.
