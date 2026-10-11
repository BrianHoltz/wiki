# Ontology critique and revised upper tree — Astra

## Summary

- **What:** a repository-informed critique of the incumbent Omniversal Ontology, GPT/Sol, the preserved Astra, Gemini and Claude Fable proposals, the subsequent Gemini and Claude critiques, and the imported and historical trees. The recommended upper tree is a bounded design target, not an instruction to replace the incumbent wholesale.
- **Conclusion:** repair identity collisions, predicate typing, and the distinction between the semantic graph and its navigation projection before merging branches. GPT supplies the strongest executable starting point, not a demonstrated winning ontology. Astra supplies useful distinctions but needs narrower claims and clearer names. Neither the number of mapped labels nor agreement among models establishes semantic correctness.
- **How:** direct document and code inspection; traversal of every active browser graph; execution of the seven-browser regression suite; GPT validation and controlled mutations in a temporary directory; archive/hash and taxonomy-evidence checks; and targeted consultation of external specifications and primary papers.
- **Where:** [BrianHoltz/wiki](https://github.com/BrianHoltz/wiki), inspected at [38b5cc3c58b47126217fbe8ee10d6995eca298e0](https://github.com/BrianHoltz/wiki/commit/38b5cc3c58b47126217fbe8ee10d6995eca298e0), not the enclosing Documents repository. The worktree was clean when inspected.
- **Who:** an AI assistant using Copilot SDK in VS Code. “Astra” is the review label and identifies the preserved starting proposal supplied for this round; the exact serving model version and reasoning setting are not available to this review. Session: `159782e3-b109-4871-ad5e-1c270433061f`.
- **When:** research and review on 2026.10.11.Sun. External retrievals and executable results below belong to that date.
- **Write boundary:** this document is the only requested repository change. [UpperOntologyAstra.md](UpperOntologyAstra.md), other proposals, ontology data, generators, tests, and source material remain unchanged. The revised proposal is contained here.

**Concurrent revision:** during drafting, another session committed [ab558412d3a75f538d9c60b67f4b2b5796071031](https://github.com/BrianHoltz/wiki/commit/ab558412d3a75f538d9c60b67f4b2b5796071031), changing only paragraph wrapping in [Ontology.md](Ontology.md). A token-for-token comparison after whitespace normalization confirmed no wording changes. The semantic and executable findings remain anchored to the inspected baseline above; that concurrent formatting work was not reverted.

## Contents

- [Scope and inspection inventory](#scope-and-inspection-inventory)
- [Executed evidence and its limits](#executed-evidence-and-its-limits)
- [Consequential findings](#consequential-findings)
- [Assessment of every candidate](#assessment-of-every-candidate)
- [Property and Relation reconciliation](#property-and-relation-reconciliation)
- [Meaning-preserving mappings and human audit](#meaning-preserving-mappings-and-human-audit)
- [Evidence](#evidence)
- [Recommended upper tree](#recommended-upper-tree)
- [Departures from the preserved Astra proposal](#departures-from-the-preserved-astra-proposal)
- [Unresolved choices and discriminating tests](#unresolved-choices-and-discriminating-tests)
- [Work log](#work-log)

## Scope and inspection inventory

### Starting position and evaluation standard

[Prompt 2](CriticPrompt.md) governs this artifact. It requires a critique of the project rather than adoption of its conclusions, a revised tree only through three subclass edges below Entity, and preservation of the initial proposals. The first paragraph of [UpperOntologyAstra.md](UpperOntologyAstra.md) discloses prior project exposure. I preserve that disclosure: Astra is not an independent blind sample. This review also uses both repository-informed critiques; its agreement with either is not independent corroboration.

The relevant project purpose is the broader organization of knowledge described in [OntologyDesignMemoranda.md](OntologyDesignMemoranda.md#1-project-goal), not merely question efficiency in a guessing game. The memoranda's cautions about uniform edges, type/instance distinctions, single-parent navigation, and unearned exhaustive partitions are useful requirements to test. Their preferred conclusions remain contestable.

An edge is defective when a counterexample violates its declared inclusion or typing. A navigation choice is not defective merely because another genuine superclass would be more useful. A restricted sense is not a defect merely because another ontology gives the same word a broader sense. An undefined term, an unsupported coverage claim, a false inclusion, and a disputed metaphysical commitment are different findings.

### Material actually inspected

| Material | Inspection performed | Evidential scope |
| --- | --- | --- |
| [CriticPrompt.md](CriticPrompt.md) | Both prompts and artifact/write requirements | Complete task contract |
| [Ontology.md](Ontology.md), [OntologyDesignMemoranda.md](OntologyDesignMemoranda.md) | Principles, goals, upper-ontology discussion and definitions, formal-level and kind/role arguments, implementation, projection, count and publishing policies; section inventories for the remaining prior-art survey | Project commitments and conflicts, not independent verification of every external survey claim |
| [UpperOntologyAstra.md](UpperOntologyAstra.md) | Upper definitions, split policies, architectural arguments, arity derivations, stress tests, alternatives, open decisions and sources | Starting proposal and departures |
| [UpperOntologyGemini.md](UpperOntologyGemini.md) | Entire short proposal | Initial Gemini candidate |
| [UpperOntologyClaudeFable.md](UpperOntologyClaudeFable.md) | Root and admission rules, formal ties, entire upper tree and definitions, principal split arguments, Property/Relation analysis, roles, capabilities, normative and object/process stress tests, navigation policy | Initial Claude candidate; not a claim to have independently rechecked every cited work |
| [CritiqueByGemini.md](CritiqueByGemini.md), [CritiqueByClaudeFable.md](CritiqueByClaudeFable.md) | Inventories, consequential findings, mappings, reconciliation arguments, revised upper trees and definitions, policies, departure and decision sections | Additional candidates and arguments, not authorities or substitutes for examining data |
| [GPT/README.md](GPT/README.md), [GPT/architecture.md](GPT/architecture.md), [GPT/FORMAT.md](GPT/FORMAT.md), [GPT/stress-tests.md](GPT/stress-tests.md) | Design and maintenance contracts | Intended GPT/Sol interpretation |
| [GPT/ontology-proposal.json](GPT/ontology-proposal.json), [GPT/coverage-map.json](GPT/coverage-map.json), [GPT/original-snapshot.json](GPT/original-snapshot.json) | Parsed completely; graph, IDs, mapping coverage, all predicate signatures, upper classes and disputed definitions examined; selected mapping decisions read in detail | Structural completeness is tested; no claim of individually endorsing all 555 English definitions or all 439 mapping judgments |
| [GPT/validate.py](GPT/validate.py), [GPT/render.py](GPT/render.py) | Validation logic, output side effects, Markdown/browser projection and packaging paths | Executable-contract and information-loss analysis |
| [ontology.json](ontology.json), [sumo.json](sumo.json), [SUMO/ontology.json](SUMO/ontology.json), [GPT/ontology.json](GPT/ontology.json), [Rogets/ontology.json](Rogets/ontology.json), [Propaedia/ontology.json](Propaedia/ontology.json), [HumanKnowledge/ontology.json](HumanKnowledge/ontology.json), [Wikipedia/ontology.json](Wikipedia/ontology.json) | Complete programmatic node/edge traversals; root, reachability, references, definitions and incoming displayed edges counted; selected content inspected | All seven active browser datasets, including the incumbent's duplicate data file |
| [SUMO/overlay_canonical.py](SUMO/overlay_canonical.py), [SUMO/generate_sumo.py](SUMO/generate_sumo.py) | Upper definitions, duplicate-ID flattening, overlay combination and PDF parent selection | Specific generation mechanisms; not a full reconstruction of the source PDF |
| [Wikipedia/generate_categories.py](Wikipedia/generate_categories.py), [HumanKnowledge/generate_human_knowledge.py](HumanKnowledge/generate_human_knowledge.py), [Propaedia/generate_propaedia.py](Propaedia/generate_propaedia.py) | Category snapshot construction, book-outline parsing, and Propædia outline/question generation | Source hierarchy semantics and definition provenance |
| [index.html](index.html), [test_browser.js](test_browser.js) | Shared renderer, normalization, search, lineage, count and loading logic; regression harness and relevant assertions | Executed JavaScript behavior in the repository's simulated browser environment |
| [WordsToCategorize.md](WordsToCategorize.md), [Rogets/crosswalk.json](Rogets/crosswalk.json) | Upper and difficult-word tables read; all table rows parsed; crosswalk method, target and sample senses examined | Coverage-accounting method, not adjudication of every lexical sense |
| [20_questions_hierarchy.yaml](20_questions_hierarchy.yaml), [v2_20_questions_hierarchy.yaml](v2_20_questions_hierarchy.yaml), [wordnet_20q.yaml](wordnet_20q.yaml), [v2_manifest.json](v2_manifest.json), [wordnet_20q_manifest.json](wordnet_20q_manifest.json) | Upper branches and profile/selection metadata | Historical proposals and enrichment profiles; lower leaf inventories not exhaustively reviewed |
| [v1010/ontology.json](v1010/ontology.json), [v1010/manifest.json](v1010/manifest.json), [snapshot-manifest.json](snapshot-manifest.json) | Active/snapshot byte comparison, nine snapshot file hashes, root manifest claims | Snapshot integrity and stale provenance |
| [GPT/source-evidence.zip](GPT/source-evidence.zip), [GPT/ontology-proposal-package.zip](GPT/ontology-proposal-package.zip), [GPT/deliverable-manifest.json](GPT/deliverable-manifest.json) | Archive membership, source hashes, package/local byte comparisons; all 59 source-identified taxa independently matched to archived XML names and lineage IDs | Evidence preservation, not blanket scientific certification |
| All seven browsers' entity-count and species-count sidecars | Every key checked against its browser node IDs; sample scope/definition data and project count policy read | Referential integrity only; external population estimates not recounted |
| Wiki [index.md](../index.md), [navigation.md](../navigation.md), [Makefile](../Makefile), ignore rules and tracked-file inventory | Project discovery and publication boundary; repository-wide Markdown search for ontology references | No additional independent ontology proposal discovered outside the ontology project |

### Omissions and access limits

I did not read every unrelated wiki essay, every lower historical YAML leaf, every Wikipedia category, the entire external biological and product-taxonomy survey, or every extracted source document in the evidence archive. Generated copies were not reviewed as independent proposals. The large GPT generated Markdown tree and coverage table were evaluated principally through their authoritative JSON and renderer.

I did not regenerate ontology data, renderers, counts or site output; fetch a complete live Wikipedia or NCBI dump; compare every extracted PDF arc with the original drawing; reconstruct all past commits; or run a visual browser, accessibility audit, OWL reasoner, or general satisfiability proof. Browser findings below concern the actual embedded JavaScript run with the repository's DOM/fetch simulation, not screenshot-based verification. Frozen biological provenance is checked more strongly than the ontology's complete phylogenetic correctness.

The enclosing Documents repository's instruction-file link points to an unavailable target. No tracked local AGENTS file or instruction file was found in the wiki repository inventory. The available task and project write restrictions were followed. No deployment or remote push is part of this critique.

## Executed evidence and its limits

<a id="e-execution"></a>

The following are results obtained in this review, not results copied from another model's report.

| Check | Observed result | What this establishes |
| --- | --- | --- |
| Test-tool discovery for [test_browser.js](test_browser.js) | The test integration found no registered tests | No pass was inferred; the repository's standalone command was used instead |
| `node Ontology/test_browser.js`, from the wiki directory | “Ontology browser tests passed for all seven browsers.” | Existing regression assertions pass |
| `python3 Ontology/GPT/validate.py <temporary-copy-directory>` | 393 checks passed; 555 classes; 554 primary edges; 31 alternate superclass edges; 46 class expressions; 20 predicate instances; all 439 original records mapped | The validator accepts the frozen package under its implemented checks |
| Six isolated invalid mutations | Self-parent cycle, missing definition, dangling parent, missing mapping, wrong predicate arity, and wrong expected taxon name all rejected | These rejection paths work; this is not a rerun of every possible graph-cycle case |
| Additional mutation: change the unary predicate's `type_id` to `Object` | Accepted | A real gap in predicate-family validation |
| Additional mutation: define Number as “A physical rock with mass.” without changing graph structure | Accepted | Nonempty prose and selected counterexample checks do not entail semantic correctness; this limitation is expected, not itself a promised natural-language reasoning feature |
| GPT source archive | All 14 source-manifest entries matched their archived hashes; all 59 source-identified taxon records matched archived scientific names and lineage-ID sets | Actual provenance inspection beyond self-comparison of the embedded name fields |
| GPT deliverables | All 19 deliverable-manifest entries matched hashes; the 24-member package had no mismatches with corresponding local files | The inspected package and local deliverables agree |
| v1010 snapshot | All nine named file hashes matched; active ontology, root `sumo.json`, and snapshot ontology were byte-identical | The frozen copy is a duplicate baseline, not a separate semantic candidate |
| Count references | No dangling ID in any of the fourteen browser sidecars | This does not prove that a population count measures the right kind of thing |

The validator writes a report. It was therefore run against disposable copies outside the repository; those copies were removed. The repository's source files were not rewritten to obtain these results.

### Graph and presentation measurements

| Dataset | Nodes | Stored displayed child edges | Nodes reached from declared roots | Nonempty definition fields |
| --- | ---: | ---: | ---: | ---: |
| Incumbent | 439 | 444 | 439 | 365 |
| SUMO browser | 518 | 517 | 514 | 435 |
| GPT browser | 555 | 554 | 555 | 555 |
| Roget browser | 1,144 | 1,138 | 1,144 | 1,000 |
| Propædia browser | 228 | 218 | 228 | 51 |
| Human Knowledge browser | 103 | 95 | 103 | 0 |
| Wikipedia browser | 12,657 | 12,655 | 12,657 | 12,657 |

These counts distinguish fields from genuine definitions and declared roots from roots reconstructed by the renderer. No missing child IDs or reachable child-edge cycles were found in these traversals. I do not infer acyclicity of the entire original Wikipedia graph or every source graph with alternate edges from this result.

The incumbent has **six**, not the reported three, nodes with multiple stored displayed parents: `Artifact`, `GeopoliticalArea`, `Government`, `Group`, `Language`, and `Organization`. Running its actual renderer produces **487 list rows for 439 distinct IDs**, and `descendantCount(Entity)` returns 486 rather than the 438 distinct other nodes. These are repeated paths, not additional concepts.

The SUMO dataset has a disconnected `GeoPoliticalArea` branch containing City, Nation and Province. Its declared root is Entity; the browser's normalization discovers **two** roots, Entity and `GeoPoliticalArea`, and renders 519 rows for 518 IDs because the differently cased `GeopoliticalArea` also has two displayed parents. Thus the four records are not invisible in the actual browser: they are outside the promised single-Entity lineage. That qualification matters.

## Consequential findings

The order reflects consequences for trustworthy interpretation and reconciliation. “Semantic” findings are relative to stated definitions. “Contract” findings concern actual data or executable behavior. “Design” findings are choices requiring an argument, not errors proved by terminology.

### Duplicate identifiers collapse different meanings before review

**Contract and semantic defect.** [SUMO/overlay_canonical.py](SUMO/overlay_canonical.py) declares `Function` both as a mathematical input/output rule and as a use or intended activity. It declares `Role` and `Status` in both the social and Property branches. Its `flatten` routine keeps the first record for an ID, records a further parent, and does not retain the second definition or append a second displayed child when the ID is already present.

In [ontology.json](ontology.json), `Function` therefore has the mathematical definition and `Property` as an alternate parent. The reusable teleological definition is gone. Role and Status likewise retain social-position definitions but inherit the alternative Property classification. A general mathematical function need not be a unary truth-valued condition; a person's office-holding is not automatically a reusable unary specification. This is not harmless multi-inheritance.

**Remedy:** reject conflicting definitions at import; distinguish mathematical function, teleological assignment, role specification, role occupancy and institutional office before flattening. An explicitly shared ID may merge parents only after meaning agreement is established.

**Cost:** identifiers and mappings need sense-qualified replacements. Keeping every old spelling as an active ID is less important than preventing the old ID from silently changing what it denotes. Preserve the original record and route readers to its sense choices.

### The incumbent does not have the single-parent projection it claims

**Contract defect.** [Ontology.md](Ontology.md#principles) promises one visible primary parent. The [shared renderer](index.html) recursively renders every `children` edge while constructing a separate `parentOf` map by repeatedly overwriting the parent for a child. In the observed order, Organization's focus parent is InstitutionalEntity even though it is also rendered under Group. Duplicate HTML IDs, repeated descendants and a different focus ancestry are predictable consequences, confirmed by the measurements above.

**Counterexample:** the same Organization record appears on two full-tree routes but has one last-write-wins lineage. The browser's 486 Entity descendants cannot mean 486 distinct descendant concepts.

**Remedy:** retain all semantic parents but derive an explicit, deterministic primary-parent map before rendering. Validate exactly one incoming primary edge per nonroot, primary-root reachability, unique rendered IDs, and restoration of the selected route. Report distinct-node counts separately from path-occurrence counts.

**Cost:** some familiar routes move to “also a” links or portals. The semantic links must not be deleted merely to make the renderer pass. The existing suite is useful but its passing result does not cover these invariants.

### The root arity vocabulary cannot classify ordinary entities safely

**Semantic ambiguity with concrete downstream defects.** The incumbent defines Realized entity and Abstract entity as entities taking no arguments, separated by embodiment; Property takes one argument and Relation more than one. [The active root](ontology.json) contains all four, whereas [the principles](Ontology.md#principles) foreground only the realized/abstract distinction.

Mixing axes is not by itself a contradiction. A deliberately defined piecewise partition could first separate applicable conditions from non-applicable subjects, then subdivide the latter by embodiment. The decisive problems are that arity is not defined for ordinary subjects, “takes arguments” also describes non-truth-valued functions, and children do not consistently satisfy the stated meanings.

A cup's mass feature depends on a cup; that dependence does **not** make the feature a function accepting the cup as an argument. Both other critiques use versions of this inference in attacking the incumbent root. The attack repeats the confusion it is intended to diagnose. Conversely, a function returning a real number is not a relation specification just because it accepts two inputs.

**Remedy:** reserve arity for declared condition specifications, distinguish applicability from dependence, and make any embodiment classification a separate, explicitly interpreted choice. [The reconciliation below](#property-and-relation-reconciliation) supplies operational tests.

**Cost:** the attractive four-label root loses its appearance of a self-evident exhaustive division. A realist predicable ontology remains an alternative; a specification ontology must not masquerade as a proof that all properties are authored descriptions.

### Specific incumbent inclusions fail their own readings

**Semantic defects or unresolved sense conflations.** These examples are checked against [ontology.json](ontology.json), not inferred from another formal ontology.

| Record or edge | Counterexample or incompatible reading | Bounded remedy | Cost or strongest objection |
| --- | --- | --- | --- |
| `Person` under SocialEntity under AbstractEntity; Person is “An individual human being considered as a social participant” | The stated human bearer is embodied. Considering that bearer socially does not remove its embodiment | Give human-person bearers an appropriate object/human route; separately represent personhood criteria and legal status | Broader philosophical personhood need not be identical to biological humanity; do not silently generalize this local definition |
| `Event` under SocialEntity under AbstractEntity | A bounded social occurrence has temporal occurrence; its record or event type is a different subject | Put occurrence senses under Occurrence and their descriptions under Content | Historical-event identity and event-type identity still need policies |
| `AstronomicalBody` under Region | Its definition includes stars, galaxies and constellations. A star is not merely a spatial extent; a constellation's sky region is not a stellar body | Split body, aggregate and conventional sky-region senses before choosing parents | A single familiar label hides multiple scientific and navigational usages |
| `GeopoliticalArea` under Agent and GeographicArea | A territory need not intend anything; the governing polity may act. Its definition also allows persistence through border change | Separate polity, jurisdiction and geographic extent | A relational or institutional territory account can be defensible; do not merely assert all territories are fixed coordinate regions |
| `Fruit` under Food; Food is food fit for humans, Fruit is botanical | An inedible botanical fruit is not food fit for humans | Retain botanical fruit by anatomy; add a food-use intersection or role classification | Culinary fruit has a different sense and needs its own route |
| Mammal and Bird under `Warm-BloodedVertebrate` | Thermoregulation is not the lineage connecting these clades; treating the grouping as monophyletic conflicts with project policy | Retain the physiological classification outside the ancestry backbone; use source-backed ancestry | Source choice and extinction treatment remain substantive work |
| Virus under MicroOrganism under Organism | The project's own biological specification requires an acellular branch; the inherited definition explicitly calls a virus an Organism | Decide and implement the cellular-organism sense plus separate acellular infectious entities | “Organism” has broader competing usages; this is a project-profile decision as well as a scientific modeling issue |
| Mineral under Mixture | The broad inherited definition includes chemically definite mineral substances as well as sand, coal and petroleum | Split mineral species/material senses from broad geological mixtures | Simply moving the existing broad label does not preserve every original example |
| Language under LinguisticExpression and RepresentationalEntity | A language system is not one expression in that system | Separate language/notation system, expression type, inscription and interpreted content | Formal languages can be modeled as sets of expressions; that still does not make the set an expression |

For biology, the live NCBI lineages inspected contain Sarcopterygii in the human lineage and Dinosauria/Theropoda in the bird lineage. That corroborates those placements in the chosen source. NCBI's own disclaimer warns that its database is not the final authority for nomenclature or classification.[†](#e-biology)

### GPT has real predicate-parent mismatches despite explicit signatures

**Semantic and validation defects.** In [GPT/ontology-proposal.json](GPT/ontology-proposal.json), ParticipationRelation is defined as connecting a participant to an occurrence and participation context. Yet `predicate:has_quality` has arguments bearer, quality instance and context, and `predicate:satisfies_role` has bearer, role specification and context. Neither signature contains an occurrence argument. The latter is satisfaction/classification; the former is feature bearing.

RepresentationalRelation connects a representation to content, referent or encoding convention. `predicate:has_quality_value` instead connects a quality instance to a value and scale context. A cup's particular mass is not automatically a representation. `predicate:has_arity` is typed MathematicalRelation, whose definition connects mathematical objects, but its first argument is PredicateSpecification, a class not declared to consist entirely of mathematical objects.

These are stronger findings than “the relation list feels flat.” Each has an actual typed record against which the parent's definition can be tested.

**Remedy:** use bearing, satisfaction, valuation and metamodel-description families with appropriate definitions; or explicitly broaden and rename the existing families. Keep the same relational meanings rather than turning quality bearers into occurrences to appease a validator. Check that signatures and examples satisfy family conditions.

**Cost:** a family taxonomy is not just labels over identical tuples. Some checks require reviewed semantic contracts or formal axioms, not range-name matching alone.

The additional mutation in [the execution record](#executed-evidence-and-its-limits) exposes a separate mechanical gap: the validator accepts a unary predicate whose type is Object. Its arity check distinguishes Relation descendants from everything else and treats the latter as eligible unary types. Require positive membership in Property or Relation ancestry, validate the type reference before asking for its ancestry, and test both valid and invalid family assignments. This is a proposed repair, not an edit made in this review.

### GPT preserves source accounting more strongly than meaning

**Contract strength with semantic limits.** [The coverage map](GPT/coverage-map.json) contains all 439 source records, including their definitions and child edges. Its source definitions also match the inspected active definitions. The four `merged_alias` records are `ArtiﬁcialLanguage`, `Certiﬁcate`, `Coorporation`, and `Senctence`. They are not mathematical-model mergers.

The [Gemini critique](CritiqueByGemini.md#4-assessment-of-existing-mappings-crosswalks-and-coverage) claims that PhysicalSystemModel and MathematicalModel were merged and that Weapon was removed into a facet. Both claims are false for the inspected package: PhysicalSystemModel remains a subclass of MathematicalModel, each has its own record and mapping, and Weapon remains a Device subclass with a design-purpose definition. Its 340 `revised` rows are not 340 independently demonstrated category-error corrections.

There is still a real migration hazard. An old Food record for edible bearers maps partly to a Food class of specifications; Person maps partly to personhood specifications and partly to qualified bearers; Quality maps to several senses. These are useful disambiguations, but reusing a familiar ID must not imply extensional equivalence or safe automatic migration of old instance assertions.

**Remedy:** separate record-accounting status from a typed mapping relation, with explicit source sense, target sense, instance-migration rule, residual ambiguity and decision status. A split is not a list of interchangeable replacement IDs.

**Cost:** some old assertions need human sense selection. That is more honest than declaring them all migrated because every row has a nonempty `targets` array.

### GPT's social and geographic identity conditions need strengthening

**Design ambiguity, not all-or-nothing rejection.** [GPT's Collection](GPT/ontology-proposal.json) is individuated by members, SocialGroup is a collection constituted by social recognition or interaction, and Organization is a social group with an enduring structure. A member-turnover example reveals missing persistence rules. It does not prove that every collective must be an extensional set: a membership-organized collective can persist while its membership changes.

**Remedy:** distinguish extensional membership identity from membership governed by an enduring rule/history. Prefer SocialObject for institutional organizations when its persistence rule carries the explanation; use membership relations to collectives. Keep informal groups available. **Cost:** neither “set of members” nor “social object” alone determines whether a split or merger preserves the organization.

Likewise, Hole and Room are SpatialRegion subclasses. A moving ring or room aboard a ship requires a host-relative identity/frame, but GPT's Region definition says “individuated by an extent rather than by what occupies it”; it does not explicitly require absolute immobility. A host-relative region account is possible. **Remedy:** choose between a cavity feature and a host-relative site, state the frame and persistence rule, and distinguish the region occupied at a time. **Cost:** multiple related subjects may be required. The validator's “Room and hole denote spaces” assertion should be a named profile commitment, not presented as a general theorem against feature accounts.

### Depth compression preserves inclusion but can misrepresent immediate ancestry

**Navigation issue with a testable contract.** [GPT/architecture.md](GPT/architecture.md) deliberately places Human directly under Ape while retaining Great ape as an alternate superclass and fuller ancestry in data. [GPT/validate.py](GPT/validate.py) enforces a 14-edge ceiling.

Human is an ape; this edge is not a false subclass inclusion. The problem is presentation: Human and Great ape can appear as peers, and a fixed ceiling makes a display preference constrain future ontology maintenance. The claim that all scientific provenance was lost is false; the archived lineage evidence and alternate ancestry survive and were checked.

**Remedy:** keep adopted immediate semantic ancestry separate from a compressed navigation route; mark skipped ancestors and show a complete semantic breadcrumb on demand. Report depth rather than reject otherwise valid classifications for exceeding 14. **Cost:** a reader must be able to distinguish immediate child from compressed descendant. Prompt 2's three-edge reporting boundary is not a global ontology-depth limit.

### Schema richness does not reach the browser

**Presentation and contract defect.** [GPT/render.py](GPT/render.py) exports IDs, labels, definitions, children, alternate parents, aliases and notes, but not class expressions, predicate instances, child policies or most formalization metadata. The [shared renderer](index.html) searches only IDs and labels and does not expose the exported aliases, alternate-parent list or notes.

The executed search for `facet:FoodBearer` returns zero matches. This is not proof that food is absent from GPT's semantic proposal; it is proof that its off-tree classification is not a browser destination. Aliases such as “Biological object” for BioticObject are also not searched by the implemented search expression.

**Remedy:** keep the small primary tree, but expose typed “also a,” “classified by,” alias and facet routes; show predicate signatures and split policies in inspectable notes. Render expression destinations as evaluated or defined classifications, never as silent assertions that their members are specifications.

**Cost:** search results need sense/type indicators. A universal lossless dump into each row is not required; the browser needs an inspectable route to the semantic record. Existing lineage and toggle behavior should remain covered by regression tests.

### Imported trees are useful for different reasons

**Scope distinction, with specific implementation defects.**

- **SUMO projection:** [generate_sumo.py](SUMO/generate_sumo.py) chooses the shortest measured incoming PDF arc, then a lexical tie-break, and adds four named provisional placements. That can be reproducible navigation; drawing geometry is not an argument for essential parenthood. The `GeoPoliticalArea`/`GeopoliticalArea` split and dual roots are an additional import/output defect, not a criticism of official SUMO. Preserve original spellings and source edges, reconcile any typo only with evidence, and test normalized root reachability. Cost: source-faithful raw data and a repaired projection need distinct identities.
- **Roget:** [the crosswalk](Rogets/crosswalk.json) explicitly uses exact normalized title or noun-phrase matches against a retired “curated v1” profile with 628 leaves. Its Unsubstantiality entry matches “air” to physical material air. That is a concrete lexical-match counterexample: metaphorical “thin air” is not atmospheric matter. Use the 1,000-concept thesaurus as a sense-candidate source, not an equivalence engine. Cost: source passages and sense adjudication must accompany matches.
- **Propædia:** [the generator](Propaedia/generate_propaedia.py) creates “Suggested question” strings. The active data has 51 such definition fields; the browser nulls all 51 but still displays a summary claiming 51 definitions. The hierarchy is an outline of knowledge, not a universal subclass tree. Keep outline relations and source labels, place prompts in a separate field if retained, and count genuine definitions. Cost: less apparent definition coverage, greater honesty.
- **Human Knowledge:** [the importer](HumanKnowledge/generate_human_knowledge.py) preserves a book outline in 103 records and supplies no definitions. Treat its chapter hierarchy as subject organization and a domain-coverage checklist. A chapter about physics is not a superclass of every physical thing. Absence of definitions is a declared limitation, not evidence that the outline is malformed.
- **Wikipedia:** [the category importer](Wikipedia/generate_categories.py) produces a bounded source snapshot; the active browser preserves a projected forest and alternate-parent data. Its 12,657 “definitions” are snapshot-depth/subcategory notices, not discriminating concept definitions. Category inclusion can express topic, administration or association. Preserve relation type and cutoff metadata, display these strings as source notes, and do not compare this definition count with GPT's 555 authored definitions. Cost: no convenient universal “coverage score.”
- **Historical v1/v2:** the upper YAML branches organize guessing questions and mix organism, biological part/product, origin and purpose. The v2 “WordNet candidate expansion” and “NCBI life taxonomy candidates” branches are workflow groupings, not kinds of living things. They are useful reservoirs of everyday nouns and prior decisions, but not competing validated upper ontologies. Preserve them as historical profiles rather than treating every candidate as an accepted addition.
- **WordNet:** the [manifest](wordnet_20q_manifest.json) identifies a frequency-selected, root-connected WordNet 3.0 noun profile plus retained ancestry. Sense IDs and glosses are valuable. Selection by frequency and generic-branch exclusion is a scope decision, not completeness. Lexical hypernymy also does not settle the project's distinction between a property universal, condition specification, quality instance and word.
- **v1010:** it is a checked frozen duplicate of the incumbent, not independent confirmation of that tree.

### Coverage and provenance claims need versioned meanings

[WordsToCategorize.md](WordsToCategorize.md) contains 1,040 parsed data rows with 1,117 check-marked cells. These numbers describe the matrix, not 1,117 meanings correctly classified. “Character” can mean a written sign, a literary subject or a trait; “function” can mean a mapping or assigned purpose; “state” can mean a polity or an obtaining condition. A single check mark cannot certify all senses. A blank “body” cell does not prove that material bodies lack a defensible home.

The [root snapshot manifest](snapshot-manifest.json) reports 530 nodes and 533 edges for a derived artifact whose active duplicate contains 439 nodes and 444 edges, and describes an older upper overlay. [GPT's README](GPT/README.md) and [architecture](GPT/architecture.md) say 32 alternate superclass links; the data and validator yield 31. These are stale contract claims, not reasons to distrust every archived source.

The [Gemini critique](CritiqueByGemini.md) names `7ad197d` as its inspected revision; that is not the wiki revision used here. The [Claude critique](CritiqueByClaudeFable.md) says the informed Gemini critique existed only in the working tree at its inspection. Git history for the inspected revision includes `aa4bebd`, “Update Gemini critique with repository-informed revision.” That historical statement must not be reused as a description of this review's baseline.

**Remedy:** regenerate manifests from named authoritative inputs; put baseline revision and source hashes on each mapping and published view; distinguish source-graph counts, projected-edge counts, unique concepts, genuine definitions and evaluated senses. Preserve dated review statements rather than editing previous reviews to make them appear current.

**Cost:** honest provenance produces more than one number. The count sidecars already distinguish population scope from descendant counts; retain that useful separation, but review count mappings after any sense change.

## Assessment of every candidate

Shared data and mapping issues above are not repeated as independent findings for every generated copy.

### Incumbent Omniversal Ontology

**Preserve:** familiar labels, the social and mathematical candidate inventory, source-linked descendants, count scopes, regression-tested browsing interactions, alternate-classification intent, and the stated biological acceptance criteria.

**Do not preserve unexamined:** the arity/embodiment root definitions, first-definition-wins identifier collisions, Property's mixture of specifications/features/values, actual people and events classified as unembodied merely because they are socially considered, and the equation of the stored DAG with a one-parent display tree.

The incumbent is a valuable reference inventory and migration baseline. It is not a sound set of class axioms simply because it is canonical.

### GPT/Sol

**Preserve:** class/specification/instance separation in the data contract; explicit scope disclaimers; off-tree defined classifications; source definitions and edges in coverage rows; corrected biological routes and archived evidence; units and content/carrier distinctions; and executable validation.

**Revise:** predicate-family membership and the unary-type validation hole; assignment-valued “properties”; the spec/class bridge; semantic-ID migration; missing browser routes; persistence policies for collections, organizations and host-relative regions; and depth as a reporting metric rather than an ontology invariant.

The Realized/Abstract routes are expressly selective and do not assert a completed partition. They are therefore not refuted by a counterexample to an exhaustive concrete/abstract metaphysics. Their remaining cost is the unresolved identity criterion for borderline social, formal and informational subjects. Moving every class into Astra's six routes would not by itself resolve it.

### Preserved Astra proposal

**Preserve:** admission versus existence versus denotation versus satisfiability; separation of bearer, feature, value and specification; explicit arity derivations; role occupancy versus office; unrestricted social/mental discussion without an automatic materialist reduction; explicit sibling policies; and a full-path depth boundary.

**Revise or narrow:**

1. **Predicate under Content needs an explicit specification label.** Calling all such instances “properties” invites the inference that mind-independent universals are content. Astra explicitly leaves universals open, so the inference is not its stated doctrine, but the label overpromises. Rename the node and children without claiming to eliminate universals.
2. **Quality-space region and Value need an identity bridge and a primary route.** Overlap is allowed, so two homes are not a contradiction. The unexplained equality between a scale point, a measured magnitude, a numeral and a value record is the risk. Treat quality spaces as mathematical structures; give determinations one primary route and distinguish their encodings.
3. **Subject competes with constitution-based Object children.** It is a valid overlapping class if its definition is met, not a false edge. For this project's primary menu, agency and experience deserve cross-cutting classifications rather than an obligatory third constitution route. Nonphysical subjects are not thereby prohibited.
4. **Capability and operative function are valid narrow subclasses only under the declared reading.** A task-assessed disposition can be a capability; an assigned function can survive loss of an operative capacity. The adjective “operative” protects Astra's edge, but the two labels are not an exhaustive split of disposition and need not occupy the primary menu.
5. **Field, law, absence and universal cases remain open.** An open root avoids a forced false inclusion but does not earn a claim of complete coverage. The unresolved set must be visible to the human reviewer.

Unlike the Claude critique, I do not reject Physical process, Mental process and Social process merely because they are also useful domain facets. “A process constituted by mental activity” is a genuine process subtype. “Whatever psychology studies” is a topic route. Their difference is the definition and edge semantics, not the presence of the word “mental.”

### Preserved Gemini proposal

**Preserve:** the effort to distinguish continuants, occurrences and dependent features; explicit property/relation arity; separate content and carriers; and recognition that institutional subjects need more than an inventory of atoms.

**Defects under its own definitions:**

- ConcreteEntity includes entities essentially tied to spatiotemporal causal powers. IntentionalEntity includes cognition-dependent institutions and content. The proposal nevertheless declares these root children disjoint. A causally effective intentional institution satisfies both broad descriptions unless different subjects or narrower criteria are explicitly introduced.
- Occurrent “never exists completely at a single instant,” but its TemporalBoundary child is a zero-duration instantaneous occurrent. The parent's universal condition excludes the admitted child.
- AbstractEntity necessarily lacks intentional genesis and exists identically across possible worlds. Placing every predicate and mathematical entity there makes substantial modal and independence commitments without supplying an exhaustive argument. Formal definability does not establish that commitment.
- Kind classification can carry identity criteria and still have a unary membership condition. Denying that kind specifications can be unary Properties does not follow from their sortal role.
- The proposed “maximal irreducible arity” test conflicts with the declared arity test for Property. `Orbits(x, Sun)` can define a new unary condition while remaining relationally grounded. It does not turn the original Orbits relation into a unary relation or eliminate the Sun.
- Norms, goals, preferences and obligations are not all desired or counterfactual content. A particular binding obligation and a particular preference attitude require separate readings.

**Remedy and cost:** weaken unearned global disjointness/exhaustiveness, repair the instantaneous occurrence definition, distinguish reified specifications from kinds and features, and track arity derivations. This sacrifices the simplicity of the tripartite metaphysics; replacing it with another asserted exhaustive list does not supply the missing argument.

### Gemini's repository-informed revision

**Preserve:** explicit feature/value/content separation, role occupancies and normative standing, more concrete counterexamples and a revised tree that engages the repository.

**Do not inherit its factual mapping errors**, identified above. Also do not treat the separation of a universal from a trope as intrinsically a “fracture”: they are different subjects whose relationship should be represented. A common parent for institutions and fictions does not identify them; the actual error in the initial tree is its incompatible definitions and disjointness.

The revised tree still declares six root categories jointly exhaustive and disjoint without an argument covering all admitted subjects. A formal semantic condition can satisfy both its Informational Content and Formal Structure definitions. Its own quality-space discussion calls a dimension “Region,” whereas the revised Region definition admits only spatial, temporal and spatiotemporal loci. Predicate Specification lists Kind Specification beside Unary Property without a clear inheritance policy for the unary kind condition. Placing a subclass beside a broader class is not inherently false, but their additional inclusion must be represented and their sibling policy must not suggest a partition.

Its physical-body account also places Physical Aggregate, defined as a loose collective, under a spatial-unity parent. An asteroid belt tests whether the intended unity is permissive enough; if not, the parent needs broadening or aggregates need a different physical-object route. “Narrative Work” requires coherence, excluding the deliberately inconsistent narratives the prompt requires the system to discuss.

**Remedy and cost:** test each asserted partition against exact child definitions; use open overlapping groups where appropriate; restore the missing semantic edges; and let narrative content include inconsistent attributed accounts. A less balanced tree is preferable to a misleading exhaustive one.

### Preserved Claude Fable proposal and its revision

**Preserve:** the distinction between a kind and its specification, typed metamodeling intent, the five different “realization” relations, identity/persistence analysis, explicit attribution versus exemplification, and willingness to withdraw the internal/external relation split as the visible organization.

**Claims requiring correction or qualification:**

1. **OntoClean does not require every class in a taxonomy to be rigid.** It constrains which rigidity assignments can coexist with subsumption. An anti-rigid Student class can be a subclass of Person; making every person necessarily a student is the problematic converse under the stated modal assumptions.[†](#e-ontoclean) The initial blanket ban is an extra editorial policy. The revised document later permits anti-rigid leaf classes, revealing the need to state the narrower rule consistently.
2. **“Any phase of a Process is the same sort” is too strong.** A subinterval of running can be a flight phase rather than itself a running; an arbitrarily short phase of a complex operation need not instantiate the whole operation type. The DOLCE paper explicitly uses non-homeomeric processes.[†](#e-dolce) Remove the universal same-sort clause; retaining Process as a useful class does not require it.
3. **The Predicable stratification needs mixed-order signatures.** The initial rules allow order-1 predicables on particulars and order-(n+1) predicables on order-n predicables. A reified HasArity relation relates a predicable to a number, and satisfaction relates a specification to an ordinary subject. A simple homogeneous-order ladder does not explain these mixed tuples. Use typed signatures with safe universe levels rather than assuming every argument shares an order.
4. **Class extensions are not automatically ordinary sets.** The initial horse table says a class's extension at a time is a Set, but a universally applicable class of sets in a usual set-theoretic metamodel cannot simply be another unrestricted set. Use a relative interpretation domain, a class-level collection or a typed metatheory, as needed. This is a formalization obligation, not a requirement to ban discussing classes.
5. **Formal Object excludes origin from identity while Proposition may concern origin-dependent individuals.** A proposition about one particular person or organization can depend on which historical individual it concerns. A structured-proposition account is defensible; it needs an identity rule linking constituents and reference, not an assertion that all proposition identity is purely mathematical.
6. **Context may legitimately be an explicit argument.** The revision's rule that all of GPT's contexts must become indices is a new convention, not a correction forced by logic. Comparing a person across two times or a norm across two jurisdictions may require quantification over those contexts. The weak `Entity` range and missing internal structure deserve repair; explicit third arguments do not deserve automatic deletion.
7. **Equivalence and classification may be classes of relation specifications.** A metaproperty can define a class of its satisfying relation specifications; typed classification relations can be reified. Prohibiting their presence in a relation inventory overcorrects genuine level ambiguities.
8. **Characterized Object is a substantive identity account.** Encoding versus exemplification is a serious option, not a uniquely correct treatment or the only way to distinguish story-internal predication from authorship claims. Zalta's theory adds a specified predication logic.[†](#e-fiction) An artifact interpretation and a fictional-subject interpretation do not acquire identical existence commitments merely by sharing a database shape.

Some criticisms in the Claude review are also too categorical: member turnover does not refute every collective identity policy; a moving hole does not refute every host-relative region theory; valid domain subclasses do not become invalid because a portal is available; and an undiscovered species does not begin to exist only when a specification is written. Astra's specification branch is not a denial of preexisting organisms or an exhaustive ontology of universals.

**Remedy and cost:** retain Claude's analytical distinctions while dropping blanket prohibitions and adding typed scope/identity policies. Its revised seven-way tree is a defensible competitor, but its disjoint formal/construct division and predicable realism remain costs to evaluate, not conclusions established by the project's needs.

## Property and Relation reconciliation

### The common interpretation

Use **Condition specification** as the shared semantic parent, with **Property specification** for exactly one declared argument and **Relation specification** for two or more. “Predicate specification” is an alias with the same stipulated meaning. A linguistic predicate expression is a Symbolic structure that expresses such a condition; it is not automatically the condition.

This is a representation-oriented decision, not a proof that properties in every metaphysics are content. A realist may additionally distinguish a universal that is specified, its linguistic expression, its instances and the specification. The ontology must permit that extension without identifying a description with what it describes.

Let `I` be an interpretation, `c` a declared evaluation context, `p` a condition specification, and `args` a tuple matching its signature. Satisfaction is `Sat(I,c,p,args)`. Class membership, a reified specification and a class handle are distinct:

- `instanceOf(x,C)` concerns an individual and a class handle at an explicit metamodel level.
- `subclassOf(C,D)` concerns class inclusion: under the accepted interpretation, every C-instance is a D-instance.
- `specifiesClass(p,C,I)` records the bridge between a unary specification and the class it defines or describes in interpretation I.
- If this is a **definitional** bridge, require `instanceOf(x,C) iff Sat(I,c,p,(x))` for the relevant scope. A merely diagnostic or imperfect specification need not support the biconditional.
- `bears(x,q,t)` relates a bearer to a particular feature. `hasDetermination(q,v,t,scheme)` relates that feature to a determination. Neither is class membership in a class of specifications.

The visible Condition specification layer earns its cost because signature, interpretation, satisfaction, derivation, entailment and metamodel-level documentation are shared. It is not justified merely by the word “predicate.” The W3C materials demonstrate why OWL class/individual punning and RDF binary-property encoding do not supply these bridges automatically.[†](#e-w3c)

### Every incumbent Property child

The active displayed branch has thirteen children. Three further intended children, Function, Role and Status, survive only through the identifier-collision/alternate-parent mechanism. All sixteen are addressed here.

| Record and incumbent wording | Does the wording establish a unary condition? | Recommended treatment and counterexample |
| --- | --- | --- |
| Quality — “A characteristic describing how an entity is” | Compatible with a unary reading, but not sufficient to distinguish a specification from a particular feature | Split the reusable condition, this bearer's quality and its determination. Equal shades on two cups do not make one numerically identical bearer-specific feature |
| Quantity — “A property specifying how many, how much, or to what extent” | Ambiguous between a truth-valued condition and a value-valued attribute | Separate quantity kind, mapping/schema, particular quantity and value. `mass(x)` returning 2 kg is not the unary truth-valued condition `mass(x)=2 kg` |
| QualityValue — “A value that specifies a quality on a scale or comparison” | No unary condition follows | Relocate the determination; retain a derived condition only with an explicit bridge. The magnitude 2 kg is not itself “weighs 2 kg” |
| Disposition — “A property that makes an entity liable to behave in a certain way” | Can describe a dispositional predicate; also suggests a particular causal feature | Split specification and particular disposition. This glass's fragility and a future breaking have different existence conditions |
| Capability — “A property representing what an entity can do or undergo” | Can be unary after the activity, conditions and assessment standard are supplied | Preserve capability-bearing specifications and task-assessed disposition classifications. A sleeping pianist can retain an ability; legal power to appoint is a different normative sense |
| Function — lost teleological definition: “A use or activity an entity is suited or intended to perform” | No; it confuses suitability, assigned purpose and activity, and collides with mathematical Function | Mint distinct senses. A broken pump can retain an assigned function without operative capacity; a numerical mapping is neither |
| Purpose — “An intended end that guides an entity or activity” | Names an end, not a unary signature | Separate target content, assignment, assigning act/history and a derived bearer condition. A stone used as a doorstop need not change its material kind |
| Role — social position / “an entity's place in a context or activity” | Unary only for a context-bound classification specification, not for all office/occupancy senses | Distinguish specification, bearer, occupancy and institutional office. An office may be vacant; its former occupant persists after resignation |
| Status — recognized standing or condition | Same ambiguity as Role, with possible temporal-state readings | Represent standing as a particular relational feature or state; derive a unary condition with framework/time supplied. Accreditation can end without destroying its former bearer |
| Norm — “A rule or standard specifying expected conduct or form” | Not as written | Keep normative content; derive a satisfaction predicate over performances or bearers only with its chosen target sort. A violated rule remains a rule |
| Obligation — “A requirement binding an agent to an action or state” | Not as written | Separate reusable requirement content, binding position and proposition reporting it. A merely quoted requirement does not bind the reader |
| Goal — “A desired or intended state treated as an end” | Not as written | Separate target content, adopting attitude and any realized state. Two agents can share target content while only one abandons its pursuit |
| Preference — “A disposition to favor one option or state over another” | Could denote a particular attitude or a derived condition; no fixed unary signature is supplied | Distinguish attitude, comparative relation and representation. A cyclic preference relation has a representation, but not a transitive ordering faithful to the cycle |
| ModalProperty — concerning possibility, necessity or contingency | Yes only after the argument sort and modal interpretation are declared | Retain as a condition classification; possibility of a proposition is not a bearer-specific material quality |
| LogicalProperty — defined by logical form or consequence | Yes for an explicit unary metacondition | `isTransitive(r)` applies to a relation specification; it does not make r unary |
| MathematicalProperty — defined or established mathematically | Compatible but underspecified | Retain with signatures; `isPrime(n)` is unary, while “has this group order” needs group/value handling or fixed-value derivation |

Relocation costs more than reparenting: separate meanings often require new records and assertion bridges. A number, value or trope does not have “arity zero” just because it is not applicable. **Arity is inapplicable unless an interpretation gives the subject an application signature.** A nullary truth condition is a different matter.

### Kinds, roles, capability and normative content

**Kinds.** Dog is a class of dogs; dog-spec is an individual condition specification. Dog is not a subclass of Kind specification. Kind specification can be a subclass of Property specification because each classification test accepts one candidate once interpretation is fixed. Identity and persistence criteria add constraints; they do not add an extra candidate argument. Broader everyday “kind” and a strict rigid sortal are not automatically the same sense.

**Roles.** A role-bearing class may be an anti-rigid subclass of a bearer kind. Its members are not role specifications. A role specification can itself have a stable identity even though its extension changes. OntoClean's constraint should be checked for the relevant class and identity assumptions, not converted into “roles may never be tree nodes.”

**Capability.** “Task-assessed disposition” is a coherent class. Its anti-rigidity relative to changing interests does not invalidate `CapabilityDisposition subclassOf Disposition`. I prefer a defined cross-cutting classification rather than a principal child in the proposed tree because task/interest is not the same axis as what individuates the disposition. This is a navigation and identity-policy choice, not a demonstration that the subtype is impossible.

**Functions and purposes.** Retain both operational capacity and assigned/selected contribution. For an assigned purpose use an explicit relation such as `AssignedPurpose(assignerOrPractice, bearer, targetContent, context, time)`. For evolutionary function, a selected-effect history may replace an intentional assigner; do not impose mental agency on every biological function. A particular assignment can be reified when it has its own history. A bare outcome is content, not the assignment.

**Norms and obligations.** Normative content can prescribe, permit, prohibit or confer powers. A binding position concerns a bearer under a normative framework; it need not have a named human obligee. A jointly borne debt or commitment can be represented as a relator where that identity account is useful. Reification does not assert the norm's moral correctness.

**Goals and preferences.** A target specification can exist without being adopted. Adoption is an attitude or relation. `Prefers(agent,a,b,context,time)` does not imply completeness or transitivity. A mathematical ordering is an additional representation supported only when its axioms fit the intended preference data. “Preference relation” is not a synonym for “preference ordering.”

### Arity, arguments and evaluation indices

An argument has an ordered, typed place in a declared specification. An index identifies an interpretation in which that specification is evaluated. Neither designation is forced by the English words “time” or “context.”

For `HasMass(bearer:PhysicalObject, value:QuantityMagnitude, time:TemporalInstant)`, all three are arguments in this declared version:

- `P(x) := HasMass(x, 2 kg, noon)` is unary.
- `Q(x,t) := HasMass(x, 2 kg, t)` is binary.
- `U(x) := exists v HasMass(x,v,noon)` is unary, but weaker than P.
- `HasMass_noon(x,v)` may be a binary member of a time-indexed family, provided the conversion from the ternary specification is recorded.
- Encoding `(x,v,t)` as one tuple object yields a unary predicate of tuples. It does not erase the three participant/value/time places in the represented condition.

Keep derivation records naming the base specification, fixed arguments, quantified arguments, substitutions, tuple encoding, and index conversion. Fixing only a role name in `PlaysRole(bearer,role,context,time)` does not yield a unary condition. Universal closure differs from existential closure; reflexive substitution differs from fixing an argument.

Require role names and range types, not merely `arity: 3`. Context can have its own schema for jurisdiction, time, comparison class, frame and interpretation. If a query must compare contexts, hiding them permanently as inaccessible indices loses expressive power. If context is fixed for the whole interpretation, repeating it in every tuple may be unnecessary. Record the choice rather than declaring one convention metaphysically correct.

### Every incumbent Relation family

The nineteen families can survive as an overlapping classification of **relation specifications**, subject to these repairs. A family class is not a subproperty axiom between all relations belonging to it.

| Family | Required distinction or example signature | Treatment |
| --- | --- | --- |
| ClassificationRelation | `instanceOf(subject,classHandle)` versus `subclassOf(classHandle,classHandle)` versus `specifiesClass(spec,classHandle,interpretation)` | Retain as a typed metamodel family; never collapse these predicates or identify a class with its specification |
| PartWholeRelation | `partOf(part,whole,time)`; declare proper/improper and temporal scope | Retain; do not infer that set membership, group membership or subclassing is parthood |
| SpatialRelation | `locatedIn(subject,region,time,frame)`; `between(x,y,z,frame)` | Retain; region, coordinate expression and occupant remain separate |
| TemporalRelation | `before(intervalA,intervalB,temporalOrder)` | Retain with instant/interval types and an order interpretation |
| CausalRelation | `contributesTo(cause,effect,causalModel,context)` | Retain; a causal relation is not the causing event and does not entail explanatory sufficiency |
| ExplanatoryRelation | `explains(explanans,explanandum,account)` | Retain separately from causation; a mathematical explanation need not be a physical cause |
| ParticipationRelation | `participatesIn(participant,occurrence,context)` | Retain its occurrence requirement; move GPT's feature-bearing and role-satisfaction examples out |
| SocialRelation | `interactsWith(agentA,agentB,practice,time)` or a specified socially constituted relation | Retain; a relation among people is not social merely because its arguments are people |
| InstitutionalRelation | `holdsOffice(person,office,institution,time)` | Make it a SocialRelation subtype where “institutional” is defined through socially constituted rules; do not assume every human relationship is institutional |
| PerceptualRelation | `perceives(subject,target,time,mode)` | Retain; distinguish successful perception from an experience purporting to present a nonexistent target |
| EpistemicRelation | `supports(evidence,claim,epistemicStandard)`; `believes(subject,content,time)` | Retain with separate specifications; knowledge, belief, justification and evidence do not share identical truth conditions |
| LogicalRelation | `entails(premiseSet,conclusion,logic)` | Retain; a premise-set argument is one typed argument, not variadic syntax silently compressed |
| SetTheoreticRelation | `memberOf(element,set)` versus `subsetOf(setA,setB)` | Retain, normally with MathematicalRelation ancestry under its chosen domain reading; preserve universe levels |
| MathematicalRelation | `lessThan(numberA,numberB,orderedStructure)` | Retain its range restrictions, or explicitly broaden its definition; do not silently admit every social specification as a mathematical object |
| TransformationRelation | `transforms(input,output,operationSpec,context)` | Retain; connect the transformation occurrence separately when one happens |
| RepresentationalRelation | `expresses(expression,content,interpretation)`; `represents(model,target,interpretation)` | Retain; split expression, encoding and reference predicates; a bearer quality is not a representation merely because it is assigned a value |
| IdentityRelation | `sameEntity(x,y,identityProfile)` with profile fixed for identity reasoning | Retain; distinguish numerical identity, co-reference, representation and sameness of value |
| EquivalenceRelation | A class of binary relation specifications satisfying reflexivity, symmetry and transitivity on a stated domain | Retain as a cross-domain metaproperty-defined classification; it need not be confined to mathematical relata |
| ProvenanceRelation | `derivedFrom(result,source,activity,method)` | Retain; provenance is not identity, and transformation history is not necessarily a subclass lineage |

**Equivalence needs a domain and exact criterion.** Equality of assigned color codes on a total coding domain can be an equivalence; vague resemblance generally is not. “Shares a nationality” is not necessarily transitive when dual nationality is allowed: an A-only citizen can share one with an A/B citizen, who shares one with a B-only citizen, while the endpoints share none. The other critiques' social equivalence examples need this qualification.

`IsEquivalenceRelation(r,D)` is a metacondition on r under D. The class of relation specifications satisfying it is still a legitimate subclass of Relation specification. Conversely, the existence of that class does not make every use of “interchangeable” mathematically reflexive, symmetric and transitive. Keep exact equivalence, approximate similarity, congruence, isomorphism and identity distinct.

## Meaning-preserving mappings and human audit

### A reconciliation record is an argument, not a synonym row

Use the GPT coverage record as a starting container, adding the following conceptual fields rather than accepting its existing treatment label as sufficient:

| Field | Required meaning |
| --- | --- |
| Source identity | Repository revision, source ID, source node kind, original definition and original edges |
| Intended sense and examples | Positive example, exclusion/counterexample, identity or persistence rule, argument interpretation if applicable |
| Target identity | Target ID, definition version and whether it denotes a class, specification individual, ordinary individual, expression or navigation portal |
| Mapping relation | Equivalent-in-scope, narrower, broader, overlapping, split-by-sense, representation-of, specification-for, instance-of, related-only, rejected or unresolved |
| Assertion migration | Which old assertions can transfer, under what conditions, and which require review; not just where a label redirects |
| Semantic and navigation parents | Accepted superclasses separately from the one preferred route; compressed ancestry separately marked |
| Decision | Proposed, accepted, modified, rejected or deferred; human reviewer, date, rationale and counterargument |
| Evidence | Source passage, version/hash and test case; citations to another critique identify an argument, not independent source confirmation |

Preserve stable identifiers **for stable senses**. Correcting a typo is different from changing “edible bearer” into “food specification.” For an ambiguous old ID, retain a deprecated source record or disambiguation endpoint; do not silently choose a “dominant” sense and migrate all assertions to it. Where a definition is broadened or narrowed materially, record the change and assess its consequences even if a local editorial policy keeps the ID.

An exact lexical match establishes neither class equivalence nor referent identity. [SKOS mapping relations](https://www.w3.org/TR/skos-reference/#mapping) offer useful distinctions for concept schemes, but `skos:exactMatch` is not a synonym for `owl:equivalentClass` or `owl:sameAs`. Its transitivity also makes careless exact matches consequential.[†](#e-w3c)

### Coverage dimensions

Report separately:

1. **Source accounting:** every source record has an explicit disposition. GPT achieves this for the inspected 439-record baseline.
2. **Sense coverage:** the intended sense has a defensible definition and home, with relevant exclusions.
3. **Assertion preservation:** accepted source statements translate without changing their meaning or losing necessary context.
4. **Navigation coverage:** a human can find the sense through search, aliases, facets or the preferred tree.
5. **Source authority and currency:** placement is supported by the declared release and interpretation, not merely a matching source label.
6. **Test coverage:** named executable invariants and counterexamples, distinguished from prose assurances.

Do not combine these into a single percentage without explaining its denominator. Imported outlines are especially useful for finding missing subjects; they do not supply subclass axioms for every subject they mention.

### Bounded audit sequence

These are recommendations for later authorized work, not changes made by this critique.

| Stage | Bounded change | Acceptance evidence and stop condition |
| --- | --- | --- |
| Freeze meanings | Name the authoritative dataset and revision; capture definition/edge hashes; record the exact candidate versions | Reproducible input manifest; no ontology relocation yet |
| Preserve distinctions | Reject conflicting duplicate IDs; distinguish semantic parents, navigation parents, node kind and typed assertions | Function/Role/Status collisions produce explicit review cases instead of silent merges |
| Repair projection | Give the incumbent six multi-parent records explicit preferred routes; reconcile the SUMO casing/root anomaly separately | Every nonroot has one primary parent; all intended roots/reachability are explicit; no duplicate rendered IDs; unique descendant counts |
| Prove the predicate contract | Correct the Object-typed unary acceptance gap; review all twenty GPT predicate instances against parent definitions | Negative family/range/level tests fail as intended; positive typed examples pass; context policy is declared |
| Reconcile Property and Relation | Use the sixteen- and nineteen-row analyses above; split only the affected senses first | Two equal-mass cups, vacant office, broken pump, cyclic preference and norm/obligation cases remain distinct and queryable |
| Repair bounded incumbent branches | Human-person and occurrence senses; botanical fruit/food; celestial body/region; language/expression; virus and warm-blooded ancestry cases | Each move or split has a mapping argument and local counterexample; no wholesale import of GPT or another tree |
| Reconcile institutional and content identity | Test organization turnover, office vacancy, contract content/agreement, text/work/token, and fictional attribution | Explicit persistence and reference policies; no inference from a quoted claim to actual existence |
| Review biological module | Verify proposed lineage changes against archived evidence plus selected taxonomic authority; preserve source paths and editorial exceptions | Biology-specific validation, provenance and migration report; do not infer monophyly from common labels or counts |
| Expose the richer graph | Search aliases; expose alternate ancestry, specifications, signatures and facet destinations | Find edible-bearer and personhood senses without classifying their bearers as specifications; existing browsing regressions still pass |
| Decide upper navigation | Compare the revised tree below, GPT's open dyad, and a predicable-realism alternative using the same difficult examples | Human acceptance of identity/scope tradeoffs; no model-vote criterion or arbitrary global depth ceiling |
| Publish accepted work | Regenerate affected views and their manifests according to the project publication contract | Source, package and published view identify the same accepted revision; do not run the broad deployment target merely to publish this critique |

Human review should accept, modify or reject each sense-level change, not approve an entire model-branded tree by reputation. Keep declined alternatives with their strongest counterexample. Stop a branch migration when the target's meaning, identity policy or assertion translation remains unresolved; unrelated accepted branches need not wait.

## Evidence

### External sources actually consulted

The following sources were opened during this review. Their commitments are not automatically this document's commitments. New proposed definitions and examples below are editorial choices.

<a id="e-w3c"></a>

- **W3C, OWL 2 Structural Specification, §5.9 Metamodeling, 2012:** [official specification](https://www.w3.org/TR/owl2-syntax/#Metamodeling). The inspected passage explicitly interprets the class and individual views of a punned IRI independently. Used for the class/specification bridge requirement, not to claim that OWL supplies all the proposed semantics.
- **W3C, Defining N-ary Relations on the Semantic Web, 2006:** [Working Group Note](https://www.w3.org/TR/swbp-n-aryRelations/). The inspected discussion distinguishes binary RDF/OWL links from multiargument modeled relationships and introduces reified patterns. Used for encoding discipline; it is a Note, not a proof that all relations are metaphysically binary.
- **W3C, SKOS Reference, 2009:** [mapping vocabulary and conditions](https://www.w3.org/TR/skos-reference/#mapping). The inspected passages distinguish exact/close/broad/narrow/related mappings, declare exactMatch symmetric and transitive, and do not give every mapping property transitivity. Used for conservative crosswalk semantics, not formal class equivalence.

<a id="e-ontoclean"></a>

- **Nicola Guarino and Christopher A. Welty, An Overview of OntoClean, 2004:** [author-laboratory PDF](https://www.loa.istc.cnr.it/wp-content/uploads/2020/03/OverviewOntoClean-compresso.pdf). Downloaded and inspected through local text extraction, especially rigidity, identity and subsumption constraints. The relevant constraint is that anti-rigid properties cannot subsume rigid properties under the stated modal interpretation, not that every taxonomy class must be rigid.

<a id="e-dolce"></a>

- **Stefano Borgo and colleagues, DOLCE: A Descriptive Ontology for Linguistic and Cognitive Engineering, 2022:** [author-hosted PDF](https://www.loa.istc.cnr.it/wp-content/uploads/2021/11/DOLCE_FOUST_2022.pdf), [DOI](https://doi.org/10.3233/AO-210259). Downloaded and inspected through local text extraction for particulars, qualities/qualia, process homogeneity, role extensions and temporalized relations. Distinct bearer-specific qualities can share a quale; process parts need not all have the whole process's type. The DOI is a bibliographic link, not a separate retrieval.
- **Johannes Röhl and Ludger Jansen, Representing dispositions, 2011:** [full paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC3194171/). Inspected the bearer/inherence and realization discussion, including unrealized dispositions. Used to reject any inference from “has a disposition” to an actual manifestation; not used as the latest BFO specification.
- **BFO 2020 project:** [official artifact overview](https://bfo-ontology.github.io/bfo-2020.html). Inspected its links to distinct Common Logic, first-order and OWL artifacts, including temporalized relations. This supports version/profile specificity; no complete BFO axiom validation was performed.
- **QUDT:** [2026.02 schema documentation](https://qudt.org/doc/2026/02/DOC_SCHEMA-QUDT.html). The inspected introduction distinguishes quantity kinds, particular quantities and numerical values in units. A direct QuantityValue-page fetch exposed only a logo to the reader tool; no detailed axiom claim rests on that fetch.

<a id="e-fiction"></a>

- **Stanford Encyclopedia of Philosophy, Properties:** [§1.1 and surrounding discussion](https://plato.stanford.edu/entries/properties/). Used as an authoritative secondary account of predicates, properties, nominalization, extensions and intensions; not as proof of property realism.
- **Stanford Encyclopedia of Philosophy, Nonexistent Objects:** [reference and quantification discussion](https://plato.stanford.edu/entries/nonexistent-objects/). Used for the distinction between quantification/admission and existence and for competing formalizations.
- **Edward N. Zalta, Further Explanation of the Distinction Underlying the Theory:** [author-maintained account](https://mally.stanford.edu/distinction.html). Inspected exemplification versus encoding and the Holmes example. Used as a substantive alternative, not an assertion that attributed claims in the proposed core implement Zalta's theory.

<a id="e-biology"></a>

- **NCBI Taxonomy Browser:** [Homo sapiens, taxon 9606](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=9606) and [Aves, taxon 8782](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=8782). Inspected full displayed lineages and the source's classification-authority disclaimer. The archived taxonomy XML checks are a separate frozen-evidence result in [the execution record](#executed-evidence-and-its-limits).

### Repository evidence

All file/record findings identify their source directly. Exact numerical and executed claims are consolidated in [Executed evidence and its limits](#executed-evidence-and-its-limits). The revision in the Summary pins the source baseline. No claim that a test ran is based solely on another critique, a checked-in report, or a README. Population estimates and unexamined external citations remain unverified here.

## Recommended upper tree

### Root and semantic contract

**Entity:** an individuated subject admitted to a specified domain of discourse for identification and predication; admission by itself asserts neither actual existence nor realizability.

This is a scope rule for the knowledge system, not a definition of being by a higher genus. Keep expression, reference record and purported subject distinct. A meaningful description may fail to denote. A model need not contain an instance of every class; writing “largest prime” does not produce a prime. A fictional attribution is not an unqualified actual-world assertion.

Every node below denotes a **class of subjects**. Every indented edge is subclass inclusion, not instance-of, part-of, topic, participation, use or expression. A specification individual is an instance of a specification class. A class handle in the metamodel is not identical to the ordinary individuals it classifies. The implementation needs typed domains or safe metamodel levels, not a universal set with unrestricted comprehension.

The six principal categories remain **open**, with explicitly qualified overlap. They are selected for recurring identity and relationship distinctions demonstrated by the repository's cases, not claimed to partition every possible metaphysics.

### Tree with discriminating definitions

Indentation is authoritative: Entity is depth 0; the deepest displayed classes are depth 3. No adopted ancestor is silently omitted to bring a deeper class into this report.

- **Entity:** an individuated subject admitted to a specified domain of discourse, without actuality or realizability being implied.
    - **Object:** a particular bearer tracked through a career by an identity rule other than the identity of an occurrence, dependent feature, locus, repeatable content or formal item as such.
        - **Physical object:** an object individuated through a physical body, material amount or physical grouping.
            - **Material body:** a physical object whose organizing unity supports its identity through relevant changes of constituents.
            - **Material portion:** a physical object individuated by a specified amount of matter, with retention of that matter central to its persistence rule.
            - **Physical aggregate:** a physical object individuated as a plurality of physical members under an explicit grouping and persistence rule, without requiring bodily unity.
        - **Social object:** an object whose identity or persistence depends on social practice, affiliation, recognition or constitutive rules.
            - **Institutional continuant:** a social object whose continuing identity is governed by an identifiable institutional framework, potentially surviving changes or absence of occupants.
            - **Social collective:** a social object individuated as a group through membership, affiliation or interaction under a stated persistence rule.
    - **Occurrence:** a particular happening or obtaining episode individuated through its temporal course, boundary or extent.
        - **Process:** an occurrence identified through ongoing activity, operation or change, with its course relevant to its identity; its phases need not all instantiate its own type.
            - **Physical process:** a process identified through changes or operations of physical systems.
            - **Mental process:** a process identified through cognitive, affective or experiential activity, without a reductive physical identity being stipulated.
            - **Social process:** a process identified through social interaction, coordinated practice or institutional operation.
        - **Event:** an occurrence individuated as a bounded happening under a stated event criterion, whether instantaneous or extended.
            - **Transition event:** an event identified by a change from one specified condition to another.
            - **Achievement event:** an event identified by reaching a specified endpoint or satisfaction condition, whether or not anyone intended it.
        - **State:** an occurrence identified by the obtaining of a specified condition over an interval rather than by the detailed course producing or maintaining it.
            - **Physical state:** a state identified through the condition or configuration of a physical system.
            - **Mental state:** a state identified through experience, cognition or an attitude's obtaining.
            - **Social state:** a state identified through social relationships, practices or institutional standing.
    - **Particular feature:** a particular characteristic whose identity depends on specified bearers or hosts and possibly a contextual framework, rather than on being a reusable condition specification.
        - **Quality:** a particular feature characterized by a determination in a qualitative or quantitative domain, without requiring a manifestation process to identify the determination.
            - **Physical quality:** a quality characterizing a physical bearer or physical aspect.
            - **Phenomenal quality:** a quality characterizing how an experience feels or appears from a subject's perspective.
        - **Disposition:** a particular feature grounding a tendency or capacity for manifestations under specified conditions, whether or not a manifestation occurs.
        - **Relational feature:** a particular feature whose individuation requires a bearer’s connection to another entity or contextual framework.
            - **Role occupancy:** a bearer's particular holding of a contextual position, distinct from its specification, its occupant and any enduring office.
            - **Normative position:** a bearer's particular standing as obligated, permitted, entitled, prohibited or empowered under a stated normative framework.
            - **Relator:** a relational feature individuated as jointly dependent on specified relata and grounding a connection among them, where the adopted identity account posits such a feature.
        - **Structural feature:** a host-dependent feature individuated by structural or topological organization rather than merely by a numerical or categorical description.
            - **Boundary feature:** a structural feature delimiting a host or part, with identity following the host rather than a fixed coordinate position.
            - **Cavity feature:** a structural feature individuated as a hole or void in a host, distinct from its boundary and the region it occupies at a time.
        - **Intentional attitude:** a particular feature consisting in a subject's orientation toward content or a target, without requiring a purported target to exist.
            - **Belief attitude:** an attitude of taking propositional content to be true.
            - **Conative attitude:** an attitude of desiring, intending or committing to an outcome or performance.
            - **Preference attitude:** an attitude of comparatively favoring alternatives under an evaluative context, without assumed completeness, transitivity or intention to obtain them.
    - **Region:** a nonempty locus or extent in a stated spatial, temporal or spatiotemporal domain, distinct from its occupant and coordinate expression.
        - **Spatial region:** a region in a specified spatial domain or frame.
            - **Spatial point:** a spatial region consisting of one position in the adopted positional model.
            - **Spatial extent:** a spatial region consisting of more than one position, without a connectedness or positive-volume requirement.
        - **Temporal region:** a region in a specified temporal domain or ordering.
            - **Temporal instant:** a temporal region consisting of one temporal position in the adopted model.
            - **Temporal extent:** a temporal region consisting of more than one temporal position, potentially including disconnected intervals.
        - **Spatiotemporal region:** a region in a domain jointly individuated by spatial and temporal positions.
            - **Spatiotemporal point:** a spatiotemporal region consisting of one joint position.
            - **Spatiotemporal extent:** a spatiotemporal region consisting of more than one joint position.
    - **Content:** a subject individuated by what is presented, asserted, prescribed or specified under an interpretation, rather than by the carrier or sign pattern expressing it.
        - **Condition specification:** content specifying a truth-evaluable or satisfaction-assessable condition with a fixed, finite, positive number of declared argument positions.
            - **Property specification:** a condition specification with exactly one argument position; alias “unary condition specification.”
            - **Relation specification:** a condition specification with two or more ordered argument positions, distinct from an application tuple, proposition or worldly relator.
        - **Propositional content:** content presenting something as being the case, assessable for truth when interpretation and contextual parameters are supplied.
        - **Directive specification:** content setting an outcome, conduct or performance standard to be pursued, followed or assessed.
            - **Goal specification:** a directive specification identifying a target outcome or condition, whether or not anyone adopts it.
            - **Plan specification:** a directive specification organizing actions, constraints or contingencies for pursuit of an outcome.
            - **Norm specification:** a directive specification prescribing, permitting, prohibiting or conferring standing or powers under a normative framework.
        - **Descriptive content:** content organizing a representation beyond one isolated open condition or closed proposition.
            - **Model specification:** descriptive content specifying a selective representation of a target with an explicit intended correspondence or interpretation.
            - **Narrative content:** descriptive content organizing attributed situations or happenings into an account, without requiring truth, consistency or a physically existing protagonist.
    - **Formal entity:** a subject individuated by mathematical, logical, symbolic or scale rules in an explicit framework rather than by a particular physical or institutional career; no mind-independent existence is implied.
        - **Mathematical entity:** a formal entity specified within a mathematical theory through its definitions, operations, relations or structural position.
            - **Number:** a mathematical entity occupying a numerical position in a stated number system, distinct from a numeral expressing it.
            - **Mathematical collection:** a mathematical entity governed by specified membership, multiplicity or ordering rules, with equality and admissible size supplied by the theory.
            - **Mathematical structure:** a mathematical entity comprising domains equipped with operations, relations or distinguished elements under an explicit identity or equivalence criterion.
        - **Symbolic structure:** a formal entity individuated as a repeatable arrangement of signs under a syntax or notation, distinct from its inscription and interpreted content.
            - **Linguistic expression:** a symbolic structure organized under a language to express something, including nonwritten language.
            - **Formal-language expression:** a symbolic structure governed by an explicit formal grammar.
            - **Diagrammatic expression:** a symbolic structure whose nonsequential or spatial relations contribute to its interpretation under a notation.
        - **Scale determination:** a formal entity identified as a determinate magnitude or alternative in a stated scale or scheme, not an arbitrary subject merely used to fill a database field.
            - **Quantity magnitude:** a scale determination fixing an amount or degree of a specified quantity kind, with unit/scale conversion and equality rules supplied.
            - **Scheme category:** a scale determination identifying an alternative in a specified classification or evaluation scheme, distinct from its label and from a predicate testing membership in it.

**Depth boundary:** Organism belongs below Material body; Organization below Institutional continuant; Kind specification and Role specification below Property specification; Integer below Number; and a fully specified Mathematical mapping below Mathematical structure in the chosen mathematical profile. These are indicated deeper extensions, not promoted nodes. Their ordinary instances are not subclass nodes.

Disposition and Propositional content remain unexpanded at depth 2 deliberately. The repository demonstrates valuable task, context and attitude distinctions but does not establish one general taxonomic split of all dispositions or propositions. No balancing categories are invented. A later domain module may add justified subclasses without a three-edge global ceiling.

### Split policies and architectural argument

All constraints apply within one declared identity interpretation and assertion scope. Open means that no exhaustive union is asserted. Allowing overlap is not an assertion that a particular pair must have a shared instance.

| Parent | Axis and policy | Strongest reason | Objection and boundary test |
| --- | --- | --- | --- |
| Entity | Open collection organized by identity/dependence and type of predication. Object, Occurrence, Particular feature and Region are pairwise disjoint in this core profile and disjoint from Content. Object, Occurrence and Particular feature are disjoint from Formal entity. Content–Formal entity and Region–Formal entity overlap is permitted | Separates recurring subjects that need different relations without imposing an abstract/concrete or particular/universal partition | More than one axis is involved. A geometric region may also be a mathematical object; a process ontology identifying an object with its career needs another identity profile |
| Object | Physical/social grounds of persistence; open and not globally disjoint | Preserves material and institutional persistence questions | An embodied institution is not automatically identical to its building. Nonphysical subjects can remain at Object pending a subject profile |
| Physical object | Bodily unity, material retention, grouping; open; overlap only when the same stated identity policy supports it | Distinguishes repaired body, original material and aggregate membership | Statue/clay or organism/material identity may diverge; co-location alone does not establish identity |
| Social object | Constitutive-framework identity versus social-group identity; open, overlap permitted | An institutional organization can also be a collective | A vacant office is not a group; informal group continuity still needs a rule |
| Occurrence | Course, bounded event criterion, obtaining condition; open, overlap permitted | A bounded operation can be both a process and an event | A steady-state operation has active processes; deciding whether its state is the same occurrence needs identity evidence |
| Process | Physical, mental and social constitution/identifying activity; open, overlap permitted | These are genuine process conditions, not disciplines as parents | A conversation has several descriptions and possibly several related processes; overlap is not automatic identity |
| Event | Transition versus endpoint attainment; open, overlap permitted | Separates changing condition from the criterion of completion | A threshold crossing satisfies both; no universal instantaneous/extended split is imposed here |
| State | Physical, mental and social identifying conditions; open, overlap permitted | Preserves different kinds of obtaining condition | Co-occurring physiological and mental states need not be numerically identical |
| Particular feature | Determination, manifestation tendency, external dependence, structure, intentional orientation; open, no blanket sibling disjointness | Matches feature types that require different explanatory relations | A standing attitude may have a dispositional account; a relational quality need not be intrinsic |
| Quality | Physical aspect versus phenomenal character; open, overlap permitted but not required | Does not identify a felt appearance with its physical correlate by fiat | A physicalist identity requires an argument; merely measuring wavelength does not identify an experience |
| Relational feature | Occupancy, normative standing, jointly dependent connection; open, overlap permitted | Keeps vacant office, bearer, duty and joint agreement distinguishable | A debt may ground several unilateral positions; do not posit one identical entity for every related record |
| Structural feature | Delimitation versus void; open; boundary and cavity disjoint under these identity rules | A cavity is not its enclosing surface | A region-only account is a defensible alternative if host dependence and motion are explicit |
| Intentional attitude | Taking true, seeking/committing, comparative favoring; open, overlap permitted for a genuinely mixed attitude | Different success and persistence conditions | Preferring a better past is not intending to produce it; separate attitudes when their contents or histories differ |
| Region | Typed ambient domain: spatial, temporal, joint spatiotemporal; open to theory-specific refinement, pairwise disjoint as typed domains | Prevents locus, duration and coordinate confusion | A spatial projection is not the original spacetime region; physical theories need not privilege a universal present |
| Each positional region class | One versus multiple positions; disjoint and exhaustive within its declared nonempty positional model | Explicit minimal point/extent semantics | Point-free theories require a different profile; these definitions are not proof that physical space consists fundamentally of points |
| Content | Open condition, proposition, directive force, organized description; open, not a global disjoint partition | Preserves condition versus assertion and instruction versus execution | Mixed directive/descriptive content can satisfy more than one class; containing a norm is not itself being that norm |
| Condition specification | Fixed positive argument count; Property/Relation disjoint and exhaustive for this parent | A checkable shared signature/satisfaction contract | Variable-arity schemas and nullary conditions require separate representations; no silent argument hiding |
| Directive specification | Target, organized means, normative force; open, overlap permitted | Separates adoption, planning, prescribing and realization | A safety target can acquire normative force; adoption/authority cannot be inferred from wording |
| Descriptive content | Selective model correspondence versus attributed account; open, overlap permitted | Supports scientific modeling and fictional or inconsistent narratives | A simulation can be both; neither is identical to the target represented |
| Formal entity | Mathematical individuation, sign pattern, scale determination; open, overlap permitted with explicit identity rules | Keeps number, numeral and measured determination distinct | Some determinations and expressions also have mathematical accounts; encoding is not sufficient for identity |
| Mathematical entity | Numerical, membership/ordering, equipped-domain structure; open, overlap permitted only under a declared foundation | Avoids fields-of-study buckets | Representing numbers as sets is not automatically adopting that identity; proper classes need a safe metatheory |
| Symbolic structure | Linguistic, explicitly grammatical, diagrammatic form; open, overlap permitted | A circuit diagram can be a formal-language expression | A language system is not one of its expressions; its grammar/model needs a separate record |
| Scale determination | Quantity amount versus scheme alternative; open, overlap permitted when a scheme enumerates magnitudes | Replaces the ambiguous “anything used as a value” category | Paris does not become formal because a field stores it. Scheme category and its membership predicate remain distinct |

This is deliberately not a proof of complete coverage. It is preferable to leave a difficult subject directly under Entity with an explicit unresolved classification than to invent a false subclass edge.

### Cross-links and stress tests

| Case | Primary treatment | Separate subject or required link |
| --- | --- | --- |
| Two cups each of mass 2 kg | Two Material bodies, each with its own Physical quality | One equal magnitude determination may be shared; two feature identities are not merged; the mass relation and unary fixed-mass condition are specifications |
| Dormant skill or unbroken fragile glass | Disposition | Manifestation is an occurrence, not a required existing witness; task-assessed capability is an additional classification |
| Broken pump | Material body with an assigned/selected contribution history | Lost pumping capacity does not delete its design or assigned function |
| Treasurer resigns; office becomes vacant | Person/object, ended Role occupancy, enduring Institutional continuant | Role specification, occupancy and office are separate; no inference that the person loses identity |
| Contract with several translations | Normative/directive content plus expressions and institutional agreement | Translation equivalence does not by itself identify all versions, legal enactments or obligations |
| Preference cycle | Preference attitude(s) and explicit comparative relation | A directed graph can represent it; a faithful transitive ordering cannot be assumed |
| Moving ring and hole | Material body and Cavity feature | Boundary feature and time/frame-relative occupied region are linked, not identical by default |
| Constant-temperature heating | Physical process plus relevant Physical state | Temperature quality persists across changing determinations; the state has its specified temporal condition |
| University replaces its members | Institutional continuant, possibly also Social collective | Membership at each time and building ownership are relations, not an extensional-set identity rule |
| Printed novel, translation and story | Material copy; Linguistic expression; Narrative content | Expression, encoding, content identity and adaptation links remain distinct |
| Number 2, numeral “2,” and 2 kg | Number, Symbolic structure and Quantity magnitude | Unit conventions and quantity kind separate the magnitude from a bare number |
| Formal proof and act of proving | Symbolic or Mathematical structure under a declared formalization; Mental/Physical process for the act | Theorem content is Propositional content, not the proof occurrence or inscription |
| Fictional detective | Source-scoped subject with attributed detective predication; Narrative content about that subject | No actual human instance is inferred. A literary-artifact account may introduce an explicitly related subject |
| Largest prime or inconsistent round-square description | Expression/content and a failed or constrained reference account | Do not assert an actual satisfier. Quoted incompatible attributions do not enter the core as unqualified classical axioms |
| Undiscovered organism or disputed natural kind | Organisms need no authored specification in order to exist | A later specification records a classification claim; whether a mind-independent universal is additionally admitted is unresolved, not denied |
| Physical field, absence, law or possible world | Retain an explicit unresolved classification where necessary | A field model is not the field; missing detailed placement is a coverage limit, not permission to label everything Formal entity |

Agency and experience remain defined cross-cutting classes over Object, with separate tests; corporations can be agents without being experiencers. Capability is a task/condition-qualified classification over Disposition. Being a field value, premise, evidence item, instrument or food is a role or use unless a narrower constructed-kind definition is adopted. Such classifications can have browser destinations without becoming superclass assertions about unrelated bearers.

Use an actual superclass as primary parent when one has been adopted; preserve the others. For overlapping scale/math classifications, prefer Scale determination for the determinate magnitude and Mathematical structure for its space/model, with a bridge rather than an unexplained duplicate magnitude. For biological compression, preserve full adopted ancestry separately from the visible shortcut. Topic portals are explicitly topic links.

## Departures from the preserved Astra proposal

| Preserved position | Revised position here | Evidence or better argument | Cost |
| --- | --- | --- | --- |
| Predicate / Property / Relation under Content | Condition specification / Property specification / Relation specification, with explicit expression and class bridges | Repository mixes natural-language predicates, specifications, classes, qualities and argument-valued schemas; GPT signatures show why labels alone do not settle types | Longer labels; realist universals remain a separately stated commitment |
| Subject as a principal Object child | Agency and experience as defined cross-cutting Object classifications | Physical/social constitution and agency answer different questions; the project's role/facet use cases need multiple routes | A subject-first primary menu is not provided; nonphysical subjects remain admissible under Object |
| Capability and Operative function as displayed Disposition children | No universal displayed Disposition split; preserve task-assessed capability and operational-function classifications off the primary menu, with assignment/history separately modeled | Broken-pump and changing-interest cases discriminate capacity from assigned contribution, not subclass validity from invalidity | Requires facet/relationship presentation; this is not a blanket ban on those subclasses |
| Quality-space region beside spatial/temporal regions | Region is the stated spatiotemporal-locus family; quality spaces are Mathematical structures, with determination links | Source/project cases require distinguishing quality, space, determination and measurement representation; having two possible routes alone is not an error | DOLCE imports need an explicit mapping, not label identity |
| Value as a Formal entity child | Scale determination, with Quantity magnitude and Scheme category; generic value use remains a role | A database slot can contain Paris; a scheme category is not necessarily a unary predicate, and a magnitude need not be identical to one number/unit inscription | “Value” remains useful UI vocabulary but is not one unrestricted ontological kind |
| Relational feature expanded only to role occupancy and normative position | Also permit jointly dependent Relator where its identity account is useful | Contracts, joint commitments and debts in the repository need a way to discuss a connection separately from each party's position | Additional reification is optional and must earn its identity; not every true relation gets a relator |
| General class/specification distinction mainly in prose | Explicit definitional versus diagnostic bridge, signature-family tests, and assertion migration criteria | GPT's class-specification predicates and type-validation mutation expose actual operational gaps | Formalization needs reviewed contracts rather than mere ancestry checks |
| Source and display preservation as architectural recommendations | Concrete single-parent, unique-row, count, alias and facet acceptance tests | Incumbent 487/439 rendered-row discrepancy, SUMO dual roots, GPT invisible expressions and aliases | Renderer/schema changes are prerequisites for adopting the richer proposal |

Retained after criticism: the open six-route architecture; genuine overlapping domain subclasses under Process and State; the distinction between feature, bearer, value and condition; explicit arity transformations; optional mental/physical identity rather than automatic reduction; and source-scoped fictional attribution. I do not treat the other models' agreement against any retained choice as sufficient reason to change it.

## Unresolved choices and discriminating tests

| Choice | What would discriminate | Consequence of each answer |
| --- | --- | --- |
| Specifications only in the representation core, or an additional realist predicable layer | Must the system assert identity and causal/explanatory claims about an unformulated universal, distinct from every specification of it? Test two rival species accounts purporting to describe the same natural kind | Add a typed universal/kind module if required; otherwise retain specs without claiming that this resolves metaphysics |
| Human person, organism and nonphysical subject identity | Is there a supported assertion true of the person but false of the organism, such as a different origin or persistence condition? | Identity or constitution links require an explicit account; the local human-person sense must not settle every possible personhood sense |
| Capability as principal subtype or defined classification | Does changing assessment interest or task change capability membership without changing the disposition? Is that classification a primary browsing need? | Both permit subclass inclusion; the answer determines rigidity annotations and navigation, not automatic rejection of a subtype |
| Functional capacity versus normative/selected function | A broken or repurposed device retains which commitments, and does a biological selected-effect claim require an operative disposition at the evaluated time? | Preserve assignment/selection and capacity separately; select a narrower function profile rather than forcing all senses under Disposition |
| Cavity feature versus host-relative site | Can the same cavity persist while moving, changing shape or changing occupancy, and what fixes its identity? | A host-relative region account can work with these rules; the feature account keeps them explicit. Fixed hosts alone do not prove identity |
| Process/state identity | Does a maintained steady condition and its maintaining activity have the same participants, temporal extent and counterfactual persistence? | Overlap is licensed only for one identified occurrence; otherwise use related state and process records |
| Institutional collective persistence | Test turnover, vacancy, schism, merger and temporary inactivity for one specified organization | Membership is not automatically an extensional set; the accepted rule controls continuance and parent selection |
| Content versus formal individuation | Test a singular proposition about a particular person, two paraphrases, two word-identical independently originated works, and one mathematical expression under two interpretations | Determine when historical provenance individuates a work, when syntax individuates an expression, and when content identity is shared |
| Fictional subject versus literary artifact | Must story-internal detection and actual authorship be predicated of one subject under a dual-predication theory, or of explicitly linked subjects/scopes? | Choose and document an inference policy; do not infer equivalence from a shared record layout |
| Point-based region profile | Does the target physics or mereotopology module require point-free regions or a nonstandard time structure? | Replace the positional point/extent profile with a declared alternative; do not infer fundamental physics from the browser taxonomy |
| Relation context as argument or index | Must users quantify over and compare times, jurisdictions, scales or interpretations inside queries? | Preserve explicit arguments where needed; indexed families need a documented retrieval/application bridge |
| Remaining upper coverage | Require worked classifications of a physical field, absence, natural law, possible world and purported universal, with identity and predication rules | Add a category only when a concrete use case defeats existing definitions; do not assert exhaustive coverage in advance |

The next decision should therefore be a reviewed, bounded sense-and-contract change, not selection of an entire model's tree as winner.

## Work log

### 10.11 Sun Repository-informed Astra critique

- **bef.13:15 PDT:** Inspected candidate arguments and repository surfaces; ran the standalone browser suite, isolated GPT validation and mutations, full browser-graph traversals, rendered-JavaScript probes, source/package hash checks and archived taxonomy comparisons. The 13:15 bound was collected from the system clock during research; earlier individual operation times were not recorded.
- **13:23 PDT:** Recorded completion of the draft and validation: 101 local file/anchor links resolved; the recommended tree has 71 uniquely named, defined nodes at depths 0–3, with exactly six root children. The only uncommitted repository file was this critique. Temporary research downloads were removed.
- Research, candidate revisions, remedies and the bounded upper-tree recommendation are preserved in this separate artifact. No incumbent or preserved independent proposal was modified.
