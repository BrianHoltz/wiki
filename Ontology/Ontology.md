# 20 Questions Ontology

## Status

The original curated tree remains committed as `index.html`,
`20_questions_hierarchy.yaml`, and `generate_20q_hierarchy.py`. It contains
678 display nodes: 50 branches and 628 terminal categories.

The first v2 implementation is also committed:

- [`v2.html`](v2.html) — the v1-organized, one-page expanded profile;
- [`v2_20_questions_hierarchy.yaml`](v2_20_questions_hierarchy.yaml) — the
  expanded tree;
- [`v2_manifest.json`](v2_manifest.json) — counts, review seeds, source
  parameters, and policy metadata; and
- [`generate_v2_ontology.py`](generate_v2_ontology.py) — the reproducible
  builder.

The default reviewed build contains 9,955 displayed nodes: 4,979 branches and
4,976 terminal categories. It preserves the v1 spine, adds 6,076 selected
WordNet 3.0 source synsets, and adds 3,183 displayed NCBI life-taxonomy taxa
from a 1,000-taxon common-name-weighted selection plus required ancestors.
The NCBI taxonomy layer is explicitly a scientific detail and candidate layer;
it does not claim that every scientific label is a good casual-game answer.
The published artifacts were generated with the NCBI Taxonomy `nodes.dmp` and
`names.dmp` files plus the local WordNet 3.0 corpus:

```sh
NLTK_DATA=~/nltk_data /tmp/wordnet-ontology-venv/bin/python \
  generate_v2_ontology.py \
  --ncbi-taxdump /path/to/ncbi-taxdump \
  --wordnet-target 4500 --ncbi-target 1000
```

The first standards-based experiment is now also committed:

- [`wordnet_20q.html`](wordnet_20q.html) — the browseable one-page profile;
- [`wordnet_20q.yaml`](wordnet_20q.yaml) — the projected tree;
- [`wordnet_20q_manifest.json`](wordnet_20q_manifest.json) — source IDs,
  glosses, frequencies, original hypernyms, and selected display parents; and
- [`generate_wordnet_20q.py`](generate_wordnet_20q.py) — the reproducible
  builder.

It uses Princeton WordNet 3.0 noun synsets. It selects the top 7,000
frequency-weighted noun synsets that have a hypernym path to WordNet's
`entity.n.01` root and adds their complete hypernym ancestry, producing 8,974
display nodes: 3,831 branches and 5,143 terminal categories. This root
connectivity filter prevents WordNet's disconnected proper names, places,
events, and other top-level records from being flattened directly under the
display root. The game profile also suppresses the degenerate generic
`thing -> horror` stub.
The selected source pool contains 82,115 noun synsets, of which 13,739 have
nonzero WordNet corpus-frequency counts.

The display tree chooses one deterministic presentation parent when WordNet
has multiple hypernym paths. That is a view projection, not a modification of
WordNet: all source hypernyms remain in the manifest.

## How the WordNet tree was generated

The tree is a reproducible presentation of WordNet 3.0, not a hand-edited
taxonomy. The builder is [`generate_wordnet_20q.py`](generate_wordnet_20q.py).
It uses NLTK only as the loader for the local WordNet release; the generated
HTML, YAML, and manifest are the project artifacts.

The build proceeds as follows:

- **Load the source:** read every WordNet noun synset, including its lemma
  names, gloss, corpus-frequency counts, and authoritative hypernym links.
- **Score familiarity:** calculate a deterministic score using twice the
  natural logarithm of one plus the synset's corpus frequency, plus the
  logarithm of one plus its number of lemma names, plus a small bounded depth
  tie-break. Higher-frequency and more lexically represented synsets rank
  first.
- **Keep the declared root:** retain only noun synsets with a hypernym path to
  `entity.n.01`, WordNet's general entity root. This excludes disconnected
  records that would otherwise be incorrectly displayed as direct children of
  the root.
- **Select the source concepts:** take the top 7,000 eligible synsets and
  always include `entity.n.01`. The number is a profile parameter, so nearby
  5K and 10K experiments can be regenerated without changing the algorithm.
- **Close over ancestry:** recursively add every hypernym required to connect
  each selected synset to the root. These added ancestors explain why the
  displayed count is larger than 7,000.
- **Project the graph to one page:** WordNet can give a synset multiple
  hypernyms. For browseability, choose one deterministic display parent,
  preferring the highest-scoring available parent and breaking ties by source
  ID. This creates a single navigable tree while preserving every original
  hypernym edge in the manifest.
- **Apply profile presentation exclusions:** suppress the generic
  `thing.n.08` branch when it would appear only as the degenerate
  `thing -> horror` stub. This is a game-profile cleanup, not a claim that
  WordNet's `horror.n.02` hypernym link is invalid.
- **Generate the outputs:** write a collapsible, searchable HTML page with
  suggested category questions; a YAML tree for inspection and tooling; and a
  JSON manifest containing source IDs, labels, glosses, frequencies, all
  hypernyms, and the selected display parent.

The source graph therefore remains authoritative. The one-parent tree is only
the game-oriented view, and changing the target size or presentation
tie-break does not silently rewrite WordNet semantics. A local regeneration
uses the documented NLTK environment and:

```sh
NLTK_DATA=~/nltk_data /tmp/wordnet-ontology-venv/bin/python \
  generate_wordnet_20q.py --target 7000 --output-dir .
```

## Practical scope and UI constraint

The useful target is **5,000–10,000 displayed nodes**, with the current 8,974
node profile as a promising operating point. The existing UI is deliberately a
single static page with collapsible sections, suggested questions, search, and
expand/collapse controls. It can remain fully expanded on one page, but the
browser should be benchmarked after each profile change.

The count convention is displayed source concepts plus required presentation
ancestors. It excludes aliases and questions from the node count. Every build
should report:

- source synsets selected and source synsets available;
- displayed branches and terminal categories;
- maximum and median depth;
- duplicate visible labels and polysemous lemmas;
- balance of candidate mass at each branch; and
- page load, search, full expansion, and memory measurements.

The current WordNet profile favors browseability and familiar vocabulary by
frequency-ranking the selected synsets. It favors 20 Questions utility by
retaining ancestry and asking category-membership questions. It favors source
fidelity by preserving synset identifiers, glosses, and all original
hypernym edges.

## V2 expansion: 5K–10K gameplay nodes

V2 is a larger, reviewed version of the v1 tree, not a wholesale replacement
with an external ontology. It keeps v1's top-level questions and everyday
answer categories intact, then adds a selective life taxonomy and source-backed
vocabulary candidates. The page remains understandable to someone playing
ordinary 20 Questions: scientific rank names and identifiers are provenance
and navigation aids, not a demand that players know biology jargon.

The target should be stated as **displayed nodes**, counting visible branches
and leaves but not aliases, source records, glosses, or hidden alternate
parents. A practical first allocation is:

- **About 1,000–1,500 nodes retained or refined from v1:** preserve the
  familiar physical, living, geographic, food, artifact, person, and abstract
  organization. V1 labels should not move merely to accommodate a source
  taxonomy.
- **About 2,500–5,000 life nodes:** expand animals, plants, fungi,
  microorganisms, and extinct life under the existing living/natural
  branches. This is the main v2 investment and can support either a 5K
  conservative profile or a 10K richer profile.
- **About 1,000–2,500 non-life additions:** use reviewed WordNet, Roget, and
  reference-source candidates for familiar tools, foods, materials, places,
  body parts, vehicles, occupations, and cultural objects. These additions
  prevent v2 from becoming a biology encyclopedia with a thin everyday shell.

The implementation uses one shared manifest and can produce narrower profiles
by lowering the source budgets:

The current profile uses a dual-resolution compromise: familiar v1 labels and
reviewed examples are directly playable, while NCBI scientific detail and
WordNet candidates are clearly labelled expansion branches. A compact profile
can be generated later by lowering `--wordnet-target` and `--ncbi-target`; a
fuller profile can raise them without forking the tree design.

### Selecting notable life entries

The biological graft should use a two-axis inclusion policy rather than simply
taking the most frequent taxa or copying every species in a source database.
Each candidate receives separate scores for **public familiarity** and
**evolutionary or scientific interest**, with a minimum evidence threshold for
either score and a manual placement review.

Public-familiarity candidates include organisms that a general player is
likely to recognize from ordinary life, food, pets, farming, medicine,
children's education, news, or common media. This favors entries such as dog,
cat, horse, cow, chicken, bee, butterfly, oak, rose, mushroom, wheat, corn,
yeast, salmon, shark, whale, and crocodile. Common names remain the primary
visible labels, with scientific names and accepted taxon IDs stored as
metadata and searchable aliases.

Scientific-interest candidates are deliberately not limited to familiar
species. They include organisms or clades that make the tree explain
evolutionary history, unusual body plans, or convergence. The initial
high-priority set should include:

- **Conspicuous evolutionary survivors and transitional examples:** coelacanth
  (correctly spelled and linked to its lobe-finned lineage), horseshoe crab,
  tuatara, nautilus, lungfish, monotremes, and other living lineages commonly
  discussed as evolutionarily distinctive.
- **Convergent-evolution examples:** marsupials as a complete visible branch
  rather than a few isolated species; separately recognizable marsupials such
  as kangaroo, koala, wombat, opossum, and Tasmanian devil; and representative
  convergences such as bats versus birds, dolphins versus fish, sharks versus
  other streamlined swimmers, cactus-like euphorbs versus cacti, and
  anteaters versus aardvarks. The tree should not imply that convergent
  appearance means close ancestry.
- **Major extinct and deep-time groups:** dinosaurs, pterosaurs, trilobites,
  ammonites, non-avian theropods, sauropods, early tetrapods, and other
  culturally or scientifically notable extinct groups. Extinct taxa should
  remain under biological history, not be diverted into “historical object” or
  fictional branches.
- **Representative diversity:** at least one playable set of entries for each
  major animal, plant, fungal, and microbial branch, including organisms that
  are ecologically important, medically important, agriculturally important,
  or morphologically unusual. Selection should avoid spending the whole
  budget on one charismatic group.

This policy is a **notability sample**, not a claim that omitted taxa are
unimportant. A candidate should be included only when its visible label has a
clear answer interpretation, its taxonomic placement is supported by a
declared source release, and it contributes either recognizable game coverage
or a meaningful evolutionary contrast. A species with only a scientific
binomial and no usable common-language label generally belongs in metadata or
an optional detail layer, not as a default leaf.

### How the graft should work

The graft should begin from the v1 organism branches and map source taxa into
those homes through an explicit reviewed crosswalk. The pipeline should:

- choose one authority for accepted names and parentage for each release,
  preferably Catalogue of Life or GBIF for broad coverage, with Open Tree of
  Life, NCBI, ITIS, and specialized sources used for validation;
- retain stable source identifiers, rank, accepted name, synonyms, extinct
  status, and source version in a manifest;
- collapse taxonomic ranks that do not improve a 20 Questions split, while
  retaining enough ancestors to explain scientific placement;
- create visible nodes only for selected notable taxa and the ancestors needed
  to make their branches intelligible;
- preserve alternate scientific placements and synonymy as metadata rather
  than duplicating visible nodes;
- attach a short plain-language description and, where useful, an “often
  confused with” or “convergent with” note; and
- run a gameplay review for every new branch: recognizable answers,
  non-trivial sibling distinctions, balanced candidate mass, and a natural
  yes/no question.

The visible hierarchy must not use evolutionary relatedness as the only
question strategy. A player should first encounter useful distinctions such
as animal versus plant, vertebrate versus invertebrate, aquatic versus
terrestrial, or domesticated versus wild where those splits are more
answerable than a deep scientific rank. Scientific taxonomy determines
correct homes and metadata; the v1 information design determines the
player-facing order.

### Acceptance and quality gates

Every proposed v2 node should have a review record containing its label,
parent, source identifier and release, common-name evidence, familiarity
score, scientific-interest rationale, and rejection reason if not accepted.
Automated checks should reject or flag:

- duplicate visible labels with no disambiguating parent context;
- branches containing only one weakly notable child;
- taxa whose source parentage is unresolved or contradictory;
- scientific-only labels that have no useful player interpretation;
- nodes that make a suggested question nearly empty or nearly universal; and
- overrepresented clades that consume the budget without adding distinct
  gameplay choices.

The implemented biological pilot is the reviewed **9,955-node profile**. It
should be judged as a candidate browser, not yet as the final gameplay tree:
the next review pass should demote or hide scientific-only leaves, retain
notable ancestors, and preserve the seed examples that explain evolutionary
history. This staged review is safer than mechanically promoting every
scientific record to a casual-game answer.

## Vocabulary coverage audits from open encyclopedias and scored word lists

The tree should have an explicit **must-include audit** in addition to
taxonomy-driven expansion. The goal is not to copy an encyclopedia's
categories. It is to extract candidate entry titles, normalize them to noun
senses, and check whether familiar answers have a clear home in v1 or v2.
This gives us a defensible answer to “what obvious things did we forget?”

### Open and openly accessible encyclopedia sources

There is no single open, modern, general-purpose encyclopedia that is both
compact and already shaped like a 20 Questions noun tree. A practical source
set is therefore a combination of open-license article title lists and
compact knowledge outlines:

- **Simple English Wikipedia:** its CC BY-SA dump is a strong approachability
  source because article titles and explanations are intentionally written for
  a wider reading audience. It is broad but editorially noisy; use titles and
  lead concepts for candidate discovery, not Wikipedia category parentage.
- **English Wikipedia:** the full CC BY-SA dump supplies the largest open
  candidate inventory, redirects, and links to taxobox-backed organism
  articles. Page views, incoming links, and article lead quality can provide
  familiarity signals, but article existence is not evidence that a noun is a
  good game answer.
- **Wiktionary:** its regularly published dumps provide open lexical entries,
  parts of speech, definitions, inflections, synonyms, and language labels.
  It is better than an encyclopedia for deciding whether a candidate is
  actually used as an English noun, but its crowdsourced sense structure
  requires filtering and quality checks.
- **Encyclopedia of Life:** the open biodiversity portal is a useful
  approachable organism-entry source with common names, images, and links to
  scientific authorities. It is not a single-volume general encyclopedia, so
  it should supply biological familiarity evidence rather than the general
  ontology root.
- **Public-domain reference works:** the 1911 *Encyclopaedia Britannica* and
  other Internet Archive or Project Gutenberg encyclopedias can supply
  historically prominent names and concepts. They are useful negative controls
  for cultural coverage, but their dated science and vocabulary make them
  unsuitable as the sole modern must-include list.

The *Propædia* browser in [`Propaedia/index.html`](Propaedia/index.html) is a
particularly useful compact outline for auditing broad domain coverage. It
should be used to ask whether our top-level organization has room for a domain,
while open encyclopedic article titles should supply candidate leaves.

### Scored noun inventories

We can also construct a ranked noun list rather than rely on one encyclopedia.
The strongest openly available signals are complementary:

- [wordfreq](https://github.com/rspeer/wordfreq) supplies frequency estimates
  and top-word lists derived from multiple corpora. It is a good first
  frequency prior, but its list is not noun-filtered and frequency is not the
  same as game usefulness.
- [WordNet](https://wordnet.princeton.edu/) supplies noun synsets, lemma
  counts, glosses, and hypernyms. Its corpus counts provide a reproducible
  lexical familiarity signal, while its sense inventory prevents treating
  every spelling as a distinct concept.
- The [MRC Psycholinguistic Database](https://websites.psychology.uwa.edu.au/school/MRCDatabase/uwa_mrc.htm)
  and [Brysbaert concreteness ratings](https://doi.org/10.3758/s13428-015-0631-6)
  provide familiarity, imageability, age-of-acquisition, and concreteness
  features for many English words. These are especially useful for separating
  playable concrete nouns from frequent but abstract function words.
- [Google Books Ngram Viewer](https://books.google.com/ngrams/) and
  [Wikipedia pageviews](https://pageviews.wmcloud.org/) provide historical
  and current prominence signals. They should be treated as measurable
  evidence, not as ground truth: corpus bias, capitalization, inflection, and
  media attention can distort rankings.

A reproducible must-include audit can combine these signals into a declared
score such as:

```text
candidate score =
    frequency
  + concreteness and imageability
  + age-of-acquisition familiarity
  + encyclopedia/pageview prominence
  + WordNet sense and noun evidence
  - ambiguity, proper-name noise, and source disagreement
```

For each proposed noun, the audit should retain the raw features, candidate
senses, source URLs or IDs, normalized label, and proposed v1/v2 parent. We
should then publish separate thresholded lists—for example, the top 1,000,
3,000, and 5,000 everyday nouns—rather than silently treating one ranking as
canonical. A candidate becomes a must-include only after it also passes the
game checks: a recognizable answer interpretation, a clear home, and a
non-trivial question against its siblings.

## Prior art

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

### 20Q.net and Akinator

These are notable game systems rather than downloadable ontologies. They are
important prior art because they optimize the actual interaction this project
is trying to support: identifying a player-selected answer through a sequence
of questions.

- **20Q.net:** Robin Burgener's computerized 20 Questions experiment began in
  1988; the commercial handheld version appeared in 2003, and the service was
  also published as a website. The system is described as a learned neural
  network and folk taxonomy rather than a fixed public hierarchy. Its current
  internal question/answer inventory and node count are proprietary or
  undocumented. Its historical existence as a web and handheld product,
  multiple category editions, and long-running public use are the relevant
  prominence measures. See the
  [20Q overview](https://en.wikipedia.org/wiki/20Q).
- **Akinator:** Elokence launched this French video game in 2007. It asks
  about characters, objects, films, and animals, learns from prior players,
  and accepts graded answers such as “probably” and “probably not.” Its
  internal classification database and node count are not public. Its
  commercial web, mobile, and game presence and its sustained international
  availability are practical prominence proxies. See the
  [Akinator overview](https://en.wikipedia.org/wiki/Akinator).
- **Fit:** both systems demonstrate that question selection, uncertainty
  handling, and feedback can matter more to gameplay than a formally pure
  hierarchy. They are useful behavioral benchmarks, but their learned
  databases should not be silently substituted for WordNet's auditable source
  graph.

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

### Online biological taxonomies

These resources are the strongest available prior art for extending the
organism portion of a general noun hierarchy. None is a complete 20 Questions
ontology: they optimize taxonomic identity, scientific names, synonymy, and
research interoperability rather than familiar labels or balanced gameplay.

#### Catalogue of Life

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

#### GBIF Backbone Taxonomy

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

#### NCBI Taxonomy

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

#### Open Tree of Life

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

#### Integrated Taxonomic Information System (ITIS)

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

#### World Register of Marine Species

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

### Approachable cladistic and evolutionary trees

The most useful biological prior art for v2 is not a single taxonomy copied
verbatim. It is a scientifically defensible source tree paired with a
deliberately compressed display. A cladistic source should be allowed to say
that humans are sarcopterygian vertebrates and therefore nested within the
broader evolutionary history of fishes, even though “fish” remains an
everyday answer category. The visible game tree can collapse intermediate
clades when they do not create a recognizable answer or a useful question,
while retaining the omitted clades, ranks, and source identifiers in metadata.

#### OneZoom Tree of Life Explorer

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
  biological for the whole 20 Questions ontology, but its zoomed overview,
  common names, images, and source links suggest how v2 can hide taxonomic
  detail without discarding it.

#### TimeTree

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

#### Recommended collapsed-clade pattern

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
  too shallow for a complete 20 Questions noun tree.

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
- **20 Questions use:** after graph validation, a 5K–10K projection could
  provide an interesting contrast to WordNet. Selection should favor
  frequently encountered, semantically concrete categories while retaining
  source IDs and alternate parent links. It should remain a separately named
  DMOZ profile rather than being silently merged into the WordNet tree.

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

## Roget and the curated v1 tree

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

[`Rogets/index2.html`](Rogets/index2.html) is the high-confidence review view.
It keeps the original 628-leaf v1 tree and does not add automatic categories.
Instead, it annotates existing labels whose exact title matches a Roget
concept, exposes a small amount of Roget vocabulary to search, links each
annotation to its source entry, and makes the first-pass uses visible:
vocabulary discovery, sibling discovery, question-wording review, and
abstract-branch review. It is an experimental review surface, not a proposed
replacement for [`index.html`](index.html).

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
- **Question wording:** use Roget's synonym neighborhoods to make search and
  question phrasing more forgiving without adding duplicate concepts.
- **Abstract branch review:** use Roget's classes to audit v1's abstract
  coverage, while retaining v1's game-oriented boundaries.
- **Separate alternate profile:** preserve the Roget browser as a conceptual
  reference rather than pretending it is a superior replacement taxonomy.

The clean next experiment after this review view is to turn accepted proposals
into a **reviewed manifest**: map each candidate Roget concept or noun phrase
to a v1 parent, record the proposed label and evidence, and accept only
familiar terms with a clear answer interpretation. The current `index2.html`
deliberately stops before that irreversible step.

## 20 Questions projection algorithm

The source graph should remain authoritative. The build profile should:

- import stable source IDs, labels, glosses, frequencies, and all source edges;
- select a declared frequency and familiarity budget;
- add complete source ancestry needed to connect selected concepts;
- choose one deterministic display parent only for presentation;
- calculate subtree candidate mass and prefer balanced displayed splits;
- generate questions from source distinctions or declared attributes; and
- preserve discarded candidates and alternate paths in a manifest.

This keeps source semantics separate from game presentation. The one-page tree
is a reproducible view, not a hand-maintained fork.

## Future experiments

The WordNet experiment should be evaluated at target sizes near 5K, 8.9K, and
10K nodes. Measure browser load, full expansion, search latency, memory,
maximum depth, duplicate labels, and the quality of suggested questions.
Prefer the smallest profile that covers common game answers while preserving
the current one-page browsing experience.

The next useful improvements are a v2 review manifest, a better question
generator based on subtree balance, a coverage report for ordinary game-answer
lists, and a biological pilot containing the high-priority survivors,
convergent examples, marsupials, and extinct groups described above. The pilot
should produce compact and fuller profiles from one source manifest rather than
forking the ontology. Wikidata, FoodOn, and Wikipedia can then be tested as
separately labeled enrichment profiles, not silently merged into the WordNet
ontology.
