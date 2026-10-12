# Upper Ontology — Astra

**Status:** a proposed upper ontology for organizing and understanding knowledge, with a preferred browsing tree and additional typed relationships. It is a design to evaluate, not a claim that the categories are uniquely correct.

**Independence disclosure.** This session received prior project context before this proposal. The user subsequently authorized proceeding despite that exposure. This therefore cannot be represented as a blind test. No project materials were retrieved as research sources for this proposal. The arguments below are presented on their own merits, with external commitments distinguished from design choices; that procedure cannot guarantee that earlier exposure had no influence.

**Label and metadata.** “Astra” identifies the authoring model. The exact model version and reasoning setting are not recorded.

## 1. Recommendation and scope

Use **Entity** above six principal categories: **Object, Occurrence, Particular feature, Region, Content, and Formal entity**. Organize these primarily by how their subjects are individuated, what they depend on, and what kinds of predication they support. Treat the six as an **open collection of partly overlapping categories**, not an exhaustive metaphysical partition. In particular, Content can overlap Formal entity, and Region can overlap Formal entity.

Use a subclass graph as the semantic structure and select one genuine superclass per node for primary navigation. Add explicit relationships for bearing features, participating in occurrences, expressing content, satisfying specifications, and assigning values. Domain portals such as Biology, Mathematics, and Fiction should offer additional routes into this structure. A portal’s “covers subject” link is not a subclass edge.

This recommendation makes substantive choices. It distinguishes persisting objects from occurrences, recognizes particular features, and admits descriptions and formal subjects into discourse. It leaves open whether mental subjects are physical, whether mathematical entities exist independently of thought, and whether fictional characters are abstract artifacts. The absence of those commitments does not make the proposal metaphysically neutral in every respect.

The display below stops at **three subclass edges below Entity**. A node at the boundary can have further subclasses, but those are not promoted into an earlier level. Examples in later sections illustrate classifications; they are not an additional domain inventory.

## 2. Entity, reference, and existence

The proposed working definition was:

> That which can be referred to, even if nonexistent.

It usefully prevents “has a catalogue entry” from implying “exists in the actual world.” It nevertheless leaves four problems.

1. **Successful reference is presupposed.** An expression may be meaningful without successfully identifying a referent. Describing “the largest prime” does not supply such a prime.
2. **Reference lacks a context.** The same name can identify different subjects in different narratives or conversations. A pronoun requires an assignment or discourse situation.
3. **Mention can be mistaken for constitution.** Writing an inconsistent description does not establish an object satisfying it. Otherwise arbitrary descriptions generate unrestricted existence commitments.
4. **Referability is a poor test of reality.** An entity’s existence should not depend on whether somebody can currently name or describe it. Conversely, an identifiable topic need not be actual.

For this knowledge system, use the more precise scope definition:

> **Entity:** an individuated subject admitted to a specified domain of discourse for identification and predication; admission alone asserts neither actual existence nor realizability.

“Individuated” means that the system has an explicit identity policy or a provisional reference anchor with its ambiguity recorded. It does not mean that every identity question has been settled. “Admitted” is a representation policy, not an existence-producing operation. This is a definition of the ontology’s range of discussion, rather than an attempted analysis of being itself.

Keep three things distinct: **an expression**, **a record anchoring an intended reference**, and **the subject that the expression purports to identify**. A record can exist even when its expression fails to denote. Categories describe subjects; they do not covertly become classes of database records.

For an actual-world interpretation, reference can be partial. For narrative discussion, a locally identified subject can be admitted without a successful actual-world denotation. Statements then retain their scope: “Holmes is a detective in the stories” and “Holmes is a fictional character discussed by readers” need not predicate the same kind of thing of the same ontological interpretation of Holmes. A theory treating the character as an actual literary artifact may introduce a separate, explicitly related subject.

The formal bookkeeping should distinguish:

| Notion | What it licenses | What it does not license |
| --- | --- | --- |
| Admission to discourse | An identifier and scoped statements about a subject | Actual existence or consistency of its description |
| Denotation | An expression identifies a subject under an interpretation | Existence in every interpretation |
| Existence claim | Existence under a stated world, time, and ontological account where relevant | Physical location, unless that is separately asserted |
| Satisfiability | A description has a model under specified constraints | Actual instantiation |
| Narrative attribution | A source presents a subject as having a characteristic | An unqualified actual-world assertion of that characteristic |

Do not implement Entity as a universal mathematical set containing every possible object, predicate, and class, including itself. Use typed domains and explicit metamodeling levels. The definition is not a comprehension principle.

**Alternative:** reserve Entity for existents and introduce a separate catalogue of descriptions and attempted references. That gives a cleaner realist ontology, but it would change the requested root’s intended scope. Another alternative, Zalta’s abstract-object theory, gives fictional predication a substantive treatment using encoding as distinct from exemplification.[10] This proposal instead uses scoped attributions without adopting that theory’s abstract-object ontology.

## 3. What the nodes and edges mean

Every displayed node denotes a **class of subjects of the stated kind**. Every indentation means subclass inclusion. At a fixed, admissible interpretation and scope:

\[
\operatorname{SubClass}(A,B)\quad\Rightarrow\quad
\forall x\,[A(x)\rightarrow B(x)].
\]

Core inclusions are intended to hold throughout the interpretations accepted by this design, rather than merely because all currently catalogued examples happen to fit. Subclass inclusion does not assert that a class has members.

An individual is a subject treated as one item at the level of the assertion: a particular cup, an episode, a number, or a reified predicate specification. **Individual is not a synonym for physical particular.** A specification can be an individual in the metamodel while classifying other individuals.

A class is first a logical classification construct here; it is not automatically another individual in the subject domain. Its specification can be reified, and an extension can be represented within an appropriate mathematical framework, but those are explicit additional representations. A realist theory may also posit a property universal distinct from every specification of it. This core does not identify such a universal with Content: an extension would need to state the universal's category and its relation to specifications and instances.

The following distinctions are mandatory:

| Item | Example and treatment |
| --- | --- |
| Class | **Dog**, whose members are dogs; a subclass of an appropriate animal class in a later domain extension |
| Reified kind specification | **dog-spec**, an individual specification of what counts as a dog under a stated account |
| Unary predicate | The condition supplied by dog-spec, applicable to one subject; its extension determines the Dog class in an interpretation |
| Expression | The string “dog,” or a formal expression used to express that specification; neither is a dog |
| Particular feature | This cup’s particular color or fragility, dependent on this cup |
| Realization | A particular breaking process that manifests this cup’s fragility; it is neither the fragility nor its specification |
| Value | A specified magnitude or category used to determine a feature, such as 2 kg or a designated color-space position |

Thus, **dog-spec is an instance of Kind specification**, while **Dog is a subclass of Animal**. Dog is not thereby a subclass of Kind specification. Likewise, a fragile cup satisfies a unary condition; a breaking episode manifests its fragility. These are different relationships.

For a reified unary specification \(p\), define its interpreted extension by:

\[
\operatorname{Ext}_{I,c}(p)=
\{x\in D_{I,c}:\operatorname{Sat}_{I,c}(p,x)\}.
\]

This is interpretation-relative semantics, not an identity between the specification and a mind-independent set. Distinct specifications can have the same extension. “Creature with a heart” and “creature with a kidney” would not become the same specification merely because a chosen dataset gave them the same members.

A class identifier and a specification identifier should normally be separate, connected by an explicit interpretation or “classifies” bridge. OWL 2 permits class/individual metamodeling, but its Direct Semantics interprets the class and individual views independently.[6] Reusing an identifier therefore does not supply this bridge automatically.

## 4. Upper tree with discriminating definitions

A compact view of the same classes defined below. Every branch means is-a; siblings are not asserted to be disjoint or exhaustive.

```text
Entity
├── Object
│   ├── Physical object
│   │   ├── Material body
│   │   ├── Material portion
│   │   └── Physical aggregate
│   ├── Social object
│   │   ├── Institutional continuant
│   │   └── Social collective
│   └── Subject
│       ├── Experiencing subject
│       └── Intentional agent
├── Occurrence
│   ├── Process
│   │   ├── Physical process
│   │   ├── Mental process
│   │   └── Social process
│   ├── Event
│   │   ├── Transition event
│   │   └── Achievement event
│   └── State
│       ├── Physical state
│       ├── Mental state
│       └── Social state
├── Particular feature
│   ├── Quality
│   │   ├── Physical quality
│   │   └── Phenomenal quality
│   ├── Disposition
│   │   ├── Capability
│   │   └── Operative function
│   ├── Relational feature
│   │   ├── Role occupancy
│   │   └── Normative position
│   ├── Structural feature
│   │   ├── Boundary feature
│   │   └── Cavity feature
│   └── Intentional attitude
│       ├── Belief attitude
│       ├── Conative attitude
│       └── Preference attitude
├── Region
│   ├── Spatial region
│   │   ├── Spatial point
│   │   └── Spatial extent
│   ├── Temporal region
│   │   ├── Temporal instant
│   │   └── Temporal extent
│   ├── Spatiotemporal region
│   │   ├── Spatiotemporal point
│   │   └── Spatiotemporal extent
│   └── Quality-space region
│       ├── Quality-space point
│       └── Quality-space range
├── Content
│   ├── Predicate
│   │   ├── Property
│   │   └── Relation
│   ├── Propositional content
│   ├── Directive specification
│   │   ├── Goal specification
│   │   ├── Plan specification
│   │   └── Norm specification
│   └── Descriptive content
│       ├── Model specification
│       └── Narrative content
└── Formal entity
    ├── Mathematical entity
    │   ├── Number
    │   ├── Mathematical collection
    │   └── Mathematical structure
    ├── Symbolic structure
    │   ├── Linguistic expression
    │   ├── Formal-language expression
    │   └── Diagrammatic expression
    └── Value
        ├── Quantity value
        └── Category value
```

The codes identify nodes for the constraint and argument tables. Depth is determined solely by indentation: E is depth 0; its children, grandchildren, and great-grandchildren are depths 1, 2, and 3. **Every edge in this list is is-a.** Bracketed comments do not add edges.

- **E — Entity:** an individuated subject admitted to a specified domain of discourse for identification and predication, without existence or realizability being implied.
    - **O — Object:** a particular bearer tracked as the same subject through its career, rather than identified as an occurrence, a dependent feature, a region, repeatable content, or a formal item as such.
        - **OP — Physical object:** an object individuated through a material body, a portion of matter, or a physical grouping.
            - **OPB — Material body:** a physical object with an organizing unity supporting its treatment as one body through relevant changes of material constituents.
            - **OPM — Material portion:** a physical object individuated by a specified amount or collection of matter, with material retention central to its identity policy.
            - **OPA — Physical aggregate:** a physical object individuated as a plurality of physical members under an explicit grouping criterion, without requiring the unity of one body.
        - **OS — Social object:** an object whose identity or persistence requires social practices, membership, recognition, or constitutive rules.
            - **OSI — Institutional continuant:** a social object whose identity is maintained by an identifiable institutional rule framework, including objects that survive changes of their occupants or participants.
            - **OSC — Social collective:** a social object individuated as a group through social membership, affiliation, or interaction.
        - **OU — Subject:** an object admitted as a center of experience or intentional agency; no material constitution is required by this definition.
            - **OUE — Experiencing subject:** a subject to which episodes with a phenomenal perspective are attributed.
            - **OUA — Intentional agent:** a subject capable of acting under intentions or commitments, rather than merely occurring as a causal participant.
    - **T — Occurrence:** a particular happening or obtaining episode individuated through its temporal unfolding or temporal extent.
        - **TP — Process:** an occurrence identified through an unfolding activity, operation, or change, with its course relevant to its identity.
            - **TPP — Physical process:** a process identified through changes or operations of physical systems.
            - **TPM — Mental process:** a process identified through cognitive, affective, or experiential activity, without a reduction to a physical process being stipulated.
            - **TPS — Social process:** a process identified through social interaction, coordinated practices, or institutional operations.
        - **TE — Event:** an occurrence individuated as a bounded happening under a stated event criterion, whether brief or extended.
            - **TET — Transition event:** an event individuated by a change from one specified condition to another.
            - **TEA — Achievement event:** an event individuated by reaching a specified endpoint or satisfaction condition, whether or not the endpoint was anyone’s goal.
        - **TS — State:** an occurrence individuated by the obtaining of a specified configuration or condition during an interval, rather than by the detailed course producing or maintaining it.
            - **TSP — Physical state:** a state whose identifying condition concerns the configuration or condition of a physical system.
            - **TSM — Mental state:** a state whose identifying condition concerns experience, cognition, or an attitude of a subject.
            - **TSS — Social state:** a state whose identifying condition concerns social relationships, practices, or institutional standing.
    - **F — Particular feature:** a particular characteristic whose identity depends on specified bearers or hosts, and sometimes on an external context; distinct from a predicate specifying a characteristic.
        - **FQ — Quality:** a particular feature characterized by a determination in a quality domain, without requiring a manifestation process to specify that determination.
            - **FQP — Physical quality:** a quality characterizing a physical bearer or physical aspect, such as this sample’s mass.
            - **FQE — Phenomenal quality:** a quality characterizing how an experience feels or appears from a subject’s perspective.
        - **FD — Disposition:** a particular feature grounding a tendency or capacity for manifestations under specified conditions, whether or not any manifestation occurs.
            - **FDC — Capability:** a disposition assessed against a designated performance or task criterion under stated enabling conditions.
            - **FDF — Operative function:** a disposition attributed an expected contribution because of a specified design, selection, or sustaining practice; this node concerns an operative capacity, not merely an assigned purpose.
        - **FR — Relational feature:** a particular feature whose individuation requires its bearer’s connection to other entities or to an external contextual framework.
            - **FRR — Role occupancy:** a bearer’s particular holding of a contextual position, distinguished from the reusable role specification and from its bearer.
            - **FRN — Normative position:** a bearer’s particular standing as subject to an obligation, permission, entitlement, prohibition, or institutional power under a stated normative framework.
        - **FS — Structural feature:** a host-dependent feature individuated by structural or topological organization, rather than merely by a value describing that organization.
            - **FSB — Boundary feature:** a structural feature delimiting a host or one of its parts, whose identity follows that host rather than a fixed coordinate location.
            - **FSC — Cavity feature:** a structural feature individuated as a hole or void relative to a surrounding host, rather than as the matter occupying it or a fixed spatial region.
        - **FA — Intentional attitude:** a particular feature of a subject consisting in an orientation toward content or a target, without requiring the target to exist.
            - **FAB — Belief attitude:** an intentional attitude of taking some propositional content to be true.
            - **FAC — Conative attitude:** an intentional attitude of desiring, intending, or committing to the obtaining of an outcome or the performance of an action.
            - **FAP — Preference attitude:** an intentional attitude of ranking alternatives under an evaluative context, without necessarily intending to obtain the preferred alternative.
    - **R — Region:** a nonempty locus or extent within an explicitly specified spatial, temporal, spatiotemporal, or other structured domain; distinct from an occupant and from its coordinate description.
        - **RS — Spatial region:** a region in a specified spatial domain or spatial frame.
            - **RSP — Spatial point:** a spatial region consisting of one position in that domain.
            - **RSE — Spatial extent:** a spatial region comprising more than one position, whether connected or disconnected and regardless of dimension.
        - **RT — Temporal region:** a region in a specified temporal domain or temporal ordering.
            - **RTI — Temporal instant:** a temporal region consisting of one temporal position.
            - **RTE — Temporal extent:** a temporal region comprising more than one temporal position, including a possibly disconnected collection of intervals.
        - **RX — Spatiotemporal region:** a region in a domain jointly individuated by spatial and temporal positions.
            - **RXP — Spatiotemporal point:** a spatiotemporal region consisting of one joint position.
            - **RXE — Spatiotemporal extent:** a spatiotemporal region comprising more than one joint position.
        - **RQ — Quality-space region:** a region in a stated space of qualitative or quantitative determinations, as distinct from a spatial or temporal location.
            - **RQP — Quality-space point:** a quality-space region consisting of one determination in that space.
            - **RQR — Quality-space range:** a quality-space region containing more than one determination, used, for example, for an interval or tolerance region.
    - **C — Content:** an entity individuated by what is presented, asserted, prescribed, or specified under an interpretation, rather than by the particular carrier or symbol pattern expressing it.
        - **CP — Predicate:** a reified condition specification with a declared, fixed, finite number of one or more argument positions, whose application yields a truth-evaluable claim or satisfaction assessment under an interpretation.
            - **CPP — Property:** a Predicate with exactly one argument position; an applicable unary condition, not a particular feature or a numerical attribute schema.
            - **CPR — Relation:** a Predicate with two or more argument positions; it specifies a condition on an ordered tuple, not the tuple, a connecting object, or an individual relational feature.
        - **CA — Propositional content:** content presenting something as being the case, assessable for truth once interpretation and contextual parameters have been supplied. [No additional universal split is adopted here.]
        - **CD — Directive specification:** content setting an outcome, conduct, or performance standard to be pursued, followed, or assessed, rather than merely reporting its obtaining.
            - **CDG — Goal specification:** a directive specification identifying a target condition or outcome, whether or not any agent adopts it.
            - **CDP — Plan specification:** a directive specification organizing actions, constraints, or contingencies for pursuit of an outcome.
            - **CDN — Norm specification:** a directive specification prescribing, permitting, prohibiting, or conferring standing or powers within a specified normative framework.
        - **CC — Descriptive content:** content organizing a representation of a target, system, or episode beyond a single open condition or closed proposition.
            - **CCM — Model specification:** descriptive content specifying a selective representation of a target system, with the intended correspondence or interpretation made explicit.
            - **CCN — Narrative content:** descriptive content organizing multiple attributed situations or happenings into an account, without requiring that account to be true or internally consistent.
    - **M — Formal entity:** an entity individuated by mathematical, logical, symbolic, or evaluation rules in an explicit framework, rather than by a particular physical career; this does not assert mind-independent existence.
        - **MM — Mathematical entity:** a formal entity specified within a mathematical theory by its definitions, operations, relations, or structural position.
            - **MMN — Number:** a mathematical entity occupying a numerical role in a specified number system, rather than a numeral expressing it.
            - **MMC — Mathematical collection:** a mathematical entity constituted by specified membership, multiplicity, or ordering rules, with its equality criterion supplied by the theory.
            - **MMS — Mathematical structure:** a mathematical entity comprising one or more domains equipped with specified operations, relations, or distinguished elements, considered under an explicit identity or equivalence criterion.
        - **MS — Symbolic structure:** a formal entity individuated as a repeatable pattern of signs under a syntax or notation, distinguished from its individual inscription and from its interpreted content.
            - **MSL — Linguistic expression:** a symbolic structure organized under a language for linguistic expression, such as a word sequence or a sign-language expression type.
            - **MSF — Formal-language expression:** a symbolic structure governed by an explicit formal grammar, such as a formula or a program expression.
            - **MSD — Diagrammatic expression:** a symbolic structure whose spatial, graphical, or other nonsequential relations contribute to its interpretation under a notation.
        - **MV — Value:** a formal entity admitted as a determinate result or position in a stated evaluation domain, distinct from an arbitrary object merely stored in a database field.
            - **MVQ — Quantity value:** a value determining a magnitude of a stated quantity kind under a scale or unit convention, rather than the bearer’s particular quantity feature.
            - **MVC — Category value:** a value identifying an alternative in a stated classification or evaluation scheme, with identity given by that scheme rather than by its label alone.

**Depth discipline.** All depth-3 nodes remain open for later expansion. For example, Organism belongs below Material body; Biological process below Physical process for a biological profile that adopts this physical-process classification; Organization below Institutional continuant; Kind specification and Role specification below Property; Integer below Number; and Mathematical mapping below Mathematical structure. Their complete paths, not shortened substitutes, are used when they are discussed below. There is no hidden Continuant or Abstract superclass being omitted from this proposed tree: those organizing alternatives have not been adopted as nodes of this core.

Propositional content stops at depth 2 deliberately. “Atomic/compound” depends on the representational language and granularity, “singular/general” does not provide a clean universal partition, and “true/false” concerns evaluation. Those distinctions may be useful facets or later theory-specific classes, but none earns a universal third-level split here.

Social rules and formal rules supply different identity conditions in this proposal. An institution depends on a history of enactment, practice, or recognition; formally describing those rules does not make the institution a Formal entity. Similarly, describing a physical object mathematically does not identify it with its model. CCN uses a deliberately composite sense of narrative content; an isolated fictional proposition can belong to CA without belonging to CCN.

## 5. Overlap, disjointness, and exhaustiveness

These are **stipulated constraints of this design**, not deductions from typography or claims that competing metaphysics are contradictory. They apply within one identity interpretation and assertion scope. Quoted claims from an inconsistent narrative are handled as claims, not imported as an inconsistent set of core axioms.

“Open” means that the listed children are not asserted to exhaust their parent. “No disjointness axiom” permits overlap; it does not assert that an overlapping instance must exist. Missing classification is not evidence of nonmembership.

| Parent | Sibling constraints and coverage |
| --- | --- |
| **E** | Open. O, T, and F are pairwise disjoint in the chosen identity profile; each is also disjoint from R, C, and M. C and R are disjoint. C–M and R–M overlap is permitted. These are all the root pair constraints. |
| **O** | OP, OS, OU: open; no pairwise disjointness is imposed. An embodied subject can be OP and OU. Whether a particular socially constituted object is identical to a physical object requires an explicit identity account. |
| **OP** | OPB, OPM, OPA: open; overlap is permitted when the same identity policy supports it. An aggregate may also have bodily organization. Do not merge a clay portion and a reshaped artifact merely because they coincide. |
| **OS** | OSI, OSC: open and overlapping; an institutional organization can also be a social collective. |
| **OU** | OUE, OUA: exhaustive by the chosen definition of Subject; overlapping. Experience does not entail agency, nor does attributed collective agency establish experience. |
| **T** | TP, TE, TS: open; no global pairwise disjointness. A sustained operation can be described as both a process and a steady state; a bounded process can be an event. Any identification must concern the same occurrence, not just related occurrences. |
| **TP** | TPP, TPM, TPS: open; overlap permitted. An identity between a mental and physical process needs an account, not an automatic reduction rule. |
| **TE** | TET, TEA: open; overlap permitted. Reaching a destination can be a transition and an achievement. |
| **TS** | TSP, TSM, TSS: open; overlap permitted where the same condition is being individuated. Correlation alone establishes no identity. |
| **F** | FQ, FD, FR, FS, FA: open; no general pairwise disjointness. A standing belief may have a dispositional analysis; a role occupancy can carry a normative position. Overlap needs justification for the particular feature. |
| **FQ** | FQP, FQE: open; no disjointness. Identifying a phenomenal and physical quality is permitted but not required. |
| **FD** | FDC, FDF: open and overlapping. An operative function can meet a capability criterion; fragility need be neither under a chosen task description. |
| **FR** | FRR, FRN: open and overlapping. Holding an office can itself confer a normative standing; not every role is normative and not every obligation arises from an office. |
| **FS** | FSB, FSC: disjoint under the selected delimiting-feature versus void-feature identities; open. A cavity’s boundary is not the cavity. |
| **FA** | FAB, FAC, FAP: open; no pairwise disjointness is imposed on a single complex attitude. Prefer separate attitudes where their contents or persistence differ. |
| **R** | RS, RT, RX, RQ: pairwise disjoint by their typed ambient domains; open to other region domains. A spatial coordinate tuple, a spatial location, and a quality-space position need not be identical. |
| **RS** | RSP and RSE: disjoint and exhaustive for nonempty spatial regions, relative to the chosen spatial domain. |
| **RT** | RTI and RTE: disjoint and exhaustive for nonempty temporal regions, relative to the chosen temporal domain. |
| **RX** | RXP and RXE: disjoint and exhaustive for nonempty spatiotemporal regions. |
| **RQ** | RQP and RQR: disjoint and exhaustive for nonempty quality-space regions. An empty tolerance set is a formal collection, not an RQ region in this convention. |
| **C** | CP, CA, CD, CC: open. CP is disjoint from the other three as a single open condition specification; CA and CC are disjoint by the “beyond a single proposition” convention. CD can overlap CA or CC when the same individuated content has directive and assertoric or descriptive force. |
| **CP** | CPP and CPR: disjoint and exhaustive because CP is explicitly restricted to fixed finite positive arity. Zero-argument propositions and variable-arity schemas are excluded from CP as defined. |
| **CD** | CDG, CDP, CDN: open; overlap permitted when a specification actually satisfies several definitions. Containing a goal as a part does not by itself make a whole plan a Goal specification. |
| **CC** | CCM, CCN: open; overlap permitted. A simulation scenario can both specify a model and organize a narrative. |
| **M** | MM, MS, MV: open; overlap permitted if their identity policies coincide. A number may be a value. Representing an entity by a string does not make the entity that string. |
| **MM** | MMN, MMC, MMS: open; no universal disjointness. A foundational account may identify numbers with sets, but an encoding into sets alone does not establish identity. |
| **MS** | MSL, MSF, MSD: open; overlap permitted. A controlled language can have an explicit formal grammar; a formal expression can be diagrammatic. |
| **MV** | MVQ, MVC: open; overlap permitted when a scheme enumerates particular magnitudes as alternatives. Raw numeric values and other value domains need not fall under either child. |

The root disjointness choices are stronger than the sibling overlaps further down. They keep, for example, a specification separate from its performance and a feature separate from its bearer. A process ontology identifying a persisting object with its entire history would require a different core identity profile, rather than quietly overriding these constraints.

## 6. Why these splits, and where they are vulnerable

The following ledger covers every nonterminal parent. A “justification” gives a reason for using the distinction, not proof that nature has exactly those divisions.

| Split | Organizing axis and strongest justification | Strongest objection | Boundary case or alternative |
| --- | --- | --- | --- |
| **E → six categories** | Identity, dependence, temporal organization, and interpretability: these distinguish things that require different predicates and relationships. | Several axes are combined; the result lacks the economy and global constraints of an exhaustive partition. | A geometric region is both R and M under a formal-space interpretation. An abstract/concrete split is simpler but leaves its criterion and exhaustiveness disputed. |
| **O → physical/social/subject** | Constitution and agency or experience: the branches offer useful routes without making agency material by definition. | These overlapping classifications use different axes, not one division by a common differentia. | A person can be physical and a subject; a corporation’s attributed agency does not establish consciousness. A wholly constitution-based hierarchy would put agency in a separate facet. |
| **OP → body/portion/aggregate** | Criteria of unity and persistence: retaining organization, retaining matter, and retaining grouped membership can come apart. | Everyday objects do not always have one settled identity criterion. | A repaired ship may preserve body identity while losing much of its original material portion. A flock can be an aggregate whose members change under a looser grouping policy. |
| **OS → institutional/collective** | Dependence on constitutive rules versus social plurality: an office can persist unoccupied, while a group need not be an office-bearing institution. | Institutions and groups are deeply interdependent; their boundaries may be historically contested. | An informal reading group is a collective; its legally incorporated successor can have a distinct institutional identity. |
| **OU → experiencer/agent** | Phenomenal perspective versus intentional action: neither criterion should be silently substituted for the other. | Both attributions are disputed for some animals, machines, and collective subjects. | A subject can undergo pain without deliberate action; a committee can make a decision without an agreed collective phenomenal perspective. |
| **T → process/event/state** | Course, bounded happening, and obtaining condition: these support different explanatory questions. | Aspectual descriptions can classify the same episode differently; the branches cannot safely be a global disjoint partition. | A reactor’s steady operation is active processing while its specified operating variables remain in a steady state. A stricter ontology could distinguish state episodes from every maintaining process. |
| **TP → physical/mental/social** | What makes the process recognizable and explanatorily relevant: this preserves nonreductive mental and social descriptions. | Explanatory relevance may be weaker than an identity criterion. | Reasoning aloud in a meeting involves related physical, mental, and social processes; do not infer they are one merely because their times overlap. |
| **TE → transition/achievement** | Change of condition versus attainment of an endpoint: distinguishes a transition from the criterion by which it counts as completion. | Many achievements are transitions, and a highly inclusive transition definition could absorb this distinction. | A temperature crossing a threshold is an achievement under that criterion without being anyone’s goal. Neither label means “instantaneous.” |
| **TS → physical/mental/social** | The condition that individuates the state: useful for stable situations across domains. | A single condition may have multiple realizations or descriptions, making identity difficult. | A strike is a social situation involving many physical and mental states; those parts are not subclasses of the strike. |
| **F → feature categories** | Determination, manifestation, external dependence, host structure, and intentional orientation: each requires different relations to explain the feature. | The axes cross, and accepting particular features is itself a metaphysical choice. | A headache’s experienced quality, its temporal episode, and a belief about it need separate treatment even when causally connected. A nominalist alternative represents only bearer-level predications. |
| **FQ → physical/phenomenal** | Public physical characterization versus first-person character: avoids defining one away. | A physicalist identity theory may identify some members of both branches; another theory may require their disjointness. | The wavelength of incident light, a surface’s reflectance, and the felt red appearance are not interchangeable descriptions without an argument. |
| **FD → capability/function** | Performance assessment versus an expected contribution grounded in design, selection, or practice: separates ability from attribution of function. | “Function” is often retained for broken things that currently lack the relevant disposition. | A broken pump retains an assigned purpose; it may lack an operative pumping function. A normative-function ontology would place that sense elsewhere. |
| **FR → occupancy/normative standing** | Holding a contextual position versus being normatively situated: supports role histories and obligations without turning people into descriptions. | A role occupancy can constitute several rights and duties; splitting it may overmultiply entities. | A borrower can have an obligation despite no named office. A participant role in an informal game need not carry legal standing. |
| **FS → boundary/cavity** | Delimitation versus host-relative void: both track a host while differing from a mere spatial extent. | Holes and boundaries have competing ontological analyses; primitive entities may be unnecessary. | Move a donut: its hole moves with it, whereas a fixed coordinate region does not. A region-only account must represent the host dependence separately. |
| **FA → belief/conation/preference** | Taking true, seeking or committing, and ranking: these have different success and consistency conditions. | Human attitudes are often mixed, partial, or not propositionally explicit. | Someone can prefer a better past while knowing it cannot be obtained and forming no intention to obtain it. |
| **R → domain types** | The ambient domain supplying positions and extent: prevents duration, location, and measurement-range confusion. | The distinctions depend on a background theory of space, time, and qualitative structure. | A map coordinate is an expression of a position; a spacetime trajectory is not identical to its spatial projection. |
| **RS → point/extent** | One versus multiple spatial positions: a minimal distinction independent of connectedness or dimension. | Point-based theories need not be fundamental to physical space. | A line has multiple positions despite zero volume in a three-dimensional measure. Use a different region profile if the adopted theory is point-free. |
| **RT → instant/extent** | One versus multiple temporal positions: separates dates or instants from spans. | Some temporal theories lack exact instants; operational timing has finite resolution. | “One hour” is a duration value; tomorrow from noon to one is a particular temporal extent. |
| **RX → point/extent** | One versus multiple joint spacetime positions: supports event localization without identifying a happening with its locus. | Some spacetime models or practices use only extended localizations. | An extended event and its occupied spacetime region are related but do not have the same causal or participant properties. |
| **RQ → point/range** | One versus multiple determinations in a stated quality space: separates a determination from an admissible or uncertain range. | A range can represent vagueness, tolerance, or ignorance; its geometry alone does not identify which. | A temperature interval can be a permitted operating range or an uncertainty interval; the range does not by itself tell us its use. |
| **C → predicate/proposition/directive/description** | Application, assertion, prescription, and organized representation: these are different semantic jobs. | Composite contents can perform several jobs, and propositional-content identity is contested. | A regulation both describes a procedure and directs compliance; the whole regulation is not thereby one predicate. A syntax-first ontology is an alternative. |
| **CP → Property/Relation** | Declared argument count: supplies an exact, economical local partition with a shared satisfaction interface. | Arity depends on what has been fixed, bound, or treated as an evaluation index; it does not reveal intrinsicness. | “Married at noon in jurisdiction J” can be unary after explicit projection from a relation. An intrinsic/extrinsic partition answers a different question. |
| **CD → goal/plan/norm** | Target, organized means, and normative force: keeps desired outcomes, instructions, and obligations apart. | A document can combine all three; users may expect categories based on document genre instead. | A safety target can become a legal norm in one context while remaining an internal goal in another. Adoption and authority must be represented separately. |
| **CC → model/narrative** | Selective representation with correspondence versus organized account: supports scientific and fictional descriptions without an actuality test. | The distinction is not exhaustive, and simulations can satisfy both definitions. | A counterfactual historical simulation is both model-based and narrative. A photograph’s content need satisfy neither. |
| **M → mathematical/symbolic/value** | Rule-governed individuation: distinguishes an interpreted mathematical subject, a sign pattern, and a result in an evaluation domain. | This combines constitution with the role of being a value; Formal entity is deliberately broad. | The number 2, the numeral “2,” and a 2 kg magnitude are three subjects even if one can be used to represent another. A separate representational-content branch would be a plausible alternative. |
| **MM → number/collection/structure** | Basic mathematical modes of individuation: supports numerical, membership, and structural questions. | Foundational reductions can identify one category with another, so this is no universal partition. | A set-theoretic construction of a number is not automatically the chosen identity account for numbers in a browsable ontology. |
| **MS → linguistic/formal/diagrammatic** | Syntax and means of expression: keeps meaningful content distinct from how it is expressed. | These axes cross; natural and formal languages are not uniformly disjoint. | A circuit diagram can be a formal-language expression. Two translations can express related content while being different expressions. |
| **MV → quantity/category** | Magnitude determination versus an alternative in an evaluation scheme: makes units and category schemes explicit. | Values are partly a functional notion, and neither branch exhausts every formal value. | A scale can enumerate 5 cm and 10 cm as two category values; their magnitude meaning remains separately specified. |

The point/extent distinctions apply uniformly because they answer a real boundary question, not to make the tree visually balanced. They depend on the selected domain admitting positions; the unresolved-decision list keeps this assumption visible.

## 7. Property, Relation, kind specifications, and arity

### 7.1 The visible Predicate layer earns its cost

Keep the path **Entity → Content → Predicate → Property / Relation** visible. Both Property and Relation specify conditions, have signatures, accept arguments, and support satisfaction assessment. They can share documentation for argument types, admissible contexts, equivalence, and entailment. This common behavior is a stronger reason for the parent than the superficial fact that both are sometimes called “attributes.”

The cost is real: **Kind specification** and **Role specification** belong below Property, at depth 4, so neither appears as an extra depth-3 sibling. Their paths are:

- Entity → Content → Predicate → Property → Kind specification. **Kind specification** is a unary classification specification offering an account of what its instances are and, for sortal kinds, how they are individuated and persist.
- Entity → Content → Predicate → Property → Role specification. **Role specification** is a unary classification specification applicable through a contextual relationship or position, without supplying the bearer’s underlying identity.

These are proposed deeper extensions, not displayed upper-tree nodes. Not every unary Property is a kind or a role: “weighs more than 2 kg at time t” is an ordinary condition. Whether a kind is rigid across possible circumstances is an additional commitment. OntoClean supplies a way to check consequences of identity and rigidity assignments; it does not establish the assignments by terminology alone.[2] For this extension, a strict sortal-kind specification and an anti-rigid role specification are disjoint readings of a specification, but they do not exhaust Property. Broader everyday “kinds of things” should not silently inherit the strict reading.

A kind specification has unary predicate character because its primary classification operation accepts one candidate. It may additionally supply identity, persistence, explanatory, or modal constraints. Those additional commitments distinguish it from an arbitrary unary test. A class of dogs and the reified specification that classifies dogs are related; dogs do not become specifications by satisfying the condition.

Masolo and colleagues explicitly investigate reifying role concepts while preserving their classification relationship to role players.[3] The present choice follows that general strategy, while separately recognizing particular role occupancies. It does not import all of their social-object axioms.

**Alternative layouts:** placing Property and Relation directly under Entity saves clicks but loses their common semantic treatment. Using Relation for predicates of all positive arities makes Property a unary subtype of Relation; that is logically coherent, but conflicts with the useful narrow Relation label adopted here. Hiding Predicate while retaining it semantically is acceptable as an interface shortcut, provided the interface does not present the shortcut as a direct semantic edge. An intrinsic/extrinsic parentage is another possible architecture, but it cannot substitute for an arity declaration.

### 7.2 Arity is not a metaphysical independence test

Arity counts **declared argument positions of a particular specification**. It does not count how many things causally explain a feature, nor how many things an observer must inspect to determine whether a condition holds.

- “Is married” can be unary and relationally grounded.
- “Is prime” is unary without being a physical feature of a bearer.
- “Is between” is ordinarily at least ternary once its spatial interpretation is specified.
- “Is a symmetric relation” is unary at a metamodeling level: its one argument is a relation specification. It does not make the relation being assessed unary.
- A pair encoded as one tuple object allows a unary predicate **of tuples**. That predicate is not silently the original binary relation **of the tuple’s members**.

“Property” in this document consequently does not mean either “intrinsic quality” or “RDF/OWL property.” The W3C n-ary-relations note uses properties for binary links and describes representations of higher-arity relationships through additional individuals and links.[7] That technical vocabulary must be translated rather than imported as metaphysics.

### 7.3 Fixing, binding, and evaluating arguments

Suppose the signature is explicitly:

\[
\operatorname{HasMass}(x,v,t)
\]

where \(x\) is a bearer, \(v\) a mass value, and \(t\) a time. HasMass is ternary. The following are different derived specifications:

\[
\begin{aligned}
P(x)&:=\operatorname{HasMass}(x,2\,\mathrm{kg},t_0),\\
Q(x,t)&:=\operatorname{HasMass}(x,2\,\mathrm{kg},t),\\
U(x)&:=\exists v\,\operatorname{HasMass}(x,v,t_0).
\end{aligned}
\]

P and U are unary Properties. Q is a binary Relation. The first fixes two arguments; the third fixes time and existentially binds the value. Neither renames the original relation without recording the transformation. The existential condition U is much weaker than P.

For a contextual role, one might declare:

\[
\operatorname{PlaysRole}(x,r,k,t).
\]

Here the bearer, role specification, contextual framework, and time remain four arguments. Fixing \(r=r_0\), \(k=k_0\), and \(t=t_0\) yields a unary condition on bearers. Fixing only the role leaves a ternary relation. Existentially projecting across all contexts means “plays this role somewhere,” which differs from holding it in the institution of interest.

An interpretation may have evaluation indices such as a world, assignment, or standard. Declare which items are indices and which are arguments. A family \(P_c(x)\) is a family of unary predicates indexed by c; the function or relation connecting c to these predicates has its own signature. Moving an object-language context argument into that index creates a derived family and must be documented. It is not permission to hide an argument to obtain a preferred placement.

After all arguments are supplied, the result is propositional or otherwise truth-evaluable content. The Predicate class excludes zero-argument predicates by convention; a logical theory that treats propositions as nullary predicates can supply an explicit alternative alignment. Similarly, a variadic schema requires its admissible arities to be declared and instantiated before classification under this fixed-arity Predicate class.

### 7.4 Reification does not create a worldly connector

Distinguish a relation specification, its application to a tuple, a proposition asserting that application, and any event or dependent feature that makes the application true. A purchase may support a relational claim about buyer, seller, item, price, and time. The purchase event is not a subclass of the relation specification. A relation concerning mathematical ordering need not have a corresponding causal event at all.

Reifying a purchase record and representing its arguments with binary links is an encoding decision. It preserves the intended multiargument condition only if the argument roles, identity of the record, and applicable constraints remain available. It does not prove that the original relation was really binary, nor that every relation has a separate material bearer.

## 8. Concrete stress tests

### 8.1 Properties, particular features, attribute schemas, and values

Take two different cups that each have a mass of 2 kg at noon.

| Subject | Placement or relation | Counterexample to conflation |
| --- | --- | --- |
| Each cup | Object → Physical object → Material body | A cup is not an instance of the class of unary predicate specifications. |
| Each cup’s particular mass feature | Particular feature → Quality → Physical quality | Equal mass values do not make the two cups share one numerically identical particular feature. |
| “Is a mass quality” | Content → Predicate → Property | This condition classifies qualities; it is not the value-taking relation connecting a cup, mass value, and time. |
| HasMass(x,v,t) | Content → Predicate → Relation | Fixing only the value leaves time free; the result is still binary. |
| A mass attribute schema | A model specification with a declared signature, or a mathematically specified mapping in an extension | Its output-valued behavior differs from a unary truth-valued condition. Do not relabel it Property merely because an interface calls mass an attribute. |
| 2 kg | Formal entity → Value → Quantity value | It is not the bare number 2, the unit kilogram, either cup, or either particular mass feature. |
| “2 kg” | Formal entity → Symbolic structure → Linguistic expression, and possibly Formal-language expression | A differently written equivalent quantity need not be a different magnitude. |

DOLCE distinguishes particular qualities from their positions in quality spaces.[1] QUDT likewise distinguishes quantity, quantity kind, and quantity value in its vocabulary.[8] These are useful precedents for preserving distinctions, not warrants to identify every node across the three systems.

For color, distinguish the surface feature, a reflectance description, a selected color-space value, and an experienced appearance. A color word such as “red” can designate a category value or express a unary predicate, depending on the interpretation. A physical color-space position and a phenomenal quality are not interchangeable merely because both are called red.

A value is not every possible filler of a relation slot. Paris can be the object of a database field named birthplace without becoming a Formal entity in this ontology. It is the **role of being a field value** in that database, a separate notion from MV. This restriction is a design choice that protects the tree from classifying everything as Value.

### 8.2 Dispositions, capabilities, functions, and manifestations

A fragile glass can remain unbroken throughout its existence. A pianist can retain an ability while asleep. Neither case requires an actual performance to instantiate the relevant Disposition or Capability. Röhl and Jansen emphasize the need to distinguish dispositions, bearers, bases, triggers, and realizations, including dispositions that are never realized.[4]

The generic specification of fragility belongs under Property once its applicability conditions are fixed. This glass’s fragility belongs under Particular feature → Disposition. A breaking belongs under Occurrence. The glass participates in the breaking, and the breaking manifests its fragility; neither connection is subclass inclusion.

Capability adds a performance criterion: a lifting system’s capacity to raise a specified load in stated conditions. It is not a guarantee of success in all environments. A claim of organizational “capability” may refer to coordinated dispositions of a system, while a legal “power to appoint” is a Normative position. Those senses should have separate specifications.

The Operative function node intentionally does not cover every use of “function.” A broken watch can retain a timekeeping purpose or assigned function without retaining an operative timekeeping capacity. Record the assigned purpose in a specification and its assignment in a relation. If one instead adopts a theory in which function is intrinsically normative and survives total loss of capacity, that function should not be forced under FD. This is a substantive alternative, not a category error.

### 8.3 Purposes, goals, preferences, norms, and obligations

Suppose a team wants to reduce energy use, plans equipment changes, and must also comply with an emissions rule.

- The **desired outcome description** is a Goal specification. Its adoption by the team is a distinct claim. The eventual low-consumption situation, if it occurs, is a State, not a kind of goal description.
- The team’s **intention to act** is a Conative attitude if collective intentional agency is accepted; the **plan** is a Plan specification. Planning is a Process, and executing the plan is another Process.
- An **assigned purpose** relates an assigner or practice, a bearer or activity, a proposed contribution, and a context. It is not automatically a capacity of the bearer. A doorstop may be assigned that purpose to a stone without changing its natural kind.
- A **preference** can be a subject’s particular Preference attitude. A comparative specification such as Prefers(agent, optionA, optionB, context, time) is a Relation. Fixing all but the agent yields a derived unary Property; fixing only the two options does not.
- A **norm** is prescriptive content under Norm specification. A printed regulation is a carrier or expression of that content. The obligation incurred by a particular party under that norm is a Normative position.

Counterexamples matter. A person may prefer a world without storms but have neither a plan nor an obligation to produce it. A stated goal can be abandoned. A norm can be violated without ceasing to be a norm. A promise can generate an obligation in an accepted normative account even when the promised act never happens. A sentence reporting “the tenant is obliged to pay” is Propositional content about a normative position; it is not necessarily the prescription that creates it.

Do not infer moral correctness from institutional recognition, or recognition from somebody’s assertion that a norm exists. Record the relevant authority, community, jurisdiction, or normative theory. These are modelling parameters; this proposal makes no claim that every valid norm requires legal or institutional recognition.

### 8.4 Kinds, roles, and the people or things bearing them

Consider Dana, a person who becomes treasurer and later resigns.

The person is an Object and a Subject under the chosen person account. “Treasurer in organization K at time t” is a unary role condition only once K and t have been fixed or explicitly bound. The reified treasurer specification follows **Entity → Content → Predicate → Property → Role specification**. Dana’s particular occupancy follows **Entity → Particular feature → Relational feature → Role occupancy**. The enduring office, if the institutional framework individuates one, follows **Entity → Object → Social object → Institutional continuant**.

Resignation ends an occupancy without necessarily ending Dana or the office. It also need not erase a disposition to perform financial work. Conversely, an unqualified person could occupy the office while lacking important capabilities. Role, capability, bearer, and office therefore require different identity conditions.

The subclass **Treasurer-person**, whose members are people occupying the role, may be a subclass of Person. It is not a subclass of Role specification, whose members are specifications. The word “treasurer” cannot select between these classes without a stated reading.

Kind and role do not divide all ordinary labels neatly. “Child” can mean a developmental phase or someone’s offspring. “Citizen” depends on a political framework. “Poison” depends on recipient, dose, and circumstances. “Food” may be a contextual role. This proposal requires those distinctions to be made in the domain module; it does not infer a strict kind merely from a noun.

### 8.5 Objects, processes, states, regions, and dependent features

A kettle, its heating, its being at a specified temperature during an interval, its temperature quality, and the temperature value are different subjects. The quality is borne by the kettle; the state obtains during an interval; the heating is a process; a spatial region is occupied. None of these relationships supplies an is-a edge between those subjects’ classes.

A whirlpool is a hard case. It may be modelled as a sustained physical process, or as a persisting organized object constituted through changing matter. The present default prefers Process when circulation is the identity criterion. An object-based treatment is a reasonable competing choice if its persistence and constitution relations are supplied. Merely asserting that all whirlpools are both Object and Occurrence would violate the chosen root constraints.

Likewise, a hole in a moving ring follows its host and may change shape. A fixed spatial region does not follow the ring. The **Cavity feature**, its **Boundary feature**, the **Spatial region currently occupied by the cavity**, and a **geometrical model** of that cavity have different roles. It is possible to build a defensible region-based theory of holes, but it must explain the missing host-relative identity.

Regions and occurrences are distinct even when they share an extent. Two concurrent happenings can occupy the same region while having different participants or causal histories. A map’s polygon can describe a territory without being identical to a polity, its legal jurisdiction, or all matter currently located inside it.

### 8.6 Texts, carriers, expressions, and content

For a printed novel, distinguish:

1. The **physical copy**, a Material body or a suitably individuated physical artifact in an extension.
2. The **inscription or encoding**, a particular physical configuration carried by it.
3. The **repeatable text expression**, a Linguistic expression under Symbolic structure.
4. The **narrative content**, under Descriptive content, interpreted through that expression.
5. The **subjects presented by the narrative**, classified under the relevant categories within narrative scope.

Destroying one copy does not by itself destroy all copies, the expression type, or the narrated subject. Translating the novel changes the linguistic expression; whether it preserves the same work or exactly the same content requires a chosen equivalence policy. Quoting a false sentence does not make its carrier false in the same sense as its propositional content.

IFLA LRM distinguishes work, expression, manifestation, and item and relates them through relationships such as realization and embodiment.[9] The present tree is not a relabeling of that model: its syntax/content separation and its Physical object class require an explicit alignment before importing bibliographic data. In particular, LRM’s entity named Expression should not be declared identical to MS merely because of the shared word.

“The text” can denote a sign sequence, a document version, a physical inscription, or interpreted content. A versioned institutional document may have its own Social object identity. Its associated expression and content should be linked, not treated as subclasses of that document.

### 8.7 Organizations and institutional entities

The proposed deeper path is **Entity → Object → Social object → Institutional continuant → Organization**. Here **Organization** means an institutional continuant with an organized arrangement of participants or offices and rules sustaining its identity and coordinated activity. This is depth 4, explicitly outside the upper display. Informal coordinated groups remain Social collectives unless the institutional identity criterion is met.

A university can persist through replacement of all current staff. A fixed mathematical set of those staff cannot retain exactly that membership while all members change. The organization is therefore not identified with that set by default. Its buildings are not subclasses or instances of the university; they can be assets, places of activity, or components of a facility. The university’s history is an Occurrence or collection of occurrences, not automatically the institution itself.

Organizations that satisfy the Intentional agent definition gain that additional semantic superclass in a later extension. This does not place all organizations under Experiencing subject, and it does not identify every group with an agent.

A contract illustrates another distinction: its written expression, prescriptive content, institutional agreement, and resulting obligations need not be one entity. A vacant office can persist institutionally without an occupant. A bank-account identifier is a symbolic expression, while the account’s institutional identity and a current balance value are different subjects. These are proposed analytical decompositions, not jurisdiction-specific legal claims.

### 8.8 Numbers, mathematical structures, logic, and values

The number 2 follows **Entity → Formal entity → Mathematical entity → Number**. Integers and more specific number classes belong deeper. The numeral “2” follows Symbolic structure. A two-element set is a Mathematical collection. A theory can construct or identify numbers using sets, but the ontology must distinguish “represented by,” “isomorphic to,” and “identical to.”

A group as a specified algebraic structure belongs under Mathematical structure. A group axiom system is content expressed by formal-language expressions. The unary condition “is a group under signature S and theory T” is a Property once S and T have been fixed. The membership class of groups is not a subclass of the class of predicate specifications. A particular group satisfies the condition and can model an axiom system; it is not an instance of the textual axiom list.

Likewise, distinguish logical syntax, propositions, consequence relations, and proof occurrences or proof structures. A consequence relation whose arguments include a set of premises and a conclusion has its declared arity even though one argument is itself a collection. A physical act of proving belongs under Process; a repeatable formal derivation is a Symbolic structure or Mathematical structure under an explicit formalization.

An accepted theorem is not automatically a Goal specification, even if proving it was someone’s goal. A false conjecture is still Propositional content. Truth values belong in a specified value domain; adopting a two-valued, many-valued, or inconsistent-information semantics is a further choice, not a root-level discovery about existence.

### 8.9 Fictional, hypothetical, mistaken, and impossible subjects

**Fictional is a provenance and mode-of-presentation classification, not a root sibling opposed to Object or Content.** Actuality, fictional presentation, and possibility are different axes. A real city can appear in a novel; a fictional city may be internally possible; an unbuilt bridge can be possible and nonactual without being fictional.

For a fictional detective, store attributions such as:

\[
\operatorname{AttributedIn}(\text{story},\text{detective-condition},\text{character-anchor}).
\]

This does not entail an actual detective, or an actual bearer of the detective’s fictional physical qualities. The story’s narrative content and its printed carriers can have ordinary existence claims independently. The character anchor is a representational device; the system must not identify it with a real person or with the stored row itself.

For “a round square in Euclidean geometry,” retain the description and any intended fictional subject with its source. Under the specified Euclidean definitions, do not assert a satisfiable actual instance of the jointly required conditions. Inconsistent narrative attributions remain quoted claims; the trusted core does not import them and infer arbitrary conclusions by classical explosion. The default proposal supports retrieval of these attributed claims, **not** unrestricted automated inference inside inconsistent stories. A paraconsistent narrative reasoning module would require additional semantics.

“The largest prime,” in ordinary arithmetic, illustrates failed description, not merely fiction. A hypothesized planet later judged not to exist would illustrate a mistaken scientific posit, a different reference problem again. An unresolved or failed denotation should remain marked as such. It need not be converted into a new actual astronomical object so that every noun phrase has a tree entry.

If a later module treats literary characters as actual abstract artifacts, classify those artifacts under the appropriate content or social-artifact account and relate them to story-internal subjects. Zalta’s distinction between encoding and exemplification is a researched alternative to the present scoped-attribution approach.[10] The two should not be equated without a formal mapping.

## 9. Semantic ancestry and preferred navigation

The full semantic graph carries subclass axioms. The displayed tree selects one parent from the immediate superclasses adopted in this proposal. A portal or shortcut may take a reader directly to a distant descendant, but it must preserve the full breadcrumb and identify the shortcut as navigation.

Consider a later **Agentive organization** class. Its institutional ancestry includes Organization, while it also has Intentional agent as a semantic superclass. Prefer the institutional branch for navigation if institutional persistence is the main explanatory question. Both inclusions remain available for inference. Do not promote Organization itself into a shorter branch simply to fit the current depth limit.

Some domain labels organize a mixture of categories. Biology can lead to organisms, biological processes, dispositions, models, and propositions. Mental subjects can lead to experiencers, mental processes, attitudes, and their contents. Fiction can lead to narratives, expressions, and scoped fictional subjects. These are useful browsing groupings, but **Biology is not the superclass of every entity discussed by biology**, and a narrative is not the superclass of its characters.

Preserve at least these non-subclass relationships, with signatures specified in a later formalization:

| Relationship | What it connects; why it is not subclass inclusion |
| --- | --- |
| instance of | A subject and a class it belongs to |
| specifies / classifies | A reified specification and the class or subjects it governs under an interpretation |
| satisfies | A subject or argument tuple and a condition specification |
| bears / depends on | A bearer or host and a particular feature |
| participates in | An object and an occurrence involving it |
| manifests | An occurrence and a disposition it manifests |
| fulfills / conforms to | A performance or situation and a goal, plan, or norm specification |
| expresses / encodes | An expression or carrier and its content or sign pattern |
| represents / is about | A content-bearing representation and its intended target |
| has value | A feature or evaluated subject, a value, and required time, scale, or context parameters |
| occupies / is located in | A subject and a region, with temporal and frame qualifications where required |
| constitutes / has part / has member | Different constitution, composition, and membership links; none is interchangeable with the others |
| attributed in | A source or discourse scope and an attributed predication |

The word “realization” should not serve as one untyped edge for all these cases. Manifesting a disposition, executing a plan, expressing a work, and instantiating a mathematical axiom system have different constraints. They can be compared under a documented general pattern, but no common word establishes their identity.

## 10. External architectures and plausible alternatives

These comparisons describe commitments actually used in the argument. The proposal is not claimed to conform to any one imported ontology.

| Source or alternative | Commitment relevant here | What this proposal adopts or changes |
| --- | --- | --- |
| **BFO and the disposition literature** [4,5] | BFO’s official project describes a scientific upper ontology of classes and relations. The consulted disposition paper distinguishes dependent dispositions from bearers and realizing processes. | Retain that separation as a useful analysis. Do not extend a scientific realist domain to fictional subjects by assuming that all admitted subjects exist. The historical paper is not treated as the specification of the current BFO hierarchy. |
| **DOLCE** [1] | Distinguishes endurants, perdurants, qualities, and abstracts, with explicit treatment of particular qualities and their quality-space positions. | Use the distinctions as checks on conflations. Do not import its whole partition, its exact feature placement, or an Abstract root branch. |
| **OntoClean** [2] | Uses identity, dependence, unity, and modal rigidity to assess taxonomic commitments and their consequences. | Require explicit identity policies and role analysis. Do not infer a class’s rigidity from its name or from a small set of examples. |
| **DOLCE-oriented role reification** [3] | Treats role concepts as discussable entities related to their players and descriptions. | Reify specifications and preserve classification links; additionally distinguish role occupancy, office, and occupant. |
| **IFLA LRM** [9] | Separates bibliographic entities and their realization/embodiment relationships. | Retain the need for distinctions among works, expressions, and carriers; supply mappings rather than label-based equivalences. |
| **Zalta’s theory** [10] | Distinguishes encoding a property from exemplifying one, with a substantive theory of abstract objects. | Consider it a serious alternative for fictional reference. Use scoped attributed claims here, without importing abstract-object existence axioms. |
| **Exhaustive Abstract / Concrete split** | A possible architectural choice, not a source-backed default in this proposal. | Reject as the first split unless a precise criterion is selected and cases such as social institutions, mental states, regions, and fictional subjects are resolved. |
| **Particular / Universal split** | Separates single subjects from repeatable characteristics on a realist account of universals. | Do not adopt it at the root: reified specifications are themselves individuals in the metamodel, and not every specification must correspond to a universal. |
| **Pure process ontology** | Takes temporally extended activity as ontologically primary and may reconstruct objects from processes. | A coherent alternative, especially for living systems. It would require different root identity and disjointness axioms. |
| **Flat subject taxonomy** | Uses domains or familiar nouns as the primary organization. | Useful as a browsing overlay, but insufficient alone for the class/specification, bearer/feature, and content/carrier distinctions required here. |

The principal tradeoff is explicit: this design gives up an exhaustive top partition and some terminological familiarity in return for semantic distinctions that remain useful across science, institutions, mathematics, and fiction.

## 11. Category errors versus contestable design choices

An error can be demonstrated **relative to the declared meanings and signatures**. That is different from proving a competing ontology wrong.

| Demonstrable error under these definitions | Why it fails |
| --- | --- |
| This cup is a subclass of Material body | The cup is an individual; its appropriate link is instance of. |
| Cup is a subclass of Mass quality because cups have mass | Bearing a quality does not make the bearer a quality. |
| 2 kg is a subclass of Mass quality | A quantity value is neither a particular quality nor a subclass of a quality class. |
| The class Dog is a subclass of Kind specification | Members of Dog are dogs; members of Kind specification are specifications. |
| A plan execution is a subclass of the plan content | Execution and prescription have different identities; the relationship is conformity or execution. |
| A printed page is a subclass of the proposition printed on it | Carrier and content are connected by encoding and interpretation, not inclusion. |
| A staff member is a subclass of a university | Membership or employment is not subclass inclusion. |
| HasMass(x, 2 kg, t) is unary while both x and t vary | Its declared free argument count is two. |
| A reified relation record proves that its multiargument condition is binary | The encoding uses binary links; the represented condition retains its signature. |
| A fictional attribution is exported as an actual-world instance assertion | The scope change lacks a valid bridge and can create false existence claims. |
| A child is placed directly under a distant ancestor only to fit the display | It hides adopted semantic ancestry and misrepresents the depth boundary. |

Reasonable choices include recognizing or dispensing with particular qualities; treating a whirlpool as an object or process; adopting Platonism or a nominalist interpretation of mathematics; treating fictional characters as artifacts or as scoped discourse subjects; using an enduring-subject or process account of mind; placing function under normative standing rather than capacity; and choosing a different genuine navigation parent. Each needs explicit consequences. Familiar terminology and the author’s confidence settle none of them.

## 12. Decisions left open for later domain expansion

1. **Identity policies.** Decide when a body, material portion, organization, document version, mental subject, or content persists through change. The upper definitions constrain these choices but do not compute all identities.
2. **Formalization language and levels.** Select the division between class axioms, reified specifications, scoped claims, and metamodeling. A generic satisfaction relation requires its own semantics; it is not automatically supplied by an OWL encoding.
3. **Predicate identity.** Decide whether specifications are identified intensionally, by a definition/version, by necessary equivalence, or by some domain-specific criterion. Extensional coincidence alone is insufficient for this proposal’s intended use.
4. **Context management.** Specify which times, frames, standards, and institutions are arguments and which are evaluation indices. Record every projection or partial application used to derive a unary condition.
5. **Mind and agency.** Decide which subjects count as agents or experiencers, and whether any mental/physical identifications are adopted. The current categories permit competing accounts without selecting one.
6. **Dispositions and functions.** Choose modal and causal commitments for dispositions, performance standards for capabilities, and whether to add a broader normative-function class beside the operative sense.
7. **Space and time.** Decide whether point-based region semantics is suitable. A point-free or theory-specific account can require revision of the point/extent splits; coordinate expressions must remain distinguishable from their targets.
8. **Content identity.** Set rules for translations, paraphrases, adaptations, quoted material, mixed directive/assertoric content, and changing institutional descriptions.
9. **Mathematical foundations.** Distinguish equality, representation, isomorphism, and equivalence. Record whether an entity is admitted within a theory without asserting a global metaphysical existence claim.
10. **Fiction and inconsistency.** Determine whether story-internal subjects need a literary-artifact counterpart, how versions and adaptations share identities, and whether retrieval of inconsistent claims is sufficient or a formal paraconsistent reasoner is required.
11. **Coverage pressure.** Test genuinely difficult additions—such as absences, facts, laws, universals, fields, and collective experiences—before adding more root categories or asserting exhaustiveness. Leaving a subject classified only as Entity is preferable to forcing a false inclusion.
12. **Navigation policy.** Choose stable preferred parents and domain portals, while preserving all semantic superclasses and honest depth breadcrumbs.

These are extension decisions, not requests for a project-specific resolution during this independent phase. The proposal ends here pending the project packet.

## Sources consulted and used

The following are external primary research or authoritative specifications actually consulted. Numbered citations identify where their commitments enter the argument. All uncited definitions, placements, constraint choices, examples, and recommendations are proposals in this document, not claims of source endorsement. Accessed 11 October 2026 UTC. Failed retrievals and sources used only in the earlier product-settings discussion are not listed as ontology evidence.

1. **Stefano Borgo, Roberta Ferrario, Aldo Gangemi, Nicola Guarino, Claudio Masolo, Daniele Porello, Emilio M. Sanfilippo, and Laure Vieu (2022).** “DOLCE: A Descriptive Ontology for Linguistic and Cognitive Engineering.” *Applied Ontology* 17(1), 45–69. [Author-hosted paper](https://www.loa.istc.cnr.it/wp-content/uploads/2021/11/DOLCE_FOUST_2022.pdf); [DOI](https://doi.org/10.3233/AO-210259). Used for its principal distinctions and quality/quale separation, especially the introductory conceptual discussion.
2. **Nicola Guarino and Christopher A. Welty (2004).** “An Overview of OntoClean.” *Handbook on Ontologies*, Springer, chapter 8 in the consulted edition. [Author-laboratory PDF](https://www.loa.istc.cnr.it/wp-content/uploads/2020/03/OverviewOntoClean-compresso.pdf). Used for rigidity, identity, unity, role analysis, and constraints on subsumption.
3. **Claudio Masolo, Laure Vieu, Emanuele Bottazzi, Carola Catenacci, Roberta Ferrario, Aldo Gangemi, and Nicola Guarino (2004).** “Social Roles and their Descriptions.” *KR 2004*, 267–277. [Author-hosted paper](https://www.loa.istc.cnr.it/wp-content/uploads/2019/10/MVBCFGG-KR04.pdf). Used for role reification, classification, contextual dependence, and the difference between concepts and their players.
4. **Johannes Röhl and Ludger Jansen (2011).** “Representing dispositions.” *Journal of Biomedical Semantics* 2(Suppl 4), S4. [Full paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC3194171/); [DOI](https://doi.org/10.1186/2041-1480-2-S4-S4). Used for bearer/base/disposition/realization distinctions and the absence of required actual manifestations. Its historical BFO hierarchy is not presented as the current specification.
5. **Basic Formal Ontology project.** [Official overview](https://bfo-ontology.github.io/) and [BFO-2020 repository overview](https://github.com/BFO-ontology/BFO-2020). Used for the project’s stated scientific upper-ontology scope. No claim is made to have reproduced or validated its complete axiom set.
6. **W3C (2012).** *OWL 2 Web Ontology Language: Structural Specification and Functional-Style Syntax*, Second Edition, especially §5.9, Metamodeling. [Recommendation](https://www.w3.org/TR/owl2-syntax/#Metamodeling). Used for the independence of class and individual interpretations under OWL 2 Direct Semantics.
7. **Natasha Noy and Alan Rector, editors; W3C (2006).** *Defining N-ary Relations on the Semantic Web*. [Working Group Note](https://www.w3.org/TR/swbp-n-aryRelations/). Used for multiargument relationship encoding patterns. This is a Working Group Note, not a W3C Recommendation or a proof of an ontological reduction to binary relations.
8. **QUDT project.** [QUDT schema documentation](https://qudt.org/doc/2026/02/DOC_SCHEMA-QUDT.html), [Quantity](https://qudt.org/schema/qudt/Quantity), and [QuantityValue](https://qudt.org/schema/qudt/QuantityValue). Used for the vocabulary’s separation of quantities, kinds, and values. No exact equivalence to FQ, CPP, RQ, or MVQ is asserted.
9. **Pat Riva, Patrick Le Bœuf, and Maja Žumer (2017).** *IFLA Library Reference Model: A Conceptual Model for Bibliographic Information*, amended through December 2017, particularly §4.1 and §4.3. [Official document](https://www.ifla.org/files/assets/cataloguing/frbr-lrm/ifla-lrm-august-2017_rev201712.pdf). This is the version consulted, not a claim about the latest version.
10. **Edward N. Zalta.** “Further Explanation of the Distinction Underlying the Theory,” author-maintained presentation of abstract object theory. [Encoding and exemplification](https://mally.stanford.edu/distinction.html). Used as a substantive alternative for fictional predication, not as an adopted metaphysics.
