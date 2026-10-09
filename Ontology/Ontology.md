# Ontology

## Principles

- The handcrafted v1 remains the player-facing canonical tree; imported systems
  are source, audit, and enrichment layers rather than replacements.
- The visible navigation tree has one primary parent per node. Alternate
  parents, aliases, definitions, source IDs, and provenance remain in data.
- The canonical upper structure is `Entity`, with `Realized entity` and
  `Abstract entity` as its principal distinction; `Object` and `Process` are
  children of `Realized entity`.
- The browser is a shared static, searchable, collapsible tree. It does not
  generate suggested questions, and it displays definitions only when supplied
  by source material or an explicit project definition.
- Source graphs remain authoritative. A one-parent tree is a reproducible
  navigation projection, not a semantic rewrite.
- Structural quality, familiar labels, useful branching, and source fidelity
  take priority over node count or premature vocabulary expansion.
- **Biology:**
  - Preserve evolutionary ancestry, including birds within dinosaurs and mammals within synapsids.
  - Keep every biological subtree monophyletic.
  - Record source, release, stable ID, rank, and date for each placement.
  - Balance familiar, agricultural, medical, ecological, extinct, and unusual taxa.
  - Prefer readable common labels; retain scientific names and aliases in metadata.
  - Compress uninformative ranks while preserving the hidden source path.
  - Keep convergent forms separate and record convergence metadata.
  - Keep extinct taxa in evolutionary context with extinct status.
  - Use one visible parent; retain alternate placements, synonyms, and source edges.
  - Expose branches only for useful distinctions and balance major clades.
  - Version snapshots and migration reports so updates cannot silently move leaves.
  - Give viruses a separate acellular-infectious-agent branch with host, genome, and transmission metadata.
  - Do not imply that viruses form one clean ranked lineage.
  - Include familiar, high-impact, food, pet, farm, disease, keystone, extinct, and evolutionary-example taxa.
  - Put scientific-only names in metadata unless they have a clear player interpretation.

## What to add

- **Categories**
  - Upper-ontology branches and missing semantic distinctions.
  - Biological clades with monophyletic, source-backed ancestry.
  - Product categories for tools, foods, appliances, clothing, vehicles, electronics, materials, and household goods.
  - Coverage categories from Propædia, Schema.org, Wikipedia, WordNet, Roget, and FoodOn.
- **Individuals**
  - Familiar, high-impact, agricultural, medical, extinct, and evolutionary-example taxa.
  - Viruses and other acellular infectious agents.
  - Everyday nouns for foods, materials, vehicles, body parts, places, occupations, cultural objects, people, and fictional entities.
  - Product leaves and lexical aliases supported by WordNet, Roget, Wiktionary, and encyclopedic sources.

## Prior art

### Biology

The immediate biological task is to replace the current organism subtree with
a curated display taxonomy. The links below are ordered by usefulness for this
project, not by scientific authority alone:

- [OneZoom Tree of Life Explorer](https://www.onezoom.org/) — best browsing
  model for a large evolutionary tree; use its interface and common-name
  presentation as design prior art, not as the sole authority.
- [Open Tree of Life](https://tree.opentreeoflife.org/) — strongest open
  candidate for evolutionary ancestry, stable taxon identifiers, and a tree
  that keeps humans within tetrapod and lobe-finned-fish history.
- [Catalogue of Life](https://www.catalogueoflife.org/explore) — strongest
  candidate for accepted names, synonyms, and broad checklist authority;
  compare its Base and Extended releases.
- [GBIF Backbone Taxonomy](https://www.gbif.org/species) — excellent
  browsable name-resolution and synonymy backbone for finding and normalizing
  familiar organisms.
- [NCBI Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi)
  — authoritative computational and sequence-linked taxonomy, especially for
  microbes and viruses; too technical to copy directly.
- [ITIS](https://www.itis.gov/) — stable government-supported name and rank
  reference useful for cross-checking accepted placement.
- [World Register of Marine Species](https://www.marinespecies.org/) —
  expert-maintained marine supplement, not a general root.
- [TimeTree](https://timetree.org/) — useful for evolutionary relationships
  and divergence context, not as the visible noun hierarchy.

#### Online biological taxonomies

These resources are the strongest available prior art for extending the
organism portion of a general noun hierarchy. None is a complete general
ontology: they optimize taxonomic identity, scientific names, synonymy, and
research interoperability rather than familiar labels or balanced gameplay.

##### Catalogue of Life

- **Origin:** an international taxonomic data initiative launched in 2001,
  coordinated through the Species 2000 and Integrated Taxonomic Information
  System communities and now hosted by the Catalogue of Life partnership.
- **Current status:** active and release-based. The [Catalogue of Life
  releases](https://www.catalogueoflife.org/data/download) distinguish a
  verified Base Release from a broader Extended Release.
- **Node count:** release-dependent; the current catalog reports millions of
  accepted species and names, with counts varying by release and inclusion
  policy. Use the release metadata rather than a timeless number.
- **Prominence proxy:** widely used as a global checklist and taxonomic
  reference, with expert-verified coverage and downloadable releases.
- **Fit:** the best initial authority for accepted organism names and
  high-level taxonomic placement. It should supply biological structure while
  the curated tree supplies playable common-language grouping.

##### GBIF Backbone Taxonomy

- **Origin:** built by the Global Biodiversity Information Facility, an
  international intergovernmental biodiversity-data infrastructure founded in
  2001.
- **Current status:** active, versioned, and designed to normalize names from
  many biodiversity datasets. See the
  [GBIF Backbone Taxonomy](https://www.gbif.org/dataset/7ddf754f-d193-4cc9-b351-99906754a03b).
- **Node count:** release-dependent and measured in names, taxa, and
  synonymized records rather than one fixed class count.
- **Prominence proxy:** GBIF is a major global biodiversity data network; its
  backbone is used for occurrence-data name matching across a large
  publishing ecosystem.
- **Fit:** excellent for resolving common names and synonyms to scientific
  taxa and for finding candidate organisms. It is more of a cross-dataset
  nomenclatural backbone than a carefully curated game hierarchy.

##### NCBI Taxonomy

- **Origin:** developed by the National Center for Biotechnology Information
  at the U.S. National Library of Medicine to organize organisms represented
  in genetic and genomic databases.
- **Current status:** active, continuously updated, and available through the
  [NCBI Taxonomy database](https://www.ncbi.nlm.nih.gov/taxonomy).
- **Node count:** release- and database-dependent; it contains hundreds of
  thousands of scientific taxa and many sequence-associated records, with
  counts exposed through NCBI's statistics and downloads.
- **Prominence proxy:** it is embedded in GenBank, RefSeq, and other major
  NCBI sequence resources, making it a standard computational taxonomy for
  molecular biology.
- **Fit:** authoritative for sequence-linked scientific identity and useful
  for validating deep organism branches, but too technical and unevenly
  familiar to serve as the visible game taxonomy.

##### Open Tree of Life

- **Origin:** an open-science collaboration funded by the U.S. National
  Science Foundation and other partners, launched in the 2010s.
- **Current status:** active research infrastructure combining a synthetic
  tree with source taxonomies and stable taxon identifiers. Browse it at the
  [Open Tree of Life](https://tree.opentreeoflife.org/).
- **Node count:** release-dependent and measured in taxa and phylogenetic
  relationships; the synthetic tree incorporates millions of named taxa from
  contributing sources.
- **Prominence proxy:** open APIs, stable identifiers, and published
  computational methods make it a notable research platform for large-scale
  comparative biology.
- **Fit:** useful for scientifically coherent ancestry and for checking
  extinct groups, including dinosaurs. It should be treated as a validation
  and enrichment source, not copied wholesale into a one-page game tree.

##### Integrated Taxonomic Information System (ITIS)

- **Origin:** a U.S. and international interagency project established in the
  1990s to provide authoritative taxonomic names and hierarchy.
- **Current status:** active, maintained, and available through the
  [ITIS database](https://www.itis.gov/).
- **Node count:** release-dependent, with hundreds of thousands of taxonomic
  names and records across included organism groups.
- **Prominence proxy:** long-running government-supported identifiers and
  reuse in biodiversity and environmental datasets.
- **Fit:** a useful stable-name and rank authority, especially for
  cross-checking Catalogue of Life and GBIF mappings. Its coverage and
  scientific granularity are too specialized to define the whole game tree.

##### World Register of Marine Species

- **Origin:** an international marine-taxonomy initiative launched in 2007
  and coordinated through the Flanders Marine Institute.
- **Current status:** active, expert-managed, and release-based; see
  [WoRMS](https://www.marinespecies.org/).
- **Node count:** release-dependent, with hundreds of thousands of marine
  taxa and names across accepted and synonymized records.
- **Prominence proxy:** the principal global reference for marine organism
  names and taxonomic status.
- **Fit:** a high-quality specialized supplement for marine life, but not a
  general organism root.

#### Approachable cladistic and evolutionary trees

The most useful biological prior art for v2 is not a single taxonomy copied
verbatim. It is a scientifically defensible source tree paired with a
deliberately compressed display. A cladistic source should be allowed to say
that humans are sarcopterygian vertebrates and therefore nested within the
broader evolutionary history of fishes, even though “fish” remains an
everyday answer category. The visible game tree can collapse intermediate
clades when they do not create a recognizable answer or a useful question,
while retaining the omitted clades, ranks, and source identifiers in metadata.

##### OneZoom Tree of Life Explorer

- **Origin:** conceived in 2011, released as open-source software in 2012,
  and maintained since 2015 by a UK charitable organization.
- **Current status:** active, free, and designed explicitly for public
  exploration. OneZoom uses a fractal, map-like interface so a very large
  tree can be explored on one page; its current tree relies heavily on the
  Open Tree of Life and mixes other declared sources. See the
  [OneZoom explorer](https://www.onezoom.org/) and its
  [data and methodology overview](https://www.onezoom.org/about.html).
- **Node count:** the project is intended to display a million-tip-scale tree;
  the exact visible count changes with its source-data release and display
  configuration.
- **Prominence proxy:** open-source software, a charitable organization,
  collaboration with the Linnean Society, and published methods including
  [Dynamic visualisation of million-tip trees](https://doi.org/10.1111/2041-210X.13766).
- **Fit:** the best interface prior art for keeping a huge scientifically
  grounded tree navigable. Its species-first display is too deep and
  biological for the whole ontology, but its zoomed overview,
  common names, images, and source links suggest how v2 can hide taxonomic
  detail without discarding it.

##### TimeTree

- **Origin:** developed by Blair Hedges, Sudhir Kumar, and collaborators as a
  public knowledge base for evolutionary relationships and divergence times;
  the current major resource is TimeTree 5.
- **Current status:** active research and teaching resource. The
  [TimeTree site](https://timetree.org/about) combines published divergence
  estimates and lets users explore the evolutionary timescale between taxa.
- **Node count:** release-dependent; TimeTree 5 is a large species-level
  synthesis rather than a compact hand-authored hierarchy. Its useful unit is
  a dated relationship, not a game category.
- **Prominence proxy:** TimeTree 5 is described in a 2022 article in
  *Molecular Biology and Evolution*,
  [An Expanded Resource for Species Divergence Times](https://doi.org/10.1093/molbev/msac174).
- **Fit:** useful for validating evolutionary-history examples and explaining
  why apparently different organisms are convergent rather than close
  relatives. It should validate relationships and dates, not dictate every
  visible v2 split.

##### Recommended collapsed-clade pattern

These resources support a three-layer design for the life portion of v2:

- **Source layer:** retain the accepted scientific tree, including clades
  that are important for statements such as “tetrapods are nested within
  lobe-finned fishes.”
- **Navigation layer:** retain only ancestors that create a useful
  distinction, explain a notable organism, or keep the visible branch
  intelligible. Collapse ranks such as some orders and families when all
  selected descendants would otherwise form a one-child chain.
- **Answer layer:** show familiar common names and notable clades such as
  mammals, birds, marsupials, dinosaurs, coelacanths, and monotremes. Add a
  short scientific note where everyday language hides a meaningful
  relationship, rather than forcing the player to answer with a Latin clade.

This is not permission to redraw evolutionary relationships for convenience.
It is a presentation projection: source parentage, alternate placements,
synonyms, and suppressed intermediate clades remain auditable. OneZoom is the
strongest model for the browsing interaction; Open Tree of Life and Catalogue
of Life remain the principal candidates for taxonomic validation; and TimeTree
is the best supplement for evolutionary-history and divergence-time context.

#### Single-pane and compressed tree renders

The previous list was not responsive to the requirement. The intended format
is now clear from this [Open University-style example image](https://miro.medium.com/v2/resize:fit:4128/1*O-o2WDx710kxPczPH0UUug.jpeg):
one tall, printable pane; colored evolutionary branches; named internal
clades; and a curated representative organism, fossil, or plant at many
leaves. This is not merely an outline of taxon names. It is a visual
knowledge map that makes the biological hierarchy browseable through familiar
specimens. The matching high-resolution copy is
[available here](https://nicolasmicheletti.wordpress.com/wp-content/uploads/2015/09/treeoflife.jpg).

The useful search target is therefore a static classroom/poster-style
whole-life tree with fewer than 300 representative leaves and clade labels.
Ranked by fit:

- [Open University tree-of-life poster](https://nicolasmicheletti.wordpress.com/wp-content/uploads/2015/09/treeoflife.jpg)
  — the exact format we should pursue. It uses roughly a hundred
  representative organisms and fossils, colored branches, readable clade
  labels, and a single origin-to-present composition. It is much closer to
  the desired 20-Questions browsing experience than a genome-only tree.
  Treat the image as presentation prior art; validate and modernize its
  taxonomy from the authoritative sources above.
- [Tree of life SVG](https://commons.wikimedia.org/wiki/File:Tree_of_life_SVG.svg)
  — still worth checking as a denser candidate, but it is a genome tree with
  tiny labels rather than a specimen-rich educational map. It may contain
  150–250 visible terminal taxa, though the vectorized lettering requires
  visual counting.
- [Phylogenetic tree of life 2](https://commons.wikimedia.org/wiki/File:Phylogenetic_tree_of_life_2.svg)
  — the cleanest strict single-pane baseline: one rooted left-to-right tree
  with 33 machine-countable labels, spanning Bacteria, Archaea, and Eukarya.
  It is public domain and easy to print, but too sparse to be the final target.
- [Tree of life](https://commons.wikimedia.org/wiki/File:Tree_of_life.svg)
  — one radial tree with approximately 35–50 readable group labels,
  including major bacterial, archaeal, fungal, plant, and animal branches.
  It is compact and visually legible, but scientifically dated and not a
  current authority.
- [Berkeley Evolution 101: The Family Tree](https://evolution.berkeley.edu/evolution-101/the-history-of-life-looking-at-the-patterns/the-family-tree/)
  — explicitly school-oriented and broad, with a single tall image containing
  nested phylogenies. It is useful presentation prior art, but not a strict
  uninterrupted single-pane outline because it embeds several zoomed trees.
- [UCMP Life on Earth / Three Domains of Life](https://ucmp.berkeley.edu/alllife/threedomains.html)
  — a compact educational whole-life treatment that gives viruses their own
  biological-entities branch and links to deeper exhibits. It is a strong
  model for visible-versus-linked detail, but it is smaller and partly
  page-linked rather than a 300-node poster.
- [Tree of life diagrams and historical examples](https://en.wikipedia.org/wiki/Tree_of_life_(biology))
  — a useful index of static Haeckel, Woese, and other whole-life diagrams.
  These are schematic or historical rather than importable authorities, but
  they provide additional candidates for visual comparison.

The immediate next step is to inspect the first SVG at full resolution and
count its visible labels. If it is genuinely below 300, it becomes the
largest discovered single-pane template; if it is too dense or exceeds the
limit, the 33-label tree is the verified fallback and we should construct an
intermediate 100–300-node display ourselves from the authoritative source
combination below.

#### Compressed taxon-backbone target

The poster is useful as a visual clue to the desired *kind* of taxonomy, but
its organism illustrations are not yet the target data. First reconstruct a
single-parent taxon tree whose nodes express the most important evolutionary
divisions and transitions; only afterward add representative, familiar,
important, and notable species beneath selected taxon leaves.

The first-pass backbone should preserve this path, while telescoping
specialist-only ranks and unstable deep clades:

```text
Cellular life
├── Bacteria
├── Archaea
└── Eukaryota
    ├── Archaeplastida
    │   ├── Red algae
    │   └── Green plants
    │       ├── Green algae
    │       └── Land plants
    │           ├── Bryophytes
    │           └── Vascular plants
    │               ├── Ferns and horsetails
    │               └── Seed plants
    │                   ├── Gymnosperms
    │                   │   └── Conifers
    │                   └── Flowering plants
    │                       ├── Early-diverging groups and magnoliids
    │                       ├── Monocots
    │                       └── Eudicots
    ├── Major protist lineages
    │   ├── SAR
    │   ├── Amoebozoa
    │   └── Other deep eukaryote branches
    └── Opisthokonta
        ├── Fungi
        │   ├── Early-diverging fungi
        │   └── Dikarya
        │       ├── Ascomycota
        │       └── Basidiomycota
        └── Animals
            ├── Sponges, comb jellies, placozoans and cnidarians
            └── Bilaterians
                ├── Protostomes
                │   ├── Arthropods and other ecdysozoans
                │   └── Molluscs, annelids and other spiralians
                └── Deuterostomes
                    ├── Echinoderms
                    └── Chordates
                        ├── Tunicates and lancelets
                        └── Vertebrates
                            ├── Jawless vertebrates
                            └── Jawed vertebrates
                                ├── Cartilaginous fishes
                                └── Bony vertebrates
                                    ├── Ray-finned fishes
                                    └── Lobe-finned vertebrates
                                        ├── Coelacanths and lungfishes
                                        └── Tetrapods
                                            ├── Amphibians
                                            └── Amniotes
                                                ├── Synapsids
                                                │   └── Mammals
                                                └── Sauropsids
                                                    ├── Lepidosaurs and turtles
                                                    └── Archosaurs
                                                        ├── Crocodilians
                                                        └── Dinosaurs
                                                            ├── Non-avian dinosaurs
                                                            └── Birds
```

This wording deliberately uses **bony vertebrates** rather than only “bony
fish,” because tetrapods are nested within Osteichthyes, and **lobe-finned
vertebrates** rather than only “lobe-finned fish,” because tetrapods are
nested within Sarcopterygii. It also places birds inside dinosaurs and
mammals inside synapsids. “Fish,” “algae,” “protist,” “invertebrate,” and
“reptile” may remain familiar search or display labels, but should not be
silently treated as equivalent to clean clades.

The backbone should retain evolutionary milestones as node annotations rather
than inventing extra taxon branches: cellular organization, mitochondria,
plastids, multicellularity, land plants, vascular tissue, seeds, flowers,
animal bilateral symmetry, moulting, jaws, bony skeletons, lobed fins,
limbs, amniotic reproduction, feathers, and mammalian traits. Deep microbial
and protist topology should use compact polytomies or “major lineages” until
the source evidence justifies more resolution. Horizontal gene transfer,
endosymbiosis, uncertain roots, and disputed deep relationships belong in
provenance and notes, not hidden by false precision.

Recommended source combination: use Open Tree of Life for evolutionary
structure, Catalogue of Life for accepted names and synonyms, GBIF and NCBI
for normalization and coverage checks, and OneZoom as the browsing-model
reference. Use ITIS, WoRMS, and TimeTree to resolve domain-specific gaps.
Do not import any of these raw. Produce one reviewed crosswalk that preserves
source IDs, accepted names, synonyms, rank, release, extinct status, and
alternate placements while projecting a readable single-parent display tree.

The visible tree should preserve major evolutionary facts—birds under
dinosaurs and humans within tetrapods and lobe-finned fishes—while collapsing
intermediate clades that do not improve a recognizable distinction. Common
names lead; scientific names remain searchable aliases and provenance.
Viruses receive a dedicated acellular-infectious-agent subtree with host,
genome, transmission, disease, and ecological metadata rather than being
forced into ordinary organism ancestry.

The detailed criteria, notable-life policy, virus policy, and graft workflow
below are the acceptance specification for this task. The later biological
prior-art entries retain source-specific notes and access details.


The figures below are scale or activity proxies, not claims that unlike
systems have directly comparable “node” semantics. Counts are release- or
snapshot-dependent; links are the authoritative places to refresh them.

### WordNet

- **Origin:** Princeton University, United States; George Miller’s project
  began in 1985, with the first public release in 1989.
- **Current status:** actively documented and distributed; this experiment uses
  WordNet 3.0 through [NLTK](https://www.nltk.org/howto/wordnet.html).
- **Node count:** 117,659 synsets in WordNet 3.0 overall; 82,115 noun synsets
  in the experiment’s installed corpus.
- **Prominence proxy:** 13,739 noun synsets have nonzero corpus-frequency
  counts in the release; the foundational
  [WordNet paper](https://doi.org/10.1007/978-94-011-2016-8_2) is a standard
  reference point for lexical-semantic systems.
- **Fit:** best initial canonical backbone for common noun gameplay.

### Upper ontologies

These systems are design prior art, not replacements for the canonical tree.
They contribute distinctions, metadata patterns, validation methods, or
coverage; none should dictate the visible hierarchy wholesale.

- **Aristotle's Categories:** substance, quantity, quality, relation, place,
  time, position, state, action, and passion. Useful as a sanity check that
  things, properties, relations, and events are not conflated.
- **Sowa's Knowledge Representation Ontology:** a lattice of physical and
  abstract, independent, relative, and mediating entities, including objects,
  processes, schemas, scripts, situations, and descriptions. Useful as a
  typed overlay, not a tree.
- **Cyc/OpenCyc:** classes, individuals, predicates, rules, exceptions, and
  context-sensitive microtheories. Useful for common-sense relations, but too
  large and access-constrained for the visible browser.
- **SUMO:** a formal hierarchy of entities, objects, processes, attributes, and
  relations with axioms and WordNet mappings. Best formal validation backbone;
  project it to one display parent rather than showing it raw.
- **Schema.org:** practical types for people, organizations, places, products,
  events, creative works, medical entities, and intangible things. Useful for
  contemporary labels and aliases, but shallow and web-oriented.
- **BFO:** continuants, occurrents, material entities, processes, qualities,
  roles, functions, dispositions, and sites. Useful for principled type checks.
- **DOLCE:** endurants, perdurants, qualities, regions, abstracts, and social
  objects. Useful for linguistic and cognitive distinctions.
- **GFO and UFO:** continuants, presentials, processes, events, objects,
  dispositions, situations, roles, relators, qualities, and social facts.
  Useful comparison families for time and dependence.
- **OntoClean:** rigidity, identity, unity, and dependence as tests for whether
  a proposed subclass relation is semantically defensible.
- **gist and PROTON:** compact practical upper vocabularies for things,
  people, organizations, events, places, information, and abstract concepts.
  Useful candidates for interoperable metadata.
- **Roget, WordNet, FrameNet, and Propædia:** lexical neighborhoods, synsets,
  frames, and knowledge domains. Useful enrichment sources, not `is-a` roots.
- **RDF/RDFS, OWL, Common Logic, and SHACL:** graph, vocabulary, logic, and
  validation infrastructure. They support the data model rather than define
  the visible noun tree.
- **Mereology, social ontology, and process ontology:** part-whole,
  institution, role, norm, event, activity, and change distinctions that the
  tree should preserve as typed relations or facets.

The combined design lesson is to keep entity kinds, properties, relations,
processes, information, and formal structures distinct; retain time,
dependence, part-whole, and social context as metadata; and use formal
ontologies to audit definitions and mappings rather than to supply the whole
player-facing branch order.

### Mathematics

Mathematics needs its own prior-art subsection because the available systems
solve different problems and none is a ready-made noun taxonomy:

- **MSC2020** is the strongest maintained classification of mathematical
  literature. It is a subject and discipline classification, not a taxonomy
  of mathematical entities. Use it as an orthogonal subject facet, never as
  the parent of `Circle`, `Algorithm`, or `Group`.
- **[OpenMath](https://openmath.org/)** represents the semantics of
  mathematical objects and expressions through symbols and content
  dictionaries. It is the best candidate for semantic symbols, operations,
  functions, and relations, but it is not a complete browseable hierarchy.
- **[OMDoc](https://en.wikipedia.org/wiki/OMDoc)** extends OpenMath to
  definitions, theorems, proofs, examples, and theories. It is especially
  useful for separating a mathematical object from a statement about it and
  from a proof or theory containing it.
- **[MMT](https://uniformal.github.io/)** is a foundation-independent
  framework for formal theories, symbols, structures, imports, and
  translations. It is a metamodel for mathematical knowledge, not a
  player-facing tree.
- **[Lean and Mathlib](https://github.com/leanprover-community/mathlib4)**
  provide a large modern typed dependency graph of definitions, structures,
  theorems, proofs, and typeclass relationships. They are valuable for
  validating modern formal practice, but raw Mathlib ancestry reflects proof
  engineering rather than a general-purpose noun hierarchy.
- **OntoMathPRO** is the closest candidate for an ontology of mathematical
  knowledge, including mathematical concepts, objects, theories, formulas,
  theorems, and proofs. Its maintenance, licensing, machine-readable
  distribution, and possible inheritance of subject-classification
  structure require a dedicated audit before grafting.
- **Type theory, category theory, set theory, and model theory** provide
  foundations and structural languages. They supply types, terms, values,
  proofs, sets, functions, morphisms, models, and interpretations, but none
  should be copied wholesale as the visible mathematical branch.
- **MathML and related notation standards** represent syntax or presentation
  and therefore belong in the representation layer, not as the taxonomy of
  the mathematical things represented.

The current grafting hypothesis is therefore selective: use OpenMath and
OMDoc for semantic mathematical objects and formal statements, MMT for
cross-foundation theory structure, Lean/Mathlib for modern machine-checked
examples, and MSC2020 as metadata. Do not graft MSC2020's disciplines into
the noun tree. The entity branch should say `Computational structures` with
separate children such as `Algorithms`, `Complexity classes`, `Computable
functions`, `Recursive functions`, `Automata`, `Formal languages`, and
`Graphs`, rather than a mixed node such as “Algorithms and complexity
classes.”


### Upper Ontology Excerpts

#### Our ontology

```text
Entity: an entity considered as a bearer of properties or participant in relations.
├── Realized entity: an entity with a physical embodiment or location in space-time.
│   ├── Object: a physical entity that is spatially bounded or self-connected.
│   └── Process: an entity that unfolds, persists, or changes through time as an event, process, activity, transition, or state.
├── Abstract entity: an idealized object considered apart from any particular realization.
├── Property: a repeatable characteristic, capability, disposition, or value attributable to an entity.
└── Relation: a way in which two or more entities are connected, compared, or ordered.
```

#### Sowa's Knowledge Representation Ontology

```text
Entity: anything that exists, whether physical or abstract.
├── Physical: an entity located in the physical world.
│   ├── Continuant: a physical entity that persists through time.
│   │   └── Object: a physical continuant with an independent identity.
│   └── Occurrent: a physical entity that unfolds or occurs in time.
└── Abstract: an entity that exists only as an abstraction.
    ├── Continuant: an abstract entity treated as persistent.
    └── Occurrent: an abstract entity treated as temporal or occurring.
```

#### Suggested Upper Merged Ontology

```text
Entity: the universal class containing every object in the ontology.
├── Physical: entities that have a location in space or time.
│   ├── Object: a physical entity that is not a process.
│   │   └── SelfConnectedObject: an object whose parts are connected.
│   └── Process: a physical entity that has temporal parts or stages.
└── Abstract: entities that are not physical.
```

#### Descriptive Ontology for Linguistic and Cognitive Engineering

```text
Particular: an individual that is not a universal.
├── Endurant: an entity wholly present at each time it exists.
│   ├── PhysicalEndurant: an endurant with physical presence.
│   │   └── PhysicalObject: a physical endurant with independent existence.
│   └── NonPhysicalEndurant: an endurant without physical presence.
├── Perdurant: an entity that unfolds over time.
│   └── Event: a perdurant with temporal boundaries.
├── Quality: an individual dependent on an entity and characterizing it.
└── Abstract: an entity that is neither physical nor temporal.
```

#### Basic Formal Ontology

```text
Entity: anything that exists in reality.
├── Continuant: an entity that persists through time while remaining present.
│   ├── IndependentContinuant: a continuant that does not inhere in another.
│   │   └── MaterialEntity: an independent continuant with a material extent.
│   │       └── Object: a material entity that is spatially bounded and self-connected.
│   └── SpecificallyDependentContinuant: a continuant dependent on one bearer.
└── Occurrent: an entity that unfolds or has temporal parts.
    └── Process: an occurrent with temporal extent and unfolding.
```

#### General Formal Ontology

```text
Entity: anything that can be represented in the ontology.
├── Concrete: an entity that exists in space-time.
│   ├── Presential: a concrete entity present at a given time.
│   │   └── MaterialObject: a material presential occupying space.
│   └── Process: a concrete entity that unfolds through time.
└── Abstract: an entity not located in space-time.
    └── Category: an abstract entity used to classify individuals.
```

#### Unified Foundational Ontology

```text
Entity: anything that exists according to the domain theory.
├── Endurant: an entity wholly present whenever it exists.
│   ├── Object: an endurant that bears properties and participates in events.
│   │   └── MaterialObject: an object with material or physical realization.
│   └── Moment: an existentially dependent endurant.
└── Perdurant: an entity whose existence unfolds over time.
    └── Event: a perdurant composed of temporal parts.
```

#### WordNet noun hierarchy

```text
Entity: something that has distinct and independent existence.
├── PhysicalEntity: an entity that has a physical existence.
│   └── Thing: an entity regarded as an object or unit.
│       └── Object: a tangible and visible entity.
└── Abstraction: a general concept formed by abstraction.
```

#### Schema.org

```text
Thing: the most generic type of item.
├── Place: a physical location.
│   └── Landform: a natural physical feature of the Earth.
├── Product: any offered product or service.
│   └── IndividualProduct: a single, identifiable product instance.
├── CreativeWork: the most generic kind of creative work.
└── Event: an event happening at a given time and location.
```

#### Aristotle's Categories

```text
Being: that which is said to be or exists in any category.
└── Substance: what is neither said of a subject nor in a subject.
    └── Body: a quantity having three dimensions.
        ├── Natural body: a body arising by nature.
        └── Artificial body: a body produced by art or craft.
```

### Wikidata

- **Origin:** Wikimedia Deutschland, Berlin, Germany, launched in 2012.
- **Current status:** active collaborative knowledge graph.
- **Node count:** live and release-dependent; the
  [Wikidata statistics portal](https://www.wikidata.org/wiki/Wikidata:Statistics)
  reports item, statement, edit, and community counts rather than a frozen
  ontology release.
- **Prominence proxy:** the live statistics portal exposes tens of millions
  of items and a very large statement/edit graph; its scale is orders of
  magnitude beyond a one-page game profile.
- **Fit:** useful later for people, places, organizations, brands, fictional
  entities, and current events; too noisy to be the first noun backbone.

### Wikipedia’s implicit ontology

- **Origin:** launched in January 2001 as a global Wikimedia project.
- **Current status:** active encyclopedia, category graph, portal system,
  infobox vocabulary, redirects, interlanguage links, and a substantial
  biological-taxonomy workflow. The [WikiProject Tree of
  Life](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Tree_of_Life)
  coordinates organism coverage; species articles commonly use standardized
  [taxoboxes](https://en.wikipedia.org/wiki/Template:Taxobox) to display
  ranks, accepted names, synonyms, and parent taxa; and
  [Wikispecies](https://species.wikimedia.org/) provides a separate
  Wikimedia taxonomy directory. These are valuable linked reference
  structures, but Wikipedia's taxoboxes and categories are editorial
  presentations, not a single versioned biological authority.
- **Node count:** the English
  [Wikipedia statistics page](https://en.wikipedia.org/wiki/Wikipedia:Statistics)
  reports roughly 7.25 million articles and 2.6 million categories in its
  2026 snapshot.
- **Prominence proxy:** the same snapshot reports about 872 million article
  edits by 12.4 million users; article and category counts are also direct
  scale measures.
- **Fit:** excellent candidate source for familiarity and named-entity
  expansion and biological cross-checking, but category membership is
  inconsistent and often editorial, topical, or maintenance-driven. Taxobox
  parentage is more useful for organisms than general Wikipedia categories,
  although it still needs source/version tracking.
- **Browser:** [`Wikipedia/index.html`](Wikipedia/index.html) provides a
  static, searchable, lazy-rendered browser beginning at
  [Main topic classifications](https://en.wikipedia.org/wiki/Category:Main_topic_classifications)
  and [Contents](https://en.wikipedia.org/wiki/Category:Contents). It
  packages [`categories.json`](Wikipedia/categories.json) and records its
  exact source, checksum, license, roots, and derivation parameters in
  [`snapshot-manifest.json`](Wikipedia/snapshot-manifest.json). The October
  3, 2026 English Categories RDF dump contains about 2 million categories
  reachable from these roots; the checked-in derived snapshot includes 12,657
  categories through depth 3 so the browser remains practical. Boundary
  categories link to live Wikipedia pages for deeper exploration. The
  reproducible parser is [`generate_categories.py`](Wikipedia/generate_categories.py).
  It deliberately presents the result as a category graph: repeated
  categories, cycles, maintenance branches, and multiple parents are not
  collapsed into a falsely authoritative single tree.

### Product-type taxonomies

Product taxonomies are valuable prior art for the artifact, food, clothing,
tool, appliance, vehicle, electronics, and household portions of the tree.
They are usually optimized for retail navigation, search, listing validation,
or supply-chain interoperability rather than general ontology design. Their
strength is dense coverage of familiar manufactured goods; their weakness is
that commercial departments, brands, attributes, and merchandising use cases
are often mixed into the hierarchy.

This detailed prior-art supplement is retained adjacent to the upper-layer
discussion for implementation convenience. It does **not** belong in the
canonical upper ontology and is not a candidate for `Entity`, `Property`, or
`Relation`. Google, GS1, UNSPSC, eCl@ss, ETIM, Amazon, and Walmart are
operational classification systems: use them to discover artifact vocabulary
and coverage gaps, preserve their source paths as metadata, and map reviewed
leaves into the physical subtree. Do not copy commercial departments, product
types, brands, or proprietary paths into the ontology's highest layers.

The top five publicly accessible product-classification systems to evaluate
are:

#### Google Product Taxonomy

- **Source:** [Google's product taxonomy](https://www.google.com/basepages/producttype/taxonomy.en-US.txt)
  and [Merchant Center product data documentation](https://support.google.com/merchants/answer/6324436).
- **Structure:** a large, human-readable category path with numeric IDs,
  designed for product feeds and shopping search.
- **Access:** the taxonomy file is publicly downloadable. Its terms and
  update policy should be recorded with each imported snapshot.
- **Fit:** probably the best first retail source for familiar product names
  and practical department coverage. It is useful for candidate discovery,
  but should not dictate the ontology's treatment of natural objects,
  services, or abstract concepts.

#### GS1 Global Product Classification (GPC)

- **Source:** [GS1 GPC](https://www.gs1.org/standards/gpc).
- **Structure:** a global supply-chain classification organized around
  segments, families, classes, and bricks, with attributes and rules that
  support product identification across trading partners.
- **Access:** the standard, browser, and release materials are publicly
  discoverable; some downloadable content and reuse rights may require GS1
  registration or acceptance of licensing terms.
- **Fit:** excellent as a stable cross-industry product backbone and for
  checking whether a proposed retail branch is missing a major category.
  Its business-oriented granularity should be compressed before display.

#### UNSPSC

- **Source:** the [UNSPSC overview](https://en.wikipedia.org/wiki/United_Nations_Standard_Products_and_Services_Code)
  and the code-set steward's historical [UNSPSC site](https://www.unspsc.org/).
- **Structure:** a four-level hierarchical code set covering segments,
  families, classes, and commodities across goods and services.
- **Access:** the taxonomy is publicly documented and widely used, but the
  steward's current site and code-set download availability should be
  revalidated before importing a snapshot; the domain may not currently be a
  reliable distribution endpoint.
- **Fit:** useful for broad coverage and procurement-oriented gaps,
  especially where consumer retail taxonomies omit industrial goods,
  services, or professional equipment. It is less friendly as a visible
  noun tree because many leaves are procurement labels.

#### eCl@ss

- **Source:** [eCl@ss International](https://eclass.eu/en/).
- **Structure:** a hierarchical product and service classification with
  standardized classes, properties, and value domains, used heavily in
  industrial and business-to-business data exchange.
- **Access:** the standard and documentation are publicly described, while
  complete releases and some reuse rights may require registration or a
  license.
- **Fit:** strong for machinery, components, materials, industrial tools,
  and technical products that consumer taxonomies underrepresent. It should
  be an audit source and vocabulary reservoir, not a direct player-facing
  hierarchy.

#### ETIM

- **Source:** [ETIM International](https://www.etim-international.com/).
- **Structure:** a product-classification model centered on standardized
  classes and product features, especially for electrical, HVAC, building,
  installation, and technical-trade products.
- **Access:** the model is publicly described and used through national
  implementations; complete releases and commercial reuse conditions vary by
  member and license.
- **Fit:** valuable for tools, hardware, building products, appliances, and
  technical equipment. It supplies detailed feature vocabulary that can
  enrich leaves, but its feature-centric design should remain metadata
  rather than become extra visible branches.

#### Amazon and Walmart operational taxonomies

Amazon and Walmart are important prior art even though neither appears to
offer an unrestricted, complete public download of its live product-type
hierarchy.

- **Amazon:** Amazon exposes public documentation for the
  [Selling Partner API product-type definitions](https://developer-docs.amazon.com/sp-api/docs/product-type-definitions-api)
  and seller-facing browse/product-type concepts, but the complete current
  category and product-type data is tied to marketplaces, regions,
  authenticated APIs, and commercial operational use. Public documentation
  is therefore available; a complete public taxonomy snapshot is not assumed.
  Amazon is especially useful for studying retail granularity, browse-node
  navigation, required attributes, and the distinction between product type
  and department.
- **Walmart:** Walmart Marketplace provides public entry points to its
  [Marketplace APIs](https://developer.walmart.com/us-marketplace/docs/introduction-to-marketplace-apis)
  and item-setup workflows, while the detailed category, item-specification,
  and validation taxonomy is generally exposed through authenticated
  seller/partner tooling. It should be treated as restricted prior art unless
  a distributable public release can be identified. Its value is high for
  practical retail category coverage, especially for grocery, consumables,
  household goods, apparel, and general merchandise.

The project should use the public systems as candidate generators and
cross-checks, not merge their department trees directly. A product leaf
should retain its source code and paths, then receive a reviewed home in the
SUMO/PDF-derived tree. Amazon and Walmart material can be used for internal
audits where authorized, but no proprietary taxonomy content should be copied
into the public repository without permission.

### Roget’s Thesaurus

- **Origin:** Peter Mark Roget’s classification began in London in 1805 and
  was published in 1852.
- **Current status:** continuously republished in commercial and public
  editions; its class/division/section structure remains recognizable.
- **Node count:** six primary classes and more than 1,000 meaning-cluster
  branches; the eighth edition is reported to contain about 443,000 words.
- **Prominence proxy:** the edition scale itself is objective; the work has
  been continuously published since 1852 and remains a standard English
  thesaurus reference. The best freely browsable view of the original
  conceptual class/division/section structure is the
  [1911 edition at Project Gutenberg](https://www.gutenberg.org/ebooks/10681);
  see also the
  [historical overview](https://en.wikipedia.org/wiki/Roget%27s_Thesaurus).
- **Fit:** useful for lexical neighborhoods and question wording, not a
  reliable hypernym ontology. It should not replace WordNet’s synset IDs.

### SUMO

- **Origin:** the IEEE Standard Upper Ontology effort, developed by the
  Teknowledge-led working group around 2000 in the United States.
- **Current status:** maintained as an open formal upper ontology and mapping
  resource.
- **Node count:** release-dependent; commonly reported at roughly 25,000
  terms with tens of thousands of axioms and mappings.
- **Prominence proxy:** the
  [SUMO overview](https://en.wikipedia.org/wiki/Suggested_Upper_Merged_Ontology)
  and its open downloads provide a reproducible formal-ontology footprint.
- **Fit:** valuable for high-level distinctions such as object, process,
  attribute, and situation; too abstract and axiom-heavy for the default
  everyday noun page.

### SUMO PDF projection

The active SUMO browser is a projection of the official Ontology4 PDF graph,
not the current KIF hierarchy. The checked-in graph contains 518 nodes and 554
arcs. The display chooses one primary parent for multi-parent nodes, retains
removed parents as alternate metadata, keeps unary nodes, and uses `Entity` as
the only root. Four provisional placements connect otherwise disconnected
labels: `List → Set`, `Number → Quantity`, `Predicate → Proposition`, and
`Sentence → Proposition`.

### DBpedia

- **Origin:** Free University of Berlin, University of Leipzig, and OpenLink
  Software; launched in 2007 in Germany.
- **Current status:** active linked-data extraction project with release-based
  datasets.
- **Node count:** release-dependent and measured in millions of extracted
  entities and hundreds of millions of RDF statements, rather than a compact
  controlled vocabulary.
- **Prominence proxy:** its recurring public releases and SPARQL endpoint make
  it one of the most reused Wikipedia-derived linked-data resources; see
  [DBpedia](https://www.dbpedia.org/).
- **Fit:** useful bridge from article names to structured entities, but not a
  clean noun hierarchy.

### Schema.org

- **Origin:** Google, Microsoft, Yahoo, and Yandex, launched in 2011 for
  interoperable web markup.
- **Current status:** actively maintained public vocabulary.
- **Node count:** a few hundred types and over a thousand properties,
  depending on whether pending and extension terms are included; the
  [official vocabulary](https://schema.org/docs/full.html) is the authoritative
  live count.
- **Prominence proxy:** its vocabulary is embedded in web search and structured
  data tooling across the four founding search ecosystems.
- **Fit:** practical for artifact, organization, person, and event categories;
  too shallow for a complete noun ontology.

### FoodOn

- **Origin:** an open food ontology effort launched in the mid-2010s by
  researchers and food-domain communities.
- **Current status:** maintained in the OBO ecosystem.
- **Node count:** release-dependent and typically tens of thousands of food
  classes and terms; use the
  [FoodOn releases](https://foodon.org/) for the current count.
- **Prominence proxy:** OBO/OLS distribution and domain reuse provide a
  measurable publication and reuse footprint.
- **Fit:** a targeted supplement if WordNet coverage of prepared foods such as
  steak and salad is inadequate.

### Encyclopaedia Britannica’s 15th-edition Propædia

- **Origin:** Encyclopaedia Britannica began in Edinburgh, Scotland, in
  1768. The one-volume *Propædia* was introduced with the 15th edition in
  1974 as the topical “Outline of Knowledge” for the *Micropædia* and
  *Macropædia*.
- **Current status:** the print 15th edition ended in 2010, while Britannica
  continues digitally. The best freely available outline of the single-volume
  knowledge scheme is the detailed
  [Propædia outline](https://en.wikipedia.org/wiki/Propaedia); Britannica’s
  own shorter [Propædia entry](https://www.britannica.com/topic/Propaedia)
  confirms its role in the 15th edition.
- **Node count:** the *Outline of Knowledge* contains 10 parts, 41
  divisions, and 167 sections. These are organizational topics, not a
  biological or noun taxonomy.
- **Prominence proxy:** it was designed over eight years by Mortimer Adler
  with dozens of subject specialists as the organizing framework for the
  entire 15th edition. It is one of the most prominent modern attempts to
  provide a single synoptic outline of human knowledge.
- **Fit:** useful prior art for broad top-level coverage and for testing
  whether v1/v2 omit an important knowledge domain. It is intentionally
  encyclopedic and circular rather than a balanced yes/no noun tree, so it
  should inform coverage audits rather than supply parentage.

### DMOZ/Open Directory Project RDF hierarchy

The large RDF/XML text dump available for this project is not a general
“Mozilla Ontology.” It is a snapshot of the **Open Directory Project (ODP),
also called DMOZ**, a human-edited web-directory topic hierarchy. The
historical association with Netscape and Mozilla explains the earlier label,
but DMOZ is the precise name for the data structure.

- **Origin:** ODP was founded in the United States in 1998 as Netscape’s Open
  Directory Project and was later commonly known as DMOZ. Its categories were
  organized as web subjects rather than as a formal noun or upper ontology.
- **Source and release:** the supplied file is an RDF/XML snapshot whose
  header says it was generated on 2006-10-10 01:06:26 GMT on `dust`; its
  records include category IDs, titles, update timestamps, editors, and
  `narrow` links to child topics. The dump size is approximately 600 MB.
- **Current status:** the directory was discontinued in 2017 and is no
  longer an actively maintained public authority. The snapshot is therefore
  historically valuable but frozen and release-specific. See the
  [Open Directory Project history](https://en.wikipedia.org/wiki/DMOZ).
- **Node count:** not yet measured for this particular dump. A valid count
  must be produced by streaming the RDF/XML, counting distinct `Topic`
  resources, counting `narrow` edges, and reporting disconnected components,
  missing targets, duplicate labels, and cycles. The count must not be
  inferred from the 600 MB file size.
- **Prominence proxy:** DMOZ was one of the best-known human-edited web
  directories, and its category data was reused by search engines,
  directories, and the RDF community during the Web 1.0 era. Historical
  prominence is the appropriate metric; it should not be compared directly
  with current Wikidata item or Wikipedia article counts.
- **Fit:** useful as a separate, human-curated topical browsing profile and as
  a source of realistic category distinctions. It is not a canonical noun
  backbone: many nodes describe websites, audiences, regions, editorial
  maintenance categories, or topical collections rather than kinds of
  things. Multiple parents and cycles must be preserved in the source
  manifest and resolved only in a declared display projection.

### Human Knowledge

- **Origin:** Brian Holtz’s *Human Knowledge 2000* outline, developed in the
  late 1990s and early 2000s.
- **Current status:** personal static reference material, not a community
  ontology or standards body.
- **Node count:** the `Thoughts 1-8.html` outline has 137 HTML heading nodes;
  this is a document-structure count, not an ontology count.
- **Prominence proxy:** no external citation, usage, or page-view metric has
  been established; its relevance here is personal authorship, not public
  prominence.
- **Fit:** explicitly **not an input, root, ranking prior, or graft target** for
  this ontology. “Ontology” is one topic within that outline, so the outline
  cannot logically serve as the ontology’s root. It may be studied separately,
  but this project will not merge it into the WordNet tree.

## Upper ontology notes

### Entity

- `Entity / Property / Relation` is our proposed triad, not a complete
  arrangement copied from one prior art.
- `Entity` as a universal domain is shared by SUMO and broad formal-ontology
  and knowledge-representation practice; this exact placement is ours.

#### Object

- `Entity` is the safer root label for anything admitted into discourse;
  `Object` is narrower and often means a particular bearer or an argument of
  predication.
- `Object` has strong precedent in SUMO's object/process distinction and in
  ordinary knowledge-representation vocabulary, but those uses do not make
  it exhaustive of events, propositions, numbers, organizations, fictional
  entities, or reified predicates.
- Renaming the current second-level `Entity` note to `Object` is useful only
  if the branch is intended to exclude properties and relations; otherwise
  `Object` falsely suggests that those reified entities are outside it.

#### Property

- `Property` as a top-level child of `Entity` has precedent in
  philosophical/formal ontology and entity-property-value modeling; RDF/OWL
  uses “property” for relations, so the term is not stable across prior art.
- The child inventory was assembled in our maximal “Property candidates”
  synthesis (`065fd48`) and copied into `overlay_canonical.py` (`f528ab0`);
  it was not imported wholesale from one prior art. Its ingredients were
  cross-compared from the prior-art families catalogued in that synthesis,
  especially Aristotelian, SUMO/BFO-inspired, and formal/type-theoretic
  variants.

#### Relation

- `Relation` as a top-level concept comes from logic, knowledge
  representation, and conceptual modeling.
- The child inventory was assembled beside the property inventory in the
  maximal candidate synthesis (`065fd48`) and copied into
  `overlay_canonical.py` (`f528ab0`); it was not imported wholesale from one
  prior art. It mixes subject-matter, logical, mathematical, operational,
  and provenance axes, so several children are not justified as siblings and
  require review.

## Entity Object Thing Item Being

The following numbered slots separate ontological work from the later choice
of English labels. The definitions are intentionally stricter than ordinary
language and are testable against the existing tree.

### Slot definitions

1. **Universal entity:** an entity considered as a bearer of properties or
   participant in relations.
2. **Realized entity:** an entity with physical embodiment or a determinate
   spatial or spatiotemporal extent, whether or not it is a self-connected
   object.
3. **Object:** a realized entity with a spatially bounded or self-connected
   physical extent.
4. **Mechanical body:** a physical entity whose state is modeled by mechanics,
   including some determinate mass, geometry, motion, or force interaction.
   Mass is not required of every useful body model.
5. **Abstract entity:** an idealized object considered apart from any
   particular realization.
6. **Occurrence:** an entity that unfolds, persists, or changes through time
   as an event, process, activity, transition, or state.
7. **Place or region:** an entity specified by spatial, temporal, or
   spatiotemporal extent, location, boundary, or coordinate relations.
8. **Information or representation:** an entity whose identity depends on
   content, encoding, signification, or reproducible informational structure,
   whether or not it has a physical carrier.
9. **Collection or system:** an entity constituted by members, parts, elements,
   or organized interactions and treated as one unit.
10. **Agent or organism:** an entity capable of autonomous activity, response,
    or directed action in the relevant model; organism is a biological
    specialization, while agent is a functional or behavioral role.
11. **Ethical subject:** an entity considered as a bearer of moral standing,
    claims, duties, or welfare.

### Candidate slot assignments

- `Entity` is the settled label for slot 1.
- `Realized entity` is the settled label for slot 2.
- `Object` is the settled label for slot 3: a realized entity with a spatially
  bounded or self-connected physical extent.
- `Body` is the candidate for slot 4, subject to deciding whether force
  interaction and mass are defining or merely typical.
- `Being` is reserved for slot 11 and is off-limits for the upper ontology.
- Slots 5 through 10 need labels that should be chosen from their technical
  prior-art uses rather than from the remaining everyday synonyms.

### Entity, Realized entity, Object

- The current chain is `Entity → Realized entity → Object`, with
  `Abstract entity`, `Property`, and `Relation` as the other direct children
  of `Entity`.
- This is defensible if `Entity` is the universal domain, `Realized entity`
  is the physically realized branch, and `Object` is the narrower
  self-connected material-object branch.
- In philosophical and formal-ontology usage, `entity` is generally the broad
  term for anything admitted as existing or as a domain individual. `Object`
  is more variable: it commonly means an ordinary bearer of properties, a
  material continuant, or the target of intentional reference, but it is not
  a stable synonym for `entity`.
- The revised chain avoids using `Object` as a broad non-predicative category
  while retaining it for the narrower physical-object branch. `Realized
  entity` includes physical processes, while `Object` is reserved for the
  narrower object branch.

### Options for the physical-entity label

- **Material entity:** precise when the slot requires matter, but potentially
  excludes fields, spacetime regions, and other physically real non-matter
  entities.
- **Concrete entity:** established as the opposite of abstract, but often
  includes events, places, and social particulars and therefore may be too
  broad or theory-dependent.
- **Object:** clear as the broad physical branch after the current rename,
  including physical processes.
- **Physical entity:** clear and currently understood, but generic enough
  that it does not distinguish the slot from `Thing`.
- **Corporeal entity:** emphasizes embodiment, but usually suggests a living
  body and is too narrow for artifacts, regions, and physical processes.
- **Natural entity:** unsuitable because artifacts and engineered systems are
  physical without being natural.
- **Continuant:** technically useful for an entity that persists through
  time, but it excludes processes and is specialized foundational-ontology
  vocabulary rather than ordinary noun vocabulary.
- **Real entity:** supports the intended contrast with fictional or merely
  possible entities, but imports a disputed metaphysical commitment and may
  conflict with the intended treatment of fictional entities as entities.

The current assignment is `Realized entity` for the broad physical branch and
`Object` for the narrower spatially bounded or self-connected object branch.

### Thing at the realized-entity or object slot

The colloquial test favors the broader slot: fire can be called “not a thing”
when its existence as a physical phenomenon is disputed, even though fire is
not an ordinary persisting object. That use treats `Thing` as “physically
existent phenomenon,” not as “self-connected material object.”

#### Thing as realized entity

- **Result:** `Thing` covers material objects, fires, processes, events, and
  other physically realized phenomena.
- **Remaining object labels:** `Object` is explicit;
  `Material object` is precise for matter-bearing objects but excludes
  nonmaterial physical entities; `Body` is too mechanics-specific.
- **Best option:** use `Object` for the narrower branch while retaining
  `Realized entity` for the broader physical branch.

#### Thing as object

- **Result:** `Thing` covers ordinary material objects but excludes fire and
  other physical processes from the colloquial “a thing.”
- **Remaining broad-object labels:** `Object` is explicit and already chosen;
  `Material entity` excludes fields and some physically real regions;
  `Concrete entity` may include events, places, and social particulars but is
  metaphysically variable.

The current assignment therefore keeps `Thing` as a discussion synonym only;
the node names are `Realized entity` and `Object`.

### Contrasts with abstract entity

- Concrete
- Physical
- Material
- Real
- Actual
- Existent
- Embodied
- Particular
- Sensible
- Tangible
- Phenomenal
- Objective
- Empirical
- Spatiotemporal
- Corporeal
- Substantial
- Worldly
- Natural
- Instantiated
- Realized

### Prior-art definitions of the candidate words

#### Entity

- **SUMO:** `Entity` is the universal class at the top of the SUMO hierarchy.
- **BFO:** `entity` is used for anything that exists or has existed, including
  continuants and occurrents; see [BFO 2020](https://basic-formal-ontology.org/bfo-2020.html).
- **Schema.org:** `Thing` is the most generic type, so Schema.org does not use
  `Entity` in the same root role; see [Thing](https://schema.org/Thing).

#### Object

- **SUMO:** `Object` is roughly an ordinary object whose spatiotemporal extent
  divides into spatial parts parallel to the time axis; this is the source
  definition currently attached to our physical branch.
- **BFO:** an object is a material entity that is spatially extended,
  maximally self-connected, and persists through time as an independent
  continuant.
- **OWL/RDF:** “object” commonly appears in the object position of a triple,
  while an `owl:ObjectProperty` relates individuals; this is a syntactic or
  relational use, not a universal ontological root.

#### Thing

- **WordNet:** `thing.n.01` is “a separate and self-contained entity.”
- **Schema.org:** `Thing` is “the most generic type of item,” with all other
  Schema.org types descending from it.
- **DOLCE-style usage:** “thing” is ordinary-language vocabulary rather than
  a sufficiently precise foundational category; formal distinctions are made
  with endurant, perdurant, quality, region, and social-object categories.

#### Item

- **CIDOC CRM:** `E77 Persistent Item` covers persistent items of material,
  immaterial, or propositional nature that can be identified and referred to;
  see [CIDOC CRM](https://cidoc-crm.org/).
- **Schema.org:** “item” is the generic vocabulary for an instance of a
  `Thing`, not a peer upper-ontology category.
- **SKOS:** an `skos:Concept` is an item in a concept scheme identified by a
  URI; this is an information-model use, not a claim about all entities.

#### Being

- **WordNet:** `being.n.01` denotes the state or fact of existing, while other
  senses denote a living thing or person; the word is therefore polysemous.
- **Aristotelian and scholastic traditions:** “being” names what is or what
  exists, but the term does not by itself supply a usable partition of beings.
- **Ethics:** “being” is commonly used for a morally considerable subject or
  living entity; reserve this specialized use for the ethics section rather
  than overload the upper ontology.

## Upper ontology

### Canonical-tree criteria

The canonical tree is a privileged presentation of the richer ontology, not
a claim that reality itself has one intrinsically correct tree shape. A
candidate projection should satisfy these criteria:

- **Coverage:** where a sibling split claims to be exhaustive, its children
  should collectively cover the parent.
- **Disjointness:** siblings should be mutually exclusive where the subject
  matter supports that claim; overlap should be represented explicitly rather
  than hidden.
- **Uniform edge semantics:** canonical parent-child edges should have one
  declared meaning, currently a subtype or kind-of relation. Instance,
  part-of, property, use, study, and provenance edges belong in the
  underlying graph or metadata, not mixed into the visible hierarchy.
- **Single canonical parent:** every non-root display node should have one
  reviewed route in the tree, while the underlying graph may preserve
  multiple inheritance and alternate parentage.
- **Principled sibling splits:** siblings should be distinguished by one
  coherent dimension or discriminating principle rather than by an
  opportunistic list of unrelated features.
- **Traversal intelligibility:** every level should earn its place by making a
  meaningful distinction that helps a human reach ordinary concepts without
  unnecessary upper-ontology machinery.

### Node naming standard

Every visible node is a singular noun or a singular noun phrase. A modifier
must refine a noun rather than stand alone; when a branch would otherwise be
named only by an adjective such as `Physical` or `Abstract`, the parent noun
is repeated as `Physical entity` or `Abstract entity`. Node names never use
`and`; split distinct concepts into separate siblings. A category such as
`Algebraic entity` is preferred to the course-like or overly generic
`Algebraic structure`, and a relation belongs under `Relation` rather than
being duplicated as a mathematical entity.

The four non-mathematical abstract branches are a strawman census, not an
assertion that they are equally mature:

- **Informational entity** — `Data`, `Record`, `Dataset`, `Signal`, `Message`,
  `Observation`, `Measurement`, `Fact`, `Knowledge`, and `Belief`. These are
  content-bearing or content-dependent entities whose identity depends on
  information, evidence, or interpretation.
- **Representational entity** — `Symbol`, `Name`, `Label`, `Notation`,
  `Description`, `Classification`, `Schema`, `Ontology`, `Language`,
  `Document`, `Image`, `Audio`, `Video`, `Software`, and `Model`. These are
  entities that encode, express, preserve, or transmit content. A physical
  inscription or device is linked separately as an embodied artifact.
- **Social entity** — `Person`, `Group`, `Community`, `Relationship`,
  `Role`, `Status`, `Agreement`, `Convention`, `Practice`, `Event`, and
  `Institution`. This branch is for socially constituted entities and
  patterns whose persistence depends on participants, recognition, or shared
  practice.
- **Institutional entity** — `Organization`, `Government`, `Corporation`,
  `Club`, `School`, `Court`, `Market`, `Currency`, `Law`, `Contract`,
  `License`, `Policy`, and `Office`. This is a proposed refinement of Social
  entity for durable rule-governed structures, rather than a claim that every
  institution is ontologically separate.

The census exposes two likely tensions. `Document`, `Software`, and `Model`
can be informational content, representational artifact, or physical
artifact depending on whether the question concerns meaning, encoding, or
embodiment. `Role`, `Status`, `Agreement`, and `Practice` can be social
entities or properties of participants. The source graph should preserve
those facets; the player-facing projection can retain the four siblings only
if they produce useful questions and recognizable leaves.

### Reification and the Entity root

Properties and relations can themselves be entities when they are reified and
discussed as objects of predication. For example, the relation `larger-than`
can have an arity, inverse, symmetry, and transitivity, while a property can
itself have a domain, range, or relation to another property. The canonical
upper structure is:

```text
Entity
├── Object
├── Property
└── Relation
```

`Property` and `Relation` may still be representational roles rather than
fundamental kinds, and `Object` may be too narrow for events, propositions,
numbers, organizations, and other admitted entities. Reification must remain
possible without forcing every reified relation or property into a second,
inconsistent copy of the tree.

The upper-ontology comparison must distinguish kinds from roles and continue
testing whether `Entity` → `Object` / `Property` / `Relation` provides a
genuinely exhaustive, appropriately disjoint, human-traversable partition.

### Formalization stress test

Formalizability is a design-quality criterion, not the immediate deliverable.
For every candidate upper structure, ask whether a competent formal
logician or type theorist could translate the ontology and its edge semantics
into a disciplined typed formalism without first repairing fundamental
category mistakes. The test should preserve distinctions among kinds and
instances, types and values, words and concepts, objects and descriptions,
and referents and representations.

This project should remain ontology-first rather than becoming a type-theory
or Lean project. Russell-style paradoxes and unrestricted self-reference are
warnings to use disciplined semantics, types, or levels; they are not
reasons to prohibit properties, relations, propositions, or classes from
being modeled as entities. A successful formalization test is evidence of
clarity and durability, not a requirement to formalize the entire ontology
now.

### Top-layer coverage inventory
Before choosing a root arrangement, we need an unordered inventory of the
important high-level kinds of thing that must have a home in the first two or
three layers. This is a coverage checklist, not a proposed hierarchy. Some
items are mutually exclusive in a particular modeling scheme; others are
orthogonal roles that should be represented as types, facets, or cross-links
rather than forced into one `is-a` tree.

#### Worldly entities and occurrences

- **Entities and instances** — particular things, individuals, collections,
  kinds, classes, types, and tokens.
- **Physical entities** — matter, energy, fields, bodies, artifacts,
  organisms, environments, and physical systems.
- **Objects and continuants** — comparatively persistent entities that can
  bear properties and participate in processes.
- **Agents** — organisms, persons, organizations, software agents, and other
  entities capable of initiating or controlling activity.
- **Artifacts** — intentionally made objects, tools, machines, buildings,
  documents, software, and engineered systems.
- **Natural entities** — particles, materials, geological bodies, planets,
  organisms, ecosystems, and other entities not primarily defined by human
  manufacture.
- **Processes and activities** — happenings extended through time, including
  actions, operations, growth, motion, computation, communication, and
  biological or social activity.
- **Events and transitions** — occurrences treated as bounded changes,
  beginnings, endings, interactions, failures, and discrete happenings.
- **States and situations** — configurations or circumstances that hold over
  an interval, including being located, owned, alive, valid, or operating.
- **Systems and wholes** — entities organized by parts, dependencies,
  boundaries, or coordinated behavior.
- **Places, regions, and spacetime** — locations, geometric regions,
  boundaries, paths, intervals, instants, and possible or actual worlds.
- **Causal and modal structure** — causes, effects, mechanisms, abilities,
  dispositions, tendencies, possibilities, necessities, counterfactuals, and
  constraints.

#### Properties and ways of being

- **Qualities** — color, shape, mass, temperature, age, health, texture,
  intelligence, beauty, and other attributes that characterize something.
- **Quantities and magnitudes** — amount, size, duration, distance, rate,
  probability, concentration, intensity, and measurement results.
- **States or values of qualities** — red, heavy, warm, large, true, healthy,
  and other value-like fillers of quality dimensions.
- **Dispositions and capabilities** — soluble, fragile, edible, executable,
  intelligent, poisonous, or able to perform an operation.
- **Norms, functions, purposes, and values** — what something is for, what it
  ought to do, permissions, obligations, goals, preferences, and evaluations.
- **Identity and equivalence** — sameness, difference, isomorphism,
  substitutability, similarity, and criteria for counting two descriptions as
  one thing.

#### Relations and structure

- **Relations** — binary and n-ary connections among entities, including
  part-of, member-of, instance-of, subclass-of, located-in, owned-by,
  caused-by, knows, uses, and precedes.
- **Attributes and role slots** — relation-like properties whose values fill a
  place in a description, record, event, or structured object.
- **Functions and mappings** — inputs, outputs, parameters, partial and total
  functions, transformations, operators, interpretations, and evaluation.
- **Collections and mereology** — sets, bags, lists, sequences, multisets,
  parts, wholes, aggregates, partitions, and membership.
- **Order and comparison** — equality, inequality, precedence, ranking,
  divisibility, inclusion, lattices, and partial orders.
- **Composition and transformation** — operations, identity operations,
  composition, inverses, products, coproducts, limits, and symmetries.
- **Structures and invariants** — entities defined by operations and laws,
  together with properties preserved by mappings or transformations.

#### Information, language, and representation

- **Information and data** — signals, measurements, records, datasets,
  observations, messages, and stored or transmitted content.
- **Signs and symbols** — names, labels, tokens, notation, codes, and formal
  symbols.
- **Descriptions and classifications** — concepts, categories, taxonomies,
  schemas, ontologies, definitions, and bibliographic or database records.
- **Propositions and statements** — claims, questions, commands, assertions,
  negations, and compound statements.
- **Truth and reference** — truth, falsity, denotation, aboutness,
  interpretation, ambiguity, context, and sense.
- **Languages and grammars** — natural languages, programming languages,
  logical languages, syntax, semantics, pragmatics, and type systems.
- **Media and works** — text, image, audio, video, software, models,
  documents, performances, and other reproducible information artifacts.
- **Knowledge and belief** — evidence, observation, belief, justification,
  explanation, prediction, inference, and uncertainty.

#### Logic and foundations

- **Logical objects** — terms, variables, constants, predicates, formulas,
  propositions, sequents, theories, and models.
- **Logical connectives and quantification** — identity, negation,
  conjunction, disjunction, implication, equivalence, universal and
  existential quantification, and higher-order quantification.
- **Inference and proof** — rules, derivations, proofs, refutations,
  satisfiability, validity, consistency, completeness, decidability, and
  computability.
- **Axioms and formal systems** — signatures, axioms, inference rules,
  deductive closure, metatheories, interpretations, and models.
- **Set-theoretic foundations** — membership, empty set, singleton,
  pairing, union, power set, replacement, infinity, choice, cardinality,
  ordinal, relation, function, and set-built structure.
- **Type-theoretic foundations** — types, terms, inhabitants, subtypes,
  products, sums, functions, dependent types, inductive types, universes,
  constructors, eliminators, and proofs-as-objects.
- **Category-theoretic foundations** — objects, morphisms, identity,
  composition, functors, natural transformations, products, coproducts,
  limits, colimits, adjunctions, and equivalences.
- **Mathematical structures** — algebraic, ordered, topological, geometric,
  measurable, probabilistic, analytic, computational, and physical
  structures.
- **Mathematical models and theories** — formal structures interpreted as
  models of mathematics, science, computation, or possible worlds.

#### Time, change, and modality

- **Time and temporal order** — instants, intervals, duration, succession,
  simultaneity, recurrence, history, and temporal precedence.
- **Change and persistence** — identity through change, creation, destruction,
  transformation, development, maintenance, and lifecycle.
- **Possibility and necessity** — actual, possible, impossible, necessary,
  contingent, hypothetical, counterfactual, and simulated.
- **Causation and explanation** — causal mechanism, intervention,
  correlation, dependence, explanation, prediction, and law.

#### Cross-cutting distinctions the upper layer must preserve

- **Particular versus universal** — an individual dog versus the kind
  `dog`, and a particular event versus an event type.
- **Class versus instance** — category membership must not be confused with
  subclassing or ordinary set membership.
- **Type versus value** — `integer` versus `3`, `red` versus a red object,
  and a Scala-like type versus one of its values.
- **Object versus description** — a tree versus a record or sentence about
  the tree.
- **Structure versus model** — a group, a formal theory of groups, and a
  physical system modeled as a group must remain distinguishable.
- **Syntax versus semantics** — a formula, its interpretation, and the
  proposition expressed by that interpretation.
- **Entity versus role** — a person, an agent-role played by that person,
  and an organization in which the role is exercised.
- **Worldly relation versus mathematical relation** — ownership, ancestry,
  and causation versus membership, ordering, and function application.
- **Source identity versus display identity** — one canonical concept may
  have aliases, synonyms, alternate parents, and multiple source mappings.

### Candidate top-level partitions

The next design question is not yet which detailed taxonomy to import. It is
which small set of divisions should organize the first layer or two. The
following are the strongest recurring proposals in prior art. Each is listed
as a candidate pattern, not as a recommendation.

#### Physical versus abstract

- **Top-level idea:** divide entities into physical things and abstract or
  non-physical things; place objects, organisms, artifacts, and processes on
  the physical side, and numbers, propositions, properties, relations, and
  formal structures on the abstract side.
- **Provenance:** common in philosophical and folk ontologies; explicit in
  Sowa's physical/abstract distinction, many SUMO renderings, and the
  current project tree.
- **Strengths:** immediately intuitive; separates most everyday nouns from
  mathematics and logic; gives the player a useful first question.
- **Weaknesses:** “abstract” becomes a dangerous catch-all; information,
  software, fictional entities, social institutions, spacetime, and
  processes can be physical, abstract, or multiply realized depending on
  the intended reading.

#### Objects versus processes

- **Top-level idea:** divide relatively persistent entities from happenings,
  activities, events, and changes.
- **Provenance:** SUMO's Object/Process pattern; BFO's continuant/occurrent
  distinction; DOLCE's endurant/perdurant distinction; process philosophy.
- **Strengths:** handles the object/process distinction the project already
  finds useful; makes time and change first-class; gives actions, growth,
  motion, computation, and communication a natural home.
- **Weaknesses:** qualities, relations, states, boundaries, information, and
  mathematical structures do not fit cleanly on either side; “object” can
  still conceal physical, abstract, social, and informational entities.

#### Continuants versus occurrents

- **Top-level idea:** divide entities that persist through time from entities
  that unfold in time, with qualities, roles, dispositions, and sites
  attached to the appropriate side.
- **Provenance:** BFO's continuant/occurrent architecture; DOLCE's
  endurant/perdurant architecture; realist foundational ontology.
- **Strengths:** more precise than physical/abstract; supports identity,
  persistence, temporal parts, processes, qualities, dispositions, and
  roles; has substantial biomedical and scientific reuse.
- **Weaknesses:** terminology is not player-facing; the distinction is
  metaphysically loaded; abstract objects, information artifacts, and
  social objects require additional decisions rather than disappearing into
  a clean binary.

#### Substance, quality, relation, and activity

- **Top-level idea:** begin with substances or things, qualities, relations,
  quantities, places, times, positions, states, actions, and passions.
- **Provenance:** Aristotle's Categories and the long Aristotelian
  substance-and-accident tradition.
- **Strengths:** covers many items in the inventory directly; keeps
  qualities, relations, quantities, and activities from becoming invisible
  subcases of “abstract”; historically durable and easy to explain.
- **Weaknesses:** not a modern formal taxonomy; categories overlap; the
  treatment of events, information, sets, types, and mathematical objects is
  underdeveloped; “substance” does not provide a practical noun hierarchy.

#### Independent, relative, and mediating

- **Top-level idea:** divide independent entities, entities that depend on or
  relate to others, and mediating structures or processes that connect them.
- **Provenance:** Sowa's top-level ontology, influenced by Peirce and
  Whitehead, including the physical/abstract and continuant/occurrent
  dimensions.
- **Strengths:** explicitly recognizes relations and mediators instead of
  treating everything as an isolated object; can represent roles,
  participation, situations, descriptions, and processes.
- **Weaknesses:** naturally forms a lattice or diamond rather than a tree;
  category boundaries are difficult to explain to players; the framework
  risks becoming a formal classification of modeling constructs rather than
  a familiar noun organization.

#### Entity, relation, attribute, and proposition

- **Top-level idea:** divide what a description talks about from the
  properties, relationships, and propositions used to describe it.
- **Provenance:** the Ontological Sextett and UMO proposals on Ontology4;
  related classical ontological rectangles and semantic modeling systems.
- **Strengths:** prevents relations, attributes, and propositions from being
  mistaken for ordinary objects; matches the project's need to keep source
  metadata and cross-links distinct from the visible noun tree.
- **Weaknesses:** is primarily a modeling ontology, not an inventory of
  worldly kinds; “entity” remains broad; it does not by itself distinguish
  physical things, events, mathematical structures, information, and
  fictional entities.

#### Thing, event, agent, place, and information

- **Top-level idea:** organize around practical semantic-web families such as
  things, actions or events, people and agents, places, products, creative
  works, and intangible entities.
- **Provenance:** Schema.org and related web-vocabulary practice.
- **Strengths:** uses readable labels; works well for people, places,
  organizations, artifacts, products, events, media, and web entities; easy
  to connect to contemporary data.
- **Weaknesses:** optimized for markup rather than philosophical
  completeness; branches mix ontological kinds with application domains;
  mathematical foundations, qualities, relations, and natural processes are
  thin or indirect.

#### Objects, events, situations, qualities, and relators

- **Top-level idea:** distinguish enduring objects, events, situations,
  qualities, and relation-like entities that mediate connections among
  objects.
- **Provenance:** UFO and conceptual-modeling traditions, with related
  distinctions in DOLCE and foundational ontology.
- **Strengths:** handles social objects, roles, relators, events,
  dispositions, situations, and qualities more explicitly than a simple
  physical/abstract split; useful for representing ownership, employment,
  membership, and institutional facts.
- **Weaknesses:** “relator” and “situation” are technical; the categories
  overlap in ordinary language; mathematical objects and formal systems need
  a parallel treatment.

#### Sets, structures, and interpretations

- **Top-level idea:** distinguish collections or sets, structures built from
  operations and relations, and interpretations or models of those
  structures.
- **Provenance:** structural mathematics, set theory, model theory,
  category theory, ETCS, type theory, and formal-methods practice.
- **Strengths:** gives numbers, functions, relations, types, proofs,
  theories, models, and mathematical structures principled homes; directly
  addresses the chart and the upper mathematical inventory.
- **Weaknesses:** not a sufficient ontology of ordinary physical and social
  life; a set-theoretic encoding is not the same as an intuitive category;
  terms such as “structure” and “model” require careful metalevel
  separation.

#### Types, terms, proofs, and values

- **Top-level idea:** distinguish types or propositions, terms or values,
  operations and constructors, and proofs or evidence.
- **Provenance:** simple and dependent type theory, typed lambda calculus,
  Martin-Löf type theory, Curry–Howard, proof assistants, and programming
  language design.
- **Strengths:** naturally separates classes from instances, types from
  values, syntax from semantics, and propositions from proofs; maps well to
  Scala-like subtyping, traits, algebraic data types, and executable
  validation.
- **Weaknesses:** a computational type system is not automatically a theory
  of physical existence; inheritance and substitutability differ from
  biological or metaphysical `is-a`; ordinary processes, qualities, and
  social relations need additional modeling patterns.

#### Things, properties, and relations

- **Top-level idea:** use a minimal three-way split between entities,
  properties or attributes, and relations or mappings, with events and
  descriptions modeled through these primitives.
- **Provenance:** recurring pattern in knowledge representation, RDF/OWL,
  conceptual modeling, semantic databases, and lightweight upper
  ontologies.
- **Strengths:** compact, orthogonal, and easy to implement; keeps
  relation-like metadata out of the entity taxonomy; supports a graph
  rather than pretending all knowledge is inheritance.
- **Weaknesses:** too sparse to guide the first two player-facing levels;
  processes, time, information, mathematics, and modality become modeling
  conventions rather than visible top-level concepts.

#### The six conceptual classes

- **Top-level idea:** divide concepts into abstract relations or ideas,
  space, matter, intellect, volition, and affection or emotion, in the
  broad conceptual ordering of Roget's Thesaurus.
- **Provenance:** Roget's six primary classes and its later divisions and
  sections.
- **Strengths:** broad lexical and conceptual coverage; closer to the
  vocabulary of human thought than a formal upper ontology; useful for
  finding familiar labels and balancing conceptual neighborhoods.
- **Weaknesses:** it is a thesaurus, not a formal `is-a` hierarchy; classes
  mix entities, properties, actions, and relations; the categories are
  historically contingent and do not provide mathematical or logical
  foundations.

#### Reality, representation, and theory

- **Top-level idea:** divide the world being described, the representations
  used to describe it, and the formal theories or models that interpret
  those representations.
- **Provenance:** model theory, formal methods, semiotics, philosophy of
  language, information ontology, and the distinction emphasized in
  Tegmark's mathematical-structure discussion.
- **Strengths:** prevents a physical object, a sentence about it, a data
  record, and a mathematical model from collapsing into one category;
  provides a natural home for logic, language, information, and ontology
  metadata.
- **Weaknesses:** this is a metalevel partition rather than a complete
  ontology of what exists; the same artifact can be both a physical object
  and an information carrier; users may find the distinction less intuitive
  than object/process or physical/abstract.

#### Domains of being, knowing, and making

- **Top-level idea:** divide the inventory into what exists, how it is
  represented or known, and how it is acted upon, designed, or produced.
- **Provenance:** broad knowledge-organization systems such as Propædia,
  library and information-science models, systems engineering, and
  practical knowledge graphs.
- **Strengths:** accommodates worldly entities, information, knowledge,
  artifacts, processes, purposes, and human practices; aligns with how the
  project will actually use the ontology.
- **Weaknesses:** mixes ontological categories with epistemic and practical
  perspectives; can classify the same item in multiple top-level branches;
  less precise as a formal upper ontology.

No candidate covers the entire inventory without auxiliary dimensions. The
most important recurring choice is therefore whether the first visible split
should be a distinction among kinds of entity (for example,
object/process/quality/relation), a distinction among levels of description
(reality/representation/theory), or a practical conceptual partition
(Roget-like classes). The later synthesis should compare these as alternative
projections over a shared typed graph rather than assuming that one tree must
serve every purpose.

### Entity, property, relation versus type, term, proof, value

The recurring three-way split between **entities, properties, and relations**
is genuinely promising, but it should not be treated as a rival to the
type-theoretic split between **types, terms, proofs, and values**. They answer
different questions.

### What the entity/property/relation triad classifies

- An **entity** is something the ontology talks about: a person, dog,
  number, event, organization, proposition, set, or mathematical structure.
- A **property** is a characteristic, quality, quantity, disposition, role,
  or predicate-like aspect attributed to an entity: red, heavy, soluble,
  employed, prime, or continuous.
- A **relation** connects two or more relata or maps inputs to outputs:
  part-of, older-than, owns, causes, member-of, subset-of, equal-to, or
  applies-to.

This is primarily a **semantic and metaphysical partition**. It says what
sort of contribution a concept makes to a description of a world or domain.
It is close to RDF-style triples, conceptual modeling, property graphs, and
the Ontological Sextett. Its advantage is breadth and intelligibility: it
can describe physical things, processes, mathematical objects, social facts,
and information without pretending they are all the same kind of entity.

Its limitation is that it is not a complete `is-a` taxonomy. “Property” can
mean a universal, a particular quality, a value, a predicate, or a field in
an information record. “Relation” can mean a worldly connection, a
mathematical relation, a logical symbol, or a database edge. The triad needs
typed subcategories and metalevel distinctions.

### What the type/term/proof/value system classifies

- A **type** specifies a family of admissible terms or values, or a
  proposition in propositions-as-types foundations.
- A **term** is a syntactic expression that may denote, compute, construct,
  or inhabit something.
- A **value** is a canonical or evaluated term, such as `3`, a record, a
  function, or a constructed data object.
- A **proof** is a term inhabiting a proposition or evidence accepted by a
  formal system; in Curry–Howard settings, propositions are types and proofs
  are terms.

This is primarily a **formal, computational, and epistemic partition**. It
describes expressions, typing judgments, computation, construction, and
justified derivation inside a language or formal calculus. Its advantage is
precision: it distinguishes a class from an instance, a formula from its
interpretation, and a proposition from a proof of that proposition. It is
also well suited to machine checking, Scala-like type systems, algebraic
data types, proof assistants, and executable ontology constraints.

Its limitation is that “value” is usually a language-relative notion, not a
category of everything that exists. A dog in the world is not automatically
a value; a physical process is not automatically a term; and a property such
as redness is not automatically a type. The same real-world entity may be
represented by many terms in many languages, while one term may denote
different things in different interpretations.

### The correspondence is partial, not one-to-one

| World-facing semantic notion | Formal/type-theoretic analogue | Why the mapping is imperfect |
| --- | --- | --- |
| Entity | Term, value, or inhabitant of a type | An entity may be represented by many terms, and not every entity is computationally canonical |
| Kind or class | Type, sort, or universe | A type may be a data domain, a proposition, or a computational interface rather than a worldly kind |
| Property | Predicate, dependent type, refinement, field, or proposition | A property may be intrinsic, relational, role-like, context-dependent, or merely representational |
| Relation | Function type, relation-valued predicate, record field, morphism, or proof | A relation can be data, logic, structure, or a worldly fact |
| Proposition | Type or proposition in a logic | A proposition may be true, false, undecided, hypothetical, or interpreted differently across models |
| Proof or evidence | Term inhabiting a proposition | Evidence is not the same thing as the fact or relation that it supports |
| Mathematical structure | Typed record, algebraic structure, category, or model | The formal encoding depends on the chosen foundation and signature |

The most important mismatch is that the first triad is **about semantic
roles in what is described**, while the second is **about expressions,
inhabitants, evaluation, and justification within a formal system**. A
relation such as `owns(person, bicycle)` is not itself a proof. A proof that
the relation holds is a separate formal object, and a term representing the
relation is yet another object at the syntax or data level.

### A reconciliation for this project

The cleanest synthesis is a typed, multi-layer graph rather than a single
four-way root:

```text
World-facing layer
├── Entities
├── Properties and qualities
└── Relations and mappings

Formal-description layer
├── Types and propositions
├── Terms and values
├── Functions and constructors
└── Proofs, evidence, and derivations

Interpretation layer
├── Denotation and reference
├── Satisfaction and truth
├── Models and possible worlds
└── Translation between representations
```

The browser could expose the first layer as the most intelligible upper
ontology while storing the latter layers as typed metadata and cross-links.
Mathematical and computational concepts could optionally enter through both
paths: `integer` is an entity-like mathematical structure and also a type;
`3` is a mathematical value and a term inhabiting that type; `3 is prime` is
a proposition; and a checked derivation of that proposition is a proof.

### What is missing from both triads

Neither triad alone covers several categories that must remain explicit:

- **Events and processes** — entities/properties/relations can represent
  them, and type theory can encode them, but neither triad says that time,
  change, activity, and participation deserve first-class treatment.
- **States, situations, and contexts** — properties and propositions often
  depend on a situation, time, agent, or possible world.
- **Functions and operations** — these are relations in one reading, terms or
  constructors in another, and structure-preserving maps in category theory.
- **Collections and mereology** — sets, lists, bags, parts, wholes, and
  membership need explicit patterns rather than being reduced to values.
- **Syntax, semantics, and pragmatics** — terms, values, denotations,
  interpretations, uses, and communicative acts belong at different levels.
- **Kinds and metatypes** — types themselves may be entities, terms, or
  inhabitants of higher universes; a type hierarchy must not be confused
  with ordinary instance membership.
- **Time, modality, causation, and normativity** — necessity, possibility,
  causes, obligations, purposes, and counterfactuals require relations to
  worlds, times, agents, or rules.
- **Identity and equivalence** — equality, sameness of entity, isomorphism,
  observational equivalence, and substitutability are not interchangeable.

The working hypothesis should therefore be: **use
entity/property/relation as the compact semantic upper partition, and use
types/terms/values/proofs as a formalization and validation layer that
cross-cuts it**. Add first-class patterns for processes, contexts, functions,
collections, interpretations, time, modality, and identity instead of
forcing those concepts into either triad.

### Design alternatives retained for comparison

The canonical tree above supersedes the earlier profiles in this subsection.
The profiles below are retained only to document rejected projections and
implementation tradeoffs; none is an alternative visible root. The visible
top level is:

```text
Entity
├── Object
├── Property
└── Relation
```

This is intentionally a semantic partition, not a claim that every concept
has only one role. A class can be an entity that classifies other entities; a
quality can be an entity in one context and a property in another; and a
proposition can reify a relation while also carrying truth, evidence, and
proof metadata. The authoritative data model should therefore permit typed
cross-links and role annotations even when the browser chooses one primary
display branch.

### Maximal candidate inventory

The following is the deliberately generous candidate space. It is not a
proposed set of siblings; several candidates are alternative ways to
partition the same material. Keeping them together makes omissions and
tradeoffs visible before we choose a compact projection.

**Entity candidates**

- **Physical entities** — matter, energy, fields, particles, materials,
  organisms, bodies, artifacts, environments, and physical systems.
- **Abstract entities** — numbers, sets, mathematical structures, properties
  treated as objects, propositions, meanings, and other nonphysical objects.
- **Informational entities** — data, symbols, records, documents, models,
  software, messages, and reproducible works.
- **Social and institutional entities** — persons, organizations, groups,
  roles, statuses, institutions, laws, contracts, and currencies.
- **Fictional, hypothetical, and possible entities** — characters, imagined
  objects, counterfactual entities, simulated entities, and possible-world
  inhabitants.
- **Agents** — organisms, persons, organizations, software agents, and
  systems capable of action, control, or communication.
- **Objects or continuants** — relatively persistent bearers of properties,
  including natural objects, artifacts, organisms, places, and abstract
  objects.
- **Processes or occurrents** — activities, events, changes, operations,
  motions, computations, communications, and histories.
- **States and situations** — temporally or contextually bounded
  configurations in which entities participate or properties hold.
- **Collections and wholes** — sets, classes, types, lists, bags, aggregates,
  parts, wholes, systems, and populations.
- **Places and spacetime regions** — locations, boundaries, paths, intervals,
  instants, coordinate regions, and possible or actual worlds.
- **Classes, types, and universals** — kinds that classify instances,
  formal types, predicates reified as concepts, and universes of types.
- **Mathematical structures** — algebraic, ordered, topological, geometric,
  measurable, probabilistic, computational, and physical structures.
- **Formal objects** — languages, signatures, formulas, theories, proofs,
  programs, terms, values, models, and derivations.
- **Propositions and statements** — reified claims, questions, commands,
  hypotheses, assertions, and compound statements.
- **Occurrences and tokens** — particular realizations of events, symbols,
  words, measurements, observations, or documents.

**Property candidates**

- **Qualities** — color, shape, texture, temperature, mass, age, health,
  intelligence, beauty, and other characteristic dimensions.
- **Quantities and magnitudes** — amount, size, duration, distance, rate,
  probability, concentration, intensity, and measurement result.
- **Quality values** — red, heavy, warm, large, healthy, prime, continuous,
  and other values filling a quality dimension.
- **States** — alive, open, occupied, valid, employed, connected, or
  functioning.
- **Dispositions and capabilities** — soluble, fragile, edible, executable,
  poisonous, intelligent, or able to perform an operation.
- **Functions and purposes** — what an object or process is for, including
  biological functions, designed functions, and intended use.
- **Roles and statuses** — agent, owner, patient, employee, citizen, leader,
  member, legal status, and other context-dependent ways of participating.
- **Norms and obligations** — permissions, duties, prohibitions, rules,
  standards, requirements, and institutional commitments.
- **Goals and preferences** — aims, desires, priorities, utility, value,
  relevance, and evaluation.
- **Modal properties** — possible, necessary, contingent, dispositional,
  counterfactual, or law-governed.
- **Logical and mathematical properties** — true, false, equal, finite,
  prime, continuous, measurable, decidable, or computable.
- **Relational properties** — being adjacent, owned, caused, located,
  represented, comparable, or dependent, when treated as a property of one
  bearer rather than as a relation node.
- **Type and refinement properties** — membership conditions, subtype
  constraints, predicates, invariants, capabilities, and effect sets.

**Relation candidates**

- **Classification relations** — instance-of, subclass-of, type-of,
  predicate application, realization-of, and member-of.
- **Part-whole relations** — part-of, proper-part-of, component-of,
  boundary-of, member-of, aggregate-of, and overlap.
- **Spatial relations** — located-in, contains, adjacent-to, connected-to,
  inside, outside, above, below, near, and intersects.
- **Temporal relations** — before, after, during, overlaps, begins, ends,
  persists-through, and occurs-at.
- **Causal and explanatory relations** — causes, enables, prevents,
  depends-on, explains, predicts, and results-in.
- **Participation relations** — agent-in, patient-in, instrument-in,
  location-of, beneficiary-of, and participant-in.
- **Social and institutional relations** — owns, employs, governs, belongs-to,
  married-to, represents, authorizes, owes, and contracts-with.
- **Perceptual and epistemic relations** — observes, knows, believes,
  justifies, evidences, measures, describes, refers-to, and is-about.
- **Logical relations** — entails, contradicts, implies, is-consistent-with,
  is-provable-from, and is-satisfied-by.
- **Set and collection relations** — member-of, subset-of, disjoint-from,
  partitions, indexes, enumerates, and is-cardinality-of.
- **Mathematical relations** — equals, less-than, divides, maps-to,
  isomorphic-to, homomorphic-to, composes-with, and is-an-instance-of.
- **Transformation relations** — converts, derives, constructs, interprets,
  translates, compiles, evaluates, and reduces-to.
- **Representational relations** — names, denotes, encodes, quotes,
  instantiates, models, formalizes, and is-described-by.
- **Identity and equivalence relations** — same-as, equivalent-to,
  observationally-equivalent-to, interchangeable-with, and version-of.
- **Provenance relations** — sourced-from, asserted-by, generated-by,
  inferred-from, proved-by, revised-from, and supersedes.

### Coherent subcategory variants

These variants show how the maximal inventory could be made navigable. They
are alternatives for the visible second and third levels, not separate
ontologies.

**Minimal semantic variant**

- **Entity:** Physical, Abstract, Informational, Social
- **Property:** Quality, Quantity, Disposition, Role, Function, Norm
- **Relation:** Classification, Part-whole, Spatial/temporal, Causal,
  Social, Representational

This is the strongest starting point for a readable player-facing browser.
It is compact, but it leaves mathematical foundations and formal systems in
metadata or deeper branches.

For the current design, we should provisionally collapse the visible
top-level entity split to:

```text
Entity
├── Physical
└── Abstract
```

“Informational” and “social” should initially be treated as abstract or
representational patterns, with an explicit physical embodiment when one
exists. A book, computer, contract, or organization can therefore have both:

```text
Abstract content, role, or institution
└── physically embodied by
    └── Physical artifact, person, document, or activity
```

This is not a claim that information or society are unreal. It is a
presentation decision that keeps the top-level question simple while
preserving their physical realizations and their relations to people,
artifacts, and events. The data model should support both facets rather than
forcing an informational or social concept to be exclusively abstract.

### Historical mathematical examples (non-canonical)

The earlier large mathematical projection has been retired as a competing
tree. Its surviving decisions are already incorporated into the canonical
branch above: mathematics is organized by entity kind, not by academic
discipline; foundations, formal artifacts, and models remain distinguishable;
and properties, relations, representations, and proofs cross-cut the
mathematical entities. The examples below are retained only to specify those
role distinctions and are not an additional navigation tree.

```text
Entity
├── Physical
│   ├── Matter, energy, fields, organisms, artifacts, places
│   └── Physical inscriptions and implementations
│       ├── Written equation on paper
│       ├── Executing program
│       ├── Printed proof
│       └── Laboratory measurement
└── Abstract
    ├── Mathematical entities
    │   ├── Foundational formal entities
    │   │   ├── Logical entities
    │   │   │   ├── Terms and formulas
    │   │   │   ├── Predicates and propositions
    │   │   │   ├── Logical operators and quantifiers
    │   │   │   ├── Inference rules and proof objects
    │   │   │   └── Logical models and truth conditions
    │   │   ├── Set-theoretic structures
    │   │   │   ├── Sets and collections
    │   │   │   ├── Set-membership and subset relations
    │   │   │   ├── Set operations and products
    │   │   │   ├── Functions and power sets
    │   │   │   ├── Natural numbers, ordinals, and cardinals
    │   │   │   └── Set-theoretic formal theories
    │   │   ├── Type-theoretic structures
    │   │   │   ├── Types, terms, and values
    │   │   │   ├── Products, sums, and function types
    │   │   │   ├── Inductive and dependent types
    │   │   │   ├── Universes and identity types
    │   │   │   └── Proofs as inhabitants of propositions
    │   │   └── Categorical structures
    │   │       ├── Objects and morphisms
    │   │       ├── Composition and identity
    │   │       ├── Functors and natural transformations
    │   │       ├── Limits, colimits, and adjunctions
    │   │       └── Equivalences, toposes, and internal logics
    │   ├── Number systems
    │   │   ├── Natural numbers
    │   │   ├── Integers
    │   │   ├── Rational numbers
    │   │   ├── Real numbers
    │   │   ├── Complex numbers
    │   │   ├── Algebraic and transcendental numbers
    │   │   └── Arithmetic operations, order relations, divisibility relations, and equations
    │   ├── Algebraic structures
    │   │   ├── Groups and subgroups
    │   │   ├── Rings and ideals
    │   │   ├── Fields and extensions
    │   │   ├── Vector spaces and linear maps
    │   │   ├── Modules, algebras, and representations
    │   │   └── Algebraic structure categories
    │   ├── Geometric and topological structures
    │   │   ├── Points, lines, planes, and spaces
    │   │   ├── Angles, distances, and coordinate systems
    │   │   ├── Curves and conic sections
    │   │   │   ├── Circle
    │   │   │   ├── Ellipse
    │   │   │   ├── Parabola
    │   │   │   └── Hyperbola
    │   │   ├── Manifolds and tangent spaces
    │   │   ├── Topological spaces and continuity structures
    │   │   ├── Metric spaces and measure spaces
    │   │   └── Differential structures and algebraic varieties
    │   ├── Analytic and dynamical structures
    │   │   ├── Sequences, limits, and convergence
    │   │   ├── Derivatives and integrals
    │   │   ├── Differential equations
    │   │   ├── Dynamical systems
    │   │   ├── Function spaces and operators
    │   │   └── Fourier transforms and distributions
    │   ├── Discrete and computational structures
    │   │   ├── Combinatorial structures and graphs
    │   │   ├── Algorithms and complexity classes
    │   │   ├── Automata and formal languages
    │   │   ├── Computable and recursive functions
    │   │   ├── Cryptographic constructions and information measures
    │   │   └── Programming-language models and semantics
    │   ├── Probabilistic and statistical structures
    │   │   ├── Sample spaces and random variables
    │   │   ├── Probability measures and distributions
    │   │   ├── Expectation and conditional probability
    │   │   ├── Statistical models and inference
    │   │   └── Stochastic processes
    │   ├── Mathematical models of physical systems
    │   │   ├── Classical dynamical models
    │   │   ├── Relativistic spacetime models
    │   │   ├── Quantum states and observables
    │   │   ├── Hilbert spaces and operator algebras
    │   │   ├── Quantum field models
    │   │   └── Gauge fields and geometric field models
    │   └── Mathematical objects and values
    │       ├── Sets, functions, sequences, and structures
    │       ├── Numbers and other values
    │       ├── Equations and solutions
    │       ├── Curves, surfaces, and spaces
    │       ├── Proofs, theorems, and counterexamples
    │       └── Models and interpretations
    ├── Informational and representational entities
    │   ├── Symbols, names, and notation
    │   ├── Data, records, and messages
    │   ├── Documents, software, and media contents
    │   ├── Definitions, classifications, and ontologies
    │   └── Statements, propositions, and theories
    └── Social and institutional entities
        ├── Roles and statuses
        ├── Organizations and communities
        ├── Rules, laws, contracts, and currencies
        ├── Norms, obligations, and permissions
        └── Institutions and collective practices
```

The naming rule is deliberate: a visible node must name a kind of entity,
property, relation, structure, artifact, process, or formal object. A
discipline, research program, school subject, or college course is
provenance or metadata, not a parent category. Thus `Circle` and `Parabola`
can be first-class geometric entities under `Curves and conic sections`,
while “geometry” belongs in the source-discipline metadata. Likewise,
`Computable function` is an entity or structure, while “computability” as a
research topic is not a parent; `Classical dynamical model` is a mathematical
model, while “classical mechanics” is a subject label.

This projection deliberately repeats some concepts in different roles. For
example:

- **Three** is an abstract mathematical entity, a value, and an inhabitant of
  the type `Natural`.
- **Prime** is a mathematical property or predicate; `Prime(3)` is a
  proposition; and a proof of `Prime(3)` is a formal evidence object.
- A **circle** is an abstract geometric structure; its equation is a
  representation; a chalk drawing is a physical artifact; and “this point
  lies on the circle” is a relation or proposition.
- **Truth** is a property of propositions or models, while `True` may be a
  logical value or a proposition depending on the formal system.
- A **conic section** is a geometric entity, its defining equation is a
  representation, and the relation between the curve and its focus or
  directrix is part of its mathematical structure.
- A **Lean theorem** is an abstract proposition, its proof term is an
  abstract formal object, its source file is an informational artifact, and
  the checked compilation is a physical or computational event.

The mathematical branch should therefore not be a flat list of school
subjects. It should distinguish at least four cross-cutting roles:

```text
Mathematical concept
├── Object or structure
├── Property or predicate
├── Relation, operation, or mapping
└── Representation, proposition, proof, or model
```

The visible browser may eventually collapse much of this structure for
ordinary play, while the formal profile retains the full distinctions.

**SUMO/BFO-inspired variant**

- **Entity:** Continuant, Occurrent, Quality, Disposition, Role, Site,
  Information artifact
- **Property:** Intrinsic quality, Relational quality, Function, Disposition,
  Role, State
- **Relation:** Participation, Parthood, Dependence, Location, Temporal,
  Causal, Classification

This is stronger for scientific and biomedical modeling, but its vocabulary
is less familiar and some candidates are better modeled as facets than
visible siblings.

**Mathematical and formal variant**

- **Entity:** Individual, Collection, Class/type, Structure, Proposition,
  Model, Formal artifact
- **Property:** Predicate, Refinement, Invariant, Quantity, Truth value,
  Computability, Proof status
- **Relation:** Membership, Typing, Application, Function, Interpretation,
  Satisfaction, Entailment, Derivation, Isomorphism

This gives numbers, sets, types, proofs, and models a principled home, but
would be a poor default tree for ordinary physical nouns.

**Event-and-situation variant**

- **Entity:** Object, Agent, Process, Event, State, Situation, Place,
  Information object
- **Property:** Quality, Capability, Function, Role, Status, Goal, Norm
- **Relation:** Participation, Part-whole, Location, Time, Causation,
  Ownership, Communication, Evidence

This is strongest for everyday questions and narratives, especially actions,
agents, places, and social facts, but less explicit about mathematical
structures and formal syntax.

**Type-system variant**

- **Entity:** Type, Term, Value, Structure, Proposition, Proof artifact,
  Model
- **Property:** Type constraint, Refinement, Effect, Invariant, Truth,
  Computability, Capability
- **Relation:** Inhabits, Subtypes, Applies-to, Evaluates-to, Constructs,
  Proves, Interprets, Composes

This variant aligns with Lean, Scala, proof assistants, and executable
semantics. It should be a formal overlay or specialist view, not the sole
visible organization of the noun ontology.

**Roget-informed conceptual variant**

- **Entity:** Matter and life, Space, Mind and knowledge, Society and action,
  Abstract relations, Emotion and value
- **Property:** Quality, Quantity, Evaluation, Disposition, Intention,
  Social status
- **Relation:** Association, Comparison, Causation, Participation,
  Representation, Classification

This variant maximizes familiar conceptual neighborhoods and vocabulary
discovery. It is useful for the player-facing language layer, but its
categories are not sufficiently formal to serve as the authoritative
semantic model.

### Canonical implementation rules

Use `Entity` as the root. Its first two semantic children are `Realized
entity` and `Abstract entity`; `Object` and `Process` are children of
`Realized entity`. `Property` and `Relation` remain top-level semantic
categories in the current projection.
Add the other variants as named profile projections over the same source
graph. In particular:

- keep physical/abstract/informational/social as entity facets or second-level
  display candidates;
- preserve process/event/state distinctions under Entity when they are
  useful for navigation;
- represent classes, types, propositions, proofs, and values as entities with
  explicit typing, membership, denotation, and proof relations;
- treat qualities, quantities, dispositions, roles, and functions as
  properties unless a particular one is reified as an entity;
- retain relation families as typed relation metadata rather than forcing all
  relations into ordinary noun branches; and
- generate specialist views for BFO/SUMO-style, mathematical, Lean/type
  system, and Roget-informed browsing without changing the canonical graph.

### Formal-layer consequences of the current projection

The current projection keeps the semantic tree separate from the formal
layer. `Entity`, `Property`, and `Relation` answer different questions from
`Type`, `Term`, `Value`, and `Proof`:

- What sort of thing is this in the world?
- Is it an object, event, quality, relation, description, or proposition?
- Is it a mathematical structure, a formal symbol system, or a model of one?
- Is it a class, an instance, a value, a type, or a type-level operation?

These distinctions are represented as typed metadata and cross-links rather
than as another visible root. SUMO remains useful as a source of formal
distinctions and axioms, but its top-level presentation is a mapping layer,
not the final upper ontology.

### Tegmark's mathematical-structure chart

The attached chart is best treated as a visual prior-art rendering of the
idea that increasingly rich mathematical structures arise by adding
operations, predicates, axioms, topology, measure, geometry, and physical
interpretation. The definitive scholarly source for that Tegmark framework is
Max Tegmark's *The Mathematical Universe*:

- [arXiv record and authoritative preprint](https://arxiv.org/abs/0704.0646)
- [Published version, Foundations of Physics](https://doi.org/10.1007/s10701-007-9186-9)

The chart image itself is not an authority for taxonomy, and its exact
provenance should not be inferred from the screenshot alone. The paper is the
source to cite for Tegmark's mathematical-structure/formal-system
distinction; the image is useful as a compact design prompt for a future
mathematical branch.

### Mathematical foundations retained as metadata

Modern mathematics supplies a more disciplined upper-level vocabulary than
SUMO's current abstraction branch, but not a ready-made everyday ontology.
The useful ideas are complementary:

- **Set-theoretic foundations** provide membership, subset, union, product,
  function, relation, and structure-building operations. ZFC is a foundation
  for mathematics, not a claim that every ordinary noun is best represented
  as a set.
- **Type theory** distinguishes terms, types, dependent types, constructors,
  and proofs. This is close to the intuition behind Scala class hierarchies:
  a type describes admissible values, subtyping expresses substitutability,
  and traits or interfaces express reusable capabilities. Scala's model is
  not itself an ontology, but it is a useful implementation metaphor for
  separating nominal categories, structural capabilities, and instances.
- **Category theory** emphasizes objects, morphisms, composition, identity,
  products, coproducts, limits, and functors. It is especially valuable for
  modeling relations and transformations that a noun-only tree cannot show.
- **Structural mathematics** treats a mathematical object by its operations,
  relations, and laws rather than by its material or name. This is a strong
  antidote to confusing a class label with the properties that make its
  instances members of the class.
- **Formal systems and model theory** distinguish syntax, axioms, derivations,
  interpretations, and models. This gives the ontology a clean place for
  languages, theories, mathematical structures, and the real-world systems
  they describe.

These foundations do not replace the canonical tree. They supply metadata
and relation vocabularies:

In the data model, a node may have a **kind** (`object`, `event`, `quality`,
`relation`, `representation`, `type`, `structure`, or `theory`) in addition
to one or more parent links. The browser can project a single primary
navigation parent while retaining cross-links between a type and its
instances, a structure and its models, and a proposition and the situation
it describes.

### Retired synthesis notes

The former source-by-source synthesis table is retired. Its recommendations
are now implemented directly: curated v1 and Roget inform player-facing
labels; SUMO supplies semantic checks; Schema.org and WordNet supply
contemporary labels and lexical bridges; and mathematical foundations supply
formal metadata. None is a competing visible upper tree.

### Implementation consequences

Before changing the published browser, build a small upper-ontology
comparison manifest. For every canonical node, record its kind, intended
children, alternate parents, and whether it is player-visible or metadata
only. Test the projection against ordinary examples such as `dog`,
`running`, `red`, `ownership`, `number`, `integer`, `group`, `function`,
`software type`, `proposition`, and `quantum field`.

The review should prefer a split whenever a node currently answers multiple
incompatible questions. In particular, `Abstract` should not remain a
catch-all for mathematical structures, attributes, propositions, relations,
and fictional or informational entities. The implementation should preserve source provenance and alternate parents
while introducing explicit kind metadata. The visible root is now fixed
provisionally as the triad; future changes should be evidence-driven rather
than another wholesale top-layer redesign.

## Roget as lexical enrichment for the curated v1 tree

This section should be retained, but its scope is narrower than the new
`Upper ontology` section. The upper-ontology discussion treats Roget as
candidate prior art for conceptual partitioning; this section records the
concrete lexical crosswalk and the implementation decision that Roget
enriches v1 without becoming its structural parent taxonomy. It is therefore
not redundant: one section concerns upper-level design, while this one
concerns vocabulary evidence, aliases, and gameplay-oriented placement.

[`Rogets/index.html`](Rogets/index.html) is a faithful browser of the 1,000
numbered concepts in the 1911 Gutenberg edition. It differs fundamentally
from v1: Roget organizes words into six broad conceptual classes, sections,
and subsections, while v1 organizes familiar answer categories around
playable physical, living, and abstract distinctions. Roget's entries are
semantic neighborhoods containing synonyms and related expressions, not
necessarily kinds of things.

[`Rogets/crosswalk.json`](Rogets/crosswalk.json) is the first review artifact.
It compares Roget's concept titles and extracted noun-list phrases with the
628 v1 terminal labels using exact normalized text only. The first pass finds
402 Roget concepts with at least one exact label or phrase match: 59 title
matches are marked high confidence and 343 noun-list matches are marked
medium confidence. These are proposals, not accepted edits; a phrase such as
“air” or “state” can match a v1 label while meaning something different in
context, so every proposal needs semantic and gameplay review.

[`Rogets/index2.html`](Rogets/index2.html) remains the detailed review view.
The canonical [`index.html`](index.html) now exposes the accepted Roget
vocabulary tranches as aliases on existing leaves and includes them in search.
The two commits are intentionally separate: the 59 high-confidence concept
matches landed first, followed by the 343 medium-confidence noun-list
matches. Neither tranche changes the category structure or silently promotes
a synonym into a new answer category.

There is no clean automatic graft from Roget into v1. A Roget concept such as
“Existence,” “Quantity,” or “Answer” does not identify a single noun category,
and even apparently concrete concepts can mix objects, actions, properties,
and phrases. Treating every Roget heading as a v1 node would make the game
tree less noun-like and would reintroduce the imbalance and abstraction that
the WordNet experiment exposed.

Roget can still improve v1 in several disciplined ways:

- **Vocabulary discovery:** use the concept entries and their noun lists to
  find familiar labels missing from v1, then place only concrete game answers
  under reviewed existing parents.
- **Sibling discovery:** compare nearby Roget concepts to identify gaps such as
  common foods, tools, materials, body parts, and organisms.
- **Vocabulary wording:** use Roget's synonym neighborhoods to make labels
  and search more forgiving without adding duplicate concepts.
- **Abstract branch review:** use Roget's classes to audit v1's abstract
  coverage, while retaining v1's game-oriented boundaries.
- **Separate alternate profile:** preserve the Roget browser as a conceptual
  reference rather than pretending it is a superior replacement taxonomy.

The next Roget step is not to add more raw words. It is to turn any proposed
new answer categories into a reviewed manifest: map each candidate noun phrase
to a v1 parent, record evidence and intended semantic placement, and accept
only familiar terms with a clear interpretation.

## Structure before scale

The central artifact is the decision tree, not its vocabulary count. Before
adding hundreds or thousands of nouns, the next candidate should be a
structure-first v1.1 review:

- require every visible internal node to have at least two useful children;
- retain unary paths when they carry useful meaning or provenance; do not
  treat one-child structure as an automatic defect;
- inspect every top-level and second-level split for balanced candidate mass;
- rewrite labels and branch descriptions so they express observable, stable
  distinctions rather than merely restating a parent label;
- identify misplaced leaves, duplicate labels, overloaded branches, and
  missing everyday sibling categories; and
- accept new leaves only after a parent and a useful discriminator already
  exist.

This ordering explains why the initial handcrafted tree performs better than
the larger imported profiles. It was designed around small numbers of
familiar, answerable distinctions, comparable siblings, and recognizable noun
categories.
Roget's tree optimizes conceptual association, Propædia optimizes coverage of
human knowledge, and biological databases optimize scientific ancestry. None
optimizes the joint objective of familiar labels, balanced semantic branches,
single-parent navigation, and useful stopping depth. That objective is a
specialized design problem, so the absence of a ready-made prior-art tree is
expected rather than evidence that the handcrafted structure is anomalous.

## Navigation projection algorithm

The source graph should remain authoritative. The build profile should:

- import stable source IDs, labels, glosses, frequencies, and all source edges;
- select a declared frequency and familiarity budget;
- add complete source ancestry needed to connect selected concepts;
- choose one deterministic display parent only for presentation;
- calculate subtree candidate mass and prefer balanced displayed splits;
- expose source distinctions and declared attributes as branch metadata; and
- preserve discarded candidates and alternate paths in a manifest.

This keeps source semantics separate from game presentation. The one-page tree
is a reproducible view, not a hand-maintained fork.

## Future experiments

The WordNet experiment should be evaluated at target sizes near 5K, 8.9K, and
10K nodes. Measure browser load, full expansion, search latency, memory, maximum depth,
duplicate labels, and branch coverage.
Prefer the smallest profile that covers common game answers while preserving
the current one-page browsing experience.

The next useful improvements are the structural audit, the biological graft
specified above, and a coverage report for ordinary noun candidates. Each
profile should come from one source manifest rather than a forked ontology;
Wikidata, FoodOn, and Wikipedia remain separately labeled enrichment sources.

## History

### Retired v2 expansion

The mechanically expanded 5K–10K profile is retained only for analysis. It was
rejected because source-driven ancestry produced sparse nonliving coverage,
unhelpful unary chains, and poor visible splits. No node budget or source target
is a current commitment. The next profile must pass structural review before
adding reviewed leaves through a shared, versioned manifest.

## Implementation

### How the WordNet tree was generated

[`generate_wordnet_20q.py`](generate_wordnet_20q.py) loads local Princeton
WordNet 3.0 through NLTK, selects a declared frequency-ranked noun profile
connected to `entity.n.01`, closes over the required hypernym ancestry, and
projects multiple hypernyms to one deterministic display parent. The manifest
retains source IDs, glosses, frequencies, all hypernym edges, and the selected
display parent; the projection does not rewrite WordNet.

Regenerate the historical profile with:

```sh
NLTK_DATA=~/nltk_data /tmp/wordnet-ontology-venv/bin/python \
  generate_wordnet_20q.py --target 7000 --output-dir .
```

### Practical scope and UI constraint

The active constraint is the shared static browser: searchable, collapsible,
single-parent navigation with source links, counts, lineage, and definitions
when supplied.
