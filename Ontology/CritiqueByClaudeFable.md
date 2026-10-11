# Critique by Claude Fable: every ontology proposal in the repository, and a revised upper tree

- **Repository:** `BrianHoltz/wiki`, local linked worktree at `Thoughts/wiki`, remote `git@github.com:BrianHoltz/wiki.git`.
- **Revision inspected:** `2c7da0cec4736f489776c03c6226a4ad95abd387` ("Preserve Gemini ontology critique", 2026.10.11.Sun.0926 PDT), **plus the uncommitted working tree**. The working tree carries a staged entity-count batch (23 files) and unstaged edits: the `My Ontology` → `Omniversal Ontology` rename across nine files, and a 560-line rewrite of [CritiqueByGemini.md](CritiqueByGemini.md). Where HEAD and working tree differ, this critique evaluates the working tree and says so.
- **Model and session:** `claude-fable-5-1` (Anthropic) running in Claude Code inside VS Code on the author's MacBook, reasoning effort set to maximum by the operator. The session had full read access to the checkout and shell access for read-only checks.
- **Saved starting position:** [UpperOntologyClaudeFable.md](UpperOntologyClaudeFable.md), commit `aab5e95`. It is treated below as one candidate among five, not as a position to defend.
- **Date:** 2026.10.11.Sun.

## Scope and inventory

### Inspected in full

- Design and workflow documents: [Ontology.md](Ontology.md) (working tree, 1321 lines), [OntologyDesignMemoranda.md](OntologyDesignMemoranda.md), [CriticPrompt.md](CriticPrompt.md), [WordsToCategorize.md](WordsToCategorize.md), [browser-regression-checklist.md](browser-regression-checklist.md), the wiki [index.md](../index.md) and [navigation.md](../navigation.md), the wiki `Makefile` and `.gitignore`.
- Proposals: [UpperOntologyAstra.md](UpperOntologyAstra.md), [UpperOntologyGemini.md](UpperOntologyGemini.md), [UpperOntologyClaudeFable.md](UpperOntologyClaudeFable.md), [CritiqueByGemini.md](CritiqueByGemini.md) in both its committed form (an 83-line blind draft) and its working-tree form (521 lines, repository-informed), and the GPT/Sol package prose: [GPT/README.md](GPT/README.md), [GPT/architecture.md](GPT/architecture.md), [GPT/FORMAT.md](GPT/FORMAT.md), [GPT/stress-tests.md](GPT/stress-tests.md), [GPT/validate.py](GPT/validate.py), and the upper levels of [GPT/ontology-tree.md](GPT/ontology-tree.md).
- Incumbent generator: [SUMO/overlay_canonical.py](SUMO/overlay_canonical.py), which is the actual source of every upper node and editorial definition in the active tree.
- Machine-readable data, traversed programmatically rather than read: [ontology.json](ontology.json) (439 nodes), [sumo.json](sumo.json), [v1010/ontology.json](v1010/ontology.json), [GPT/ontology.json](GPT/ontology.json) (555), [GPT/ontology-proposal.json](GPT/ontology-proposal.json), [GPT/coverage-map.json](GPT/coverage-map.json) (439 rows), [GPT/original-snapshot.json](GPT/original-snapshot.json), [GPT/validation-report.json](GPT/validation-report.json), [GPT/validation-negative-tests.json](GPT/validation-negative-tests.json), [GPT/provenance-checks.json](GPT/provenance-checks.json), [GPT/deliverable-manifest.json](GPT/deliverable-manifest.json), [SUMO/ontology.json](SUMO/ontology.json) (518), [Rogets/ontology.json](Rogets/ontology.json) (1144), [Rogets/crosswalk.json](Rogets/crosswalk.json), [Propaedia/ontology.json](Propaedia/ontology.json) (228), [HumanKnowledge/ontology.json](HumanKnowledge/ontology.json) (103), [Wikipedia/ontology.json](Wikipedia/ontology.json) (12,657), every `snapshot-manifest.json`, [v1010/manifest.json](v1010/manifest.json), [entity-count-references.json](entity-count-references.json), every browser's `entity-counts.json` and `species-counts.json`, and [taxon-species-counts.json](taxon-species-counts.json).
- Git history: the 40 most recent commits, the committed versus working-tree diff of each modified file, and the membership of every revision cited by other critiques.

### Executed

- `python3 GPT/validate.py`: **393 checks passed**; 555 classes, 554 canonical edges, 31 alternate superclass edges, 46 class expressions, 20 predicate instances, 439 of 439 original records mapped (340 revised, 72 disambiguated, 23 faceted, 4 merged aliases), maximum canonical depth 14. The script rewrites `validation-report.json` as a side effect; the regenerated file was byte-identical to the committed one, so the working tree is unchanged.
- `node test_browser.js`: **passed for all seven browsers**. The suite reads files only.
- Python traversals over every `ontology.json`: depth distributions, incoming-edge counts, alternate-parent records, definition provenance, unresolved identifier checks for every count sidecar and crosswalk, and a recomputation of the [WordsToCategorize.md](WordsToCategorize.md) matrix against actual node labels.

### Sampled or not inspected

- Not read: the retired profiles [20_questions_hierarchy.yaml](20_questions_hierarchy.yaml), [v2_20_questions_hierarchy.yaml](v2_20_questions_hierarchy.yaml), the WordNet artifacts, [Wikipedia/categories.json](Wikipedia/categories.json), [GPT/coverage-map.md](GPT/coverage-map.md) (derived from the JSON that was traversed), the lower 780 lines of [GPT/ontology-tree.md](GPT/ontology-tree.md), the contents of the two GPT zip archives (listed only), [SUMO/graft_organism.py](SUMO/graft_organism.py), the Propædia, Wikipedia and Human Knowledge generators, and `render.py` (not executed because it writes browser files).
- Not verified: any live URL; biological placements beyond the 59 NCBI identities and 61 ancestry edges that `validate.py` checks from frozen records; Astra's statement about the extent of its prior exposure; whether the SUMO PDF graph matches the current SUMO KIF hierarchy.
- Every claim below about a node, edge, definition or count was checked against the files named; claims about rendering behaviour rest on the regression suite and on reading `index.html`, not on a browser session.

### Inventory discrepancies

- **No separate "Claude" proposal exists.** [CriticPrompt.md](CriticPrompt.md) lists "Claude" and "your own initial proposal" as distinct candidates; the only Claude-authored artifact in history is `UpperOntologyClaudeFable.md`. This critique treats the two names as one candidate.
- **The committed Gemini critique is the blind draft.** HEAD's `CritiqueByGemini.md` states that it could not reach the repository and evaluates only Gemini's own proposal. The informed critique exists only uncommitted. The commit message "Preserve Gemini ontology critique" therefore preserved a document that critiques none of the repository's proposals.
- **The informed Gemini critique cites a revision from the wrong repository.** Its header gives `7ad197d`, which is not an object in this repository; it is the enclosing Documents repository's commit "Move LLM limits notes to wiki". No revision of this repository is identified.
- **Astra's proposal is not independent.** Its own disclosure records prior project exposure before writing. Agreement between Astra and the incumbent, or between Astra and any later document, cannot be counted as convergence.
- **The Entity definition differs across project artifacts.** `overlay_canonical.py`, `ontology.json` and the excerpt in `Ontology.md` say "That which can be referred to."; `CriticPrompt.md` and the GPT package say "…, even if nonexistent." The critiques of the root definition in all four external proposals address the longer form.

## Repository-wide defects

Each finding names the file and claim, gives the counterexample or inconsistency, a remedy, and the cost. Findings are ordered by consequence within each group.

### Data model cannot carry any proposal's distinctions

- **Where:** the browser schema shared by every `ontology.json`: `id`, `label`, `definition`, `definitionSource`, `children`, `alternateParents`, `directParentCount`.
- **Problem:** every proposal in the repository, including the incumbent's own principles ("roles… should normally be represented as properties, relations, or alternate classifications"), depends on typed non-tree relations (bears, instantiates, specifies, expresses, participates in), on a node-kind marker (class versus specification versus individual), on split policies per sibling group, and on a status attribute (actual, historical, fictional, posited). The active schema can express none of these. The GPT package is the only artifact with a schema that can ([GPT/FORMAT.md](GPT/FORMAT.md): `node_kind`, `child_policy`, `class_expressions`, `predicate_instances`, `dimensions`), and `render.py` drops most of it when producing the browser JSON.
- **Consequence:** reconciliation at the level of labels and parents cannot succeed. "Property" versus "Dependent feature" versus "Quality value" is a distinction between a predicable, a trope and a magnitude; in a schema with only `children`, the three can only be made siblings or ancestors, which is the error that produced the incumbent's Property branch.
- **Remedy:** adopt the GPT data contract (or a trimmed equivalent) as the canonical format for whichever tree wins; make the browser JSON a projection that retains `node_kind`, `child_policy`, alternate parents, and a `status` field. Do this before moving nodes.
- **Cost:** one migration of the generator pipeline and the browser; the regression suite already covers the browser.

### Stale and inconsistent provenance

- [snapshot-manifest.json](snapshot-manifest.json) reports 530 nodes, 533 projected edges, 43 unary nodes, 121 canonical and 414 physical nodes, and points its `upperOntology` field at `../Ontology.md#canonical-synthesis`. The data it describes has 439 nodes, 444 edges, 38 unary nodes, 123 canonical and 321 physical nodes, and no heading in `Ontology.md` produces the anchor `canonical-synthesis` (the JSON itself points at `#upper-ontologies`, which exists). The manifest predates the overlay and was never regenerated.
- `ontology.json`'s `multipleParentNodeCount` is 3, counting only nodes with a recorded `alternateParents` entry (Function, Role, Status). Six nodes appear in two parents' `children` arrays: `GeopoliticalArea` (Agent, Geographic Area), `Group` (Agent, Social entity), `Artifact` (Corpuscular Object, Item), `Organization` (Group, Institutional entity), `Government` (Institutional entity, Political Organization), `Language` (Linguistic Expression, Representational entity). Each appears under both parents, and the data carries nothing that would let the browser mark either placement as an alternate. [GPT/FORMAT.md](GPT/FORMAT.md) already records this ("six multiply-parented records, although its statistics report three"); the incumbent was not corrected.
- The "Our ontology" excerpt in `Ontology.md` lists `Location: To be moved` as a child of Object. No node named Location exists in the data. The two "To be moved —" prefixes that do exist (`Agent`, `Self Connected Object`) are shipped as the nodes' definitions.
- `sumo.json` and `ontology.json` are byte-identical, as are `v1010/ontology.json` and `ontology.json`. A SUMO-named file holding the canonical overlay invites the wrong inference; the v1010 copy is a snapshot and correctly so.
- **Remedy:** regenerate `snapshot-manifest.json` from the overlay output; compute multiple parents from incoming edges, as `validate.py` does; delete the stale Location line; replace placeholder definitions with real ones or with no definition.

### Identifier collisions silently discard definitions

- **Where:** [SUMO/overlay_canonical.py](SUMO/overlay_canonical.py), `CANONICAL` tree and `flatten()`.
- **Problem:** the canonical source declares `Function` twice (under Mathematical entity: "A rule or entity that assigns each allowed input a result"; under Property: "A use or activity an entity is suited or intended to perform"), and likewise `Role` and `Status` (under Social entity and under Property). `flatten()` keeps the first definition, records the second parent as an alternate, and drops the second definition. The result asserts that every mathematical function is a unary property and that a social role is simultaneously an entity that "takes no arguments" (Abstract entity) and one that "takes one argument" (Property). The teleological sense of *function*, which the Property branch intended, does not exist in the data at all.
- **Counterexample:** the heart's function to pump blood has no node; `sin` is classified as something that takes one argument of a bearer.
- **Remedy:** distinct identifiers (`MathematicalFunction`, `TeleologicalFunction`; `RoleSpecification`, `RoleHolding`; `StatusSpecification`, `StatusState`) and a generator check that rejects duplicate ids inside `CANONICAL`.
- **Cost:** three id splits with coverage-map rows; the GPT map already models the split for Role and Status.

### Source extraction artifacts shipped as ontology

- 232 of 439 definitions contain SUMO's `&%` term markup; `index.html` contains no handling for the token, so users read "&%Organization is a corporate or similar institution".
- Two identifiers contain a typographic ligature (`ArtiﬁcialLanguage`, `Certiﬁcate`) and two are misspelled (`Coorporation`, `Senctence`), all from PDF text extraction. The GPT coverage map's four `merged_alias` rows exist only to repair these.
- 74 nodes have no definition: 16 capitalized ids, among them structural nodes (`MicroOrganism`, `Hole`, `State`, `Particle`, `OrganizationUnit`, `Warm-BloodedVertebrate`), and 58 lowercase ids (`advertise`, `attach`, `bet`, `borrow`, `buy`, `calculate`, `order`, `request`, `taste`…) that are SUMO process classes labelled by verbs.
- **Remedy:** strip `&%` at overlay time; normalize ids; either define or remove the undefined classes; label process classes with nouns.

### Crosswalks and coverage claims account for labels, not meanings

- **[WordsToCategorize.md](WordsToCategorize.md)** marks a word present in the Omniversal Ontology when a node label matches exactly (recomputation: one mismatch in 1,040 rows, `artwork`). Exact label match is not concept coverage. `character` is marked present; the node is SUMO's "element of an alphabet", not a fictional character. `function` is present as the mathematical function only. `state`, `order`, `taste`, `substitute` and `request` are marked present and have no definition at all; `state` is the SUMO political territory under Land Area, and the other four are verb-labelled process classes, so the noun senses the word list intends (a state of affairs, an ordering, a flavour) are not covered. The Roget column uses a different criterion (Roget head titles), and the Wikipedia column leaves 47 words unmarked although the word or its plural is a category label in the checked-in snapshot (`object`, `place`, `algorithm`, `concept`, `corporation`, `document`, `ecosystem`, `hole`, `map`…), so columns are not comparable. **Remedy:** record `(node id, sense note)` per cell instead of a check mark, and one matching rule for all columns.
- **[Rogets/crosswalk.json](Rogets/crosswalk.json)** maps 402 Roget concepts to a "curated v1 tree" of 628 leaves whose paths (`Physical / Artifact`, `Abstract / Information and media`, `Abstract / Person or character`…) belong to the retired [20_questions_hierarchy.yaml](20_questions_hierarchy.yaml) profile that `Ontology.md` says is "retained only for analysis". None of its 991 `v1_matches` carry an active node id; 104 of 991 match labels coincide with an active label. The crosswalk is a relic of the retired tree, and nothing in the repository says so. **Remedy:** regenerate against active ids or move it under `v1010/`-style archival with a note.
- **[Propaedia/ontology.json](Propaedia/ontology.json)** supplies all 51 of its "definitions" as "Suggested question: Is it related to 1.1 atoms?", while `Ontology.md`'s principles state that the browser "does not generate suggested questions, and it displays definitions only when supplied by source material or an explicit project definition." The data contradicts the stated policy. **Remedy:** move suggested questions to a separate field or drop them.
- **Credit where due.** Every node reference in [entity-count-references.json](entity-count-references.json) (127 mappings across seven browsers), every per-browser `entity-counts.json`, and every `species-counts.json` resolves to an existing node. The count policies (kinds versus instances versus catalogue records; no roll-up; explicit scope) are the best-specified part of the repository and should be the model for the crosswalks.

### The critique workflow has no acceptance gate

- A blind critique was committed under a message implying a repository critique; a critique citing a revision from another repository is sitting in the working tree; a non-independent proposal is filed beside independent ones with its caveat visible only inside the file; and the protocol names a candidate ("Claude") that does not exist. None of this is caught because nothing checks a critique before it is preserved.
- **Remedy:** a short acceptance checklist applied before `git add` of any `CritiqueBy*.md`: the revision hash resolves in this repository; the inventory names files that exist; every "executed" claim has an output quoted; the independence status is one of {independent, exposed, informed} and is recorded in a one-line index of proposals in `Ontology.md`.
- **Cost:** a dozen lines of Markdown and a minute per import.

## The incumbent Omniversal Ontology

Source of record for the upper levels: [SUMO/overlay_canonical.py](SUMO/overlay_canonical.py); rendered data: [ontology.json](ontology.json). The physical branch below Realized entity is a projection of the SUMO Ontology4 PDF graph with an organism graft.

### The root split crosses two axes and contradicts itself

- **Edge:** `Entity → Realized entity | Abstract entity | Property | Relation`, with definitions "takes no arguments and has spatiotemporal embodiment" / "takes no arguments and lacks spatiotemporal embodiment" / "takes one argument" / "takes more than one argument".
- **Problem:** the first pair splits by embodiment, the second by arity. The two axes cross, so the four cannot be jointly exhaustive and disjoint without a rule for the crossed cells, and the data already occupies crossed cells: `Role` and `Status` are children of Abstract entity (zero arguments) and alternate children of Property (one argument). The Memoranda anticipated exactly this ("this may classify roles in representation/predication, rather than fundamental kinds of being").
- **Counterexample:** this apple's redness is embodied (it is where the apple is) and characterizes one bearer. Under the definitions it is both a Realized entity and a Property.
- **Remedy:** make instantiability the first cut (predicables versus the rest) and let embodiment be a facet; see the recommended tree. GPT's dyad is a lesser repair that keeps the arity confusion out of the root but still has no place for particular features except under "Realized entity".
- **Cost:** every upper id survives; only `Entity`'s children change.

### Abstract persons, institutions and events

- **Edges:** `Person`, `Group`, `Community`, `Institution`, `Event`, `Role`, `Status`, `Relationship`, `Agreement`, `Convention`, `Practice` under `Social entity ⊑ Abstract entity`; `Organization`, `Government`, `Corporation`, `Club`, `School`, `Court`, `Market`, `Currency`, `Law`, `Contract`, `License`, `Policy`, `Office` under `Institutional entity ⊑ Abstract entity`.
- **Problem:** Abstract entity is defined as lacking spatiotemporal embodiment. A person has a mass; a court sits in a building; an event ("a bounded occurrence recognized as socially or otherwise significant") is by definition an occurrence. The branch is a list of socially flavoured words, not a category: it mixes objects (person, organization), kinds of relator (relationship, agreement, contract), predicables (role, status), contents (law, policy, convention, license), occurrences (event, practice) and a reference magnitude (currency).
- **Counterexample:** Socrates is under Abstract entity as `Person` and nowhere under Realized entity except as an instance of `Human`; the data gives no link between the two, so "Socrates weighed 70 kg" and "Socrates was an Athenian citizen" are about two unrelated entities.
- **Remedy:** the relocation table in the reconciliation section distributes these 24 nodes by form. Person's own definition ("An individual human being…") already entails `Person ⊑ Human`.
- **Cost:** 24 moves, all id-preserving; `Organization` and `Government` also lose their second parents.

### Region holds planets; Agent holds territories; Food holds fruit

- `Astronomical Body ⊑ Region ⊑ Object`, Region defined as "an object defined by spatial extent or boundaries". A star is matter, not an extent; the GPT validator carries a negative test for exactly this ("Celestial bodies are not regions").
- `Geopolitical Area` is a child of both `Agent` and `Geographic Area`. A territory is not "an entity capable of intentional action"; the state that governs it is. SUMO's multiple inheritance was projected without review.
- `Food ⊑ Self Connected Object` with children `Beverage`, `Fruit`, `Meat`, `Vegetable`, where `Fruit` is defined botanically ("comes from the flowering part of a FloweringPlant and contain Seeds"). An anti-rigid class (food: a role a portion plays) sits above a rigid anatomical kind. A fallen inedible fruit is a fruit and not food; the edge is false, and it violates the incumbent's own principle "classify by kind, not role". GPT separates `Botanical fruit` from `Fruit food specification`; that split is correct.
- **Remedy:** `Astronomical Body` under the material-body branch; `Geopolitical Area` under Region only, with governance as a relation to a Social Object; `Food` becomes a role (a facet over material portions), with `Fruit` under anatomical structures.

### The biology violates its own acceptance specification

- `Human < Hominid < Primate < Mammal < Warm-Blooded Vertebrate < Vertebrate`. "Warm-Blooded Vertebrate" (birds plus mammals) is polyphyletic; the principles require "every biological subtree monophyletic".
- `Virus < Micro Organism < Organism`, with `Micro Organism` undefined. The principles require "a separate acellular-infectious-agent branch" and say "do not imply that viruses form one clean ranked lineage".
- `Mineral ⊑ Mixture ⊑ Substance`: quartz is a compound, not a mixture; SUMO's placement was inherited.
- The GPT package corrects all three (Mammal under Synapsid under Amniote; `Acellular infectious entity` beside Organism; geological material portions) and checks the first two mechanically.

### Mathematical entity is a field-flavoured grab bag

- Seventeen children under `Mathematical entity ⊑ Abstract entity` mix objects (Number, Set, Function), discipline-named residues (Algebraic, Topological, Analytic, Probability entity — the Memoranda's warning against fields-of-study nodes applies: "Algebraic entity: an entity defined through algebraic operations" is "whatever algebra studies"), texts and acts (Proof, Definition, Formal expression), representations (Physical system model, Mathematical model), and truth-bearers (Proposition, Theorem).
- **Counterexample:** a definition is a sentence that fixes a term; it has an author and a wording and can be ill-formed. A number has none of these. They are siblings here.
- **Remedy:** objects by kind of identity condition (number, collection, mapping, structure, magnitude, proposition); expressions and proofs and models to the construct branch; discipline names to a domain facet. GPT already does most of this (`Abstract structure` / `Mathematical entity` / `Information content`).

### Relation is a flat family index without signatures

- Nineteen leaf children, none with argument places, ranges, or indices; `Classification relation` ("assigns an entity to a kind or category") conflates instance-of with subclass-of and puts the framework's own tie beside domain relations; `Equivalence relation` names a logical property of relations, not a family; `Institutional relation` is a sibling of `Social relation` although every institutional relation is social. [Ontology.md](Ontology.md) already records that the inventory "mixes subject-matter, logical, mathematical, operational, and provenance axes and needs sibling review."
- **Remedy:** in the reconciliation section.

### What should survive from the incumbent

- `Item | Collection | Region` as distinct identity criteria (the body/portion/aggregate split below is its refinement).
- The split between an `Informational entity` branch and a `Representational entity` branch is a confused attempt at the content/expression distinction; the intent survives as Content versus Symbolic Form.
- The social inventory itself, which is more complete than any proposal's.
- The biological acceptance specification, the publishing discipline, the browser regression suite, and the count pipelines.
- The principle "treat ambiguity as information": alternate parents as data, one navigation parent.

## The GPT/Sol package

Source of record: [GPT/ontology-proposal.json](GPT/ontology-proposal.json), built against repository commit `d8619c5`; the 439-record baseline is identical to the current `ontology.json` id set.

### Strengths that no other candidate supplies

- A data contract with per-sibling split policies (192 groups, all `selective`; disjointness `not_asserted` 149, `overlapping` 17, `overlapping_ancestry` 25, `disjoint_in_same_context` 1), 46 defined class expressions for role-like classifications, 20 typed predicate examples, 10 orthogonal dimensions, and 31 recorded alternate superclasses that the browser JSON retains.
- A coverage map with a decision per original record and a validator with six negative mutation tests. The package is the only candidate whose claims about itself can be rerun.
- Carrier versus content (`Printed book ⊑ Manufactured information carrier ⊑ Artifact`; `Book content ⊑ Document content ⊑ Representational content`), specification versus instance (72 disambiguated records: `Quality`/`QualityProperty`/`QualityValue`, `Disposition`/`DispositionProperty`, `Role`/`RoleInstance`, `Obligation`/`ObligationInstance`, `Purpose`/`PurposeInstance`), monophyletic ancestry with retrieved NCBI records, and the `Food`/`Fruit` and `Mineral`/`Water` repairs.

### Organizations are classified as collections and then defined as surviving their members

- **Edges:** `Corporation ⊑ Organization ⊑ Social group ⊑ Collection ⊑ Object`, with `Collection` defined as "an object individuated by its members" and `Social group` as "a collection whose membership is constituted by social recognition".
- **Counterexample:** the United States Senate of 1950 and of 2020 share no member. Under the Collection definition they are two collections; under [GPT/architecture.md](GPT/architecture.md) ("organizations have membership, charter, and recognition aspects"; "Organization is primarily a Social group, with Social object as an additional superclass") they are one organization. The primary parent contradicts the alternate parent's rationale.
- **Remedy:** primary parent `Social object` (identity by recognition under rules), with membership as a relation. Keep `Social group` for groups that *are* individuated by members (a reading circle, a cohort).
- **Cost:** one edge per organization kind; `Human group` ("material aggregate of humans") stays where it is.

### Three social homes, with an entailed edge missing

- `Social object ⊑ Object`, `Social group ⊑ Collection`, and `Socially constituted entity ⊑ Realized entity` (one child, `Institutionally constituted entity`, zero children) coexist. `Social object` ("identity constituted by situated social recognition or practice") satisfies the definition of `Socially constituted entity` ("identity depends on social recognition, interaction, or practice"), yet neither a primary nor an alternate edge asserts `Social object ⊑ Socially constituted entity`. The superclass is a near-synonym that classifies almost nothing.
- **Remedy:** either remove `Socially constituted entity` and attach `Institutionally constituted entity` under `Social object`, or make it the common superclass of `Social object`, `Social group` and the social `Relational state`s and say so in `child_policy`.

### Holes are regions by fiat, against the Region definition

- `Hole ⊑ Spatial region` and `Room ⊑ Spatial region`, and `validate.py` asserts it ("Room and hole denote spaces"). `Region` is "individuated by an extent rather than by what occupies it"; `Hole` is "delimited by an opening or cavity in a surrounding object".
- **Counterexample:** carry the doughnut across the room; the hole comes with it, the region it occupied does not. The hole's identity follows the host, which is the opposite of the Region definition. This is a BFO-style site reading, defensible as a choice, but it is enforced by a test while contradicting the package's own definition.
- **Remedy:** either define Region to admit host-relative delimitation, or move holes and rooms to a host-dependent feature class (Astra's cavity feature; this critique's Topological Feature) and drop the test.

### Context arguments change arity silently

- Thirteen of the twenty predicate instances carry a third argument named `context`, `reference_context`, `scale_context`, `interpretation` or `derivation_context`, with range `Entity`. `part_of`, `located_in`, `participates_in`, `has_quality` and `causally_contributes_to` are declared ternary.
- **Problem:** an untyped third place of range `Entity` is not an argument, it is an index that has been promoted to an argument so that the signature can carry it. The FORMAT contract says "explicitly exposed context arguments make an application relation multiargument" without saying which contexts are indices and which are participants. The prompt's requirement is the mirror image: do not change arity silently. Here the change is explicit but unprincipled.
- **Remedy:** declare per predicate which places are participants and which are indices (time, world, frame, scale), type the indices, and compute arity over participants.

### Classification predicates mix levels

- `predicate:instance_of` takes `individual : Entity` and `class_specification : EntityKind`; `predicate:subclass_of` relates two `EntityKind` specifications. FORMAT insists that the class symbol and its reified specification are distinct, yet the instantiation predicate relates an individual to the specification. The same slip appears in the `Classification relation specification` definition ("connecting an entity to a class it instantiates").
- **Remedy:** `instance_of(individual, class)` and `subclass_of(class, class)` as framework ties outside the domain relations, with `specifies(specification, class)` as the bridge; keep `has_arity` as a genuine higher-order relation.

### Equivalence is not a mathematical family

- `Equivalence relation specification ⊑ Mathematical relation specification`. *Is the same colour as* and *is a compatriot of* are equivalence relations among physical objects and persons. Equivalence (reflexive, symmetric, transitive) is a logical property of relations across every domain, exactly as `has_arity` is; it belongs with the logical features, not under a domain family. `Institutional ⊑ Social` and `Identity ⊑ Logical`, by contrast, are correct nestings.

### A sibling that is also a superclass

- `Human ⊑ Ape` as primary edge, with `Great ape` both Human's alternate superclass and Human's sibling under Ape, done to hold the longest path at 14 edges. The browser then shows Human beside Great ape. The validator enforces the 14-edge ceiling as an invariant. The incumbent's own principle permits compressing uninformative ranks, but it says to hide them, not to demote the child to the hidden rank's sibling. A depth ceiling chosen for display is an arbitrary limit of the kind the prompt rules out.
- **Remedy:** hide the compressed rank in navigation (the browser's lineage view already supports hidden ancestors) or accept depth 15; remove the ceiling from the invariants and keep it as a report.

### Judgements that are design choices, not errors

- `Purpose instance ⊑ Dependent feature` is coherent: the definition includes the assignment ("an intended outcome assigned to a bearer"), which is what distinguishes a paperweight from an indistinguishable pebble. The Gemini critique's objection assumes dependent features must be intrinsic; nothing in the package says so. What is missing is a statement of what the purpose instance depends on besides the bearer (the assigning act or history).
- `Goal content ⊑ Proposition` and `Theorem ⊑ Proposition` are anti-rigid subclasses (a proposition becomes a goal when adopted, a theorem when proved). Permitted by rigidity rules, but the `child_policy` should mark them as status classifications so nobody files a rigid kind beneath them.
- `Event ⊑ Process` with `Event` defined as a bounded process: a terminological choice that loses the process/event aspect contrast; acceptable if stated.
- Retaining `Realized entity | Abstract entity` at the root: the dyad no longer carries the arity confusion, and the package's six realized children do the real work. The cost is that the root pair contributes nothing a user needs and forces "Dependent feature" and "State instance" to be reached through "Realized entity", which no one browses to.

## The Astra proposal

Source: [UpperOntologyAstra.md](UpperOntologyAstra.md). Not an independent sample, by its own disclosure.

### Overlapping roots leave magnitudes with two homes

- `R` (Region) and `M` (Formal entity) are allowed to overlap, and the proposal supplies two classes for a determinate magnitude: `RQP` (quality-space point) and `MVQ` (quantity value). "2 kg" satisfies both definitions. The proposal's navigation rule ("select one genuine superclass per node for primary navigation") is stated for classes, not for the categories an entity falls under; it does not say which of the two is the navigation home of magnitudes.
- **Remedy:** choose one; this critique's view is that quality spaces are Mathematical Structures and their points are Magnitudes, so `RQ` is not needed as a Region subclass.

### Subject is a mixed-axis sibling

- `O → OP (Physical object) | OS (Social object) | OU (Subject)`: the first two split by what grounds existence, the third by a capacity. The proposal says so ("these overlapping classifications use different axes"). The same defect appears in this critique's own proposal (Agent) and in Gemini's reconciled tree (Agentic System); it is treated once, in the departures section, where it is withdrawn.

### Domain splits used as subclass splits, against the proposal's own rule

- Astra's opening section says domain portals "offer additional routes" and "a portal's 'covers subject' link is not a subclass edge". The tree then splits `Process`, `State` and `Quality` by physical / mental / social (`TPP TPM TPS`, `TSP TSM TSS`, `FQP FQE`). Each child is a genuine subclass, so the edges are is-a; the axis, however, is the domain facet the proposal reserved for portals, and the Memoranda require one coherent principle per sibling set.
- **Counterexample:** a conversation is sound (physical), thinking (mental) and an institution-governed exchange (social) at once; three homes under one parent. A temporal-profile split (process / event / state) gives it one home and leaves the domain to the facet.

### Properties are specifications by construction

- `Content → Predicate → Property | Relation` makes every property a "reified condition specification". Instantiation is then satisfaction of a specification, and the realist's universal is explicitly left out ("this core does not identify such a universal with Content"). This is a conceptualist commitment presented as neutrality. It is coherent, and it is the same move the GPT package makes; the cost is that a kind with no specification (an undiscovered species) has no counterpart in the ontology until someone writes one.

### Operative function and capability

- `FD → FDC (Capability) | FDF (Operative function)` places function under disposition and then concedes that a broken watch can retain its purpose "without retaining an operative timekeeping capacity". The concession is correct and shows that the teleological sense of function is not a disposition; Astra files that sense elsewhere ("record the assigned purpose in a specification"). The node label invites the conflation the text avoids.

### What should survive from Astra

- The five-way bookkeeping of admission, denotation, existence claim, satisfiability and narrative attribution: the clearest statement in the repository of what a catalogue entry does and does not assert.
- The argument/index discipline and the worked `HasMass(x, v, t)` derivations; the sentence "moving an object-language context argument into that index creates a derived family and must be documented" is the rule the GPT predicates need.
- The ledger format for splits (axis, justification, objection, boundary case) and the explicit identity-policy requirement for bodies, portions and aggregates.
- Role occupancy distinguished from role specification and from office.

## The Gemini proposal and critique

Sources: [UpperOntologyGemini.md](UpperOntologyGemini.md); [CritiqueByGemini.md](CritiqueByGemini.md) in its working-tree form.

### The initial proposal

- `ConcreteEntity | AbstractEntity | IntentionalEntity` is asserted "disjoint and exhaustive" without argument. Disjointness can always be rescued by splitting one word into several entities, as the proposal does for software (algorithm abstract, source meaning intentional, execution concrete); exhaustiveness cannot be rescued that way, and the proposal never shows where regions, tropes, magnitudes or the mixed cases (a natural language: abstract structure or intentional product?) fall. "A node cannot be both purely abstract (Platonic) and intentional (human-generated)" is a stipulation an intuitionist about mathematics rejects, and the tree offers no neutral reading.
- `Property ⊑ Predicate ⊑ AbstractEntity` and the trope ⊑ `DependentContinuant ⊑ ConcreteEntity`: the proposal itself later calls this a fracture. It is not a fracture; it is the correct distinction between a predicable and a particular feature, made at the wrong depth (a user wanting "mass" must know which they mean before the first click). The remedy is navigation, not merger.
- `TemporalBoundary` as the only sibling of `Process` under Occurrent, and spatial regions as `IndependentContinuant`: a BFO transcription without the parts of BFO that make it work (sites, spatiotemporal regions, the quality/realizable split).
- "Kinds are not grouped under Predicate; only properties are predicates": this confuses the class node (Horse, a tree node) with the kind as a predicable (the thing Secretariat instantiates). Gemini's own reconciled tree later puts `Kind Specification` under `Predicate Specification`, so the initial position was abandoned.

### The working-tree critique: provenance and factual accuracy

- The revision cited does not exist in this repository (see inventory). The statement that biological placements were "verified against retrieved NCBI taxonomy tables embedded in `GPT/ontology.json`" is inaccurate: the browser JSON holds no taxonomy records; they are in `ontology-proposal.json` and the source-evidence archive.
- "Lossy Mergers (4 records): Merging `PhysicalSystemModel` and `MathematicalModel`" is false. Both are `revised` rows with distinct targets; the four `merged_alias` rows are the ligature and spelling repairs.
- "`Agent` was mapped to a faceted class expression `QualifiedObject` with `AgencySpecification`" misreports the data: the expression is `Entity ⊓ satisfies_specification(AgentRole)`, base class Entity, not Object.
- The claims about the incumbent that were checked here are correct: Person, Institutional entity, Quality value, Norm/Obligation/Goal/Purpose, Classification relation, 19 flat relation children, Human demoted beside Great ape.
- "Purpose instance… ontological incoherence" is overstated, as argued above.

### The reconciled tree

- Six level-one categories are declared "jointly exhaustive and mutually disjoint" with no argument beyond a one-sentence gloss. Facts, absences, possible worlds and spacetime as a whole are unplaced; nothing shows they fall under one of the six.
- `Predicate Specification → Kind Specification | Unary Property | Relation Specification` lists a subclass beside its superclass: every kind specification is a unary property specification. This is the arity/metaphysics merger that the Property analysis warns against, in the critique's own recommendation.
- `Agentic System` as a third child of Object, with humans given `Organism` as primary parent and `Agentic System` as a semantic superclass: the mixed-axis construction the critique faults in Astra ("creates a direct identity crisis") and in Claude Fable, reproduced.
- `Process → Physical | Biological | Cognitive`, `Event → Natural | Action | Social`, `State → Physical | Mental | Relational`: domain splits as subclass splits, as in Astra.
- `Functional Capacity: an operative capability selected or engineered… (e.g., conductivity of a wire)`: copper conducts without selection or engineering; the example contradicts the definition. `Computational Model (Turing machine)` under `Symbolic System` (patterns of tokens): an automaton is a mathematical structure, not a notation.
- The stable-identifier guidance proposes `urn:onto:…:v2` URIs; the repository uses plain ASCII ids and already has a per-id migration ledger (the coverage map). The guidance does not connect to either.

### What should survive from Gemini

- The five-tier predication analysis (trope, repeatable condition, quality space, value, contextual assignment) is sound and matches the analysis below.
- The emergency repair list for the incumbent is correct in substance and in priority.
- The insistence on browsing intelligibility at the first level, which motivates the main departure from the Claude Fable proposal below.

## The Claude Fable proposal, as the critic now sees it

Source: [UpperOntologyClaudeFable.md](UpperOntologyClaudeFable.md).

- **The visible `Particular | Predicable` first cut fails the project's traversal criterion.** The Memoranda require that each level "earn its place" and that `Entity` to `Organism` be short; the browser opens the root and first-level nodes by default, so the first level is the menu. A two-item menu, one item of which almost no reader wants, spends the most valuable screen on a logical distinction. The distinction is right; its visibility is wrong. Withdrawn in the departures below, kept as a semantic class.
- **`Agent` as an overlapping child of `Object` mixes axes**, as the proposal admitted. Project evidence against it: the incumbent's "classify by kind, not role", the Memoranda's single-principle test, the GPT package's working facet for agency, and the incumbent's own definition of Person as a human being. Withdrawn.
- **`Physical Object` and `Social Object` were left unexpanded**, which was adequate for an independent sketch and inadequate for a repository whose physical branch holds 321 nodes needing homes for substances, collections and bodies. Expanded below with the identity-criterion split (body / portion / aggregate) that the incumbent's `Item | Collection | Substance` and the GPT `Item | Material portion | Collection` already use.
- **`Relation → Internal | External`** was flagged as the least secure split. The project's users browse relations by family, and the real defect in the repository is missing signatures, not a missing metaphysical split. Withdrawn as a displayed split; signatures made mandatory.
- **The proposal presupposes a typed relation layer** (`inheresIn`, `participatesIn`, `characterizedAs`, `hasValue`, `derivedFrom`) and an ontic-status attribute. The repository's schema has neither, so the proposal's distinctions are currently unimplementable; the GPT contract is the nearest carrier.
- **Dual predication for Characterized Objects is invisible in a one-parent browser.** The design is still right (it is the only one of the five that lets "Holmes is a detective" and "Holmes was created in 1887" both be true without a shadow class), but its payoff requires the schema change above.
- **`Formal Object` under the particulars** drew the objection that mathematical objects read as universals. The placement follows standard logic (numbers are objects, not predicables) and is kept; the label can carry the alias "formal entity". `Proposition` stays under Formal Object with an explicit reason now stated: a proposition's identity is fixed by its structure and constituents, not by an origin, so it is neither a Construct nor a Predicable; singular propositions about contingent individuals are the boundary case and are recorded as unresolved.
- **`Relator`, `Attitude` and `Topological Feature`** were called overhead. The incumbent files debts, marriages, obligations and offices as abstract social words or as properties; without relators those have nowhere correct to go. The categories stay, with the note that a project may leave them unpopulated.
- **The proposal said nothing about biology, counts or crosswalks.** It could not; it is silent, not wrong, and the recommendations below defer to the GPT package's organism backbone and to the incumbent's count pipelines.
- **What survives unchanged:** rigid tree nodes with roles and phases as predicables; the five realization ties kept distinct; the derived-predicate record for every arity change; kind distinct from kind specification; existence as a status, not a class; the "institutional is not one class" distribution table, which is reused below as the relocation plan for the incumbent's social inventory.

## Property and Relation reconciliation

### Five things the word "property" names in this repository

| Tier | What it is | Where it belongs | Incumbent label today | GPT | Astra | Gemini (final) |
| --- | --- | --- | --- | --- | --- | --- |
| Predicable | Repeatable; instantiated by bearers; has an arity | `Predicable → Property` (Kind, Phase, Role, Attribute) and `→ Relation` | `Property`, `Relation` | `Property specification`, `Relation specification`, `Entity kind` | `CP → CPP / CPR`, Kind and Role specification below CPP | `Predicate Specification` |
| Particular feature | This bearer's own quality, disposition, attitude; or a relator binding several bearers | `Feature` | `Quality`, `Disposition`, `Capability` (ambiguously) | `Dependent feature`, `Relational state` | `F` | `Dependent Feature` |
| Magnitude or value | A position in a dimension of comparison; "value" is the role it plays in an attribution | `Formal Object → Magnitude`; nominal values are Attributes | `Quality value` (under Property) | `Quality value`, `Quantity value` | `MV`, also `RQ` | `Evaluation Value` |
| Content | What a norm, goal, plan or design says; zero argument places | `Construct → Content` | `Norm`, `Goal`, `Purpose` (under Property); `Law`, `Policy` (under Abstract) | `Normative content`, `Goal content` | `CD` | `Directive Specification` |
| Role-playing bearer | The portions, objects or agents that currently satisfy an anti-rigid condition | A defined class over the bearers' kind, never a tree node above a kind | `Food`, `Agent`, `Product`, `Weapon` as tree nodes | `class_expressions` (facets) | role occupancy `FRR` plus specification | role facets |

The incumbent's `Property` collapses the first four tiers into one node whose definition ("takes one argument") is true of the first tier only.

### Which children of the incumbent's Property satisfy its definition

The overlay source declares sixteen children; three (`Function`, `Role`, `Status`) are lost to the id collision described above and are included here because the intent is recorded in the source.

| Node | Incumbent definition | Takes exactly one argument? | Counterexample or inconsistency | Disposition |
| --- | --- | --- | --- | --- |
| Quality | "A characteristic describing how an entity is." | Yes, read as a predicable; but the project also uses it for this bearer's quality | Two sacks of 5 kg share one attribute and have two masses; one can change while the other does not | **Split:** `Quality` → Attribute (predicable); new `QualityInstance` → Feature › Quality |
| Quantity | "A property specifying how many, how much, or to what extent." | Yes | Its values are magnitudes, not properties | **Retain** as a magnitude-valued Attribute; cross-link to Magnitude |
| Quality value | "A value that specifies a quality on a scale or comparison." | No; zero places | "5 kg is more than 3 kg" needs no bearer; a value is an argument, not a predicate | **Relocate** to Formal Object › Magnitude (quantitative) or to Attribute (nominal, e.g. *scarlet*) |
| Disposition | "A property that makes an entity liable to behave in a certain way." | Yes as a predicable; ambiguous with the trope | The glass's fragility is destroyed with the glass; *fragile* is not | **Split:** dispositional Attribute and Feature › Disposition |
| Capability | "A property representing what an entity can do or undergo." | Yes as a predicable | A seized pump can do nothing yet keeps its function; a stone's suitability for cracking nuts is a capability for nobody until someone wants nuts cracked | **Relocate** to Role (a role dispositions play relative to an interest and a standard); alternative recorded below |
| Function (Property sense) | "A use or activity an entity is suited or intended to perform." | No; *for*(bearer, activity, source) is ternary | Paperweight versus indistinguishable pebble: no intrinsic difference | **Split id** `TeleologicalFunction` as an External Relation with a derived unary Attribute recorded via saturation; `Function` stays mathematical |
| Purpose | "An intended end that guides an entity or activity." | No; ternary | Same pebble | **Split:** the end → Content; the assignment → External Relation (or Relator when it binds assigner and bearer); derived unary recorded |
| Role (Property sense) | "A property describing an entity's place in a context or activity." | Yes (anti-rigid, relational) | Student, prey, catalyst | **Retain** as Property › Role; the office is a Role instituted by rules; the holding is a Relator |
| Status (Property sense) | "A property describing a recognized condition or standing." | Yes (anti-rigid) | Married, accredited | **Retain** as Property › Role or Phase; the standing itself is a Relator or State |
| Norm | "A rule or standard specifying expected conduct or form." | No; it prescribes, nothing is predicated of a bearer | One norm, two translations; a speed limit binds no one on an empty road | **Relocate** to Construct › Content |
| Obligation | "A requirement binding an agent to an action or state." | No; binds obligor to obligee under a norm | A debt survives repeal of the statute that created it | **Relocate:** the particular → Feature › Relator; the type → Kind of relators |
| Goal | "A desired or intended state treated as an end." | No | Two people share a goal; one abandons it: one Content, two Attitudes | **Split:** Content (what is aimed at) and Feature › Attitude (the aiming) |
| Preference | "A disposition to favor one option or state over another." | No; *prefers*(agent, a, b) is ternary | Intransitive preferences exist; no ordering represents them | **Split:** Feature › Attitude; Relation `prefers`; an ordering → Mathematical Structure |
| Modal property | "A property concerning possibility, necessity, or contingency." | Yes | — | **Retain** under Attribute |
| Logical property | "A property defined by logical form or consequence." | Yes, often of order 2 | *Transitive* applies to relations | **Retain** under Attribute; order recorded |
| Mathematical property | "A characteristic defined or established mathematically." | Yes | — | **Retain** under Attribute |

### Kinds, bearer-specific qualities and the unary question

- A kind is a unary predicable that is rigid and carries identity criteria; it is the subclass `Kind ⊑ Property`. GPT's alternate edge `Entity kind ⊑ Property specification`, Astra's `Kind specification` under `CPP`, and the Claude Fable `Kind` agree on the arity; Gemini's final tree makes Kind Specification a sibling of Unary Property, which lists a subclass beside its superclass.
- A kind specification is a Content that `specifies` a kind; it is not the kind. GPT's package conflates the two in its `instance_of` signature while separating them in prose.
- Bearer-specific qualities (this apple's redness) are Features; their predicables (red) are Attributes; their values (a hue) are Magnitudes or nominal Attributes. The incumbent has one node for all three; GPT has three; Astra has three plus a quality-space point; Gemini has three.
- Dispositions and capacities: the disposition is a Feature; the dispositional predicable is an Attribute; capability is either a Role of dispositions (this critique) or a subclass of Disposition (GPT, Astra, Gemini). The broken-pump case decides nothing here because both sides can say the pump lost a disposition while keeping an assigned function; it decides that *function* is not a disposition.
- Roles: role (predicable, anti-rigid) ≠ role-holding (Relator with dates) ≠ office (a Role instituted by rules, which exists while vacant). The incumbent has one node (`Role`, under Social entity) plus a lost duplicate; GPT has specification and instance; Astra has specification, occupancy and institutional continuant; Gemini has occupancy only.
- Normative content and binding instances: norm (Content) ≠ obligation (Relator) ≠ the proposition that someone is obliged (Proposition). GPT and Astra make this split; the incumbent has none of it.
- Goals, purpose assignments and preference orderings: goal content (Content) ≠ intending it (Attitude) ≠ the assignment of a purpose to an artifact (relation, saturated to a unary Attribute when the end is fixed) ≠ a preference ordering (Mathematical Structure representing Attitudes).

### Relation groupings: the three tests the prompt names

- **Classification versus instantiation.** `instanceOf` (individual to class) and `subclassOf` (class to class) are framework ties, not domain relations; a third tie, `specifies` (specification to class), bridges the reified specification. The incumbent's `Classification relation` ("assigns an entity to a kind or category") names both ties with one node and files it beside causal and spatial relations. GPT types both `instance_of` and `subclass_of` as `ClassificationRelation` and gives `instance_of` an `EntityKind` *specification* as its second argument, so an individual is said to instantiate a specification. Astra keeps "instance of" and "specifies / classifies" out of the subclass graph as distinct relationships. **Verdict:** remove `Classification relation` from the domain inventory; record the three ties in the schema; GPT's two predicates need their second argument typed as a class.
- **Institutional versus social.** Every institutional relation is constituted by collective recognition under a rule, so institutional ⊑ social; nothing is institutional and not social. *Is the mayor of* is both; *is a friend of* is social only. The incumbent lists them as siblings; GPT nests `Institutional relation specification ⊑ Social relation specification`. **Verdict:** nest.
- **Equivalence across domains.** Equivalence is a conjunction of logical features (reflexive, symmetric, transitive) that relations in any domain can have: *is the same colour as* (physical), *is a compatriot of* (social), *is congruent to* (mathematical). The incumbent makes `Equivalence relation` a family beside `Spatial relation`; GPT nests it under `Mathematical relation specification`. **Verdict:** it is a metaproperty, recorded in `logical_features`, not a family; GPT's placement is a domain error.

### Signatures: what every relation record must carry

- `places`: ordered participant places with a name and a range class each; `arity` is their count.
- `indices`: time, world, reference frame, scale, standard of comparison, and institutional context, each typed; an index is not a place. GPT's thirteen `context : Entity` third arguments become indices under this rule, and `part_of`, `located_in`, `participates_in`, `has_quality` and `causally_contributes_to` return to arity 2.
- `derivedFrom`: for every unary predicable obtained from a relation, the base relation, the operation (saturation, value-fixing, existential or universal closure, reflexivization, sortal restriction) and the fixed arguments. *Married* records `∃y married-to(x, y)`; *has the purpose of cutting* records `for(x, cutting, —)` with the third place closed.
- `features`: reflexive, symmetric, transitive, functional, internal or external; `rigidity` and `sortality` for unary predicables; `order` when the predicable applies to predicables.
- `family`: one or more of the incumbent's families (part-whole, spatial, temporal, causal, explanatory, participation, social, institutional, perceptual, epistemic, logical, set-theoretic, mathematical, transformation, representational, provenance) kept as a facet for browsing; `classification` and `equivalence` and `identity` are not families (ties, metaproperty, logical relation respectively).

### What must be renamed, split, relocated, cross-linked or retained

| Action | Items | Why |
| --- | --- | --- |
| Rename | `Property` → keep label, redefine as "unary predicable"; `Realized entity`/`Abstract entity` → facet values, not nodes | The label is standard; the definition is what fails |
| Split | `Quality`, `Disposition` (predicable ⊕ feature); `Function` (mathematical ⊕ teleological); `Role`, `Status` (predicable ⊕ relator/state); `Goal`, `Preference`, `Purpose` (content ⊕ attitude or relation); `Group` (social collective ⊕ physical aggregate ⊕ age-group kind); `Currency` (unit magnitude ⊕ monetary token ⊕ currency system); `Contract` (relator ⊕ terms ⊕ wording) | Each incumbent node currently names two or three entities with different identity conditions |
| Relocate | `Quality value` → Magnitude; `Norm`, `Law`, `Policy`, `Convention` → Content; `Obligation`, `Relationship`, `Agreement`, `License` → Relator; `Event`, `Practice` (the practising) → Occurrence; `Person` → under Human; `Organization`, `Government`, `Corporation`, `Club`, `School`, `Court`, `Market`, `Institution` → Social Object › Institutional Object; `Community` → Social Collective; `Office` → Role; `Astronomical Body` → Material Body; `Geopolitical Area` → Region only; `Virus` → acellular branch; `Proof`, `Definition`, `Formal expression` → Construct; `Physical system model`, `Mathematical model`, `Document`, `Image`, `Audio`, `Video`, `Description`, `Classification`, `Schema`, `Ontology` → Content; `Symbol`, `Name`, `Label`, `Notation`, `Language` → Symbolic Form; `Theorem` → an anti-rigid status over Proposition | Each is under a parent whose definition it fails |
| Cross-link | Attribute ↔ Magnitude (`hasValue` range); Kind ↔ its specifications (`specifies`); Role ↔ Relator (`plays`); teleological Function ↔ Disposition (`groundedIn`, optional); Content ↔ Symbolic Form (`expresses`); carrier objects ↔ Content (`carries`) | The tree cannot express these; the schema must |
| Retain | `Quantity`, `Modal`/`Logical`/`Mathematical property`; the relation families as facet values; `Item`-style identity distinctions; the incumbent's ids wherever the dominant sense survives | Correct as predicables or as navigation |

## Mappings, coverage and reconciliation policy

### Do the existing mappings preserve meaning?

- **GPT coverage map.** The 340 `revised` rows keep the id and reparent; most preserve meaning because the original definitions were short and the new ones are discriminating. The 72 `disambiguated` rows are where meaning is preserved *by splitting*; this is the right pattern and should be the template. The 23 `faceted` rows preserve the classification as a defined class; whether the browser can present a facet as a navigable destination is a presentation question that the map answers only with `canonical_entry`. Three rows preserve a label while changing the sense: `Person` → `Person` (now a role specification), `Food` → `Food` (now a specification class), `Quality` → `Quality` (now the instance class). Keeping the id across a sense change is the one thing a stable-identifier policy must forbid; these three should mint new ids for the new sense and deprecate the old with `replacedBy`.
- **Roget crosswalk.** Label accounting against a retired tree; preserves nothing about the active ontology.
- **WordsToCategorize matrix.** Label accounting; the `character`, `function`, `state` cells show that a check mark is not coverage of the intended concept.
- **SUMO projection.** Honest: PDF-derived edges, primary-parent rule stated, four provisional placements marked in data (`provisionalParent`). The one-parent projection is a navigation choice and is labelled as such.
- **Wikipedia and Propædia browsers.** Wikipedia is presented as a category graph (7,486 multi-parent nodes retained), which is the right honesty; Propædia's generated questions in the definition field are not.
- **Counts.** Independent of the tree by policy, with every reference resolving. Preserve as is.

### Policy for additions, omissions, splits, mergers, broadened meanings, alternate parents and disagreements

- **Identifiers:** an id names one sense forever. A split keeps the id on the dominant surviving sense and mints ids for the others; a merge deprecates ids with `replacedBy`; a broadened or narrowed meaning is a new definition version recorded in `definition_status` with the old text retained in the snapshot, never a silent edit.
- **Ledger:** extend the GPT coverage-map schema with `decision_status` (accepted, modified, rejected, deferred), `decided_by`, `decided_on` and a link to the argument (a section of a critique or memorandum). One row per id, including ids introduced by proposals, so the ledger is the audit trail the Memoranda ask for.
- **No union.** Where two proposals share a label with incompatible definitions (`Quality`, `Region`, `Event`, `Function`, `Role`, `Person`), they are different classes; the ledger records both and the decision picks one per sense. A reconciled node is created only when its definition is written and its sibling policy stated.
- **Alternate parents:** every semantic superclass is recorded; the navigation parent is the one that supplies the identity criterion (body, portion, aggregate, institution…), by rule rather than case by case.
- **Disagreements:** recorded with the discriminating test from the unresolved list below; a disagreement without a test is a preference and is decided by the project owner, recorded as such.
- **Crosswalks:** regenerate against active ids with a `sense` note per cell; archive the retired-tree crosswalk beside `v1010/` with a manifest line saying what tree it targets.

## Recommended upper tree

Three subclass edges below Entity. Indentation is the navigation parent and always a true superclass. "▸" marks deeper categories indicated but not expanded. Node definitions follow; split policies follow those. Compared with the saved proposal, the visible `Particular` node and the `Agent` node are gone, `Physical Object` and `Social Object` are expanded, and `Relation` has no displayed split.

```text
Entity
├── Object
│   ├── Physical Object
│   │   ├── Material Body            ▸ organism, artifact, celestial body, cell, particle
│   │   ├── Material Portion         ▸ water sample, ore, mineral specimen, gas volume
│   │   └── Physical Aggregate       ▸ flock, crowd, forest, asteroid belt
│   └── Social Object
│       ├── Institutional Object     ▸ company, state, court, university, church
│       └── Social Collective        ▸ community, family, ethnic group, movement
├── Occurrence
│   ├── Process                      (domain subtypes are facet values, not children)
│   ├── Event
│   └── State
├── Feature
│   ├── Quality
│   ├── Disposition
│   ├── Attitude                     ▸ belief, desire, intention, preference
│   ├── Relator                      ▸ bond, commitment, obligation, right, role-holding
│   └── Topological Feature          ▸ boundary, surface, hole
├── Region
│   ├── Spatial Region
│   ├── Temporal Region
│   └── Spatiotemporal Region
├── Construct
│   ├── Content                      ▸ work, specification (norm, plan, design, standard), description, record
│   ├── Symbolic Form                ▸ expression, symbol, notation, language
│   └── Characterized Object         ▸ fictional, mythical, posited, impossible
├── Formal Object                    (alias: formal entity)
│   ├── Number
│   ├── Set
│   ├── Function
│   ├── Mathematical Structure       ▸ group, space, graph, automaton, algorithm
│   ├── Magnitude
│   └── Proposition
└── Predicable
    ├── Property                     (arity 1)
    │   ├── Kind
    │   ├── Phase
    │   ├── Role
    │   └── Attribute
    └── Relation                     (arity ≥ 2; families and internal/external are facets; signature required)
```

Two classes exist semantically without a navigation node: **Particular** (the union of the six categories under Entity other than Predicable; "an entity that cannot have instances") and **Agent** (a defined class: an Object of a kind whose members bear Attitudes and perform actions; overlaps Material Body and Institutional Object). Both are declared in the schema and may be shown as portals.

### Definitions

- **Entity** — anything admitted as a value of the ontology's variables: an item falling under at least one category whose definition supplies or inherits an identity criterion, so that it can be told apart, counted and predicated of. Entityhood does not entail existence; every entity carries an explicit ontic status (actual at *t*, historical, posited, refuted, fictional, impossible, contested).
- **Object** — a particular that persists as one whole through time, can change while remaining itself, bears features and takes part in occurrences, and is not itself a feature or occurrence of something else.
- **Physical Object** — an object located in space and bearing physical qualities such as mass, charge or extension.
- **Material Body** — a physical object whose organizing unity makes it one body through change of its matter.
- **Material Portion** — a physical object individuated as an amount of matter of some kind, persisting only while that matter does.
- **Physical Aggregate** — a physical object individuated as a plurality of physical objects under a grouping criterion, without the unity of one body.
- **Social Object** — an object whose existence and unity consist in collective recognition or constitutive rules; constituted by members or a material basis without being identical to them.
- **Institutional Object** — a social object whose identity is fixed by a constitutive rule framework, so that it persists through complete change of members or office-holders.
- **Social Collective** — a social object unified by membership, affiliation or shared practice without a rule framework fixing its identity.
- **Occurrence** — a particular that happens or obtains over time, has temporal phases or is the instantaneous boundary of something that does, and depends on what takes part in it.
- **Process** — an occurrence that is ongoing: it can continue, pause and resume, and any phase of it is an occurrence of the same sort.
- **Event** — an occurrence that is bounded and countable, with a start and end or a culmination; once over, it is fixed.
- **State** — an occurrence consisting in something's being a certain way throughout an interval, with no change required.
- **Feature** — a particular that exists only as a feature *of* one or more specific bearers and cannot move to another bearer.
- **Quality** — a feature fully present whenever it exists and taking a value at each time.
- **Disposition** — a feature that is a readiness to behave in a certain way under certain conditions; it can exist unmanifested.
- **Attitude** — a feature of an agent directed at a content.
- **Relator** — a feature borne jointly by two or more bearers and binding them.
- **Topological Feature** — a feature that is a boundary, surface or void of a host, with location and shape but existing only as something of the host.
- **Region** — a particular that is a portion of space, time or spacetime, identified by extent and position and not by what occupies it.
- **Spatial Region**, **Temporal Region**, **Spatiotemporal Region** — regions extended in space only, time only, or both.
- **Construct** — a particular whose identity is anchored in an origin (an act or tradition of representing) together with what is represented, tied to no single carrier.
- **Content** — a construct at the level of what is meant, presented or prescribed, independent of wording or notation.
- **Symbolic Form** — a construct at the level of signs: a symbol or arrangement of symbols in a language or notation, independent of any one inscription.
- **Characterized Object** — a construct that is what a source presents as an object; identity fixed by the source and the properties ascribed there, whether or not anything satisfies them. Related to properties by `characterizedAs` (ascribed) and `instanceOf` (actual).
- **Formal Object** — a particular whose identity is fixed entirely by a formal definition or structural condition; origin, location and carrier play no part.
- **Number** — a formal object answering "how many" or "how much", identified by its place in a number system.
- **Set** — a formal object identified solely by its members.
- **Function** — a formal object assigning exactly one output to each admissible input, identified by domain, codomain and assignments.
- **Mathematical Structure** — a formal object consisting of a domain with relations or operations on it, identified by that pattern.
- **Magnitude** — a formal object that is a determinate amount, degree or position in a dimension of comparison, identified independently of units and numerals.
- **Proposition** — a formal object that is true or false as a whole, identified by its structure and constituents: what a declarative sentence says and what can be believed or denied.
- **Predicable** — an entity that can be predicated of entities and can have instances (or, for relations, ordered groups of instances); neutral between universals, trope classes and concepts.
- **Property** — a predicable applying to one thing at a time.
- **Kind** — a property that says what its instances are, belongs to each for as long as it exists, and carries a criterion for counting and re-identifying them.
- **Phase** — a property classifying instances by a stage they pass through owing to their own condition, which they can leave while remaining themselves.
- **Role** — a property classifying instances by the part they play relative to something else, which they can leave while remaining themselves.
- **Attribute** — a property that says how its instances are, not what they are.
- **Relation** — a predicable applying to two or more things taken in an order, including variable arity; every relation record carries the signature described above.

### Split policies

Unchanged splits (Occurrence, Feature, Region, Construct, Formal Object, Property) keep the axis, status, justification, objection and boundary cases given in the saved proposal's §6; they are not repeated. Changed or new splits:

| Split | Axis | Status | Justification | Strongest objection | Boundary cases |
| --- | --- | --- | --- | --- | --- |
| Entity → Object, Occurrence, Feature, Region, Construct, Formal Object, Predicable | Instantiability separates Predicable from the rest (by definition); the rest divide by principle of individuation, applied as an ordered series of questions (formal condition? origin plus content? a location? exists only of bearers? unfolds in time? otherwise an object) | Predicable disjoint from each of the six by definition; the six pairwise disjoint, asserted; exhaustive, **not asserted** | Each child supplies an identity criterion; the hidden `Particular` class keeps the logical first cut available to formalization while the menu shows what readers look for | Seven siblings on two axes is not a single-principle split; the Memoranda's §3.5 is satisfied only level by level, not at the root | Facts and states of affairs, absences, possible worlds, fields, spacetime as a whole: unplaced, left at Entity |
| Object → Physical Object, Social Object | What grounds existence and unity: physical constitution versus collective recognition under rules | Disjoint, asserted; exhaustive, not asserted | Removes the mixed-axis Agent sibling; a banknote is a Physical Object playing a role, a company a Social Object | An immaterial mind, if any, is neither; a dualist about persons gets no navigation node for persons other than Human | A crowd (aggregate, not social); a state (social) versus its territory (region) versus its population (aggregate) |
| Physical Object → Material Body, Material Portion, Physical Aggregate | Identity criterion: organizational unity, amount of matter, membership | Pairwise disjoint as identity policies, asserted; coincidence (statue and clay) yields distinct entities; exhaustive, not asserted | The incumbent's `Item / Collection / Substance` and GPT's `Item / Material portion / Collection` already divide this way; the atom-versus-element and molecule-versus-compound cases in the GPT architecture show why | Everyday things lack one settled identity criterion; a repaired ship keeps body identity while losing its portion | Fields and waves (unplaced); a river (body or portion?); a forest (aggregate of trees or body?) |
| Social Object → Institutional Object, Social Collective | Whether a constitutive rule framework fixes identity | Overlap permitted; navigation preference institutional when a rule framework exists; exhaustive, not asserted | The incumbent's two social branches and GPT's `Social object / Social group / Institutionally constituted` show the same need; an institution survives total turnover, a collective is its members-under-a-criterion | Institutions and collectives are historically intertwined; the boundary is contested for nations and churches | An incorporated reading club (both); a family (collective with institutional aspects); a mob (physical aggregate) |
| Relation → (no displayed children) | — | — | Families (spatial, causal, social…) are browsing groupings on a domain facet; internal/external is a theory-laden metaproperty; neither earns a tree level, and the real need is signatures | A reader expects to open Relation and see something; the facet view must be rendered | Equivalence (metaproperty, not family); classification (tie, not relation) |

## Material departures from the saved proposal

- **`Particular` hidden from navigation.** Motivated by the Memoranda's traversal criterion and §15 ("Entity may be the only truly universal tree node"), and by the browser's default view, which opens the root and first-level nodes: the first level is the menu. The class remains declared; the Predicable/non-Predicable disjointness remains asserted on Entity's split policy.
- **`Agent` withdrawn as a tree node; persons placed by kind.** Motivated by the incumbent's principle "classify by kind, not role", the Memoranda's single-principle test, the incumbent's own definition of Person as a human being, and the working facet machinery in the GPT package. Human persons have navigation parent `Human`; *personhood* (legal, moral) is a Role that humans, corporations and possibly artificial systems play. The saved proposal kept Agent to avoid assuming materialism about persons; the project's criteria do not ask for that neutrality, and the cost (a mixed-axis sibling group) was paid by every reader of the tree.
- **`Physical Object` expanded to body, portion, aggregate.** Motivated by the repository's 321-node physical branch, which needs homes for substances, collections and bodies, and by the identity-criterion arguments in the GPT architecture and Astra's ledger.
- **`Social Object` expanded to institutional object and social collective.** Motivated by the incumbent's 24-node social inventory, which has to land somewhere specific, and by the organization-survives-turnover argument that both GPT and Astra make and the incumbent's data violates.
- **`Relation → Internal | External` withdrawn as a displayed split.** Motivated by the incumbent's family inventory, which is what users browse, and by the finding that the repository's actual defect is missing signatures. Internal/external becomes a feature in the signature; families become a facet.
- **Occurrence subtypes by domain declared facet values.** Already the saved proposal's position; restated because three of the other four candidates (incumbent via SUMO, Astra, Gemini) split Process or State by physical/mental/social, and the conversation counterexample shows why that gives one occurrence three homes.
- **Alias "formal entity" for Formal Object.** A label concession to familiarity; no edge changes.
- **Schema dependency made explicit.** The saved proposal assumed ties and a status attribute without saying what carries them. Here the GPT data contract is named as the carrier, which turns the proposal from a sketch into something the repository can implement.

Not departed from, after re-examination against the repository: Formal Object as a particular category; Proposition under Formal Object; works as particulars with derived kinds; Magnitude as particular; the five realization ties; dual predication for characterized objects; order stratification of predicables.

## Unresolved choices and what would discriminate

- **Navigation parent of human persons: `Human` or a separate `Person` object.** Discriminator: does the project need to assert anything true of the person and false of the organism (coming into existence at a different time, surviving as something other than the body)? If no, `Human`; if yes, a `Person` class under Object with `constitutedBy Human`.
- **Capability: a Role of dispositions or a subclass of Disposition.** Discriminator: whether a disposition can become or cease to be a capability with no change in its bearer (interest-relativity). If the project accepts that, Role; if it wants capability to be intrinsic, subclass.
- **Holes and rooms: Topological Feature or Region.** Discriminator: does any use case need the hole to move with its host (a hole in a moving ring, a room in a ship)? If yes, Feature; if all holes are in fixed hosts, Region is harmless.
- **Proposition: Formal Object or Content.** Discriminator: whether the project admits singular propositions about contingent individuals as existing before and after those individuals. If it does, Formal Object is right; if propositions are treated as authored or discovered contents, Content.
- **Region at the first level versus features of fields.** Discriminator: whether jurisdictions, places and intervals are needed as subjects with their own identity (the repository's `Geopolitical Area`, `Geographic Area` and time regions say yes), which keeps Region; a physics module can add relational interpretation without moving the node.
- **Species and other taxa: Kinds, or historical lineages.** Discriminator: whether an organism is an instance of its species or a part of it; this decides what the organism graft's edges mean and whether `Taxon specification` (GPT) is a kind specification or a lineage description.
- **Facets versus nodes for food, weapon, vehicle, product, tool.** Discriminator: whether the browser can render a defined class as a destination with its members listed. If it can, facets; if it cannot, anti-rigid leaf classes (`Food portion ⊑ Material Portion`) are permitted by the rigidity rule as long as no rigid kind sits beneath them.
- **Works and symbol types: particulars with derived kinds, or kinds with tokens.** Discriminator: Menard's *Quixote*; if the project wants one word-sequence and two works, particulars.
- **Characterized objects across adaptations: one entity or one per source.** Discriminator: whether the project wants to say "the Holmes of the 2010 series is Holmes" as identity or as `basedOn`.
- **Whether `Realized entity | Abstract entity` survives as a facet.** It is derivable from the six categories (Object, Occurrence, Feature, Region are realized; Formal Object and Predicable are not; Construct is created and destructible but unlocated). Keep as a dimension for continuity with the GPT package; do not make it a node.

## Audit sequence and bounded branch changes

The order matters: each stage makes the next one checkable. None of them replaces the tree; the recommended tree above is a target for the top three levels, reached by moving branches of the existing 439 (or GPT's 555) under stable ids.

- **Schema first.** Adopt the GPT data contract ([GPT/FORMAT.md](GPT/FORMAT.md)) as the canonical format: `node_kind`, `definition_status`, `child_policy` per sibling group, alternate parents, `class_expressions`, `predicate_instances` with the signature fields above (places, indices, `derivedFrom`, features, family), `dimensions` including ontic status. Make the browser JSON a lossless projection except for layout. Regenerate `snapshot-manifest.json` from the generator. Add a duplicate-id check to `overlay_canonical.py`. Nothing moves yet.
- **Repair demonstrable errors in place.** Bounded branch changes to the active tree, each a coverage-map row with the original definition retained: `Person` under `Human`; `Event` to Occurrence; `Quality value` to Magnitude; `Norm`, `Goal`, `Law`, `Policy`, `Convention` to Content; `Obligation`, `Relationship`, `Agreement`, `License` to Relator; `Purpose`, `Preference`, teleological `Function` split as tabled; `Role` and `Status` split; `Astronomical Body` to Material Body; `Geopolitical Area` out of Agent; `Virus` to an acellular branch; `Warm-Blooded Vertebrate` to a facet; `Food` to a facet with `Fruit` under anatomical structures; `Mineral` to material portions; `Proof`, `Definition`, `Formal expression`, models and documents to Construct; `Language` to Symbolic Form with one parent; `Group` and `Organization` and `Government` given one navigation parent each; `&%` stripped; ligature and spelling ids normalized; "To be moved" removed; the 74 undefined classes defined or dropped. Run `test_browser.js` and the validator after each batch.
- **Decide the top.** Two live options: the seven-way split recommended here, or the GPT dyad with its six realized children. The discriminating question is whether the project wants a first-level menu of categories readers recognize (seven-way) or a two-item logical gate followed by the same categories (dyad). Record the decision in the Memoranda with the reason; either way, the lower structure is GPT's organism backbone and the incumbent's physical projection.
- **Property and Relation pass.** Apply the disposition table: split, relocate, retain as listed; give every surviving predicable its signature; move `Classification relation` out of the domain inventory; nest institutional under social; demote equivalence to a feature. This is the pass that most changes meaning, so each row needs its own ledger entry.
- **Social inventory relocation.** Apply the relocation table to the 24 social and institutional nodes; create `Institutional Object` and `Social Collective`; record the organization-versus-collection decision for GPT's `Social group`.
- **Crosswalks re-aimed.** Regenerate the Roget crosswalk against active ids and archive the retired-tree version; replace the word-matrix check marks with `(id, sense)`; move Propædia's generated questions out of the definition field; leave the count pipelines alone.
- **Critique gate.** Add the acceptance checklist to `CriticPrompt.md`; add a one-line proposal index to `Ontology.md` recording each candidate's independence status (Astra: exposed; Gemini, Claude Fable: independent in phase one; GPT: built against commit `d8619c5` with repository access); commit the informed Gemini critique, with a correct revision, in place of the blind draft only if its author or the project owner confirms that is the intended import.

Things not to do: assemble a union of the five label sets; reuse an id for a new sense; introduce a depth ceiling as an invariant; add root categories to absorb the unplaced items (facts, absences, fields) before a use case needs them.

## Provenance

- **Revision:** `2c7da0cec4736f489776c03c6226a4ad95abd387`, branch `main`, inspected 2026.10.11.Sun together with the uncommitted working tree described in the header.
- **Tools run:** `python3 GPT/validate.py` (393 checks passed; regenerated report byte-identical to the committed file), `node test_browser.js` (seven browsers passed), read-only Python traversals of every `ontology.json`, `coverage-map.json`, `ontology-proposal.json`, count and crosswalk files, and `git` history and diff commands. No renderer or generator was executed; `validate.py` rewrote `GPT/validation-report.json` with identical bytes; no other file's content was changed, and this file is the only one created.
- **External sources:** none newly consulted in this session. The external basis for the categorial arguments is the source list in [UpperOntologyClaudeFable.md](UpperOntologyClaudeFable.md) §13; the repository's own citations (SUMO, BFO, DOLCE, UFO, OntoClean, LRM, CIDOC CRM, QUDT, OWL 2) were not re-opened.
- **Limitations:** no live retrieval; biological placements checked only through the frozen NCBI records the GPT validator uses; the Wikipedia, Propædia, Roget and Human Knowledge generators were not read; the two GPT zip archives were listed, not opened; no browser was driven, so rendering claims rest on the regression suite and on reading `index.html`.
- **Unresolved findings:** whether the working-tree Gemini critique is intended for import as is; which tree `Rogets/crosswalk.json` should be regenerated against; whether `sumo.json` is meant to remain a copy of `ontology.json`; the origin of the Property-branch `Function`/`Role`/`Status` duplicates in the overlay source (deliberate or accidental); and every item in the unresolved-choices list above.

*Prepared by `claude-fable-5-1` in Claude Code in VS Code.*
