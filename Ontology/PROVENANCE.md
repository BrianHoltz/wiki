# 20 Questions Ontology Provenance

## Current tree

The published 678-node tree is a curated, embedded baseline in
`generate_20q_hierarchy.py`. It is not currently imported from WordNet,
Wikidata, or another external ontology. Its 50 semantic branches, 628 terminal
categories, and suggested questions were authored for this project.

That makes the current tree useful as a prototype, but it also explains its
coverage gaps: familiar answers such as steak and salad can be absent even
when related ingredients or biological categories are present.

## Preferred standards-based direction

The first canonical source should be [Princeton WordNet](https://wordnet.princeton.edu/),
using a pinned WordNet release and noun synset IDs as stable identifiers.
WordNet is a good initial fit because it is:

- explicitly lexical, with familiar noun lemmas and synonym sets;
- organized by typed hypernym and hyponym relations;
- mature, documented, downloadable, and available through
  [NLTK's WordNet interface](https://www.nltk.org/howto/wordnet.html); and
- closer to a parlor-game vocabulary than a foundational ontology such as BFO
  or DOLCE.

[Wikidata](https://www.wikidata.org/) is a valuable second source for named
people, places, organizations, fictional entities, brands, and contemporary
concepts. It is much broader than WordNet, but its subclass graph is noisy,
cyclic, multilingual, and unevenly curated. It should initially enrich the
WordNet-based game profile rather than replace the noun backbone.

Specialized standards can fill measured gaps without changing the canonical
identity model. [FoodOn](https://foodon.org/) is a candidate for food and
prepared dishes; [GeoNames](https://www.geonames.org/) is a candidate for
geographic entities; and [Schema.org](https://schema.org/) can supply
practical web-facing categories. Each addition should remain source-labeled
and optional rather than silently merged into a hand-maintained taxonomy.

## Information-theoretic presentation

The source ontology should remain a graph or DAG exactly as published by its
maintainers. The 20 Questions tree should be a reproducible presentation
projection:

- Import source nodes, stable IDs, labels, and authoritative edges.
- Filter by a declared game profile, such as common nouns and familiar proper
  names, without deleting anything from the source.
- Select a small set of candidate roots and calculate each subtree's
  candidate mass.
- At each displayed branch, choose the available source split that most nearly
  balances the remaining candidate mass.
- Use deterministic tie-breakers, such as source order, synset ID, and
  frequency, so regeneration is stable.
- Give every displayed node one canonical presentation path, while retaining
  source IDs and alternate source edges as provenance metadata rather than
  inventing duplicate concepts.
- Generate suggested questions from source distinctions and declared
  attributes. A question is a view-level operation; it is not a new ontology
  edge.

This separates **what the source ontology says** from **how the game asks
about it**. The tree can therefore change as a game profile changes without
creating an untracked fork of the source ontology.

## Expansion decisions

Before importing a larger source, the generator needs explicit settings for:

- source and release version;
- allowed parts of speech and root synsets;
- familiarity or frequency threshold;
- treatment of proper names, brands, fictional entities, and technical terms;
- synonym policy, including whether lemmas are displayed separately;
- handling of polysemy and multiple hypernym paths;
- language and regional vocabulary;
- `unknown` and `partly` answers; and
- maximum candidate-set size and question-depth budget.

The first useful experiment is a WordNet-backed comparison report: measure
coverage of the current 628 terminal categories, identify additions such as
food and prepared dishes, and inspect ambiguous or low-frequency imports
before replacing the curated prototype.
