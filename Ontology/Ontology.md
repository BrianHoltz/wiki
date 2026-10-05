# 20 Questions Ontology

## Status

The original curated tree remains committed as `index.html`,
`20_questions_hierarchy.yaml`, and `generate_20q_hierarchy.py`. It contains
678 display nodes: 50 branches and 628 terminal categories.

The first standards-based experiment is now also committed:

- [`wordnet_20q.html`](wordnet_20q.html) — the browseable one-page profile;
- [`wordnet_20q.yaml`](wordnet_20q.yaml) — the projected tree;
- [`wordnet_20q_manifest.json`](wordnet_20q_manifest.json) — source IDs,
  glosses, frequencies, original hypernyms, and selected display parents; and
- [`generate_wordnet_20q.py`](generate_wordnet_20q.py) — the reproducible
  builder.

It uses Princeton WordNet 3.0 noun synsets. It selects the top 7,000
frequency-weighted noun synsets and adds their complete hypernym ancestry,
producing 8,957 display nodes: 3,774 branches and 5,183 terminal categories.
The selected source pool contains 82,115 noun synsets, of which 13,739 have
nonzero WordNet corpus-frequency counts.

The display tree chooses one deterministic presentation parent when WordNet
has multiple hypernym paths. That is a view projection, not a modification of
WordNet: all source hypernyms remain in the manifest.

## Practical scope and UI constraint

The useful target is **5,000–10,000 displayed nodes**, with the current 8,957
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
  infobox vocabulary, redirects, and interlanguage links. This is an implicit
  ontology assembled for navigation and editorial work, not one formal
  ontology.
- **Node count:** the English
  [Wikipedia statistics page](https://en.wikipedia.org/wiki/Wikipedia:Statistics)
  reports roughly 7.25 million articles and 2.6 million categories in its
  2026 snapshot.
- **Prominence proxy:** the same snapshot reports about 872 million article
  edits by 12.4 million users; article and category counts are also direct
  scale measures.
- **Fit:** excellent candidate source for familiarity and named-entity
  expansion, but category membership is inconsistent and often editorial,
  topical, or maintenance-driven.

### Roget’s Thesaurus

- **Origin:** Peter Mark Roget’s classification began in London in 1805 and
  was published in 1852.
- **Current status:** continuously republished in commercial and public
  editions; its class/division/section structure remains recognizable.
- **Node count:** six primary classes and more than 1,000 meaning-cluster
  branches; the eighth edition is reported to contain about 443,000 words.
- **Prominence proxy:** the edition scale itself is objective; the work has
  been continuously published since 1852 and remains a standard English
  thesaurus reference. See the
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

### Encyclopaedia Britannica and the Macropædia

- **Origin:** Encyclopaedia Britannica began in Edinburgh, Scotland, in
  1768. The 15th edition’s three-part structure, including the Macropædia,
  was introduced in 1974.
- **Current status:** Britannica is online; the final printed 15th edition
  ended in 2010 and the company focuses on digital publication.
- **Node count:** the Macropædia consisted of 17 volumes of long articles;
  the broader 15th edition had 32 volumes and 32,640 pages. These are
  editorial units, not ontology nodes.
- **Prominence proxy:** Britannica reports a roughly 40-million-word
  twentieth-century scale and has published continuously since 1768; see the
  [Britannica history](https://en.wikipedia.org/wiki/Encyclop%C3%A6dia_Britannica).
- **Fit:** useful as a high-quality familiarity and importance prior, not as a
  machine-readable noun hierarchy.

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

### Mozilla

There is no single broadly recognized, maintained “Mozilla Ontology”
comparable to WordNet, Wikidata, or SUMO. Mozilla has web-platform
vocabularies, browser schemas, extension manifests, and RDF-era projects, but
no canonical general-purpose noun ontology with a stable node count.

- **Origin/status:** Mozilla began as an open-source browser project in 1998
  and remains active; see the
  [Mozilla Manifesto](https://www.mozilla.org/about/manifesto/).
- **Node count:** not applicable for a general Mozilla ontology; any claimed
  number would refer to a particular schema or project.
- **Prominence proxy:** Mozilla’s browser/community reach is measurable, but
  that is not an ontology prominence metric.
- **Fit:** excluded as a canonical source unless a specific Mozilla schema is
  identified and its scope is justified.

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

The next useful improvements are a better question generator based on subtree
balance and a coverage report for ordinary game-answer lists. Wikidata,
FoodOn, and Wikipedia can then be tested as separately labeled enrichment
profiles, not silently merged into the WordNet ontology.
