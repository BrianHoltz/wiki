# Ontology

## Principles

- **Canonical projection:** The project maintains a human-facing single-parent
  tree over a richer source graph. The tree is a navigation view, not the
  complete ontology.
- **Current upper structure:** `Entity` has `Realized entity`, `Abstract
  entity`, `Property`, and `Relation`. `Realized entity` has `Object` and
  `Process`.
- **Current definitions:** `Entity` is an entity considered as a bearer of
  properties or participant in relations. `Realized entity` has physical
  embodiment or a location in space-time. `Abstract entity` is an idealized
  object considered apart from any particular realization.
- **One visible parent:** Every displayed node has one primary navigation
  parent. Alternate source parents remain metadata and cross-links.
- **Source fidelity:** Preserve source identifiers, labels, definitions,
  aliases, edges, and provenance. A projection may simplify presentation but
  must not silently rewrite source meaning.
- **No generated questions:** The browser provides search, lineage, expansion,
  counts, and definitions when supplied by the source. It does not generate
  suggested questions or question prompts.
- **No invented definitions:** Display a definition only when it is present in
  source material or an explicitly recorded project definition.
- **Blank-node safety:** Empty structural nodes are flattened into their
  nearest titled parent. Root lists are derived from incoming edges so a child
  cannot appear as a duplicate root.
- **Shared browser contract:** Every rendered tree uses the same controls,
  layout, renderer, and data contract. Only title, source data, and source
  links vary.
- **Evidence before scale:** Structural clarity, familiar labels, source
  coverage, and useful branching take priority over node count.

## Current state

The canonical browser is [My ontology](index.html). It is a curated
human-facing projection with historical and source-derived descendants. The
other browsers are separately named reference trees:

- [Human Knowledge](HumanKnowledge/index.html) — Brian Holtz's
  *Human Knowledge: Foundations and Limits* outline.
- [SUMO](SUMO/index.html) — a PDF-derived SUMO projection.
- [Roget's 1911 conceptual tree](Rogets/index.html) — the public-domain
  thesaurus classification.
- [Propædia](Propaedia/index.html) — Encyclopaedia Britannica's *Outline of
  Knowledge*.
- [Wikipedia categories](Wikipedia/index.html) — a category snapshot
  projected into a navigable tree.

The underlying source data may be a graph with multiple parents, facets, and
relations. The browser intentionally exposes one navigable projection while
retaining source graph information in JSON and manifests.

## Canonical hierarchy

```text
Entity
├── Realized entity
│   ├── Object
│   └── Process
├── Abstract entity
├── Property
└── Relation
```

`Object` is a physical entity that is spatially bounded or self-connected.
`Process` is an entity that unfolds, persists, or changes through time as an
event, process, activity, transition, or state. `Property` is a repeatable
characteristic, capability, disposition, or value attributable to an entity.
`Relation` is a way in which two or more entities are connected, compared, or
ordered.

## Prior art

Prior art is grouped by the problem each system solves. None is adopted
wholesale as the canonical visible tree.

### Lexical and conceptual systems

- **WordNet** supplies synsets, glosses, corpus frequencies, and hypernymy.
  It is the principal lexical source for common nouns, but its multiple
  inheritance and disconnected records require a declared projection.
- **Roget's Thesaurus** supplies broad conceptual classes and synonym
  neighborhoods. It is useful for wording and vocabulary discovery, not as a
  reliable `is-a` taxonomy.
- **FrameNet** organizes meanings around situations, roles, and lexical
  realizations. It is useful for event and participant metadata.
- **Propædia** organizes human knowledge into domains and disciplines. It is
  useful for coverage audits, not noun parentage.
- **Schema.org** supplies familiar contemporary labels for people, places,
  products, events, creative works, and intangible entities. It is shallow and
  web-oriented.

### Formal upper ontologies and logic

- **SUMO** supplies formal entities, objects, processes, attributes, relations,
  axioms, and WordNet mappings. It is the strongest semantic validation
  source in this project, but too formal to display raw.
- **BFO** distinguishes continuants and occurrents, material entities,
  processes, qualities, roles, functions, and dispositions.
- **DOLCE** distinguishes endurants, perdurants, qualities, regions,
  abstracts, and social objects for linguistic and cognitive modeling.
- **GFO** supplies continuants, presentials, processes, time, space, and
  levels of reality.
- **UFO** models objects, events, dispositions, situations, roles, relators,
  qualities, and social commitments.
- **Sowa's ontology** combines physical/abstract, independent/relative, and
  continuant/occurrent distinctions in a lattice rather than a tree.
- **Aristotle's Categories** separates substance, quantity, quality, relation,
  place, time, position, state, action, and passion. It remains a sanity
  check, not a game hierarchy.
- **Cyc/OpenCyc** models common-sense classes, individuals, predicates, rules,
  and context-sensitive microtheories. Its reasoning scope exceeds this
  browser's needs.
- **RDF, RDFS, OWL, Common Logic, and SHACL** provide graph, vocabulary,
  logical, and validation standards. They are implementation infrastructure,
  not visible noun trees.

### Biology

Biological taxonomy is the clearest case where scientific ancestry is useful
prior art but a poor default interface. The project should retain a
scientifically defensible source tree and a compressed, familiar display.

- **Catalogue of Life** is the leading candidate for accepted names,
  synonyms, and broad checklist authority.
- **Open Tree of Life** is the leading candidate for evolutionary ancestry,
  stable taxon identifiers, and source-linked relationships.
- **GBIF Backbone Taxonomy** is strong for name resolution and synonymy across
  biodiversity datasets.
- **NCBI Taxonomy** is authoritative for sequence-linked scientific identity,
  especially microbes and viruses, but too technical for the visible tree.
- **ITIS** and **Catalogue of Life** provide stable-name cross-checks.
- **WoRMS** is a specialist marine supplement.
- **OneZoom** is the best interface prior art for navigating a very large
  evolutionary tree.
- **TimeTree** supplies divergence-time context and evolutionary validation.

The biological display should use three layers:

- **Source layer:** preserve accepted scientific parentage, identifiers,
  synonyms, and intermediate clades.
- **Navigation layer:** retain ancestors that create a useful distinction or
  explain a notable organism; compress unhelpful one-child rank chains.
- **Answer layer:** show familiar names such as mammals, birds, dinosaurs,
  marsupials, monotremes, and coelacanths, with scientific notes as metadata.

This is a display projection, not permission to redraw evolutionary history.
Open Tree of Life and Catalogue of Life are validation candidates; OneZoom is
the interface model; TimeTree supplies historical context.

### Mathematics and logic

Mathematical and logical systems organize formal objects, theories, proofs, and
relations rather than everyday nouns.

- **MSC2020** classifies mathematical literature and disciplines. Use it as a
  subject facet, never as the parent of `Circle`, `Algorithm`, or `Group`.
- **OpenMath** represents mathematical objects and expressions through symbols
  and content dictionaries.
- **OMDoc** represents definitions, theorems, proofs, examples, and theories.
- **MMT** represents symbols, structures, imports, and translations across
  formal theories.
- **Lean/Mathlib, Coq, Agda, Isabelle, and HOL** expose machine-checked
  definitions, types, terms, and proofs; their dependency graphs are not
  general noun hierarchies.
- **ZFC, NBG, type theory, dependent type theory, category theory, topos
  theory, model theory, and universal algebra** provide foundations and
  structural vocabularies.
- **Formal methods and proof assistants** distinguish syntax, axioms,
  derivations, interpretations, and models.

The project should use these systems as metadata and validation sources. A
future mathematical branch may include algorithms, graphs, functions,
automata, formal languages, structures, propositions, proofs, and theories,
but should not graft a literature classification directly into the visible
tree.

### Product, food, geography, and knowledge organization

- **FoodOn** is a targeted source for prepared foods and food production.
- **Google Product Taxonomy, GS1 GPC, UNSPSC, eCl@ss, and ETIM** provide
  practical artifact and product vocabulary, but their department structures
  are not universal ontologies.
- **CIDOC CRM, FRBR/IFLA LRM, GeoSPARQL, and ISO 15926** model cultural
  heritage, bibliographic identity, geography, and engineering lifecycles.
- **Wikidata, DBpedia, Wikipedia categories, and DMOZ** provide broad entity,
  article, and topical coverage. They require source snapshots, graph
  validation, and an explicit display projection.
- **Human Knowledge: Foundations and Limits** is a personal outline of
  philosophy, mathematics, natural science, technology, and social science.
  It is rendered as a separate reference tree, not treated as the canonical
  ontology's root.

## Compact upper-level comparisons

```text
Our ontology
Entity
├── Realized entity
│   ├── Object
│   └── Process
├── Abstract entity
├── Property
└── Relation

SUMO
Entity
├── Physical
│   ├── Object
│   └── Process
└── Abstract

BFO
Entity
├── Continuant
│   └── Independent continuant
│       └── Material entity
│           └── Object
└── Occurrent
    └── Process

DOLCE
Particular
├── Endurant
│   └── Physical endurant
│       └── Physical object
├── Perdurant
│   └── Event
├── Quality
└── Abstract

Schema.org
Thing
├── Place
├── Product
├── CreativeWork
└── Event

WordNet
Entity
├── Physical entity
│   └── Thing
│       └── Object
└── Abstraction

Aristotle
Being
└── Substance
    └── Body
```

These compact trees are comparison aids. They do not imply that the systems
share definitions or that any one of them is the project's hidden canonical
hierarchy.

## Implementation

### Data and projection contract

Each browser dataset contains `source`, `root`, `rootNodes`, `nodes`, and
`stats`. Each node has an `id`, `label`, `children`, optional `definition`,
and optional source or alternate-parent metadata.

The projection pipeline:

- retains source IDs and source edges;
- chooses one primary display parent;
- preserves alternate parents as metadata;
- removes empty structural nodes from the display;
- derives displayed roots from incoming edges;
- computes direct-child and descendant counts; and
- emits a normalized JSON dataset for the shared renderer.

### Shared browser

The six pages use identical CSS and renderer code. The renderer provides
search, result lineage, source links, definition expansion, expand/collapse,
child counts, descendant counts, and the upper-left lineage control. It does
not provide generated questions or suggested searches.

The regression suite is [`test_browser.js`](test_browser.js). It checks data
integrity, roots, branches, leaves, definitions, source links, structural
normalization, and exact renderer/style parity.

### WordNet regeneration

WordNet is retained as a reproducible lexical experiment, not as an active
question-generation system. [`generate_wordnet_20q.py`](generate_wordnet_20q.py)
loads local WordNet 3.0 through NLTK, selects a declared frequency-ranked
source pool connected to `entity.n.01`, closes over required hypernyms, chooses
one deterministic display parent, and writes the HTML, YAML, and manifest.

Regenerate the existing profile with:

```sh
NLTK_DATA=~/nltk_data /tmp/wordnet-ontology-venv/bin/python \
  generate_wordnet_20q.py --target 7000 --output-dir .
```

The generated profile is useful for source comparison and coverage analysis;
its old suggested-question text is retired.

### SUMO projection

The SUMO browser uses the checked-in PDF graph, not current KIF. The
reproducible path is:

- extract vector edges and labels from the official PDF;
- choose one primary incoming edge when a node has multiple parents;
- retain removed parents as alternate metadata;
- apply only declared provisional placements; and
- generate the normalized browser JSON.

The current browser has `Entity` as its only root. The four provisional
placements are `List → Set`, `Number → Quantity`, `Predicate → Proposition`,
and `Sentence → Proposition`.

### Human Knowledge and Propædia

The Human Knowledge dataset is generated by
[`HumanKnowledge/generate_human_knowledge.py`](HumanKnowledge/generate_human_knowledge.py)
from the book's outline in `Thoughts/HumanKnowledge.txt`. It does not invent
definitions.

The Propædia dataset is generated from the checked-in public outline source.
Its generated question prompts are not rendered as definitions.

## History

- The project began as a broad 20 Questions noun hierarchy and first produced
  a handcrafted, player-facing tree.
- A mechanically expanded v2 profile was tested and retired after its
  source-driven ancestry produced unary chains, weak splits, and poor
  nonliving coverage.
- WordNet was added as a standards-based lexical experiment and retained as
  an auditable source comparison, not a replacement for the curated tree.
- The canonical upper hierarchy was revised to `Entity`, with `Realized
  entity` and `Abstract entity` as the principal entity distinction and
  `Object`/`Process` under realized entities.
- SUMO, Roget, Propædia, Wikipedia, and Human Knowledge received separate
  rendered browsers over the shared interface.
- The Human Knowledge browser was corrected to use Brian Holtz's book rather
  than the Britannica Propædia outline.
- The Collection-to-Group edge and other source projection defects were
  repaired; blank structural nodes and duplicate roots are now normalized
  before rendering.
- Alternate-parent and alternate-child panels were removed from the visible
  interface while source metadata was retained.
- Generated suggested questions and preset suggestions were removed from the
  active browsers.

## Future scope

The next useful work is evidence-driven structural review, not another
wholesale expansion:

- audit branch balance and misplaced or duplicate visible labels;
- improve biological coverage using the source/display/answer layers above;
- review mathematical, food, artifact, and geographic gaps;
- map candidate leaves to source identifiers and definitions; and
- keep each source tree separately labeled and reproducible.
