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

### Upper Ontologies

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

#### Upper Ontology Definitions

##### Entity

- **SUMO:** `Entity` is the universal class at the top of the SUMO hierarchy.
- **BFO:** `entity` is used for anything that exists or has existed, including
  continuants and occurrents; see [BFO 2020](https://basic-formal-ontology.org/bfo-2020.html).
- **Schema.org:** `Thing` is the most generic type, so Schema.org does not use
  `Entity` in the same root role; see [Thing](https://schema.org/Thing).

##### Object

- **SUMO:** `Object` is roughly an ordinary object whose spatiotemporal extent
  divides into spatial parts parallel to the time axis; this is the source
  definition currently attached to our physical branch.
- **BFO:** an object is a material entity that is spatially extended,
  maximally self-connected, and persists through time as an independent
  continuant.
- **OWL/RDF:** “object” commonly appears in the object position of a triple,
  while an `owl:ObjectProperty` relates individuals; this is a syntactic or
  relational use, not a universal ontological root.

##### Thing

- **WordNet:** `thing.n.01` is “a separate and self-contained entity.”
- **Schema.org:** `Thing` is “the most generic type of item,” with all other
  Schema.org types descending from it.
- **DOLCE-style usage:** “thing” is ordinary-language vocabulary rather than
  a sufficiently precise foundational category; formal distinctions are made
  with endurant, perdurant, quality, region, and social-object categories.

##### Item

- **CIDOC CRM:** `E77 Persistent Item` covers persistent items of material,
  immaterial, or propositional nature that can be identified and referred to;
  see [CIDOC CRM](https://cidoc-crm.org/).
- **Schema.org:** “item” is the generic vocabulary for an instance of a
  `Thing`, not a peer upper-ontology category.
- **SKOS:** an `skos:Concept` is an item in a concept scheme identified by a
  URI; this is an information-model use, not a claim about all entities.

##### Being

- **WordNet:** `being.n.01` denotes the state or fact of existing, while other
  senses denote a living thing or person; the word is therefore polysemous.
- **Aristotelian and scholastic traditions:** “being” names what is or what
  exists, but the term does not by itself supply a usable partition of beings.
- **Ethics:** “being” is commonly used for a morally considerable subject or
  living entity; reserve this specialized use for the ethics section rather
  than overload the upper ontology.

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


#### Upper Ontology Excerpts

##### Our ontology

```text
Entity: that which can be referred to.
├── Realized entity: an entity that takes no arguments and has spatiotemporal embodiment.
│   ├── Object: a realized entity regarded as persisting through time.
│   └── Process: a realized entity regarded as occurring through time.
├── Abstract entity: an entity that takes no arguments and lacks spatiotemporal embodiment.
├── Property: an entity that takes one argument.
└── Relation: an entity that takes more than one argument.
```

##### Sowa's Knowledge Representation Ontology

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

##### Suggested Upper Merged Ontology

```text
Entity: the universal class containing every object in the ontology.
├── Physical: entities that have a location in space or time.
│   ├── Object: a physical entity that is not a process.
│   │   └── SelfConnectedObject: an object whose parts are connected.
│   └── Process: a physical entity that has temporal parts or stages.
└── Abstract: entities that are not physical.
```

##### Descriptive Ontology for Linguistic and Cognitive Engineering

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

##### Basic Formal Ontology

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

##### General Formal Ontology

```text
Entity: anything that can be represented in the ontology.
├── Concrete: an entity that exists in space-time.
│   ├── Presential: a concrete entity present at a given time.
│   │   └── MaterialObject: a material presential occupying space.
│   └── Process: a concrete entity that unfolds through time.
└── Abstract: an entity not located in space-time.
    └── Category: an abstract entity used to classify individuals.
```

##### Unified Foundational Ontology

```text
Entity: anything that exists according to the domain theory.
├── Endurant: an entity wholly present whenever it exists.
│   ├── Object: an endurant that bears properties and participates in events.
│   │   └── MaterialObject: an object with material or physical realization.
│   └── Moment: an existentially dependent endurant.
└── Perdurant: an entity whose existence unfolds over time.
    └── Event: a perdurant composed of temporal parts.
```

##### WordNet noun hierarchy

```text
Entity: something that has distinct and independent existence.
├── PhysicalEntity: an entity that has a physical existence.
│   └── Thing: an entity regarded as an object or unit.
│       └── Object: a tangible and visible entity.
└── Abstraction: a general concept formed by abstraction.
```

##### Schema.org

```text
Thing: the most generic type of item.
├── Place: a physical location.
│   └── Landform: a natural physical feature of the Earth.
├── Product: any offered product or service.
│   └── IndividualProduct: a single, identifiable product instance.
├── CreativeWork: the most generic kind of creative work.
└── Event: an event happening at a given time and location.
```

##### Aristotle's Categories

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

## History

### Retired v2 expansion

The mechanically expanded 5K–10K profile is retained only for analysis. It was
rejected because source-driven ancestry produced sparse nonliving coverage,
unhelpful unary chains, and poor visible splits. No node budget or source target
is a current commitment. The next profile must pass structural review before
adding reviewed leaves through a shared, versioned manifest.

## Implementation

### Publishing the tree to the wiki

Any change to the ontology tree or to the page that presents it must be
published to the wiki before the work is complete. Regenerate the affected
`ontology.json` and `index.html` artifacts from their source data and
generator, run the browser regression checks, and copy the validated artifacts
to the wiki's `Ontology/` publication directory. Publish the corresponding
manifest or source snapshot whenever the generated data or its provenance
changes. The regression checks must exercise the example search buttons as
well as ordinary search, expansion, collapse, and lineage navigation. Do not
leave a source-tree or browser change visible only in a local working copy.

### Node information notes

The browser should place a Unicode information glyph `ⓘ` after child and
descendant counts. Clicking it opens a terse node note. `Property` and
`Relation` notes should retain their reviewed child inventories and provenance;
other notes are source- or node-specific.

- **Property:** inventory assembled in the maximal synthesis and cross-compared
  across Aristotelian, SUMO/BFO, and formal/type-theoretic sources.
- **Relation:** inventory assembled beside Property; it mixes subject-matter,
  logical, mathematical, operational, and provenance axes and needs sibling
  review.

### Projection rules

- Preserve source IDs, labels, definitions, aliases, and all source edges.
- Select one deterministic primary parent for visible navigation.
- Retain alternate parents and suppressed ancestors as metadata.
- Derive roots from incoming displayed edges.
- Flatten empty structural nodes in the rendered view.
- Keep source semantics separate from the navigation projection.

### SUMO PDF extraction

The SUMO browser is generated from the checked-in PDF graph: download and hash
its source, convert it to SVG and positioned text, extract labeled arcs, and
run `generate_sumo.py --pdf-graph`. Keep the 518-node, 554-arc source graph;
choose one primary parent for display, retain alternate parents, and record the
four provisional placements separately from PDF-derived edges.


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
