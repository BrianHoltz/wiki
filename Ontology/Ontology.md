# 20 Questions Ontology

## Status

The original curated tree remains committed as `index.html`,
`20_questions_hierarchy.yaml`, and `generate_20q_hierarchy.py`. It contains
678 display nodes: 50 branches and 628 terminal categories.

The mechanically expanded v2 profile has been retired from the public
navigation. Its source artifacts remain available for analysis, but its
display projection exposed too many unary branches and weak source-driven
splits. The next expansion will follow structural review of v1 rather than
adding more source ancestry to that profile.

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

The current phase is tree-first: structural quality, source comparison, and
ordinary-language coverage take priority over question-generation mechanics.
The historical 20 Questions material remains as provenance and as a
downstream success criterion; it is not an active implementation workstream.

Firm decisions:

- The handcrafted v1 remains the incumbent player-facing tree; imported
  ontologies are source, audit, and enrichment layers rather than replacements.
- The mechanically expanded v2 is retired. Structural refinement comes before
  large vocabulary batches.
- The visible navigation tree has one primary parent per node. Alternate
  parents remain typed, source-backed cross-links; unary nodes are allowed.
- SUMO's public browser is a PDF-derived projection, not a current KIF-derived
  taxonomy. Its PDF arc rule and four provisional placements are recorded in
  the SUMO artifacts.
- Biological expansion will use a curated, evolutionary source tree with
  readable labels and compressed intermediate clades. Viruses get a separate
  acellular-infectious-agent policy rather than being forced into ordinary
  organism ancestry.
- Definitions, aliases, source IDs, alternate edges, and provenance belong in
  the data layer even when the default browser keeps them compact.

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

## Retired v2 expansion

The mechanically expanded 5K–10K profile is retained only for analysis. It
was rejected because source-driven ancestry produced sparse nonliving coverage,
unhelpful unary chains, and poor visible splits. No node budget or source
target should be treated as a current commitment. The next profile must first
pass the structural audit and then add reviewed leaves through a shared,
versioned manifest.

## Biological taxonomy graft

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

### Single-pane and compressed tree renders

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

## Future leaf-node priorities

The immediate objective is to improve the tree and its information design
before adding a large undifferentiated noun list. Leaf additions should be
grafted into a reviewed structural home, not used to compensate for a weak
parent branch. The task list is:

- [ ] **Complete the structural audit:** repair overloaded v1 branches,
  improve sibling balance, clarify observable distinctions, and document
  intentional unary paths before adding major leaf batches.
- [ ] **Replace the organism subtree:** choose a public biological source
  combination and build a curated display taxonomy that preserves
  evolutionary accuracy while compressing opaque intermediate clades.
- [ ] **Add the virus policy and pilot:** include important viruses and virus
  families, but do not imply that viruses are ordinary organisms or that
  viruses are primarily related to one another by host. Keep host range,
  genome type, and transmission metadata separate from the visible parentage.
- [ ] **Graft notable life leaves:** add familiar, medically or agriculturally
  important, ecologically important, extinct, and evolutionarily instructive
  organisms under the reviewed biological tree.
- [ ] **Map Roget and WordNet vocabulary:** use their concepts, synsets,
  aliases, glosses, and sense frequencies to make SUMO and the biological
  tree searchable in ordinary language without copying their parentage
  blindly.
- [ ] **Graft product vocabulary:** compare Google Product Taxonomy, GS1 GPC,
  UNSPSC, eCl@ss, ETIM, and authorized Amazon/Walmart category exports to
  identify missing tools, foods, appliances, clothing, vehicles, electronics,
  materials, and household goods. Import reviewed leaves and source mappings,
  not retail department structure wholesale.
- [ ] **Audit everyday noun coverage:** score candidate tools, foods,
  materials, vehicles, body parts, places, occupations, cultural objects,
  people, and fictional entities from encyclopedias, Schema.org, Wikipedia,
  word-frequency lists, and concreteness data.
- [ ] **Run tree and coverage review:** test branch balance, duplicate labels,
  ambiguous senses, recognizable stopping points, source completeness, and the
  5K–10K page-performance budget before promoting a tranche. Compatibility with
  20 Questions remains a downstream success criterion, not the current design
  activity.

### Biological replacement criteria

The organism replacement should be judged as a curated display taxonomy, not
as a raw dump from whichever database has the most records. In addition to the
three proposed criteria—scientific accuracy, notable organism coverage, and
readable labels—it should satisfy these gates:

- **Evolutionary correctness:** the tree should allow humans and other
  tetrapods to remain nested within lobe-finned fish ancestry, birds beneath
  dinosaurs, and mammals within the appropriate synapsid lineage. Everyday
  labels such as “fish” may remain useful gameplay categories, but they must
  not silently replace the scientific provenance.
- **Authority and reproducibility:** every parentage decision needs a source,
  release, stable identifier, rank, and date. Conflicts between authorities
  should be retained as evidence and resolved by an explicit policy.
- **Notability diversity:** budget for familiar organisms, food and farm
  species, pets, disease agents, keystone organisms, culturally important
  organisms, extinct groups, and evolutionary oddities. Do not let species
  count or corpus frequency alone crowd out entire branches.
- **Readable presentation:** every opaque taxon needs a short plain-language
  description, an understandable visible label where one exists, and a
  searchable scientific-name alias. Scientific-only names should normally be
  metadata or an expandable detail layer rather than default leaves.
- **Rank compression with provenance:** retain an intermediate clade when it
  explains a major evolutionary distinction or supports a useful question;
  collapse it when it adds no playable split. The hidden source path must
  preserve every omitted ancestor.
- **Convergence and polyphyly clarity:** convergent forms such as bats and
  birds, dolphins and fish, cacti and euphorbs, or marsupial and placental
  analogues must not be placed together merely because they look or behave
  alike. Add “convergent with” metadata instead.
- **Extinct-life continuity:** fossils, dinosaurs, trilobites, ammonites, and
  other extinct groups should remain in the same evolutionary history as
  living relatives, with extinct status visible in metadata and descriptions.
- **Single-parent usability:** the visible tree needs one reviewed display
  parent per node, while alternate placements, synonyms, taxonomic opinions,
  and source edges remain available for audit.
- **Classification utility:** each visible branch should create an intuitive,
  non-trivial distinction and have a clear interpretation for a general
  reader. Scientific rank alone is not a sufficient reason to expose a
  branch.
- **Budget and balance:** measure both node count and candidate mass by branch,
  reserve capacity for plants, fungi, microbes, and extinct life, and prevent
  charismatic animals from consuming the entire profile.
- **Version stability:** retain a snapshot manifest and a migration report so
  that a source update cannot silently move familiar leaves or erase aliases.

### Virus placement policy

Viruses deserve inclusion but should not be forced into the organism taxonomy.
They are acellular infectious entities with diverse evolutionary histories;
many are more meaningfully related through host, genome, replication strategy,
or shared viral ancestry than through a single universal tree. The default
visible design should therefore use a dedicated **Virus and other acellular
infectious agents** subtree under the physical/biological-agent region, while
retaining host associations and biological hypotheses as cross-links.

The virus pilot should include familiar and high-impact examples—such as
influenza, HIV, SARS-CoV-2, Ebola, rabies, herpesviruses, bacteriophages, and
plant viruses—alongside a compact set of major genome or replication groups.
It should not imply that all named viruses form a clean ranked lineage.
Each entry should record host range, disease or ecological relevance, genome
type, transmission mode, accepted name, synonyms, and source release. If a
future authoritative source supports a stronger viral tree, it can replace
the provisional subtree without changing the host-association metadata.

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
- run a tree review for every new branch: recognizable entries, non-trivial
  sibling distinctions, balanced candidate mass, and a clear semantic split.

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

### Ontology4 upper-ontology survey

The [Ontology4 upper-ontology index](https://www.ontology4.us/english/Ontologies/Upper-Ontologies/)
collects several historically important approaches: Aristotle, Sowa, Cyc,
SUMO, Schema.org, and the Ontological Sextett. The Sextett page also links
the proposed UMO. Ontology4 is useful as a comparative visual catalog, but
its pages are adaptations and diagrams rather than authoritative releases of
the underlying ontologies. The following entries evaluate the linked
approaches against this project's specific goal: a familiar, navigable,
question-oriented noun hierarchy.

#### Aristotle's categories

- **Source:** [Ontology4's Aristotle page](https://www.ontology4.us/english/Ontologies/Upper-Ontologies/Aristotle%20Ontology/index.html)
  and the [historical text](https://classics.mit.edu/Aristotle/categories.html).
- **What it is:** a philosophical account of categories of being and
  predication, traditionally including substance, quantity, quality,
  relation, place, time, position, state, action, and passion.
- **Structure:** a small conceptual partition, not a deep `is-a` hierarchy.
  It separates entities from properties, relations, and event-like
  predicates, but does not supply ordinary leaves such as `animal → mammal →
  dog`.
- **Status and access:** the historical work is public domain; the Ontology4
  rendering is a modern adaptation with no clearly stated independent release
  or machine-readable distribution.
- **Fit:** low as the game hierarchy, medium as a design sanity check.
  Aristotle can remind us to distinguish things, qualities, relations, and
  events, but “substance” is far too broad and abstract to be a useful
  player-facing branch.

#### Sowa's KR ontology

- **Source:** [Sowa's top-level ontology](https://www.jfsowa.com/ontology/toplevel.htm)
  and [Ontology4's Sowa page](https://www.ontology4.us/english/Ontologies/Upper-Ontologies/Sowa%20Ontology/index.html).
- **What it is:** a formal synthesis influenced by Peirce and Whitehead,
  organized around distinctions such as independent, relative, and mediating;
  physical and abstract; and continuant and occurrent.
- **Structure:** a lattice or diamond rather than a tree, with categories such
  as object, process, schema, script, participation, description, situation,
  reason, and purpose. Its formal combinations are useful for knowledge
  representation but do not naturally become familiar questions.
- **Status and access:** maintained primarily as scholarly explanatory web
  material rather than as a current, populated, independently versioned
  ontology release. The source page is openly viewable; licensing for
  derivative diagrams and text should be checked before redistribution.
- **Fit:** low to medium. It is a useful internal type system if the game
  expands beyond nouns into events, properties, and relations, but its
  categories are not suitable as ordinary player language.

#### Cyc and OpenCyc

- **Source:** [Cyc](https://cyc.com/), the [Cyc FAQ](https://cyc.com/faq/),
  and [Ontology4's Cyc rendering](https://www.ontology4.us/english/Ontologies/Upper-Ontologies/Cyc%20Ontology/index.html).
- **What it is:** a large formal common-sense knowledge base, inference
  system, and ontology rather than merely an upper-level taxonomy. It
  represents classes, individuals, predicates, rules, and contextual
  microtheories.
- **Structure:** rich logical assertions and relations, with collections,
  functions, predicates, and context-sensitive knowledge. It can express
  exceptions and practical facts that a simple hierarchy cannot.
- **Status and access:** Cycorp remains commercially active, but the current
  Cyc system and knowledge base are not an unrestricted public ontology
  download. Historical OpenCyc material should not be confused with the
  current commercial system, and its exact license and currency require
  verification before reuse.
- **Fit:** medium for symbolic reasoning, low for a lightweight game tree.
  Cyc could inspire rules such as typical uses or contexts, but its scale,
  engineering burden, and access model make it a poor incumbent replacement.

#### SUMO

- **Source:** [Ontology4's SUMO page](https://www.ontology4.us/english/Ontologies/Upper-Ontologies/Sumo%20Ontology/index.html),
  the [SUMO project](https://www.ontologyportal.org/), and its active
  [public repository](https://github.com/ontologyportal/sumo).
- **What it is:** the Suggested Upper Merged Ontology, combining a formal
  upper ontology with broad domain ontologies, logical axioms, relations, and
  WordNet-related mappings.
- **Structure:** a substantial `subclass` hierarchy plus `instance`,
  part-whole, temporal, spatial, and other relations. It covers animals,
  anatomy, vehicles, geography, artifacts, processes, and culture, but uses
  multiple inheritance and formal relations that do not fit a strict
  single-parent browser.
- **Status and access:** actively maintained in a public repository. The
  repository is inspectable and substantially more current and reproducible
  than the Ontology4 diagram. Licensing must be checked per file and
  subcomponent, especially where WordNet-derived data is involved.
- **Fit:** high as a semantic and provenance backbone, medium as direct game
  vocabulary. SUMO is the best candidate from the Ontology4 list for a
  structured improvement vector, but it should be projected into a curated
  game tree rather than displayed raw.

#### Schema.org

- **Source:** [Ontology4's Schema.org page](https://www.ontology4.us/english/Ontologies/Upper-Ontologies/schema.org%20Ontology/index.html),
  [Schema.org](https://schema.org/), its [latest vocabulary](https://schema.org/version/latest/),
  and the [source repository](https://github.com/schemaorg/schemaorg).
- **What it is:** a pragmatic web-markup vocabulary jointly developed for
  structured data understood by search engines, not a universal formal upper
  ontology.
- **Structure:** a human-readable `Thing` hierarchy with branches such as
  Person, Organization, Place, Product, Event, CreativeWork, MedicalEntity,
  and Intangible, plus many properties and enumerations. It has multiple
  inheritance and web/commerce/media/medical biases.
- **Status and access:** actively released and openly inspectable through the
  official site and repository. Its release process and licensing information
  are documented by the project, but the exact terms should be preserved when
  redistributing derived data.
- **Fit:** medium-high for contemporary familiar labels and broad category
  discovery, low as a complete noun ontology. It is especially useful for
  people, places, products, food, media, vehicles, and events, but it omits
  much of the ordinary physical and biological world that v1 handles well.

#### Ontological Sextett

- **Source:** [Ontology4's Sextett page](https://www.ontology4.us/english/Ontologies/Upper-Ontologies/Sextett%20Ontology/index.html).
- **What it is:** a proposed extension of the classical ontological
  rectangle, notably adding explicit relationships so statements such as
  “Picasso painted Guernica” are not forced into an entity-only taxonomy.
- **Structure:** a compact set of primitives involving entities, attributes,
  and relations. The page does not establish a complete, independently
  standardized machine-readable hierarchy.
- **Status and access:** a static Ontology4 proposal with no evident current
  release process, standards body, or independent implementation. No clear
  redistribution license is stated.
- **Fit:** low to medium as modeling inspiration, low as content. Its
  strongest contribution is the reminder that relations and attributes should
  be stored alongside the noun hierarchy rather than confused with noun
  categories.

#### UMO

- **Source:** [Ontology4's UMO page](https://www.ontology4.us/english/Ontologies/Upper-Ontologies/UMO%20Ontology/index.html);
  it is introduced from the [Sextett page](https://www.ontology4.us/english/Ontologies/Upper-Ontologies/Sextett%20Ontology/index.html).
- **What it is:** an “upmost minimal ontology,” intended to extend the
  Sextett with relations while reducing category names to base symbols.
- **Structure:** minimal primitives, explicit relationships, attributes, and
  superclass inheritance. The page illustrates distinguishing things using
  attributes such as age, color, weight, nationality, and height.
- **Status and access:** a static Ontology4 proposal without an evident
  versioned release, active standards process, maintained repository, or
  independent user community. Licensing is not clearly stated.
- **Fit:** low as a ready-made hierarchy, medium as a custom-engineering
  pattern. UMO's attribute emphasis could inform question generation, but it
  supplies neither the familiar nouns nor the reviewed parentage needed by
  this project.

#### Ontology4 recommendation

None of these upper ontologies should replace the incumbent v1 tree directly.
The best alternative is **SUMO as a semantic backbone**, with Schema.org as a
secondary source for contemporary human-facing categories and WordNet as the
lexical bridge. The best improvement vector is therefore layered:

- retain v1's player-facing top-level organization and hand-reviewed
  discriminators;
- map v1 leaves and future candidates to SUMO classes where a stable semantic
  anchor exists;
- use SUMO relations and axioms as validation and metadata, not as visible
  unary or multi-parent branches;
- use Schema.org and WordNet to discover familiar labels, aliases, and
  missing everyday siblings; and
- preserve all source identifiers and alternate parents in a manifest while
  projecting only a balanced single-parent navigation tree.

This is an improvement in auditability and scientific consistency, not a
reason to let SUMO dictate the game structure. The incumbent's main advantage
is precisely that its visible questions were designed for play rather than
inherited from a formal ontology.

#### SUMO PDF tree projection and unary-node policy

The [SUMO browser](SUMO/index.html) is rebuilt from the nodes and directed blue
arcs in the [official Ontology4 SUMO PDF](https://www.ontology4.us/download/dot/SumoOntology.pdf),
not from the current KIF hierarchy. The checked-in
[`pdf-graph.json`](SUMO/pdf-graph.json) records the extracted 518 PDF nodes and
554 vector arcs. Unary nodes are first-class citizens: a node having one child
is not, by itself, evidence of a bad tree or a reason to collapse it.

For each PDF node with multiple incoming arcs, the projection repeatedly
removes the longest measured incoming arc until one primary parent remains.
Removed parents remain visible as alternate cross-links. This makes `Object`
have exactly the PDF's four visible children: `Agent`, `Collection`, `Region`,
and `SelfConnectedObject`.

`Entity` is now the only root. The four disconnected PDF labels receive
explicit provisional placements: `List → Set`, `Number → Quantity`,
`Predicate → Proposition`, and `Sentence → Proposition`. These are marked
provisional in the browser and data rather than being misrepresented as
PDF-derived edges. `Number` therefore sits in the abstract quantity branch,
near the truth-value branch without being made a child of `True` or `False`.

The projection contains 518 nodes and 517 primary edges, with 39 nodes having
alternate parents and 51 unary nodes. The [complete unary-node inventory](SUMO/unary-nodes.md)
is retained as a data reference, not a cleanup queue.

The reproducible extraction recipe is:

- download the PDF and record its URL and SHA-256 in
  [`snapshot-manifest.json`](SUMO/snapshot-manifest.json);
- convert it with `pdftocairo -svg` and `pdftotext -bbox`;
- run [`extract_pdf_edges.py`](SUMO/extract_pdf_edges.py) to map vector arc
  endpoints to PDF labels and measure each directed arc;
- run [`generate_sumo.py`](SUMO/generate_sumo.py) with `--pdf-graph`;
- for multiple incoming arcs, remove the longest repeatedly until one primary
  parent remains, retaining removed parents as alternate cross-links; and
- apply only the four explicitly marked provisional placements needed to keep
  `Entity` as the sole root.

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
