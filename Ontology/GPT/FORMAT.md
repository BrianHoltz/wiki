# Machine-readable format and maintenance contract

`ontology-proposal.json` is UTF-8 JSON and the authoritative edited artifact. All IDs are stable within this proposal. They retain many recognizable legacy spellings for easy cross-reference; labels are the presentation vocabulary. An ID is not an ontological axiom.

## Canonical classes

`nodes` is an ordered array. Every record requires:

| Field | Meaning |
|---|---|
| `id` | Unique ASCII class identifier. |
| `label` | Unique readable label. |
| `definition` | Concise definition of instances admitted by the class. |
| `node_kind` | Always `class`; the node is not an ordinary individual. |
| `primary_parent` | Exactly one existing class ID, or null for Entity only. |
| `alternate_parents` | Additional valid superclass IDs, never role or part-whole links. |
| `aliases` | Search/display vocabulary, not asserted equivalences of all word senses. |
| `definition_status` | `proposal_editorial`: definitions were authored for this proposal, not quoted authority. |

Nonleaf classes also have `child_policy`: the split's `axis`, `coverage`, `disjointness`, and `note`. All current splits are selective. These are review annotations, not exported logical union/disjointness axioms. `overlapping_ancestry` explicitly marks display compression. Optional `notes` explain sense limits. Optional `biology` records scientific name, independently expected name, source identifier, rank, retrieval date, source lineage, and validation scope. Do not infer extinct status from a record's absence. The source is a live retrieval frozen through hashes, not an invented release version.

Children are derived by collecting records whose `primary_parent` equals a node's ID. File order supplies the proposed display order. A parent edge always means universal instance inclusion. Alias spelling must not create extra class records.

## Defined classifications outside the tree

`class_expressions` contains noncanonical classes. Each requires a unique `facet:` ID, label, definition, expression, canonical entry, and status. A canonical entry is a navigation destination, not a claim that the expression is equivalent to that class.

An expression is either a class reference or an intersection of a `base_class` with restrictions:

- `instance_of`: additional class membership.
- `not_instance_of`: complement relative to the specified base, not an unrestricted universal complement.
- `satisfies_specification`: there exists a specification instance of the named specification class that the bearer satisfies in the supplied context.
- `all_members_satisfy_specification`: each admitted collection member satisfies the specification in context.
- `contextual_facet`: an identified domain criterion still requiring an operational interpretation. Its string is explanatory metadata, not executable code or a formal logical formula.

Expressions preserve important classifications without changing the primary kind route. All expression bases and referenced classes are validated. A context-bound specification can be unary once the context is fixed; an explicit application relation includes context as an additional argument.

## Predicates and formal levels

`predicate_instances` is a separate array of typed specification instances, identified by the `predicate:` namespace. `type_id` names a class in the tree. `arguments` specifies ordered names and range classes; `arity` equals the number of arguments. Unary examples have Property specification types; relation examples have arity at least two. `logical_features` gives only the stated features; a contextual comparator is not silently declared globally transitive over incompatible scales.

A downstream logical exporter must distinguish a class symbol from an object reifying its specification and from ordinary instances. It must distinguish an application of a property from membership in the class of property specifications. Property specification classes are not automatically OWL properties. Class-to-object reification needs an explicit bridge. Never introduce unrestricted comprehension or treat a universal class as an ordinary set of all classes.

`dimensions` holds orthogonal annotations, not primary class edges. An empty `values` array means an open domain, not an empty range. Context, interpretation, source, and perspective should be stored explicitly where required.

## Source coverage

`coverage-map.json` has one row per original ID with original label, treatment, targets, explanation, legacy definition, and all original child/alternate-parent edges. Targets may be canonical classes or defined class expressions. A split row may include broad navigation routes requiring an extra context criterion; it is not an assertion that the original extension equals the union of every target.

`original-snapshot.json` preserves the retrieved active data without semantic edits. Some source counts and direct-parent metadata are stale; validation computes actual incoming child edges rather than trusting those counts. In particular, the active source has six multiply-parented records, although its statistics report three.

`validate.py` is dependency-free. It checks data contracts, unique identifiers, one primary root, connectedness, acyclicity including alternate superclasses, definitions, expression references, predicate arities/ranges, complete 439-record coverage, source definitions/edges, intended taxon identities, ancestry, depth, and targeted category mistakes. It does not implement a general ontology reasoner or certify English definitions. `render.py` derives both Markdown outputs from the authoritative JSON sources.
