# Ontology redesign proposal

Start with [the architectural rationale](architecture.md), then browse [the complete tree with definitions](ontology-tree.md). The [complete comparison](coverage-map.md) explains where every original record went.

The authoritative source is [ontology-proposal.json](ontology-proposal.json). It contains 555 canonical class records, 32 alternate superclass links, 46 cross-cutting class expressions, 20 typed predicate examples, split policies, dimensions, biological lineages, aliases, and source hashes. All 439 original records are mapped in [coverage-map.json](coverage-map.json); the baseline is preserved in [original-snapshot.json](original-snapshot.json).

The proposal is an is-a tree with an explicitly richer classification graph. No branch silently asserts that its children exhaust the parent or exclude each other. Role specifications and actual role bearers are distinct.

[Validation results](validation-report.json) report the exact checks and limitations. The maximum canonical depth is 13 edges; Organism is 5 edges from Entity, Human 12, and Corporation 6. All classes and expressions have definitions.

To verify or regenerate after editing the JSON, use Python 3 with its standard library:

```sh
python3 validate.py
python3 render.py
```

Read [the data-format notes](FORMAT.md) before making machine-assisted edits. [Stress-test cases](stress-tests.md) make the intended distinctions concrete. The source evidence archive contains the retrieved documents and taxonomy responses named in the proposal's source manifest; it supports provenance inspection without changing the original repository.

The existing GitHub repository was read only. Nothing was pushed, published, or changed there.
