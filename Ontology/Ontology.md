# Omniversal Ontology

❓ Decision: [Composition’s immediate children](#pending-decision-compositions-immediate-children).

## Principles

- The incumbent with the accepted upper graft remains the canonical tree; imported systems are source, audit, and enrichment layers rather than replacements.
- The canonical tree has one primary parent per node. Definitions, alternate classifications and qualifications of a split must be inspectable from the public tree; aliases, source IDs and provenance support the same account in data.
- The canonical upper structure is Entity → Particular / Predicable. Particular contains Object, Occurrence, Feature, Region, Composition and Formal entity. Descendants in the [incumbent browser](index.html) are a provisional graft beneath these accepted categories.
- The browser is a shared static, searchable, collapsible tree. It does not generate suggested questions, and it displays definitions only when supplied by source material or an explicit project definition.
- The canonical tree, its definitions and visible annotations state the project ontology. Machine-readable data must encode the same commitments without a substantially different, more authoritative hidden ontology. Imported source graphs remain authoritative for their own source claims; preserve those claims separately when the project makes a different decision.
- Classify by kind, not role. The canonical parent should express what an entity is, not a role it happens to play. Roles such as agent, location, participant, container, bearer, or instrument should normally be represented as properties, relations, or alternate classifications unless the role defines the entity's kind.
- Prefer coverage over forced uniqueness. Every concept should have at least one defensible home. Multiple defensible classifications are preferable to leaving a concept unclassified; the canonical tree selects one primary home while preserving useful alternatives.
- Treat ambiguity as information. Multiple plausible homes are expected in a multidimensional ontology and should be preserved as alternate classifications. Persistent ambiguity near the upper ontology is also a signal to reexamine whether the categories represent genuinely distinct kinds.
- Choose the canonical parent by essence, alternatives by applicability. When several classifications apply, prefer as the primary parent the category that best describes what the entity is; retain categories describing what it does, where it is, how it is used, or what relationships it participates in as alternate structure or metadata.
- Structural quality, familiar labels, useful branching, and source fidelity take priority over node count or premature vocabulary expansion.
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

The immediate biological task is to replace the current organism subtree with a curated display taxonomy. The links below are ordered by usefulness for this project, not by scientific authority alone:

- [OneZoom Tree of Life Explorer](https://www.onezoom.org/) — best browsing model for a large evolutionary tree; use its interface and common-name presentation as design prior art, not as the sole authority.
- [Open Tree of Life](https://tree.opentreeoflife.org/) — strongest open candidate for evolutionary ancestry, stable taxon identifiers, and a tree that keeps humans within tetrapod and lobe-finned-fish history.
- [Catalogue of Life](https://www.catalogueoflife.org/explore) — strongest candidate for accepted names, synonyms, and broad checklist authority; compare its Base and Extended releases.
- [GBIF Backbone Taxonomy](https://www.gbif.org/species) — excellent browsable name-resolution and synonymy backbone for finding and normalizing familiar organisms.
- [NCBI Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi) — authoritative computational and sequence-linked taxonomy, especially for microbes and viruses; too technical to copy directly.
- [ITIS](https://www.itis.gov/) — stable government-supported name and rank reference useful for cross-checking accepted placement.
- [World Register of Marine Species](https://www.marinespecies.org/) — expert-maintained marine supplement, not a general root.
- [TimeTree](https://timetree.org/) — useful for evolutionary relationships and divergence context, not as the visible noun hierarchy.

#### Online biological taxonomies

These resources are the strongest available prior art for extending the organism portion of a general noun hierarchy. None is a complete general ontology: they optimize taxonomic identity, scientific names, synonymy, and research interoperability rather than familiar labels or balanced gameplay.

##### Catalogue of Life

- **Origin:** an international taxonomic data initiative launched in 2001, coordinated through the Species 2000 and Integrated Taxonomic Information System communities and now hosted by the Catalogue of Life partnership.
- **Current status:** active and release-based. The [Catalogue of Life releases](https://www.catalogueoflife.org/data/download) distinguish a verified Base Release from a broader Extended Release.
- **Node count:** release-dependent; the current catalog reports millions of accepted species and names, with counts varying by release and inclusion policy. Use the release metadata rather than a timeless number.
- **Prominence proxy:** widely used as a global checklist and taxonomic reference, with expert-verified coverage and downloadable releases.
- **Fit:** the best initial authority for accepted organism names and high-level taxonomic placement. It should supply biological structure while the curated tree supplies playable common-language grouping.

##### GBIF Backbone Taxonomy

- **Origin:** built by the Global Biodiversity Information Facility, an international intergovernmental biodiversity-data infrastructure founded in 2001.
- **Current status:** active, versioned, and designed to normalize names from many biodiversity datasets. See the [GBIF Backbone Taxonomy](https://www.gbif.org/dataset/7ddf754f-d193-4cc9-b351-99906754a03b).
- **Node count:** release-dependent and measured in names, taxa, and synonymized records rather than one fixed class count.
- **Prominence proxy:** GBIF is a major global biodiversity data network; its backbone is used for occurrence-data name matching across a large publishing ecosystem.
- **Fit:** excellent for resolving common names and synonyms to scientific taxa and for finding candidate organisms. It is more of a cross-dataset nomenclatural backbone than a carefully curated game hierarchy.

##### NCBI Taxonomy

- **Origin:** developed by the National Center for Biotechnology Information at the U.S. National Library of Medicine to organize organisms represented in genetic and genomic databases.
- **Current status:** active, continuously updated, and available through the [NCBI Taxonomy database](https://www.ncbi.nlm.nih.gov/taxonomy).
- **Node count:** release- and database-dependent; it contains hundreds of thousands of scientific taxa and many sequence-associated records, with counts exposed through NCBI's statistics and downloads.
- **Prominence proxy:** it is embedded in GenBank, RefSeq, and other major NCBI sequence resources, making it a standard computational taxonomy for molecular biology.
- **Fit:** authoritative for sequence-linked scientific identity and useful for validating deep organism branches, but too technical and unevenly familiar to serve as the visible game taxonomy.

##### Open Tree of Life

- **Origin:** an open-science collaboration funded by the U.S. National Science Foundation and other partners, launched in the 2010s.
- **Current status:** active research infrastructure combining a synthetic tree with source taxonomies and stable taxon identifiers. Browse it at the [Open Tree of Life](https://tree.opentreeoflife.org/).
- **Node count:** release-dependent and measured in taxa and phylogenetic relationships; the synthetic tree incorporates millions of named taxa from contributing sources.
- **Prominence proxy:** open APIs, stable identifiers, and published computational methods make it a notable research platform for large-scale comparative biology.
- **Fit:** useful for scientifically coherent ancestry and for checking extinct groups, including dinosaurs. It should be treated as a validation and enrichment source, not copied wholesale into a one-page game tree.

##### Integrated Taxonomic Information System (ITIS)

- **Origin:** a U.S. and international interagency project established in the 1990s to provide authoritative taxonomic names and hierarchy.
- **Current status:** active, maintained, and available through the [ITIS database](https://www.itis.gov/).
- **Node count:** release-dependent, with hundreds of thousands of taxonomic names and records across included organism groups.
- **Prominence proxy:** long-running government-supported identifiers and reuse in biodiversity and environmental datasets.
- **Fit:** a useful stable-name and rank authority, especially for cross-checking Catalogue of Life and GBIF mappings. Its coverage and scientific granularity are too specialized to define the whole game tree.

##### World Register of Marine Species

- **Origin:** an international marine-taxonomy initiative launched in 2007 and coordinated through the Flanders Marine Institute.
- **Current status:** active, expert-managed, and release-based; see [WoRMS](https://www.marinespecies.org/).
- **Node count:** release-dependent, with hundreds of thousands of marine taxa and names across accepted and synonymized records.
- **Prominence proxy:** the principal global reference for marine organism names and taxonomic status.
- **Fit:** a high-quality specialized supplement for marine life, but not a general organism root.

#### Approachable cladistic and evolutionary trees

The most useful biological prior art for v2 is not a single taxonomy copied verbatim. It is a scientifically defensible source tree paired with a deliberately compressed display. A cladistic source should be allowed to say that humans are sarcopterygian vertebrates and therefore nested within the broader evolutionary history of fishes, even though “fish” remains an everyday answer category. The visible game tree can collapse intermediate clades when they do not create a recognizable answer or a useful question, while retaining the omitted clades, ranks, and source identifiers in metadata.

##### OneZoom Tree of Life Explorer

- **Origin:** conceived in 2011, released as open-source software in 2012, and maintained since 2015 by a UK charitable organization.
- **Current status:** active, free, and designed explicitly for public exploration. OneZoom uses a fractal, map-like interface so a very large tree can be explored on one page; its current tree relies heavily on the Open Tree of Life and mixes other declared sources. See the [OneZoom explorer](https://www.onezoom.org/) and its [data and methodology overview](https://www.onezoom.org/about.html).
- **Node count:** the project is intended to display a million-tip-scale tree; the exact visible count changes with its source-data release and display configuration.
- **Prominence proxy:** open-source software, a charitable organization, collaboration with the Linnean Society, and published methods including [Dynamic visualisation of million-tip trees](https://doi.org/10.1111/2041-210X.13766).
- **Fit:** the best interface prior art for keeping a huge scientifically grounded tree navigable. Its species-first display is too deep and biological for the whole ontology, but its zoomed overview, common names, images, and source links suggest how v2 can hide taxonomic detail without discarding it.

##### TimeTree

- **Origin:** developed by Blair Hedges, Sudhir Kumar, and collaborators as a public knowledge base for evolutionary relationships and divergence times; the current major resource is TimeTree 5.
- **Current status:** active research and teaching resource. The [TimeTree site](https://timetree.org/about) combines published divergence estimates and lets users explore the evolutionary timescale between taxa.
- **Node count:** release-dependent; TimeTree 5 is a large species-level synthesis rather than a compact hand-authored hierarchy. Its useful unit is a dated relationship, not a game category.
- **Prominence proxy:** TimeTree 5 is described in a 2022 article in *Molecular Biology and Evolution*, [An Expanded Resource for Species Divergence Times](https://doi.org/10.1093/molbev/msac174).
- **Fit:** useful for validating evolutionary-history examples and explaining why apparently different organisms are convergent rather than close relatives. It should validate relationships and dates, not dictate every visible v2 split.

##### Recommended collapsed-clade pattern

These resources support a three-layer design for the life portion of v2:

- **Source layer:** retain the accepted scientific tree, including clades that are important for statements such as “tetrapods are nested within lobe-finned fishes.”
- **Navigation layer:** retain only ancestors that create a useful distinction, explain a notable organism, or keep the visible branch intelligible. Collapse ranks such as some orders and families when all selected descendants would otherwise form a one-child chain.
- **Answer layer:** show familiar common names and notable clades such as mammals, birds, marsupials, dinosaurs, coelacanths, and monotremes. Add a short scientific note where everyday language hides a meaningful relationship, rather than forcing the player to answer with a Latin clade.

This is not permission to redraw evolutionary relationships for convenience. It is a presentation projection: source parentage, alternate placements, synonyms, and suppressed intermediate clades remain auditable. OneZoom is the strongest model for the browsing interaction; Open Tree of Life and Catalogue of Life remain the principal candidates for taxonomic validation; and TimeTree is the best supplement for evolutionary-history and divergence-time context.

#### Single-pane and compressed tree renders

The previous list was not responsive to the requirement. The intended format is now clear from this [Open University-style example image](https://miro.medium.com/v2/resize:fit:4128/1*O-o2WDx710kxPczPH0UUug.jpeg): one tall, printable pane; colored evolutionary branches; named internal clades; and a curated representative organism, fossil, or plant at many leaves. This is not merely an outline of taxon names. It is a visual knowledge map that makes the biological hierarchy browseable through familiar specimens. The matching high-resolution copy is [available here](https://nicolasmicheletti.wordpress.com/wp-content/uploads/2015/09/treeoflife.jpg).

The useful search target is therefore a static classroom/poster-style whole-life tree with fewer than 300 representative leaves and clade labels. Ranked by fit:

- [Open University tree-of-life poster](https://nicolasmicheletti.wordpress.com/wp-content/uploads/2015/09/treeoflife.jpg) — the exact format we should pursue. It uses roughly a hundred representative organisms and fossils, colored branches, readable clade labels, and a single origin-to-present composition. It is much closer to the desired 20-Questions browsing experience than a genome-only tree. Treat the image as presentation prior art; validate and modernize its taxonomy from the authoritative sources above.
- [Tree of life SVG](https://commons.wikimedia.org/wiki/File:Tree_of_life_SVG.svg) — still worth checking as a denser candidate, but it is a genome tree with tiny labels rather than a specimen-rich educational map. It may contain 150–250 visible terminal taxa, though the vectorized lettering requires visual counting.
- [Phylogenetic tree of life 2](https://commons.wikimedia.org/wiki/File:Phylogenetic_tree_of_life_2.svg) — the cleanest strict single-pane baseline: one rooted left-to-right tree with 33 machine-countable labels, spanning Bacteria, Archaea, and Eukarya. It is public domain and easy to print, but too sparse to be the final target.
- [Tree of life](https://commons.wikimedia.org/wiki/File:Tree_of_life.svg) — one radial tree with approximately 35–50 readable group labels, including major bacterial, archaeal, fungal, plant, and animal branches. It is compact and visually legible, but scientifically dated and not a current authority.
- [Berkeley Evolution 101: The Family Tree](https://evolution.berkeley.edu/evolution-101/the-history-of-life-looking-at-the-patterns/the-family-tree/) — explicitly school-oriented and broad, with a single tall image containing nested phylogenies. It is useful presentation prior art, but not a strict uninterrupted single-pane outline because it embeds several zoomed trees.
- [UCMP Life on Earth / Three Domains of Life](https://ucmp.berkeley.edu/alllife/threedomains.html) — a compact educational whole-life treatment that gives viruses their own biological-entities branch and links to deeper exhibits. It is a strong model for visible-versus-linked detail, but it is smaller and partly page-linked rather than a 300-node poster.
- [Tree of life diagrams and historical examples](https://en.wikipedia.org/wiki/Tree_of_life_(biology)) — a useful index of static Haeckel, Woese, and other whole-life diagrams. These are schematic or historical rather than importable authorities, but they provide additional candidates for visual comparison.

The immediate next step is to inspect the first SVG at full resolution and count its visible labels. If it is genuinely below 300, it becomes the largest discovered single-pane template; if it is too dense or exceeds the limit, the 33-label tree is the verified fallback and we should construct an intermediate 100–300-node display ourselves from the authoritative source combination below.

#### Compressed taxon-backbone target

The poster is useful as a visual clue to the desired *kind* of taxonomy, but its organism illustrations are not yet the target data. First reconstruct a single-parent taxon tree whose nodes express the most important evolutionary divisions and transitions; only afterward add representative, familiar, important, and notable species beneath selected taxon leaves.

The first-pass backbone should preserve this path, while telescoping specialist-only ranks and unstable deep clades:

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

This wording deliberately uses **bony vertebrates** rather than only “bony fish,” because tetrapods are nested within Osteichthyes, and **lobe-finned vertebrates** rather than only “lobe-finned fish,” because tetrapods are nested within Sarcopterygii. It also places birds inside dinosaurs and mammals inside synapsids. “Fish,” “algae,” “protist,” “invertebrate,” and “reptile” may remain familiar search or display labels, but should not be silently treated as equivalent to clean clades.

The backbone should retain evolutionary milestones as node annotations rather than inventing extra taxon branches: cellular organization, mitochondria, plastids, multicellularity, land plants, vascular tissue, seeds, flowers, animal bilateral symmetry, moulting, jaws, bony skeletons, lobed fins, limbs, amniotic reproduction, feathers, and mammalian traits. Deep microbial and protist topology should use compact polytomies or “major lineages” until the source evidence justifies more resolution. Horizontal gene transfer, endosymbiosis, uncertain roots, and disputed deep relationships belong in provenance and notes, not hidden by false precision.

Recommended source combination: use Open Tree of Life for evolutionary structure, Catalogue of Life for accepted names and synonyms, GBIF and NCBI for normalization and coverage checks, and OneZoom as the browsing-model reference. Use ITIS, WoRMS, and TimeTree to resolve domain-specific gaps. Do not import any of these raw. Produce one reviewed crosswalk that preserves source IDs, accepted names, synonyms, rank, release, extinct status, and alternate placements while projecting a readable single-parent display tree.

The visible tree should preserve major evolutionary facts—birds under dinosaurs and humans within tetrapods and lobe-finned fishes—while collapsing intermediate clades that do not improve a recognizable distinction. Common names lead; scientific names remain searchable aliases and provenance. Viruses receive a dedicated acellular-infectious-agent subtree with host, genome, transmission, disease, and ecological metadata rather than being forced into ordinary organism ancestry.

The detailed criteria, notable-life policy, virus policy, and graft workflow below are the acceptance specification for this task. The later biological prior-art entries retain source-specific notes and access details.


The figures below are scale or activity proxies, not claims that unlike systems have directly comparable “node” semantics. Counts are release- or snapshot-dependent; links are the authoritative places to refresh them.

### WordNet

- **Origin:** Princeton University, United States; George Miller’s project began in 1985, with the first public release in 1989.
- **Current status:** actively documented and distributed; this experiment uses WordNet 3.0 through [NLTK](https://www.nltk.org/howto/wordnet.html).
- **Node count:** 117,659 synsets in WordNet 3.0 overall; 82,115 noun synsets in the experiment’s installed corpus.
- **Prominence proxy:** 13,739 noun synsets have nonzero corpus-frequency counts in the release; the foundational [WordNet paper](https://doi.org/10.1007/978-94-011-2016-8_2) is a standard reference point for lexical-semantic systems.
- **Fit:** best initial canonical backbone for common noun gameplay.

### Upper Ontologies

These systems are design prior art, not replacements for the canonical tree. They contribute distinctions, metadata patterns, validation methods, or coverage; none should dictate the visible hierarchy wholesale.

- **Aristotle's Categories:** substance, quantity, quality, relation, place, time, position, state, action, and passion. Useful as a sanity check that things, properties, relations, and events are not conflated.
- **Sowa's Knowledge Representation Ontology:** a lattice of physical and abstract, independent, relative, and mediating entities, including objects, processes, schemas, scripts, situations, and descriptions. Useful as a typed overlay, not a tree.
- **Cyc/OpenCyc:** classes, individuals, predicates, rules, exceptions, and context-sensitive microtheories. Useful for common-sense relations, but too large and access-constrained for the visible browser.
- **SUMO:** a formal hierarchy of entities, objects, processes, attributes, and relations with axioms and WordNet mappings. Best formal validation backbone; project it to one display parent rather than showing it raw.
- **Schema.org:** practical types for people, organizations, places, products, events, creative works, medical entities, and intangible things. Useful for contemporary labels and aliases, but shallow and web-oriented.
- **BFO:** continuants, occurrents, material entities, processes, qualities, roles, functions, dispositions, and sites. Useful for principled type checks.
- **DOLCE:** endurants, perdurants, qualities, regions, abstracts, and social objects. Useful for linguistic and cognitive distinctions.
- **GFO and UFO:** continuants, presentials, processes, events, objects, dispositions, situations, roles, relators, qualities, and social facts. Useful comparison families for time and dependence.
- **OntoClean:** rigidity, identity, unity, and dependence as tests for whether a proposed subclass relation is semantically defensible.
- **gist and PROTON:** compact practical upper vocabularies for things, people, organizations, events, places, information, and abstract concepts. Useful candidates for interoperable metadata.
- **Roget, WordNet, FrameNet, and Propædia:** lexical neighborhoods, synsets, frames, and knowledge domains. Useful enrichment sources, not `is-a` roots.
- **RDF/RDFS, OWL, Common Logic, and SHACL:** graph, vocabulary, logic, and validation infrastructure. They support the data model rather than define the visible noun tree.
- **Mereology, social ontology, and process ontology:** part-whole, institution, role, norm, event, activity, and change distinctions that the tree should preserve as typed relations or facets.

The combined design lesson is to keep entity kinds, properties, relations, processes, information, and formal structures distinct; retain time, dependence, part-whole, and social context as metadata; and use formal ontologies to audit definitions and mappings rather than to supply the whole player-facing branch order.

#### Upper Ontology Definitions

##### Entity

- **SUMO:** `Entity` is the universal class at the top of the SUMO hierarchy.
- **BFO:** `entity` is used for anything that exists or has existed, including continuants and occurrents; see [BFO 2020](https://basic-formal-ontology.org/bfo-2020.html).
- **Schema.org:** `Thing` is the most generic type, so Schema.org does not use `Entity` in the same root role; see [Thing](https://schema.org/Thing).

##### Object

- **SUMO:** `Object` is roughly an ordinary object whose spatiotemporal extent divides into spatial parts parallel to the time axis; this is the source definition currently attached to our physical branch.
- **BFO:** an object is a material entity that is spatially extended, maximally self-connected, and persists through time as an independent continuant.
- **OWL/RDF:** “object” commonly appears in the object position of a triple, while an `owl:ObjectProperty` relates individuals; this is a syntactic or relational use, not a universal ontological root.

##### Thing

- **WordNet:** `thing.n.01` is “a separate and self-contained entity.”
- **Schema.org:** `Thing` is “the most generic type of item,” with all other Schema.org types descending from it.
- **DOLCE-style usage:** “thing” is ordinary-language vocabulary rather than a sufficiently precise foundational category; formal distinctions are made with endurant, perdurant, quality, region, and social-object categories.

##### Item

- **CIDOC CRM:** `E77 Persistent Item` covers persistent items of material, immaterial, or propositional nature that can be identified and referred to; see [CIDOC CRM](https://cidoc-crm.org/).
- **Schema.org:** “item” is the generic vocabulary for an instance of a `Thing`, not a peer upper-ontology category.
- **SKOS:** an `skos:Concept` is an item in a concept scheme identified by a URI; this is an information-model use, not a claim about all entities.

##### Being

- **WordNet:** `being.n.01` denotes the state or fact of existing, while other senses denote a living thing or person; the word is therefore polysemous.
- **Aristotelian and scholastic traditions:** “being” names what is or what exists, but the term does not by itself supply a usable partition of beings.
- **Ethics:** “being” is commonly used for a morally considerable subject or living entity; reserve this specialized use for the ethics section rather than overload the upper ontology.

### Mathematics

Mathematics needs its own prior-art subsection because the available systems solve different problems and none is a ready-made noun taxonomy:

- **MSC2020** is the strongest maintained classification of mathematical literature. It is a subject and discipline classification, not a taxonomy of mathematical entities. Use it as an orthogonal subject facet, never as the parent of `Circle`, `Algorithm`, or `Group`.
- **[OpenMath](https://openmath.org/)** represents the semantics of mathematical objects and expressions through symbols and content dictionaries. It is the best candidate for semantic symbols, operations, functions, and relations, but it is not a complete browseable hierarchy.
- **[OMDoc](https://en.wikipedia.org/wiki/OMDoc)** extends OpenMath to definitions, theorems, proofs, examples, and theories. It is especially useful for separating a mathematical object from a statement about it and from a proof or theory containing it.
- **[MMT](https://uniformal.github.io/)** is a foundation-independent framework for formal theories, symbols, structures, imports, and translations. It is a metamodel for mathematical knowledge, not a player-facing tree.
- **[Lean and Mathlib](https://github.com/leanprover-community/mathlib4)** provide a large modern typed dependency graph of definitions, structures, theorems, proofs, and typeclass relationships. They are valuable for validating modern formal practice, but raw Mathlib ancestry reflects proof engineering rather than a general-purpose noun hierarchy.
- **OntoMathPRO** is the closest candidate for an ontology of mathematical knowledge, including mathematical concepts, objects, theories, formulas, theorems, and proofs. Its maintenance, licensing, machine-readable distribution, and possible inheritance of subject-classification structure require a dedicated audit before grafting.
- **Type theory, category theory, set theory, and model theory** provide foundations and structural languages. They supply types, terms, values, proofs, sets, functions, morphisms, models, and interpretations, but none should be copied wholesale as the visible mathematical branch.
- **MathML and related notation standards** represent syntax or presentation and therefore belong in the representation layer, not as the taxonomy of the mathematical things represented.

The current grafting hypothesis is therefore selective: use OpenMath and OMDoc for semantic mathematical objects and formal statements, MMT for cross-foundation theory structure, Lean/Mathlib for modern machine-checked examples, and MSC2020 as metadata. Do not graft MSC2020's disciplines into the noun tree. The entity branch should say `Computational structures` with separate children such as `Algorithms`, `Complexity classes`, `Computable functions`, `Recursive functions`, `Automata`, `Formal languages`, and `Graphs`, rather than a mixed node such as “Algorithms and complexity classes.”


#### Upper Ontology Excerpts

##### Our ontology

```text
Entity
├── Particular
│   ├── Object
│   │   ├── Physical object
│   │   │   ├── Material body
│   │   │   ├── Material portion
│   │   │   └── Physical aggregate
│   │   └── Social object
│   │       ├── Institutional continuant
│   │       └── Social collective
│   ├── Occurrence
│   │   ├── Process
│   │   │   ├── Physical process
│   │   │   ├── Mental process
│   │   │   └── Social process
│   │   ├── Event
│   │   │   ├── Transition event
│   │   │   └── Achievement event
│   │   └── State
│   │       ├── Physical state
│   │       ├── Mental state
│   │       └── Social state
│   ├── Feature
│   │   ├── Quality
│   │   ├── Disposition
│   │   ├── Relationship
│   │   ├── Structural feature
│   │   └── Attitude
│   ├── Region
│   ├── Composition
│   └── Formal entity
└── Predicable
    ├── Property       [provisional inherited branch]
    └── Relation       [provisional inherited branch]
```

##### Sowa's Knowledge Representation Ontology

```text
Entity: anything that exists, whether physical or abstract.
├── Physical: an entity located in the physical world.
│   ├── Continuant: a physical entity that persists through time.
│   │   └── Object: a physical continuant with an independent identity.
│   │       ├── Physical object
│   │       ├── Biological object
│   │       ├── Artifact
│   │       ├── Social object
│   │       ├── Region
│   │       ├── Location
│   │       └── Collection
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
│   │   ├── SelfConnectedObject: an object whose parts are connected.
│   │   │   ├── ContentBearingObject
│   │   │   ├── CorpuscularObject
│   │   │   ├── Food
│   │   │   └── Substance
│   │   ├── Agent
│   │   ├── Collection
│   │   ├── Region
│   │   └── Location
│   └── Process: a physical entity that has temporal parts or stages.
└── Abstract: entities that are not physical.
```

##### Descriptive Ontology for Linguistic and Cognitive Engineering

```text
Particular: an individual that is not a universal.
├── Endurant: an entity wholly present at each time it exists.
│   ├── PhysicalEndurant: an endurant with physical presence.
│   │   └── PhysicalObject: a physical endurant with independent existence.
│   │       ├── AgentivePhysicalObject
│   │       ├── NonAgentivePhysicalObject
│   │       ├── Region
│   │       ├── Place
│   │       └── Collection
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
│   │           ├── ObjectAggregate
│   │           ├── FiatObjectPart
│   │           └── Site
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
│   │       ├── PhysicalObject
│   │       ├── BiologicalObject
│   │       ├── Artifact
│   │       ├── Region
│   │       ├── Place
│   │       └── Collection
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
│   │       ├── PhysicalObject
│   │       ├── BiologicalObject
│   │       ├── SocialObject
│   │       ├── Region
│   │       ├── Place
│   │       └── Collection
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
│           ├── Region
│           ├── Location
│           └── Collection
└── Abstraction: a general concept formed by abstraction.
```

##### Schema.org

```text
Thing: the most generic type of item.
├── Action: an event caused by an agent.
├── BioChemEntity: a biological or chemical entity.
├── CreativeWork: the most generic kind of creative work.
├── Event: an event happening at a given time and location.
├── Intangible: an item that is not physical or tangible.
│   └── ItemList: a collection of items.
├── MedicalEntity: an entity relevant to medicine or healthcare.
├── Organization: a structured group of people.
├── Person: an individual human being.
├── Place: a physical location.
│   └── AdministrativeArea: a geographic region.
├── Product: any offered product or service.
└── Taxon: a biological taxonomic group.
```

##### Aristotle's Categories

```text
Being: that which is said to be or exists in any category.
└── Substance: what is neither said of a subject nor in a subject.
    └── Body: a quantity having three dimensions.
        ├── Natural body: a body arising by nature.
        ├── Artificial body: a body produced by art or craft.
        ├── Region
        ├── Place
        └── Collection
```

### Wikidata

- **Origin:** Wikimedia Deutschland, Berlin, Germany, launched in 2012.
- **Current status:** active collaborative knowledge graph.
- **Node count:** live and release-dependent; the [Wikidata statistics portal](https://www.wikidata.org/wiki/Wikidata:Statistics) reports item, statement, edit, and community counts rather than a frozen ontology release.
- **Prominence proxy:** the live statistics portal exposes tens of millions of items and a very large statement/edit graph; its scale is orders of magnitude beyond a one-page game profile.
- **Fit:** useful later for people, places, organizations, brands, fictional entities, and current events; too noisy to be the first noun backbone.

### Wikipedia’s implicit ontology

- **Origin:** launched in January 2001 as a global Wikimedia project.
- **Current status:** active encyclopedia, category graph, portal system, infobox vocabulary, redirects, interlanguage links, and a substantial biological-taxonomy workflow. The [WikiProject Tree of Life](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Tree_of_Life) coordinates organism coverage; species articles commonly use standardized [taxoboxes](https://en.wikipedia.org/wiki/Template:Taxobox) to display ranks, accepted names, synonyms, and parent taxa; and [Wikispecies](https://species.wikimedia.org/) provides a separate Wikimedia taxonomy directory. These are valuable linked reference structures, but Wikipedia's taxoboxes and categories are editorial presentations, not a single versioned biological authority.
- **Node count:** the English [Wikipedia statistics page](https://en.wikipedia.org/wiki/Wikipedia:Statistics) reports roughly 7.25 million articles and 2.6 million categories in its 2026 snapshot.
- **Prominence proxy:** the same snapshot reports about 872 million article edits by 12.4 million users; article and category counts are also direct scale measures.
- **Fit:** excellent candidate source for familiarity and named-entity expansion and biological cross-checking, but category membership is inconsistent and often editorial, topical, or maintenance-driven. Taxobox parentage is more useful for organisms than general Wikipedia categories, although it still needs source/version tracking.
- **Browser:** [`Wikipedia/index.html`](Wikipedia/index.html) provides a static, searchable, lazy-rendered browser beginning at [Main topic classifications](https://en.wikipedia.org/wiki/Category:Main_topic_classifications) and [Contents](https://en.wikipedia.org/wiki/Category:Contents). It packages [`categories.json`](Wikipedia/categories.json) and records its exact source, checksum, license, roots, and derivation parameters in [`snapshot-manifest.json`](Wikipedia/snapshot-manifest.json). The October 3, 2026 English Categories RDF dump contains about 2 million categories reachable from these roots; the checked-in derived snapshot includes 12,657 categories through depth 3 so the browser remains practical. Boundary categories link to live Wikipedia pages for deeper exploration. The reproducible parser is [`generate_categories.py`](Wikipedia/generate_categories.py). It deliberately presents the result as a category graph: repeated categories, cycles, maintenance branches, and multiple parents are not collapsed into a falsely authoritative single tree.

### Product-type taxonomies

Product taxonomies are valuable prior art for the artifact, food, clothing, tool, appliance, vehicle, electronics, and household portions of the tree. They are usually optimized for retail navigation, search, listing validation, or supply-chain interoperability rather than general ontology design. Their strength is dense coverage of familiar manufactured goods; their weakness is that commercial departments, brands, attributes, and merchandising use cases are often mixed into the hierarchy.

This detailed prior-art supplement is retained adjacent to the upper-layer discussion for implementation convenience. It does **not** belong in the canonical upper ontology and is not a candidate for `Entity`, `Property`, or `Relation`. Google, GS1, UNSPSC, eCl@ss, ETIM, Amazon, and Walmart are operational classification systems: use them to discover artifact vocabulary and coverage gaps, preserve their source paths as metadata, and map reviewed leaves into the physical subtree. Do not copy commercial departments, product types, brands, or proprietary paths into the ontology's highest layers.

The top five publicly accessible product-classification systems to evaluate are:

#### Google Product Taxonomy

- **Source:** [Google's product taxonomy](https://www.google.com/basepages/producttype/taxonomy.en-US.txt) and [Merchant Center product data documentation](https://support.google.com/merchants/answer/6324436).
- **Structure:** a large, human-readable category path with numeric IDs, designed for product feeds and shopping search.
- **Access:** the taxonomy file is publicly downloadable. Its terms and update policy should be recorded with each imported snapshot.
- **Fit:** probably the best first retail source for familiar product names and practical department coverage. It is useful for candidate discovery, but should not dictate the ontology's treatment of natural objects, services, or abstract concepts.

#### GS1 Global Product Classification (GPC)

- **Source:** [GS1 GPC](https://www.gs1.org/standards/gpc).
- **Structure:** a global supply-chain classification organized around segments, families, classes, and bricks, with attributes and rules that support product identification across trading partners.
- **Access:** the standard, browser, and release materials are publicly discoverable; some downloadable content and reuse rights may require GS1 registration or acceptance of licensing terms.
- **Fit:** excellent as a stable cross-industry product backbone and for checking whether a proposed retail branch is missing a major category. Its business-oriented granularity should be compressed before display.

#### UNSPSC

- **Source:** the [UNSPSC overview](https://en.wikipedia.org/wiki/United_Nations_Standard_Products_and_Services_Code) and the code-set steward's historical [UNSPSC site](https://www.unspsc.org/).
- **Structure:** a four-level hierarchical code set covering segments, families, classes, and commodities across goods and services.
- **Access:** the taxonomy is publicly documented and widely used, but the steward's current site and code-set download availability should be revalidated before importing a snapshot; the domain may not currently be a reliable distribution endpoint.
- **Fit:** useful for broad coverage and procurement-oriented gaps, especially where consumer retail taxonomies omit industrial goods, services, or professional equipment. It is less friendly as a visible noun tree because many leaves are procurement labels.

#### eCl@ss

- **Source:** [eCl@ss International](https://eclass.eu/en/).
- **Structure:** a hierarchical product and service classification with standardized classes, properties, and value domains, used heavily in industrial and business-to-business data exchange.
- **Access:** the standard and documentation are publicly described, while complete releases and some reuse rights may require registration or a license.
- **Fit:** strong for machinery, components, materials, industrial tools, and technical products that consumer taxonomies underrepresent. It should be an audit source and vocabulary reservoir, not a direct player-facing hierarchy.

#### ETIM

- **Source:** [ETIM International](https://www.etim-international.com/).
- **Structure:** a product-classification model centered on standardized classes and product features, especially for electrical, HVAC, building, installation, and technical-trade products.
- **Access:** the model is publicly described and used through national implementations; complete releases and commercial reuse conditions vary by member and license.
- **Fit:** valuable for tools, hardware, building products, appliances, and technical equipment. It supplies detailed feature vocabulary that can enrich leaves, but its feature-centric design should remain metadata rather than become extra visible branches.

#### Amazon and Walmart operational taxonomies

Amazon and Walmart are important prior art even though neither appears to offer an unrestricted, complete public download of its live product-type hierarchy.

- **Amazon:** Amazon exposes public documentation for the [Selling Partner API product-type definitions](https://developer-docs.amazon.com/sp-api/docs/product-type-definitions-api) and seller-facing browse/product-type concepts, but the complete current category and product-type data is tied to marketplaces, regions, authenticated APIs, and commercial operational use. Public documentation is therefore available; a complete public taxonomy snapshot is not assumed. Amazon is especially useful for studying retail granularity, browse-node navigation, required attributes, and the distinction between product type and department.
- **Walmart:** Walmart Marketplace provides public entry points to its [Marketplace APIs](https://developer.walmart.com/us-marketplace/docs/introduction-to-marketplace-apis) and item-setup workflows, while the detailed category, item-specification, and validation taxonomy is generally exposed through authenticated seller/partner tooling. It should be treated as restricted prior art unless a distributable public release can be identified. Its value is high for practical retail category coverage, especially for grocery, consumables, household goods, apparel, and general merchandise.

The project should use the public systems as candidate generators and cross-checks, not merge their department trees directly. A product leaf should retain its source code and paths, then receive a reviewed home in the SUMO/PDF-derived tree. Amazon and Walmart material can be used for internal audits where authorized, but no proprietary taxonomy content should be copied into the public repository without permission.

### Roget’s Thesaurus

- **Origin:** Peter Mark Roget’s classification began in London in 1805 and was published in 1852.
- **Current status:** continuously republished in commercial and public editions; its class/division/section structure remains recognizable.
- **Node count:** six primary classes and more than 1,000 meaning-cluster branches; the eighth edition is reported to contain about 443,000 words.
- **Prominence proxy:** the edition scale itself is objective; the work has been continuously published since 1852 and remains a standard English thesaurus reference. The best freely browsable view of the original conceptual class/division/section structure is the [1911 edition at Project Gutenberg](https://www.gutenberg.org/ebooks/10681); see also the [historical overview](https://en.wikipedia.org/wiki/Roget%27s_Thesaurus).
- **Fit:** useful for lexical neighborhoods and question wording, not a reliable hypernym ontology. It should not replace WordNet’s synset IDs.

### SUMO

- **Origin:** the IEEE Standard Upper Ontology effort, developed by the Teknowledge-led working group around 2000 in the United States.
- **Current status:** maintained as an open formal upper ontology and mapping resource.
- **Node count:** release-dependent; commonly reported at roughly 25,000 terms with tens of thousands of axioms and mappings.
- **Prominence proxy:** the [SUMO overview](https://en.wikipedia.org/wiki/Suggested_Upper_Merged_Ontology) and its open downloads provide a reproducible formal-ontology footprint.
- **Fit:** valuable for high-level distinctions such as object, process, attribute, and situation; too abstract and axiom-heavy for the default everyday noun page.

### SUMO PDF projection

The active SUMO browser is a projection of the official Ontology4 PDF graph, not the current KIF hierarchy. The checked-in graph contains 518 nodes and 554 arcs. The display chooses one primary parent for multi-parent nodes, retains removed parents as alternate metadata, keeps unary nodes, and uses `Entity` as the only root. Four provisional placements connect otherwise disconnected labels: `List → Set`, `Number → Quantity`, `Predicate → Proposition`, and `Sentence → Proposition`.

### DBpedia

- **Origin:** Free University of Berlin, University of Leipzig, and OpenLink Software; launched in 2007 in Germany.
- **Current status:** active linked-data extraction project with release-based datasets.
- **Node count:** release-dependent and measured in millions of extracted entities and hundreds of millions of RDF statements, rather than a compact controlled vocabulary.
- **Prominence proxy:** its recurring public releases and SPARQL endpoint make it one of the most reused Wikipedia-derived linked-data resources; see [DBpedia](https://www.dbpedia.org/).
- **Fit:** useful bridge from article names to structured entities, but not a clean noun hierarchy.

### Schema.org

- **Origin:** Google, Microsoft, Yahoo, and Yandex, launched in 2011 for interoperable web markup.
- **Current status:** actively maintained public vocabulary.
- **Node count:** a few hundred types and over a thousand properties, depending on whether pending and extension terms are included; the [official vocabulary](https://schema.org/docs/full.html) is the authoritative live count.
- **Prominence proxy:** its vocabulary is embedded in web search and structured data tooling across the four founding search ecosystems.
- **Fit:** practical for artifact, organization, person, and event categories; too shallow for a complete noun ontology.

### FoodOn

- **Origin:** an open food ontology effort launched in the mid-2010s by researchers and food-domain communities.
- **Current status:** maintained in the OBO ecosystem.
- **Node count:** release-dependent and typically tens of thousands of food classes and terms; use the [FoodOn releases](https://foodon.org/) for the current count.
- **Prominence proxy:** OBO/OLS distribution and domain reuse provide a measurable publication and reuse footprint.
- **Fit:** a targeted supplement if WordNet coverage of prepared foods such as steak and salad is inadequate.

### Encyclopaedia Britannica’s 15th-edition Propædia

- **Origin:** Encyclopaedia Britannica began in Edinburgh, Scotland, in
  1768. The one-volume *Propædia* was introduced with the 15th edition in 1974 as the topical “Outline of Knowledge” for the *Micropædia* and *Macropædia*.
- **Current status:** the print 15th edition ended in 2010, while Britannica continues digitally. The best freely available outline of the single-volume knowledge scheme is the detailed [Propædia outline](https://en.wikipedia.org/wiki/Propaedia); Britannica’s own shorter [Propædia entry](https://www.britannica.com/topic/Propaedia) confirms its role in the 15th edition.
- **Node count:** the *Outline of Knowledge* contains 10 parts, 41 divisions, and 167 sections. These are organizational topics, not a biological or noun taxonomy.
- **Prominence proxy:** it was designed over eight years by Mortimer Adler with dozens of subject specialists as the organizing framework for the entire 15th edition. It is one of the most prominent modern attempts to provide a single synoptic outline of human knowledge.
- **Fit:** useful prior art for broad top-level coverage and for testing whether v1/v2 omit an important knowledge domain. It is intentionally encyclopedic and circular rather than a balanced yes/no noun tree, so it should inform coverage audits rather than supply parentage.

### DMOZ/Open Directory Project RDF hierarchy

The large RDF/XML text dump available for this project is not a general “Mozilla Ontology.” It is a snapshot of the **Open Directory Project (ODP), also called DMOZ**, a human-edited web-directory topic hierarchy. The historical association with Netscape and Mozilla explains the earlier label, but DMOZ is the precise name for the data structure.

- **Origin:** ODP was founded in the United States in 1998 as Netscape’s Open Directory Project and was later commonly known as DMOZ. Its categories were organized as web subjects rather than as a formal noun or upper ontology.
- **Source and release:** the supplied file is an RDF/XML snapshot whose header says it was generated on 2006-10-10 01:06:26 GMT on `dust`; its records include category IDs, titles, update timestamps, editors, and `narrow` links to child topics. The dump size is approximately 600 MB.
- **Current status:** the directory was discontinued in 2017 and is no longer an actively maintained public authority. The snapshot is therefore historically valuable but frozen and release-specific. See the [Open Directory Project history](https://en.wikipedia.org/wiki/DMOZ).
- **Node count:** not yet measured for this particular dump. A valid count must be produced by streaming the RDF/XML, counting distinct `Topic` resources, counting `narrow` edges, and reporting disconnected components, missing targets, duplicate labels, and cycles. The count must not be inferred from the 600 MB file size.
- **Prominence proxy:** DMOZ was one of the best-known human-edited web directories, and its category data was reused by search engines, directories, and the RDF community during the Web 1.0 era. Historical prominence is the appropriate metric; it should not be compared directly with current Wikidata item or Wikipedia article counts.
- **Fit:** useful as a separate, human-curated topical browsing profile and as a source of realistic category distinctions. It is not a canonical noun backbone: many nodes describe websites, audiences, regions, editorial maintenance categories, or topical collections rather than kinds of things. Multiple parents and cycles must be preserved in the source manifest and resolved only in a declared display projection.

### Human Knowledge

- **Origin:** Brian Holtz’s *Human Knowledge 2000* outline, developed in the late 1990s and early 2000s.
- **Current status:** personal static reference material, not a community ontology or standards body.
- **Node count:** the `Thoughts 1-8.html` outline has 137 HTML heading nodes; this is a document-structure count, not an ontology count.
- **Prominence proxy:** no external citation, usage, or page-view metric has been established; its relevance here is personal authorship, not public prominence.
- **Fit:** explicitly **not an input, root, ranking prior, or graft target** for this ontology. “Ontology” is one topic within that outline, so the outline cannot logically serve as the ontology’s root. It may be studied separately, but this project will not merge it into the WordNet tree.

## Consolidating upper ontologies

The agent drives the comparison, testing and synthesis. Brian decides the consequential design choices, one compact brief at a time. The aim remains a general-purpose ontology with an intelligible canonical tree, as described in the [design memoranda](OntologyDesignMemoranda.md#1-project-goal).

### Pending decision: Composition’s immediate children

**Question for Brian:** adopt Content and Symbolic form as Composition’s immediate children, distinguishing what a product presents from its organization of signs?

**Recommendation:** adopt the pair from the [Fable comparison sketch](UpperOntologyClaudeFable.md#construct-expansion-for-comparison), restricted by Composition’s accepted origin-sensitive identity. Use these definitions:

- **Content:** a Composition identified by what it presents, asserts, prescribes or specifies, together with its originating history, independently of a particular wording or notation.
- **Symbolic form:** a Composition identified by an originating organization of signs, independently of any one physical inscription or performance.

These are open categories, not an asserted exhaustive or disjoint partition. Overlap requires the same subject to satisfy both identity accounts; one product expressing another does not establish identity. A purely origin-independent sign pattern belongs under Formal entity. Whether a natural language satisfies either definition requires its own identity review.

**Strongest alternative:** Work and Expression. This gives familiar library distinctions between a work and its realizations, but imposes a narrower model on theories, standards, plans and sign systems. Keep those distinctions available as descendants rather than equating all Content with Work and all Symbolic form with a work’s Expression.

**Reconciliation tests:** a novel versus its authored English wording and a paper copy; a building code’s requirements versus its enacted wording; two independently originated texts with identical words; a specification of redness versus redness itself. [Astra’s Content and Symbolic structure](CritiqueByAstra.md#recommended-upper-tree) cannot be merged by label alone: its formal sign structures need not share Composition’s originating-history criterion.

**Decision boundary:** adopt the two immediate children and their meanings. Work, Specification, Expression and Sign system descendants remain separate decisions; fictional subjects retain classification by their portrayed kind.

### Accepted decision: Region’s immediate children

Adopt Spatial region, Temporal region and Spatiotemporal region as Region’s immediate children, distinguished by the positional domain that identifies them.

- **Spatial region:** a Region individuated by positions within a specified spatial domain or frame.
- **Temporal region:** a Region individuated by positions within a specified temporal domain or ordering.
- **Spatiotemporal region:** a Region individuated jointly by spatial and temporal positions within a specified domain or frame.

**Rationale:** the family shared by [Fable](UpperOntologyClaudeFable.md#4-the-upper-tree) and [Astra](CritiqueByAstra.md#recommended-upper-tree) distinguishes loci from their occupants and supports space, time and joint extents without requiring a universal present or one physical theory. Keep the family open without a universal disjointness claim. A spatial slice or temporal projection need not be identical to the spacetime region it projects; overlap requires an explicit identity account.

**Steelman of Spatial and Temporal beneath Spatiotemporal:** unified spacetime can explain their connections, but an aspect or projection is not automatically an is-a subtype. A room differs from its spatial extent, a process from its duration and a moving hole from its occupied regions. Mathematical color spaces follow formal identity rather than the word “space.” Point / Extent grandchildren and inherited geographic placements remain unadopted.

### Accepted decision: Predicable’s immediate children

Adopt Property and Relation as Predicable’s immediate children, using the [published definitions](#published-root-and-predicable-definitions). Property has one subject position; Relation has two or more ordered subject positions. Subjects may themselves be Predicables. The split is disjoint and exhaustive for predicables of determinate arity; variable-arity cases require an explicit account before extending that claim.

**Rationale:** predicative arity supplies one organizing criterion while preserving familiar names. Redness and taller-than-Alice are Properties; taller-than and married-to are Relations. This wall’s redness and Alice and Bob’s marriage bond are particular Features. Transitive can be a Property of a Relation. Specifications represent predicables and retain distinct identities.

**Steelman of Property beneath Relation:** treating properties as unary relations gives a uniform logical account. Its cost is an extra broad tree level and a wider meaning of Relation than the familiar multi-subject contrast. A formal representation can treat both uniformly while the tree retains the adopted siblings. Property and Relation grandchildren remain unadopted.

### Provisional incumbent graft

The [incumbent browser](index.html) displays the accepted Particular / Predicable root and six Particular categories from the [published data](ontology.json). Realized entity and Abstract entity are retired as root wrappers; their inherited descendants remain reachable. The graft retains all 437 inherited records other than the retired wrappers, adds twenty-six upper records, and selects exactly one displayed parent per nonroot record. It has 463 records and 462 ancestry edges.

The accepted Object and Occurrence children and grandchildren, and Feature and Region children, are displayed with their adopted definitions. Property and Relation are accepted beneath Predicable. Deeper inherited placements remain provisional, including the unresolved Agent and Collection branches retained directly under Object. The browser marks these placements; definitions state consequential readings such as bearer-specific Quality, normative content versus obligation, and the contract agreement versus its text. Removing repeated displayed parents does not establish that every retained lower inclusion is sound. The inherited biology, physical carriers, mathematical subjects and social senses still require their planned review; the graft is not a validated domain ontology.

[graft_upper_ontology.py](graft_upper_ontology.py) reads accepted definitions from this document and applies the explicit placement choices to the inherited data. Run it after rebuilding the legacy projection with [SUMO/overlay_canonical.py](SUMO/overlay_canonical.py). Its input checksum and retired wrapper IDs are recorded in the published data. The browser regression checks verify the root, reachability, unique displayed paths, search and navigation. The existing count annotations still refer to retained records; counts are not evidence for the graft's semantic placements.

### Definition format: compact definitions and optional support

Each core definition stands alone and carries the necessary membership and identity conditions. Add at most two unlabeled supporting bullets only when explanation or a concrete contrast resolves a likely misunderstanding that the core and children do not resolve. Neither a supporting bullet nor an example adds a hidden membership condition. Prefer ordinary language; keep extended defenses and additional tests in the rationale sections. Examples from ordinary life do not restrict admission to actual subjects.

The browser starts the core beside the name, truncates it in a collapsed row and wraps it fully when expanded. Supporting bullets appear only for an expanded taxon, immediately beneath its definition and before its children, indented farther than the immediate child taxa. They are explanatory prose, not taxonomic nodes: no Core / Explanation / Example labels, taxon counts or navigation controls. Definitions without supporting text add no supplementary block.

The adopted upper definitions use this format without changing their scope, dependence or identity commitments. The published root and accepted Predicable children below use the same presentation.

#### Published root and predicable definitions

- **Entity:** That which can be referred to.
- **Property:** a Predicable applicable to one subject as a characterization; its subject may itself be a Predicable.
- **Relation:** a Predicable applicable to two or more subjects as an ordered relational characterization.
  - Married-to is a Relation; Alice and Bob's particular marriage bond is a Relationship.

### Accepted decision: Relationship as the Feature branch name

Relationship replaces Relational feature as the name of the accepted branch, preserving its scope. The browser retains its existing stable identifier; the inherited narrower social-connection record is labeled Social relationship to distinguish it from the broader parent.

**Rationale:** the familiar word names bearer-specific connections and standings while its contrast with Relation makes the particular / predicable distinction explicit. Neither name alone proves that every relational assertion denotes a further Feature. Association is approachable but can imply an organization or mutual ties; Relational standing emphasizes participant-specific positions but underplays whole bonds and physical connections. Relator remains a narrower candidate descendant, not the parent name.

#### Relation, relationship and relator

The [adopted Relationship definition](#accepted-decision-features-principal-categories) distinguishes a bearer-specific Feature from a repeatable Relation.

**Relation versus relationship:** married-to is a repeatable multi-subject characterization under Predicable / Relation. A particular marriage bond is a bearer-dependent subject under Particular / Feature. A spouse's particular entitlement is another relational feature. A marriage ceremony is an Occurrence; the marriage's obtaining over an interval is a State. Identifying these subjects needs more than changing their labels.

**Relator:** a relational feature jointly dependent on at least two specified participants and grounding their connection, where the adopted identity account posits such a feature. In [OntoUML's definition](https://ontouml.readthedocs.io/en/latest/classes/sortals/relator/index.html), relators ground material relations. [gUFO's employment example](https://nemo-ufes.github.io/gufo/examples/04-relators/index.html) distinguishes the employment relator from the employee's right to salary and the employer's duty to pay, which are its bearer-specific aspects. This supplies a reason for a narrower Relator subtype: the whole jointly grounded tie versus a particular participant's standing within it. Relator remains a candidate descendant, not an adopted commitment to the full UFO framework.

**Why not simply “instance of a relation”:** a relation's holding for specified subjects does not automatically supply an additional bearer-dependent entity. Two being less than three does not, by itself, posit a Feature; nor does one person's being taller require a separately identified jointly grounded tie rather than their heights. Conversely, one employment relator can ground multiple relations and include several distinct rights and duties. Relation exemplification, a relational Feature and a Relator therefore are not interchangeable. Use “particular connection or standing” rather than “relation instance” unless a separate account of relational instantiation establishes the required identity and dependence.

**Steelman of Relationship:** the familiar Relation / Relationship contrast can teach the repeatable-characterization versus bearer-specific-subject distinction directly. Its cost is that ordinary and academic usage do not reliably reserve those words for opposite categories; definitions and examples must carry that convention. “Relationship” also cannot be used as a blanket promise that every true relational statement names a Feature.

The examples below are candidate subjects within this branch, not accepted new subclass nodes. They include one-sided standing, jointly grounded ties and physical connections; not all are institutional. They denote bearer-specific features, not the reusable predicables, documents or obtaining episodes. The candidate names are suggestions rather than exact synonyms; several cover only part of the scope.

#### Relationship examples

- A particular marriage bond
- A particular employment relationship
- A person's occupancy of a treasurer position
- A student's enrollment in a university
- A person's citizenship in a polity
- A tenant's tenancy of an apartment
- An owner's title to a particular parcel
- A creditor's claim against a particular debtor
- A debtor's obligation to repay a particular loan
- A licensee's permission to use a patented invention
- A judge's jurisdiction over a particular case
- A guardian's responsibility for a particular child
- A person's membership in an informal group
- A partner's stake in a particular venture
- A promisor's commitment to a particular promisee
- A particular parent–child kinship tie
- One component's attachment to another
- One object's separation from another at a specified time
- One part's alignment with another at a specified time
- One organism's symbiotic association with another

#### Candidate names

- Connection
- Tie
- Bond
- Link
- Association
- Attachment
- Affiliation
- Alliance
- Partnership
- Membership
- Standing
- Position
- Status
- Capacity
- Claim
- Stake
- Commitment
- Obligation
- Social tie
- Relational standing

### Accepted decision: Feature's principal categories

Feature has Quality, Disposition, Relationship, Structural feature and Attitude as its five working immediate children. These are open and potentially overlapping, not an exhaustive partition. Every edge means is-a and inherits bearer-specific identity and the omniversal admission rule. Grandchildren remain unadopted.

- **Quality:** a Feature characterized by a determination in a qualitative or quantitative domain, without requiring a manifestation process to identify that determination.
  - This apple's mass is a Quality; the formal value used to describe it is a different subject.
- **Disposition:** a Feature grounding a tendency or capacity for manifestations under specified conditions, whether or not a manifestation occurs.
- **Relationship:** a Feature consisting in a bearer-specific connection or standing whose identity depends on another entity or a contextual framework.
  - A relation's holding does not by itself establish a further Feature; a Relationship needs its own identity and dependence account.
  - Married-to can characterize many couples; Alice and Bob's particular marriage bond is a Relationship.
- **Structural feature:** a host-dependent Feature individuated by structural or topological organization, rather than merely by a numerical or categorical description.
  - A ring's hole follows its host when the ring moves; it is distinct from the spatial Region it occupies at a time.
- **Attitude:** a Feature consisting in a subject's orientation toward content or a target, without requiring a purported target to exist.
  - Attitude here means a belief, desire or preference, not bodily posture or a general manner of behaving.

**Rationale:** determinations, manifestation tendencies, connections, host structures and directed orientations give useful homes to recurring bearer-dependent subjects. Fable and Astra broadly converge on these groups, although Astra's Relational feature is broader than Fable's Relator. Agreement supports the grouping without making their scopes identical.

**Naming rationale:** Attitude carries the directed sense in its definition; Intentional adds terminology without a needed distinction here. Prefer single-word names where they preserve scope and legibility. Relationship preserves the accepted relational scope; Structural feature retains its working name pending an adequate alternative.

**Steelman of alternatives:** Intrinsic / Relational first offers a uniform dependence criterion, but contested accounts of dispositions, structures and attitudes would control their principal placement. Intentional attitude makes directedness explicit and distinguishes posture or demeanor at a glance, but the adopted definition does that work. Relator supplies an established concise label for jointly dependent connections; broadening it to the entire relational branch loses the distinction between a bearer's contextual standing and a posited jointly dependent grounding feature.

**Boundary tests:** belief as an attitude versus an interval of believing as a State; fragility versus a shattering Process; a hole versus its occupied Region; office occupancy versus the office and occupant; a permission versus its text and the reusable permission condition. Overlap requires an identity argument; multiple applicable descriptions need not identify one subject.

### Accepted decision: Occurrence's children and grandchildren

Adopt [Astra's Occurrence branches](CritiqueByAstra.md#recommended-upper-tree): Process, Event and State as immediate children, with the children defined below. Every edge means is-a. All groups remain open and potentially overlapping; none asserts exhaustiveness, disjointness, actuality or physical reduction.

- **Process:** an Occurrence identified through ongoing activity, operation or change, with its course relevant to its identity.
  - A complex process need not have every phase instantiate the same process kind at every granularity.
- **Physical process:** a Process identified through changes or operations of physical systems.
- **Mental process:** a Process identified through cognitive, affective or experiential activity, without stipulating its identity with a physical process.
- **Social process:** a Process identified through social interaction, coordinated practice or institutional operation.
- **Event:** an Occurrence individuated as a bounded happening under a specified event criterion, whether instantaneous or extended.
  - A storm can be both a bounded Event and an ongoing Process; boundedness need not mean perfectly sharp instants.
- **Transition event:** an Event identified by a change from one specified condition to another.
- **Achievement event:** an Event identified by attaining a specified endpoint or satisfaction condition, whether or not intended by an agent.
  - A reservoir reaching its specified capacity can be an Achievement event without anyone pursuing that result.
- **State:** an Occurrence identified by a specified condition obtaining over an interval, rather than by the detailed course producing or maintaining it.
  - An interval of believing is a State; the bearer's belief attitude is a Feature, and the proposition believed is another subject.
- **Physical state:** a State identified through the condition or configuration of a physical system.
- **Mental state:** a State identified through experience, cognition or an attitude's obtaining.
- **Social state:** a State identified through social relationships, practices or institutional standing.

**Rationale:** course, bounded happening and obtaining condition are distinct ways to individuate occurrences. Physical, mental and social subclasses preserve their identifying activities or conditions without requiring reductive identity claims. Transition and Achievement separate condition change from endpoint attainment; a finish-line crossing may satisfy both. One primary tree route does not deny another genuine subclass relation.

**Steelman of alternatives:** Process / State with Event below Process reduces the principal branches and treats events as bounded processes, but makes eventhood subordinate even where an endpoint rather than a detailed course identifies the subject. Instantaneous / Extended events offers a uniform duration criterion, but duration depends on granularity and does less to distinguish what identifies a happening. Physical / Nonphysical for Process or State offers a binary division, but its remainder needs a positive account and prejudges how mental and social occurrences relate to physical ones. A stricter homogeneous-process account captures activities such as running, but requiring every phase to be of the same kind is too strong across granularities and complex processes.

**Boundary tests:** a storm as process and event; a finish-line crossing as transition and achievement; a steady-state operation containing active processes; a mental state and its physiological correlate without assumed numerical identity; a belief attitude versus the episode of believing. The occurrence sense of State has a separate record from the incumbent geographic State territory; no territorial subject is converted into an episode.

### Accepted decision: Object's children and grandchildren

Adopt [Astra's Object branches](CritiqueByAstra.md#recommended-upper-tree), with Physical object and Social object as immediate children. Physical object has Material body, Material portion and Physical aggregate; Social object has Institutional continuant and Social collective. These branches are open and potentially overlapping, not an exhaustive partition. Each inclusion means is-a and inherits Object's persistence criterion and the omniversal admission rule.

- **Physical object:** an Object individuated through a physical body, retained matter or physical grouping.
- **Material body:** a Physical object whose bodily organization or unity governs its identity through relevant changes of constituents.
  - A repaired machine can remain the same body despite replacement of its original material.
- **Material portion:** a Physical object individuated by specified matter, whose retention governs its identity rather than the persistence of a shape or organized body.
  - The clay used for a statue can remain the same portion after reshaping; replacing it with equally heavy clay need not preserve that portion.
- **Physical aggregate:** a Physical object individuated as a plurality of physical members under a specified grouping and persistence rule, without requiring the unity of a single body.
- **Social object:** an Object whose identity or persistence depends on social practice, affiliation, recognition or constitutive rules.
  - A company can survive staff turnover without being identical to its staff or building.
- **Institutional continuant:** a Social object whose continuing identity is governed by an identifiable framework of constitutive rules, potentially surviving changes of members or occupants and periods of vacancy or inactivity.
  - A treasurer's office can remain the same office when its occupant resigns and it becomes vacant.
- **Social collective:** a Social object individuated as a group through membership, affiliation or interaction under a specified persistence rule.

**Rationale:** the Physical / Social split distinguishes grounds of identity, while their children distinguish bodily unity, retained matter, physical grouping, institutional continuity and social membership. Fable and Astra converge on the principal branches; Astra makes the material and social persistence distinctions explicit at the next level. This agreement supports a trial but does not prove disjointness or coverage.

**Naming rationale:** Social object includes informal collectives, so Institutional object is too narrow for that parent. Institutional continuant names the narrower rule-governed bearer. Continuant emphasizes identity through change; endurance alone does not distinguish institutions from other Objects, and no minimum lifespan or theory of temporal parts is imposed.

**Steelman of alternatives:** Institutional object is plainer and avoids a technical term; it can name the same narrower category if its definition preserves continuity through turnover and vacancy. Material / Immaterial gives an apparently uniform first split but leaves the immaterial remainder without a common positive identity account. Agent as an immediate principal child foregrounds intentional subjects, but agency crosses physical and social identity grounds and needs its own placement review.

**Boundary tests:** statue versus its clay; repaired machine versus original material; corporation versus staff and building; vacant office versus former occupant; informal group versus institution. A single displayed ancestry does not imply that other genuine subclass claims are false. Nonphysical subjects may remain at Object pending a justified branch.

### Accepted decision: Particular's six principal categories

Particular has Object, Occurrence, Feature, Region, Composition and Formal entity as its six working immediate children. Adopt the following definitions for developing and testing the tree. The categories remain open; neither exhaustive coverage nor pairwise disjointness is asserted. All inherit the Particular definition and omniversal admission rule. Names may change without changing the adopted meanings.

- **Object:** a Particular individuated as a unified, persisting bearer through continuity of its body, material, membership or constitutive organization.
- **Occurrence:** a Particular happening or obtaining episode individuated through its temporal unfolding, boundary or extent.
- **Feature:** a Particular characteristic whose identity depends on specified bearers or hosts.
  - This wall's redness is a Feature; redness applicable to many walls is a Predicable.
- **Region:** a Particular locus or extent individuated by positions within a specified spatial, temporal or spatiotemporal domain or frame, rather than by its occupant.
- **Composition:** a Particular intellectual or artistic product whose identity depends on its originating history together with its content or symbolic form, independently of any one carrier.
  - Independently originated works with identical wording can be different Compositions while sharing one formal word-pattern.
  - A fictional human is not a Composition merely because a story portrays that human.
- **Formal entity:** a Particular whose identity is fixed entirely by mathematical, logical or structural conditions within a specified framework, rather than by a physical or social career or an origin in representing it.
  - A mathematical description of a bridge does not make the bridge a Formal entity.

**Rationale:** persisting bearers, temporal episodes, bearer-dependent characteristics, positional extents, origin-anchored intellectual products and formally identified subjects raise different identity and classification questions. These six give those distinctions explicit homes beneath Particular. Naming refinement does not need to delay testing the meanings.

**Identity test for Composition / Formal entity:** independently originated works with identical wording can be different Compositions while sharing one formal word-pattern. Mathematical theories, software and language systems remain important tests. Accepting the distinction does not settle every case, every identity criterion or the proposed Characterized Object branch in the [Fable expansion sketch](UpperOntologyClaudeFable.md#construct-expansion-for-comparison).

**Naming rationale and alternatives:** Feature inherits particularity from its ancestry; its definition preserves bearer-specific identity. Composition names a product, while composing as an activity belongs under Occurrence and material composition has a different sense. Expression is attractive for representational subjects but has a narrower [IFLA LRM sense](https://www.ifla.org/files/assets/cataloguing/frbr-lrm/ifla-lrm-august-2017_rev201712.pdf) that distinguishes expression from work; keep that distinction available below Composition. Formal entity is broader than [Formalism as a framework](https://arxiv.org/abs/1804.07860) or a [philosophical position](https://plato.stanford.edu/entries/formalism-mathematics/), and does not name a quality or procedure as [Formality](https://www.oxfordlearnersdictionaries.com/definition/english/formality) commonly does. Abstraction is a short alternative but can encompass Compositions and can suggest a process. These naming costs favor the adopted pair without forbidding better labels.

**Steelman of Content instead of Composition:** Astra's interpretation-based category brings meaning directly into view and separates it from symbolic structures. Its cost is that works and expressions whose identity depends on origin need an adequate account across Content and Formal entity. Composition foregrounds that identity question while keeping content and symbolic form distinguishable beneath it.

**Steelman of Realizable / Abstract as an intermediate division:** it offers a familiar broad overview. Its cost is an additional disputed criterion before these more specific identity questions, and possible cross-cutting classifications. The working shape starts directly with the six; it does not prohibit a later justified account of realizability.

#### Composition examples for testing

These are illustrative placements under the accepted origin-sensitive definition, not adopted new nodes. The named subject is the work, expression, image, curated content or specification; paper, stored bits and performances supply different subjects. An origin-independent formal pattern can be distinguished from its origin-anchored expression. The institutional force of a norm and its enactment are likewise separate questions.

- **Moby-Dick as a novel:** a work retaining identity across copies and translations.
- **A specified German translation of Moby-Dick:** an origin-anchored linguistic expression of that work.
- **Hamlet as a dramatic work:** distinct from its scripts, performances and the people it portrays.
- **Beethoven's Fifth as a musical composition:** a work distinguishable from a performance or sound recording.
- **A particular edited score of Beethoven's Fifth:** a notational expression with an editorial origin.
- **A particular studio recording's audio content:** an origin-anchored recorded expression, distinguished from a playback event or storage medium.
- **A particular photographic image:** the image arising from a photographic origin, distinguished from a print and depicted scene.
- **An organization's adopted logo design:** an origin-anchored visual design, distinguished from any one display or a generic geometric pattern.
- **A surveyor's authored map:** a representation tied to a survey and interpretation, distinguished from its territory.
- **An architect's design for an unbuilt bridge:** a specification, independent of whether the bridge is ever built.
- **A chef's written recipe:** an originated procedure specification, distinguished from a meal or cooking episode.
- **The U.S. Constitution considered as a normative text:** a historically originated content/expression, distinguished from parchment, enactment and the institutions governed.
- **An agreed contract's terms:** originated specifications, distinguished from the document carrier and resulting obligations.
- **A prescribed wedding liturgy:** a ceremony specification, distinguished from any performance or marriage.
- **A choreographer's dance work:** an originated composition, distinguished from a dancer's movements at a time.
- **A specified chess rulebook's rules:** a normative formulation, distinguished from a particular game or an origin-independent mathematical game model.
- **A particular software release's source text:** an authored expression, distinguished from its execution and the mathematical function it may compute.
- **A research team's climate-model formulation:** a selective representation with an intended interpretation, distinguished from climate and from underlying equations considered formally.
- **A curated archaeological catalogue's content:** a provenance-sensitive selection and description, distinguished from the artifacts and an extensional set considered mathematically.
- **An author's presented proof of a theorem:** an originated argument or exposition, distinguished from the theorem's truth and a derivation considered solely as a formal sequence.

### Accepted decision: Particular / Predicable root split

Entity has Particular and Predicable as its immediate children. The split is disjoint and exhaustive under the adopted distinction: an entity is either constitutively applicable as a characterization or complete as a subject without that applicability. This is a conceptual root partition, not a requirement that every later split be disjoint or exhaustive.

- **Particular:** an entity complete as a subject of characterization, rather than constitutively applicable to subjects as a characterization.
  - Complete means no unfilled predicative positions, not being fully described, physically independent, actual or finished.

**Identity cautions:** copies, performances, representations and mathematical realizations do not by themselves settle category membership. The [accepted Predicable definition](#accepted-decision-constitutive-predicative-applicability) supplies the complementary criterion.

**Rationale:** a common distinction organizes the difference between subjects and the properties or relations applicable to them without substituting specifications for their referents. It is adapted from the logical precedents in the [academic survey](#particular-academic-terminology), rather than importing an entire historical theory. It accommodates abstract and dependent particulars and higher-order predication while respecting the omniversal admission rule.

**Steelman of direct principal categories:** exposing objects, occurrences, features and other familiar kinds immediately saves a broad intermediate level and avoids a technical first choice. Its cost is leaving their fundamental relation to predicables unstated at the root. The adopted split gives that relation priority, while its branches still need useful positive structure.

**Steelman of Realizable / Abstract / Predicable:** it foregrounds embodiment or possibility alongside applicability and preserves familiar project vocabulary. Its cost is mixing criteria at one level and deciding what realization means before the particular kinds clarify it. Realizability may remain relevant below Particular, with an explicit criterion, rather than determining the root split.

### Accepted decision: constitutive predicative applicability

- **Predicable:** an entity constitutively applicable to one or more subjects as a characterization of whether or how they qualify or stand related, whether or not exemplified.
  - Its subject positions give it predicative arity; its subjects may themselves be Predicables.
  - Redness characterizes candidate bearers; a book describing redness represents it without becoming applicable to red things as redness is.

**Consequence:** predicables need a visible home distinct from specifications of them. Specifications under Content are legitimate subjects; they are not exhaustive substitutes for their referents. The [root split](#accepted-decision-particular--predicable-root-split) places Particular and Predicable immediately under Entity. Neither decision settles the identity theory of properties or posits an independently existing universe of universals.

**Rationale and tests:** redness characterizes a candidate bearer; being taller than relates candidates in ordered positions. Redness can itself be characterized as a color property. A book describing redness represents it without becoming applicable to red things as redness is. Two specifications can disagree about the same property without producing two different properties. A particular wall's redness remains distinguishable from the repeatable predicable. A function's numerical output does not by itself establish predicative applicability. “Aboutness” alone is too broad: a biography's subject can be essential to its identity, yet its representational aboutness differs from a predicable's applicability.

**Taxonomic merit is separate:** formulating a condition does not earn it a named node. Seek defensible distinctions in the subjects classified, with definitions, explanatory or structural grounds and counterexamples, rather than verbal combinations alone. Redness needs a home independently of expressions specifying it; apple-specific redness, mass or altitude does not earn a separate branch merely because it can be described. An unusual intersection can still earn a place if it has a substantive justification. The accepted allowance for overlap does not license arbitrary subdivisions.

**Steelman of specifications as the representation core:** [Astra's account](CritiqueByAstra.md#the-common-interpretation) classifies assessable conditions without inferring that each predicate names an independently individuated universal. Content includes interpreted meaning, not merely wording. Open conditions have explicit signatures and satisfaction criteria; particular features, bearers, specifications and class membership remain distinct. This offers useful classification while leaving disputed metaphysics open. Astra [expressly permits an additional predicable layer](CritiqueByAstra.md#unresolved-choices-and-discriminating-tests).

**Why that alternative is insufficient here:** a general-purpose ontology must classify properties and relations themselves, not only representations of them. Restraint about universals does not justify leaving those subjects without a home; Fable's Predicable is neutral among universals, trope classes and concepts. Avoiding arbitrary named categories is a taxonomic discipline, not an argument for replacing predicables with specifications. Identity, equivalence and boundaries with particular features remain matters to test within the accepted distinction.

### Particular: academic terminology

This survey compares representative definitions and their suitability for the accepted Predicable distinction; it does not adopt a root split. Historical terms are not interchangeable, and a naming pool contains near-synonyms rather than equivalent technical definitions.

- **Particular / individual in Aristotle:** [On Interpretation, chapter 7](https://classics.mit.edu/Aristotle/interpretation.1.1.html), 17a38–40, contrasts what is by nature predicable of many with an individual that is not thus predicated. The emphasis is natural predicability rather than the number of actual instances. This is direct precedent for the accepted definition, but the complementary individual is still characterized negatively; the classical formulation also needs adaptation for relations and predicates applying to at most one subject.
- **Particular as logical subject in Russell:** [On the Relations of Universals and Particulars](https://www.hist-analytic.com/Russelluniversals.pdf), pp. 23–24, defines particulars through their ability to occur only as subjects of predicates or terms of relations. He explicitly prefers this logical criterion to space/time criteria, whose universality he questions. This closely fits the project and includes relations, but supplies a role distinction rather than a wholly independent positive essence. Being a subject alone does not suffice: universals can also receive predicates.
- **Object as complete, concept/relation as unsaturated in Frege:** [On Concept and Object](https://fitelson.org/proseminar/frege_ocao.pdf), pp. 182–193, distinguishes objects from predicative concepts and relations. An unsaturated component needs argument completion to contribute to a complete thought; an object supplies an argument without itself functioning as that predicative link. Numerical objects are included. This is the strongest positive conceptual lead: completeness versus constitutive applicability. Completeness here is neither physical independence nor complete description. Frege's higher-level concepts and his difficulty with nominalizing concepts show why the full theory cannot simply be imported as the project's treatment of predicables as subjects.
- **Substantial particular / object and non-substantial particular / mode in Lowe:** [The Four-Category Ontology](https://academic.oup.com/book/3774) distinguishes objects and modes from kinds and attributes, with the distinction articulated through [formal ontological relations](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1746-8361.2004.tb00306.x). A particular includes a bearer-specific mode, not only an independent thing. This supports retaining the distinction between redness as a predicable and this bearer's particular redness. Object or Substance alone would omit modes and is therefore too narrow for the intended complementary branch.
- **Primary substance in Aristotle:** [Categories](https://classics.mit.edu/Aristotle/categories.1.1.html), 2a11–19, identifies primary substances as neither said of nor present in a subject. Its additional independence condition gives more than non-predicability, but excludes dependent particular qualities. It is a useful narrower category, not a replacement for all non-predicables.
- **Particular in DOLCE:** the [authors' account](https://arxiv.org/pdf/2308.01597) takes particulars as its domain and properties and relations as universals; its principal categories include endurants, perdurants, qualities and abstracts. It thus supplies applied-ontology precedent for a broad particular domain containing dependent qualities and abstract subjects. The same paper discusses reified concepts as particulars that classify, showing why an application's reified classifier and the universal it concerns must not be conflated. It supplies no simple independent positive definition that resolves all the project's boundary cases.

**Assessment:** the closest precedents favor Particular or Individual as conventional labels for the non-predicative side, rather than revealing a universally agreed positive essence. Abstractness, physical independence, spatial uniqueness and being an instance each add commitments or answer different questions. The number two can be an object in Frege's account; calling it a particular across all philosophical frameworks would overstate agreement.

**Adopted Frege-inspired definition:** the [root decision](#accepted-decision-particular--predicable-root-split) uses completeness as a subject contrasted with constitutive predicative applicability. This is a project adaptation, not a quotation or an adoption of Frege's full theory. Test it on books, numbers, particular qualities and predicables receiving higher-order predication.

### Accepted decision: is-a parentage and first-pass scope

Every primary ancestry edge in the first-pass tree means is-a/class inclusion. Keep instance membership, parthood and other relations distinct from ancestry. Cross-links remain a possible future enhancement; no cross-link machinery, expanded relation inventory or implementation design is required for drafting the tree's overall shape.

**Rationale:** one edge meaning keeps ancestry intelligible and its inclusion inferences consistent. Concentrate effort on a defensible root and upper branches, concise definitions and concrete counterexamples. Record a missing relationship as a limitation when it matters; neither build infrastructure for it nor disguise it as is-a.

**Steelman of developing typed cross-links immediately:** additional relations can expose distinctions a class tree cannot express and reveal where apparently simple placements rely on hidden assumptions. Its cost is premature design and implementation before the categories are stable. Preserve the option through clear meanings and visible caveats, and defer the machinery. The [existing inventory](#candidate-edge-types) remains a reference, not an adopted schema or first-pass work requirement.

### Accepted decision: admission and actuality

**Rule:** a category does not require actuality in our universe unless that restriction is explicitly justified by what the category means. Membership requires satisfying its defining criteria under a stated context; fictional or hypothetical status alone neither establishes nor defeats membership.

**Rationale:** the Omniversal Ontology is not confined to our local indexical universe. Actuality, present existence, fictional origin and possibility cross kinds and are not interchangeable. Do not build mirror actual and fictional trees. A category whose members happen all to be actual need not make actuality essential to membership. The public tree and annotations must expose context and status wherever they change the interpretation; its data must encode the same account.

**Limits:** scope does not guarantee that every definition applies unchanged across universes. A historical clade requires the specified ancestry, not resemblance; an independently evolved bird-like organism is not thereby in our bird clade. Fictional classification must distinguish portrayed membership from actual-world assertion. A failed description such as “the largest prime” need not denote a subject; an impossible characterization does not establish a realizable instance. This rule settles the admission principle, not every reference or fiction identity policy.

**Steelman of actuality-restricted membership:** limiting membership to actual entities supplies one comparatively clear domain for class inclusion and existence claims. Fiction and failed hypotheses can still be discussed through actual works, descriptions and acts of reference, avoiding commitments to nonexistent objects and inconsistent instances. Its cost is that the intended subject is replaced by its representation as the classificatory target, and a local domain restriction becomes fundamental to a project intended to extend beyond it. Retain an actuality restriction where a category's explicit meaning justifies it, rather than impose it across the tree.

**Realizability remains open:** Brian's intended sense of the incumbent Realized entity is realizable, admitting hypothetical subjects such as Sasquatch. Logical consistency, physical possibility and metaphysical possibility require different criteria. This clarification does not adopt any of them as a root split or replace the accepted admission rule.

### Accepted direction: design priority

**Brian's direction:** tree first, with philosophical and academic defensibility. Simplicity and legibility contribute to defensibility. The public tree, definitions and annotations must express the substantive ontology; a significantly different hidden structure must not outrank them. No candidate upper tree is selected by this direction.

**Agent assessment:** use the tree as the authoritative account and make its data a faithful encoding. However, legibility does not establish a classification's truth, coverage or exclusivity. If a clean split fails a counterexample, revise the split or qualify its claim; presentation cannot rescue it. This differs from prioritizing an independently authoritative underlying graph.

**Steelman of a richer graph as authority:** multiple inheritance and typed relations can express overlapping kinds and dependencies without forcing one route to carry every commitment. Its cost here is that the tree can become an incomplete guide to the ontology. The accepted direction requires those commitments to be inspectable in the public tree and annotations instead of allowing a hidden account to overrule them.

### Accepted decision: sibling policy

Seek disjointness where justified and permit overlap where necessary. Every proposed overlap needs an explicit reason and a counterexample to the stricter alternative; record the policy visibly with the split. Exhaustiveness is a separate claim requiring its own argument. Neither property follows from tree layout.

Primary biological ancestry remains monophyletic. Habitat, diet and similar cross-cutting groupings cannot replace clades or become intermediate ancestry nodes. This requirement is unaffected by permission for other sibling groups to overlap.

**Rationale:** justified overlap avoids manufacturing sharp boundaries where the definitions and cases do not support them. **Steelman of strict partitions:** exclusive, exhaustive children simplify classification, comparison and inference, and force clearer definitions. Preserve that discipline where defensible; reject it as a universal requirement when its exclusions lack a substantive argument. Monophyly is an ancestry criterion for biology, not a universal test for all ontology categories.

### Working method

**First-pass scope:** draft and challenge the overall tree shape. Use the conceptual gates below as checks when a concrete placement needs them; do not require complete formalization, crosswalks, relation inventories, schema design or browser enhancements before proposing upper branches. Meaning-preserving migration, representation readiness and publication of changed tree artifacts belong to later accepted implementation work.

For each turning point, the agent supplies the question, recommendation, viable alternatives and their main consequences. Keep the opening brief short and high-level; retain supporting definitions, examples and objections below it or in linked analysis. Offer more detail when Brian requests it. Give an independent recommendation and the strongest counterargument to Brian's preference; change that recommendation only for better evidence or reasoning. Record his answer with the strongest defensible rationale, qualifications and steelman of rejected alternatives before advancing dependent work. Distinguish adopted choices from clarifications and unresolved questions.

The agent owns input/version checks, claim verification, sense-level comparison, counterexample testing, decision records and synthesis. Bring Brian choices that materially change scope, identity, metaphysical commitments or the browsing experience; handle routine analysis and implementation within accepted decisions. Split a gate into several briefs when its choices are independent. Continue unrelated work while a decision is open, but do not treat silence as acceptance.

### Evaluation contract and common baseline

After the first decision, the agent translates the chosen priority into evaluation criteria and separates binding requirements from hypotheses under review. Reconcile game-oriented language and the incumbent's realized/abstract preference with the broader purpose and open root question. Distinguish a false inclusion under agreed definitions from a contested definition, incomplete coverage or navigation preference. Ask Brian only about remaining conflicts that materially affect the design.

Compare the latest recommendations against one named source snapshot. Record each claim with its source passage, intended sense, supporting example, strongest objection and proposed discriminating test. Verify reported data defects against that snapshot rather than inheriting a critique's conclusion. Preserve first responses as evidence of starting positions; cross-reading and prior exposure mean model agreement is not independent corroboration.

**Gate exit:** the chosen priority is recorded, the evaluation contract reflects it, and exact input versions and a decision ledger are established. Source-accounting percentages, passing validators and model votes cannot establish semantic correctness.

### Admission, reference and assertion scope

The agent tests admission policies and reference cases; Brian chooses the scope of Entity and the treatment of nonexistent subjects.

Decide what Entity admits: actual subjects, formal subjects within a theory, fictional subjects, hypothetical posits and impossible characterizations. Separate admitting a record, successful reference, asserted existence, satisfiability and source-attributed predication. Choose how failed descriptions are retained without manufacturing an actual referent. Decide which existence questions remain explicitly open.

**Gate exit:** a root definition and admission policy that handle a rock, a number, Holmes, a refuted planet and the largest prime without exporting story claims or failed descriptions as actual-world existence claims. The policy must still permit discussion of an undiscovered kind without equating that kind with an authored description.

### Node meanings and relationship contract

The agent prepares worked representations and identifies incompatible meanings; Brian chooses the semantic contract, including the interpretation of Property and Relation.

Decide what the tree's nodes denote and what every primary edge asserts. The recommended starting contract is classes with subclass inclusion: every child instance is a parent instance. Ordinary individuals, words, class handles, specifications, predicate applications and navigation portals require explicit distinctions. Instance-of, part-of, membership, bearing, participation, expression and satisfaction have their own typed links.

Resolve whether Property and Relation denote predicables, condition specifications, or separately linked subjects of both sorts. Distinguish a kind from its specification and a particular quality from a reusable condition. Declare predicate arguments, range types, evaluation indices and derivation rules before using arity to classify anything; dependence on a bearer is not argument-taking.

**Gate exit:** worked representations of Dog, Fido, the word “dog”, a dog concept, a dog-kind specification, one cup's mass and a statement about relation arity. A typed formalization must preserve their differences without unrestricted comprehension. Selecting a proof assistant or export language is not required at this gate.

### Identity, dependence and cross-cutting classifications

The agent compares persistence and classification policies using shared examples; Brian decides the identity commitments and the division between primary ancestry and cross-cutting classifications.

Decide the criteria for treating two descriptions as one subject or as related subjects. Establish provisional persistence rules for bodies, material portions, aggregates, institutions, occurrences, features, works, expressions and formal structures. Distinguish identity from co-location, representation, equal value and equivalence within a theory.

Decide when kinds, phases, roles, domains and ontic status belong in primary ancestry, defined classifications or metadata. Test rigidity—the claim that an instance cannot cease belonging while remaining itself—rather than assigning it from a familiar label. A role-bearing class can be a valid subclass; whether it deserves primary navigation is a separate question. A designed tool and a rock used as a tool need not share the same kind. Explicitly compare combinations of proposed dimensions and explain incompatible combinations rather than assuming independence.

**Gate exit:** decisions for organization turnover, statue/clay, a moving hole, a student who graduates, and a broken pump. Record unresolved identity profiles and their costs; do not require agreement on every philosophical theory.

### Root partition or open grouping

The agent presents tested candidate root structures and their tradeoffs; Brian chooses the root grouping and which partition claims it makes.

Decide whether Entity's children must form an exhaustive, disjoint partition or may be an open set of overlapping categories. Require the public root grouping to state the accepted semantic commitments. A useful menu is not proof of a fundamental partition; any compressed route must visibly identify skipped semantic ancestors, and its data must encode the same account.

Compare the GPT realized/abstract dyad, particular/predicable approaches, the six-category Astra and Gemini revisions, the seven-category Claude revision, and a root with orthogonal classifications instead of a mandatory exhaustive cut. Compare definitions and consequences, not labels. For each candidate require an organizing principle, inclusion argument, overlap/coverage policy, strongest objection and results on the same [stress tests](#stress-testing). In particular, test claimed disjointness between content and formal structures and claimed coverage of fields, absences, facts and possible worlds.

**Gate exit:** an accepted root structure and navigation policy, with every root category defined and every asserted partition property justified. Unclassified cases remain visible; they are not evidence of exhaustiveness. A provisional open structure is acceptable when its known gaps and next discriminating cases are recorded.

### Upper branches and predication reconciliation

The agent drafts branches under the accepted contract and tests disputed placements; Brian decides remaining substantive alternatives, grouped into focused briefs.

Resolve the children of the accepted root categories before expanding domain inventories. Review objects/processes/states, regions/features, content/formal subjects, social institutions and fictional representation under the agreed contract. A conversation's physical, mental and social classifications must be assessed for genuine overlap rather than assumed to denote either one subject or three.

Give Property and Relation a dedicated pass. Resolve qualities, values, quantity mappings, dispositions, capabilities, operational versus assigned/selected functions, goals, attitudes, norms, obligations, role specifications and role occupancies. Decide whether relation families are semantic subclasses or browsing facets; distinguish classification from instantiation and specification, institutional from social, and exact equivalence from similarity. Decide whether a visible Predicate layer earns its place. Arity splits and kind/role distinctions are different axes.

**Gate exit:** an upper-tree proposal through the reporting scope, with discriminating definitions, sibling policies and typed cross-links. Each disputed placement has a counterexample or an explicit design tradeoff. Deeper ancestry remains intact; no branches are invented to balance the display.

### Meaning-preserving reconciliation and coverage

The agent prepares and checks sense-level mappings; Brian decides unresolved losses, changes of meaning or conflicting interpretations. Routine mappings follow accepted policy.

Map source senses and assertions into the accepted structure before moving branches. Use the [GPT coverage map](GPT/coverage-map.json) as a starting record format, not an equivalence certificate. Include proposal additions and omissions as well as incumbent records. For each mapping specify source and target meanings, equivalence/narrowing/broadening/overlap or split-by-sense, old-assertion migration rules, evidence and decision status.

Preserve identifiers for stable meanings. Give incompatible senses distinct identities, retain ambiguous legacy records as disambiguation routes, and reject conflicting duplicate definitions rather than letting import order choose one. Resolve Function, Role and Status collisions explicitly. Lexical matches in [Roget's crosswalk](Rogets/crosswalk.json) and ticks in [WordsToCategorize](WordsToCategorize.md) are candidate matches, not proof that the intended sense survives.

**Gate exit:** reviewed mappings for each affected branch and a sense-level difficult-case ledger. Report source accounting, semantic coverage, assertion preservation and findability separately. No move is approved while its meaning or assertion translation remains unresolved.

### Representation and validation readiness

The agent specifies and validates a representation that carries the accepted decisions. Bring Brian any capability or presentation tradeoff that would change those decisions.

Specify the authoritative editable source, semantic parents, one primary navigation parent, typed assertions, defined classifications, aliases, scope, provenance and decision records. Evaluate [GPT's format](GPT/FORMAT.md) against the accepted decisions; adopting its engineering does not entail adopting its metaphysics. Require inspectable browser destinations for off-tree classifications and distinctions that the tree cannot display.

**Gate exit:** a representation contract carrying the accepted distinctions and an acceptance suite covering both valid cases and deliberately invalid mutations. A validator must reject wrong predicate types and relation-family assignments, not merely check tuple length. Semantic reasoning, structural checks and browser behavior have separately stated limits.

### Bounded migration and publication

The agent implements accepted changes in bounded batches, verifies them, and publishes completed work. Bring Brian any newly exposed design choice before making a dependent semantic change.

Apply accepted sense changes in dependency order: identity and duplicate-record repairs, predication distinctions, affected upper branches, then domain refinements and crosswalk updates. Preserve source graphs and historical snapshots. For biology, select and document authority and lineage policy before accepting grafts; do not let familiar group labels or counts dictate ancestry. Independent accepted branches may proceed while other decisions remain open.

**Gate exit:** the affected stress tests and structural checks pass, navigation exposes retained senses, and the approved source generates reproducible published artifacts and manifests under [the publication contract](#publishing-the-tree-to-the-wiki). Browser acceptance includes search presets, ordinary search, expansion, collapse and lineage restoration. Acceptance of this process document does not itself accept a candidate ontology.

### Candidate edge types

Reference only; further expansion and implementation are deferred during the first pass. The inventory does not authorize additional parentage types or a hidden authoritative structure.

This is an extensible inventory of relation families to evaluate, not a finite list of every possible predicate. Each reads subject → target; the displayed tree can draw the inverse direction. Thus Mammal above Dog asserts Dog subclass-of Mammal. A relation's presence in the ontology does not make it eligible to supply tree parentage.

#### Classification and membership

- **Subclass-of / kind-of / is-a:** class → class; Dog → Mammal. Every instance of the child satisfies the parent under the same interpretation. Supports chaining class inclusion. A role-defined subclass need not be a rigid kind.
- **Instance-of / instantiates:** individual → class; Fido → Dog. Membership can propagate through subclass inclusion, but two instance-of links do not generally compose into another instance-of link.
- **Subset-of:** set → set; {2, 4} → {2, 4, 6}. Every member of the first is a member of the second. This resembles inclusion of class extensions, but a set, a class and an individual are not automatically interchangeable.
- **Member-of:** element → set, or participant → collective under separately defined senses. 2 belongs to {2, 4}; a person belongs to a club. Neither relation is subclassing; social membership is not automatically set-theoretic membership.
- **Subproperty-of / relation specialization:** predicate → predicate; a narrower relation's applications are also applications of the broader relation with compatible signatures. This differs from classifying a relation specification as an instance of a relation-family class.
- **Satisfies / classified-by / plays-role:** bearer or argument tuple → condition or role specification, with interpretation and context. A dog satisfying Pet criteria is not itself a Pet specification.

The distinction between class inclusion and instance membership is explicit in [RDF Schema](https://www.w3.org/TR/rdf-schema/#ch_subclassof) and [OWL class assertions](https://www.w3.org/TR/owl2-syntax/#Class_Assertion_Axioms). These are formalization references, not a commitment to adopt their entire metamodel.

#### Composition, constitution and dependence

- **Part-of / has-part:** part → whole, or its inverse; this tail → this dog. State time, proper versus inclusive parthood and composition policy. “Is-a-part-of” is not a subtype of is-a; it normally names parthood. A class-level claim that tails are parts of dogs needs its own quantification rather than treating Tail as a subclass of Dog.
- **Constituted-by / made-of:** subject → constituting body, material or constituents; statue → clay. Constitution need not establish identity or the same persistence conditions.
- **Bears / inheres-in / depends-on:** bearer → feature, feature → bearer, or dependent subject → required subject. Distinguish cup, particular mass feature and recorded mass value; a dependence link does not count as a predicate argument by itself.
- **Descends-from / lineage-member-of:** organism or lineage → ancestor or lineage, with the intended sense declared. Historical ancestry is not automatically subclassing. An organism-class taxonomy and a tree of historical lineage subjects require different node and edge contracts.

#### Location, time and activity

- **Located-in / occupies / contained-in:** subject → region, place or container with time/frame. Occupying a room does not make the occupant a room subtype; physical containment differs from parthood.
- **Before / during / overlaps-in-time:** temporal subjects → temporal subjects under an ordering. Temporal relations require separate definitions; their chaining rules are not interchangeable.
- **Participates-in / performs:** participant → occurrence, with role and context. A dancer participates in a dance; neither becomes a subtype of the other.
- **Causes / enables / manifests / fulfills:** appropriately typed subjects or occurrences → effect, capacity or specification. Separate causal contribution, a disposition's manifestation and conformity to a plan; the shared English verb “realizes” does not establish one relation.

#### Representation, attribution and provenance

- **Expresses / encodes / carries:** expression or carrier → content under an interpretation. A page is not a subclass of the proposition printed on it.
- **Represents / denotes / is-about:** representation → target or intended subject. Denotation failure needs a policy; being about something does not imply its actuality.
- **Specifies / defines:** specification → class or condition under an interpretation. Distinguish an exact definition from a diagnostic description; satisfaction implies membership only under the accepted bridge.
- **Attributed-in / portrayed-as:** claim or subject → source/scope or attributed classification. Preserve story claims without exporting them as actual-world assertions. The precise signature remains part of the admission formalization.
- **Derived-from / authored-by / based-on:** result → source, author or antecedent with provenance context. Derivation and adaptation need not preserve identity.

#### Identity, values and domain relations

- **Identical-to / equivalent-to / similar-to:** distinguish one subject from equality of extension, isomorphism and approximate resemblance. Each equivalence requires a stated domain and criterion; resemblance does not inherit equivalence axioms.
- **Has-value / measures / compares-with:** feature or measured subject → value, scale or comparator with relevant units, time and method. A value is not a predicate merely because it fills a field.
- **Owns / owes / holds-office / prefers / believes:** domain-specific relations with named argument roles and normative or interpretive context. Inventory by family, then evaluate concrete signatures; no generic “related-to” supplies their inference rules.

Relations involving more than two arguments may require a contextual assertion record rather than a bare binary edge. The [W3C n-ary relation note](https://www.w3.org/TR/swbp-n-aryRelations/) supplies encoding patterns; such an encoding does not erase the represented argument roles.

#### Navigation without ontological inclusion

- **Alias-of / search-redirect / see-also / topic-portal:** lexical or browsing connections. Exact wording is not proof of identity, and “studied by Biology” does not make an organism a subtype of the discipline. These links must be distinguishable from semantic assertions.

#### Implications of expanding edge types

An additional relation can improve coverage without changing is-a ancestry. The stronger change is permitting it to select a parent: root reachability then no longer guarantees class inclusion along the path. Mixed paths require rules for specific compositions, not automatic transitivity.

Before adopting a family, require its endpoint types, direction/inverse, interpretation, time/context parameters, allowed inference and a prohibited inference. Add a concrete case that cannot be expressed adequately under the existing public contract. Specify whether the relation supplies parentage, is a cross-link, or appears as a note/member entry; its representation must remain inspectable and agree with the data.

Allowing additional edge types does not by itself require multiple parents, nor does allowing overlapping classes require a mixed-edge tree. These are separate choices. Evaluate coverage gains against visual complexity, ambiguity, validation burden and migration cost. An all-is-a tree still needs a declared policy for individuals and other relations; excluding them from ancestry does not make those distinctions disappear.

### Review inputs

The comparison inputs are the preserved proposals by [Astra](UpperOntologyAstra.md), [Gemini](UpperOntologyGemini.md), and [Claude Fable](UpperOntologyClaudeFable.md); their repository-informed critiques by [Astra](CritiqueByAstra.md), [Gemini](CritiqueByGemini.md), and [Claude Fable](CritiqueByClaudeFable.md); the incumbent and [historical snapshot](v1010/Ontology.md); and the [GPT/Sol package](GPT/README.md), including its [architecture](GPT/architecture.md), [format](GPT/FORMAT.md), [coverage map](GPT/coverage-map.json), and [stress tests](GPT/stress-tests.md). Imported systems in [Prior art](#prior-art) supply distinctions, provenance and coverage probes; lexical and topical hierarchies do not automatically supply subclass axioms. The [critic prompts](CriticPrompt.md) explain the proposals' reporting scope, not a permanent ontology depth limit.

## Metaphysical commitments and neutrality

How philosophically partisan is the tree? Distinguish **adopted commitments**, **interpretive leanings** and **open questions**. A category's presence admits subjects for discussion; it does not assert their actuality, mind-independent existence or metaphysical fundamentality. Nevertheless, definitions, identity criteria and inference rules can favor a philosophical position even when labels appear neutral.

The [2020 PhilPapers Survey](https://survey2020.philpeople.org/) supplies a map of professional disagreement, not an authority for selecting the ontology. The [target-group results](https://survey2020.philpeople.org/survey/results/all) below report rounded inclusive “accept or lean toward” percentages, excluding skipped and insufficiently familiar answers. Respondents could endorse multiple answers; omitted alternatives and “Other” mean rows need not total 100%. These are survey-population results, not a vote of all philosophers or metaphysics specialists alone.

| Dispute | Survey comparison | Project commitment or open question |
| --- | --- | --- |
| Abstract objects: Platonism or nominalism | Platonism 38%; nominalism 42%. | Formal entity admits mathematically or structurally individuated subjects. Under the [admission rule](#accepted-decision-admission-and-actuality), this does not assert that abstract objects actually exist independently of minds. Platonist, nominalist and conceptualist interpretations remain open. |
| Properties: universals, tropes, classes or nonexistent | Immanent universals 21%; transcendent universals 20%; tropes 15%; classes 11%; nonexistent 8%. | Feature distinguishes bearer-specific characteristics from reusable Predicables. This resembles trope/universal distinctions without adopting either existence theory. Immanent universals are instantiated repeatables; transcendent universals need not depend on instances; tropes are particular characteristics. Conceptualism, which grounds generality in concepts, is not a separate survey option here. |
| Statue and lump: one thing or two | Two things 42%; one thing 30%. | Different persistence criteria for an organized body and its material portion favor distinguishing statue and clay: reshaping can preserve the clay while destroying the statue. This is an interpretive leaning, not an adopted two-object verdict; apply the [identity tests](#bodies-portions-aggregates-and-persistent-institutions). |
| Personal identity: psychological, biological or further-fact view | Psychological 44%; biological 19%; further-fact 15%. | Person beneath Human in the provisional graft does not establish person–organism identity or biological persistence. Decide whether person and organism are one subject or constituted/related subjects; psychological continuity, organism continuity and an additional identity fact are competing accounts. |
| Temporal ontology: eternalism, presentism or growing block | Eternalism 40%; presentism 18%; growing block 17%. | Occurrences and regions do not assert equal actuality of past, present and future. Eternalism admits all times; presentism only the present; growing block the past and present. Discussing past events and avoiding a universal present do not by themselves select a theory. |

### Commitment discipline

Adopt commitments when they clarify identity, preserve distinctions or support justified inference under the project's purpose. Record their rationale, strongest alternative, discriminating cases and costs. Preserve neutrality where rival accounts fit the same requirements; neutrality must not conceal incompatible meanings or undefined identity criteria.

For each proposed branch, ask what membership entails about existence, dependence, persistence, modality and predication. Separate representation choices from claims about reality. The disjoint, exhaustive Particular / Predicable root split is an adopted conceptual commitment; the six Particular categories are an open, potentially overlapping grouping. Neither policy proves one uniquely correct decomposition of reality.

Apply the [shared stress tests](#stress-testing) to rival accounts without requiring the project's preferred labels or placements. Distinguish equivalent accounts with different navigation, empirically or logically defective accounts, and coherent alternatives with different metaphysical commitments. Popularity is context, not validation; unresolved questions remain unresolved rather than silently becoming adopted positions.

## Stress testing

The [WordsToCategorize inventory](WordsToCategorize.md), especially [Difficult Words](WordsToCategorize.md#difficult-words), is the vocabulary reservoir. Its upper-ontology, biology and Roget sections supply additional probes. A word can require several sense-specific tests; a tick establishes neither definition coverage nor a valid placement. Supplement it with the [memoranda's cases](OntologyDesignMemoranda.md#17-immediate-next-research-task), [GPT's worked examples](GPT/stress-tests.md), and counterexamples from the three critiques.

For each test record the intended sense and context, subjects distinguished, identity assumptions, proposed class memberships, primary route, alternate classifications, required relations, permitted inferences and forbidden inferences. Record a result as pass, fail, unresolved or outside declared scope, with rationale. Unresolved or out-of-scope cases are not passes. A pass means the agreed distinctions and inference constraints survive; it does not require one predetermined school of ontology or a dedicated node for every word. Run a shared representative set during root selection, the full sense inventory before consolidated acceptance, and affected cases after each change. Add unfamiliar cases to test whether the rules generalize beyond examples used to design them.

### Admission and nonexistent subjects

Compare Holmes, Holmes in an adaptation, a refuted scientific posit, a round square, the largest prime, absence and nothingness. Preserve source characterization without implying actuality or importing contradictions into unrestricted core inference. Distinguish fictional subject, actual description, failed reference and impossible conditions. Check cross-work identity and actual authorship claims under the chosen fiction policy.

### Classes, instances and reification

Compare Dog, Fido, “dog”, a dog concept and a kind specification; distinguish a biological taxon as a classification from a historical lineage. State a relation's arity and transitivity without changing its argument-level meaning. Keep instance-of, subclass-of, specification-for, set membership and parthood distinct. Attempt Russell-style unrestricted self-membership and require the formal contract to prevent the inference rather than forbid all discussion of classes.

### Features, conditions and values

Give two cups the same measured mass. Distinguish their bearer-specific qualities, a reusable condition, quantity kind, measurement mapping, magnitude, unit and numeral. Equal values must not merge particular qualities. Test mass, color, severity and a database field storing Paris: being used as a value does not automatically make Paris a formal magnitude or predicate.

### Arity and context transformations

Start with HasMass(bearer, value, time). Fix value and time, fix only value, quantify over value, and encode the tuple as one object; record the different derived conditions. Compare jurisdiction, frame and time as arguments versus indices. Reject silent argument deletion, confusing a numerical function with a truth-valued predicate, and assigning a bearing relation to a participation family requiring an occurrence. Test nullary, variable-arity and higher-order cases with an explicit policy rather than silently excluding them.

### Kinds, roles, phases and designed purposes

Test a student who graduates, a dog becoming a pet, an inedible botanical fruit, a tomato as culinary vegetable, a designed hammer and a stone used to hammer. Preserve underlying identity and ancestry through changed roles. Distinguish artifact design history from temporary use; test whether a claimed rigid superclass can legitimately contain the proposed role or phase class.

### Disposition, capability and function

Test unbroken glass that never shatters, an unused capability, a task assessment that changes without changing the bearer, a broken pump retaining its assigned purpose, and an evolved biological function without an intentional designer. Separate capacity, manifestation, task-relative assessment, assignment and selection history. A lost capacity must not automatically erase design purpose or historical function.

### Norms, goals, attitudes and binding positions

Compare a norm's wording/content, its enactment, a particular obligation, a vacant office and its occupant. Distinguish goal specification, adopting the goal, purpose assignment, successful performance and preference. Test an obligation without a named beneficiary, an unadopted goal, preference for an unchangeable past, and cyclic preferences. Do not assume every norm is binding or morally correct, every preference is an intention, or every preference relation is an ordering.

### Bodies, portions, aggregates and persistent institutions

Compare statue/clay, a repaired ship, a river with changing water, a forest, a flock and a singleton set containing that flock. Test a corporation after total membership turnover, vacancy, schism and merger. Compare corporation, charter, building, members and legal personhood; compare state, government, territory and population. Co-location and institutional association must not substitute for identity, and changing members must follow a stated persistence rule.

### Objects, processes, events and states

Compare waterfall, flowing water, whirlpool, soliton, computation, wedding, wedding record and continuing marriage. Compare a steady condition with the activity maintaining it; test a conversation under physical, mental and social descriptions. State when descriptions classify one occurrence and when they identify related subjects. An event is not its record or type; its participants are not subclasses of it.

### Regions, hosts, fields and physics commitments

Move a ring with a hole and a ship with a room; distinguish cavity, boundary, occupant, host-relative region and region occupied at a time. Compare lake/water, mountain/extent, coordinate/location, vacuum/absence, a physical field and its mathematical model. Handle spacetime descriptions without a universal present or silently identifying a body with its career. Make point-based versus point-free and physical versus geometric interpretations explicit.

### Content, syntax, carriers and execution

Compare two printed copies, a digital copy, a translation, identical wording in independently originated works, a proposition and its sentence, a diagram and what it depicts. Distinguish language system from expression; genome sequence from molecule; algorithm from code, installed artifact and execution. Relate these subjects without making carriers subclasses of content or forcing one ambiguous word into one sense.

### Mathematics, logic and truth

Compare number/numeral, set/member, group as mathematical structure/social group, function as mapping/purpose, theorem/proposition/proof/proof-checking, model/target and fact/true proposition/worldly condition. Preserve identity versus isomorphism, equivalence and representation under declared foundations. Test singular propositions about contingent individuals, possible worlds and natural laws; unknown placement must not be concealed by a residual label such as Abstract.

### Relation families and metaproperties

Test institutional versus informal social relations, causation versus explanation, participation versus bearing, and attribution versus actual assertion. Require types, argument roles, domain and context. Test identity, exact equality, isomorphism, approximate similarity and shared nationality, including dual nationality: the last does not guarantee transitivity. Decide separately whether a family is a semantic subclass, a facet or a metamodel classification.

### Biology and cross-domain coverage

Test bird/dinosaur, mammal/synapsid and human/lobe-finned ancestry; separate carnivoran ancestry from carnivorous diet, thermoregulation from clade, and familiar fish/algae groupings from monophyletic lineage. Test extinct taxa, viruses, viroids and prions without asserting one clean lineage for all acellular infectious agents. Include RNA catalysts, mineral species versus coal samples, and pure water versus saline mixtures. Require declared source scope, preserved lineage and editorial exceptions; broad source accounting is not biological validation.

### Preservation, findability and validator resistance

Replay legacy assertions through split, merge, narrowed and broadened mappings; test Food, Person, Quality, Function, Role and Status across formal levels and senses. Every accepted sense must be findable through label, alias, disambiguation or facet, including off-tree edible-bearer classifications. Distinguish distinct-node counts from displayed path occurrences and entity-population counts. Deliberately introduce duplicate IDs, cycles, dangling links, multiple primary parents, missing definitions, wrong predicate types and scope leakage; require rejection. Exercise the [browser regression suite](test_browser.js) and extend its acceptance checks for semantic destinations, full ancestry and unique rendered identities. Passing browser tests cannot certify English definitions or philosophical coverage.

## History

### Retired v2 expansion

The mechanically expanded 5K–10K profile is retained only for analysis. It was rejected because source-driven ancestry produced sparse nonliving coverage, unhelpful unary chains, and poor visible splits. No node budget or source target is a current commitment. The next profile must pass structural review before adding reviewed leaves through a shared, versioned manifest.

## Implementation

### Publishing the tree to the wiki

Any change to the ontology tree or to the page that presents it must be published to the wiki before the work is complete. Regenerate the affected `ontology.json` and `index.html` artifacts from their source data and generator, run the browser regression checks, and copy the validated artifacts to the wiki's `Ontology/` publication directory. Publish the corresponding manifest or source snapshot whenever the generated data or its provenance changes. The regression checks must exercise the example search buttons as well as ordinary search, expansion, collapse, and lineage navigation. Do not leave a source-tree or browser change visible only in a local working copy.

GitHub synchronization and website publication are separate steps. Upload the validated, committed files over SSH to `holtzorg@holtz.org:~/public_html/Thoughts/wiki/Ontology/`, which serves [the live browser](https://humanknowledge.net/wiki/Ontology/). Use a bounded file list and `rsync --inplace`, without deletion, including changed data, browser files and their source/provenance documents. Fetch the public files after upload and compare their SHA-256 hashes with the committed artifacts; a successful Git push alone does not establish publication.

### Entity counts

Counts describe the population or vocabulary represented by a class, not the number of nodes displayed below it. Each entry specifies whether it counts kinds, instances, or catalogue records, and gives its scope. The inventory covers countable categories found in the [GPT tree](GPT/ontology.json) and [SUMO projection](ontology.json), plus useful narrower categories such as chemical elements and sovereign states even when they have no dedicated node. Source pages checked 2026.10.10; release and observation dates are stated where available. Approximate values are estimates, not exhaustive enumerations. Biological species counts use the separate [taxon catalogue](taxon-species-counts.html).

The [entity count catalogue](entity-counts.html) exposes each claim, source, scope, and reviewed node mapping. [entity-count-references.json](entity-count-references.json) maintains the shared records; [render_entity_counts.py](render_entity_counts.py) generates each browser’s count sidecar and publishes the annotations. Rerun it after regenerating a browser. Counts remain independent of source graphs and tree child counts. The GPT [Markdown tree](GPT/ontology-tree.md) also includes the annotations.

Entity annotations use the [taxon count symbol convention](#taxon-species-counts) for supported extant/extinct splits. Living-human and living-language counts have ♥︎; unsupported extinct counts remain omitted. ℵ₀ denotes countably infinite collections, and 𝔠 = 2^ℵ₀ denotes the uncountable continuum without assuming 𝔠 = ℵ₁. Broader nodes retain qualifiers such as “finite graphs,” “ℕ→ℕ,” or “Solar System.” Anatomical bone and muscle counts are not attached to GPT tissue-portion classes.

#### Chemistry and physics

- [Chemical elements](https://iupac.org/what-we-do/periodic-table-of-elements/) — **118 recognized kinds**, corresponding to atomic numbers 1–118; applies to Atom and Elemental substance portion. Element 119 is not an accepted discovery.
- [Elementary particles](https://home.web.cern.ch/science/physics/standard-model/) — **17 Standard Model kinds** in the conventional chart: six quark flavours, six leptons, four gauge-boson kinds, and the Higgs boson. Antiparticles and colour states are not counted separately; this is not a count of all composite subatomic particles.
- [Chemical substances](https://www.cas.org/cas-data/cas-registry) — **over 290 million registered substances** in CAS REGISTRY. A catalogue lower bound for known substances, not a count of every possible molecule or compound, nor of physical substance portions.
- [Minerals](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf) — **6,239 valid mineral species**, IMA-CNMNC master list, 2026.09; kinds represented by Mineral substance portion, not individual mineral grains.
- [Vitamins](https://www.medlineplus.gov/ency/article/002399.htm) — **13 essential vitamin categories for humans**, including eight B vitamins; chemical vitamers within a category are not separate vitamins in this convention.
- [Protein-building amino acids](https://medlineplus.gov/genetics/understanding/howgeneswork/protein/) — **20 standard kinds**; [nine are nutritionally essential for humans](https://www.medlineplus.gov/ency/article/002222.htm). This is the conventional standard set, not every naturally occurring amino acid.

#### Astronomy

- [Planets](https://science.nasa.gov/solar-system/planets/) — **eight Solar System planets**; **6,445 confirmed exoplanets** in the [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/), release 2026.10.08. The exoplanet count is a discovery catalogue, not the estimated cosmic population.
- [Dwarf planets](https://science.nasa.gov/solar-system/planets/) — **five officially recognized Solar System examples**: Ceres, Pluto, Haumea, Makemake, and Eris; many additional candidates exist.
- [Natural satellites](https://science.nasa.gov/saturn/moons/) — **293 confirmed moons of Saturn**, NASA's 2026.08 reference count. This bounded-system count does not imply a total for all natural satellites.
- [Asteroids](https://science.nasa.gov/solar-system/asteroids/facts/) — **about 1.1–1.9 million main-belt asteroids larger than 1 km**, plus millions of smaller bodies; an estimated population, not a discovery-list count.
- [Comets](https://science.nasa.gov/solar-system/10-things-whats-that-space-rock/) — **likely billions in the Solar System**, NASA's population estimate; a discovery catalogue contains only a small fraction.
- [Stars](https://science.nasa.gov/universe/stars/) — **more than 100 billion in the Milky Way**, an estimated population within our galaxy.
- [Galaxies](https://science.nasa.gov/exoplanets/what-is-the-universe/) — **at least 100 billion in the observable universe**, NASA's broad estimate; faint-galaxy extrapolations depend on detection limits and cosmological models.
- [Constellations](https://iauarchive.eso.org/public/themes/constellations/) — **88 IAU-defined sky regions**; this is a conventional partition of the sky, not 88 physical stellar systems.

#### Geography and society

- Sovereign states — **195 under the UN convention**: [193 member states](https://www.un.org/library/unms) and [two non-member observer states](https://research.un.org/en/unmembers/observers), the Holy See and Palestine. Recognition disputes change broader counts; “nation,” ethnic group, and state are not interchangeable. Applies to State territory and Geopolitical Area.
- [Continents](https://en.wikipedia.org/wiki/Continent) — **seven in the familiar English-language convention**; other conventions use four, five, or six. Applies to Continental area.
- [Oceans](https://oceanservice.noaa.gov/facts/howmanyoceans.html) — **five named oceans** within one connected global ocean; applies to Saltwater area.
- [Lakes](https://doi.org/10.1002/2014GL060641) — **about 117 million with area at least 0.002 km²**, the GLOWABO satellite inventory (2014), excluding Greenland and Antarctica. A size-threshold estimate relevant to Standing-water area; lakes are not necessarily freshwater.
- [Islands](https://www.usgs.gov/publications/global-islands) — **340,686 mapped marine islands**, calculated from 21,818 larger than 1 km² and 318,868 at most 1 km² in the USGS-described 30 m satellite inventory (2014 imagery, 2020 publication). Excludes its five continental mainlands; map resolution and shoreline rules limit completeness.
- [Humans](https://en.wikipedia.org/wiki/World_population) — **about 8.3 billion living individuals in 2026**, a rounded global population estimate, not a count of everyone who has ever lived.
- [Currency systems and codes](https://www.six-group.com/dam/download/financial-information/data-center/iso-currrency/lists/list-one.xml) — **178 distinct active ISO 4217 alphabetic codes** in SIX List One, published 2026.09.17; counted by deduplicating nonempty Ccy fields. Includes funds, precious-metal, testing, and no-currency codes, so this is not 178 circulating national currencies.

#### Human anatomy

- [Bones](https://seer.cancer.gov/training/manuals/Book4.pdf) — **206 in the conventional adult human skeleton**; individual variation and counting of fused bones can change the count. Applies to anatomical bones, not kinds of Bone tissue portion.
- [Muscles](https://my.clevelandclinic.org/health/body/21048-skeletal-system) — **more than 600 in a human body**; anatomical count varies with grouping, not a count of muscle-tissue kinds.
- [Chromosomes](https://www.genome.gov/genetics-glossary/Chromosome) — **46, arranged in 23 pairs, in a typical human diploid cell**; gametes and chromosomal variants have different counts.
- [Cells](https://pubmed.ncbi.nlm.nih.gov/37722043/) — **about 36 trillion in a reference adult male and 28 trillion in a reference adult female**, Hatton et al. (2023); model-dependent individual counts, not cell-type counts or a total for all organisms.

#### Language and formal vocabularies

- [Human languages](https://en.wikipedia.org/wiki/Language#Linguistic_diversity) — **7,170 living languages**, Ethnologue's 29th edition (2026), as reported by Wikipedia. Language-versus-dialect boundaries depend on the catalogue; extinct and constructed languages are outside this total.
- [Computer languages](https://hopl.info/) — **8,945 programming languages catalogued by HOPL**, including historical languages; this roster is not restricted to languages in active use and does not exhaust every possible formal language.
- [Characters](https://www.unicode.org/versions/Unicode18.0.0/) — **172,808 encoded characters in the Unicode 18.0 summary**, dated 2026.09.16. The source retains a draft-status notice, so this count is provisional; it counts an encoding repertoire, not every symbol or glyph humans can create.
- [Measurement units](https://www.nist.gov/pml/owm/metric-si/si-units) — **seven SI base units and 22 derived units with special names**, not all possible derived or non-SI units. The [SI prefix vocabulary](https://www.nist.gov/pml/owm/metric-si-prefixes) has **24 prefixes**.

#### Mathematical cardinalities

These are exact mathematical cardinalities rather than empirical estimates; the distinctions follow [Sundstrom's finite and infinite sets treatment](https://people.math.sc.edu/girardi/m300/book/Sundstrom2-1.pdf#page=486).

- Natural number, Integer, and Rational number — each **countably infinite**, cardinality ℵ₀.
- Real number and Complex number — each **uncountably infinite**, cardinality of the continuum, 2^ℵ₀; a complex number is a pair of real numbers.
- Algorithm, Computable function, and Recursive function — each **countably infinite** under the usual finite-description convention. Finite formal expressions, finite symbol strings, and finite graphs of arbitrary size are also countable; this follows by finite-string encoding, not from a survey of existing examples.
- Function — **2^ℵ₀ functions from natural numbers to natural numbers**; no single cardinality applies without fixing the domain and codomain. Set likewise has no universal set of all sets in ordinary set theory, so it receives no total.

#### Scope limits

Broad classes such as Entity, Object, Process, Organization, Artifact, Language system, Property specification, and Relation specification have no defensible finite global total without a narrower domain and counting rule. Books, buildings, games, software, words, ethnic groups, mountains, and constructed human languages likewise require a named catalogue or explicit inclusion boundary; no unsupported global number is assigned here. A blank count is not zero. Counts for nested or overlapping classes must not be added together.

#### Taxon species counts

All rendered ontologies use independent reference counts for taxon nodes. Choose a high-quality taxonomy with a useful count for each node and each extinction category; the two categories may use different sources. Map to the closest reference taxon when no exact match has data, recording any scope difference. Counts need not agree across sources or roll up through our tree. Do not assemble composite counts for paraphyletic or informal groups; a subtotal published by a reference source is usable directly.

Living counts primarily use [Catalogue of Life](https://doi.org/10.48580/dgz5n) reference-taxon metrics (`speciesExtantCount`), supplemented by specialist checklists and [OneZoom](https://www.onezoom.org/data_sources.load?tabs=all). Extinct counts primarily use the [Paleobiology Database](https://paleobiodb.org/data1.2/taxa/list): accepted species below the reference taxon, `extant=no`, excluding ichnotaxa and form taxa. These are catalogued species, not estimates of every species that ever lived. Living-tree and non-fossil checklist counts are suggestive proxies and can retain recently extinct species. Use source-reported values without subtracting uncertain extinction flags or reconciling different classifications.

The monochrome symbols follow their counts: ☠︎ for extinct and ♥︎ for extant, with extant last and `+` between them. Omit unavailable counts; show a known zero as zero. An available total without an extinction split has no symbol. Abbreviate thousands and millions with K and M, using at most three significant digits and retaining significant trailing zeros. Thus 30,040 becomes 30.0K.

The [source and mapping catalogue](taxon-species-counts.html) records each reference taxon, source, retrieval date, count and method, including approximate matches. Its maintained data is [taxon-species-counts.json](taxon-species-counts.json); [render_species_counts.py](render_species_counts.py) generates the catalogue and each browser's count sidecar.

### Browser navigation

Clicking a node title shows only its primary lineage and direct children, with those children collapsed. A second consecutive click on the same title restores the complete prior view, including its expansion states and any previous lineage focus. Clicking a different title focuses that node and makes the current view its restoration target.

A triangle toggles only its own node, preserving every other expansion state and the current lineage projection. A triangle click breaks a consecutive title-click pair. Global Expand and Collapse return to the full tree.

The [browser regression suite](test_browser.js) checks visible lineage and children, switching focus, restoring full and focused views, and isolated triangle toggles in every browser. GPT rendering and species-count builds run this suite automatically; other artifact builds must run it before publication.

### Node information notes

The browser should place a Unicode information glyph `ⓘ` after child and descendant counts. Clicking it opens a terse node note. `Property` and `Relation` notes should retain their reviewed child inventories and provenance; other notes are source- or node-specific.

- **Property:** inventory assembled in the maximal synthesis and cross-compared across Aristotelian, SUMO/BFO, and formal/type-theoretic sources.
- **Relation:** inventory assembled beside Property; it mixes subject-matter, logical, mathematical, operational, and provenance axes and needs sibling review.

### Projection rules

- Preserve source IDs, labels, definitions, aliases, and all source edges.
- Select one deterministic primary parent for visible navigation.
- Retain alternate parents and suppressed ancestors as metadata.
- Derive roots from incoming displayed edges.
- Flatten empty structural nodes in the rendered view.
- Keep source semantics separate from the navigation projection.

### SUMO PDF extraction

The SUMO browser is generated from the checked-in PDF graph: download and hash its source, convert it to SVG and positioned text, extract labeled arcs, and run `generate_sumo.py --pdf-graph`. Keep the 518-node, 554-arc source graph; choose one primary parent for display, retain alternate parents, and record the four provisional placements separately from PDF-derived edges.


### How the WordNet tree was generated

[`generate_wordnet_20q.py`](generate_wordnet_20q.py) loads local Princeton WordNet 3.0 through NLTK, selects a declared frequency-ranked noun profile connected to `entity.n.01`, closes over the required hypernym ancestry, and projects multiple hypernyms to one deterministic display parent. The manifest retains source IDs, glosses, frequencies, all hypernym edges, and the selected display parent; the projection does not rewrite WordNet.

Regenerate the historical profile with:

```sh
NLTK_DATA=~/nltk_data /tmp/wordnet-ontology-venv/bin/python \
  generate_wordnet_20q.py --target 7000 --output-dir .
```

### Practical scope and UI constraint

The active constraint is the shared static browser: searchable, collapsible, single-parent navigation with source links, counts, lineage, and definitions when supplied.
