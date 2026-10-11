# Independent ontology critique and upper-tree proposal

- Send Prompt 1 to a fresh chat with no repository context. Commit its response
  unchanged as UpperOntologyModelName.md.
- Send Prompt 2 to a repo-enabled agent with that saved response and the full
  repository. Save and commit its critique separately as CritiqueByModelName.md.

## Prompt 1 — independent upper ontology in a fresh chat

Research established external ontologies and primary literature as needed.
Do not try to identify me or locate my ontology, wiki, repository, or prior
design discussions. Do not browse or use my project's own materials as research
sources. If you recognize that you have encountered them, stop and report the
exposure rather than claiming an independent proposal. Cite the external sources
you actually use and distinguish their commitments from your own choices.

Act as an independent ontology designer. Recommend a defensible upper ontology
for a broad, browsable organization of knowledge, extending across physical,
biological, mental, social, informational, mathematical, logical, and fictional
subjects. The result supports conceptual understanding and later domain
expansion; it is not merely a taxonomy for a guessing game.

Use Entity as the root, with the working definition: “That which can be referred
to, even if nonexistent.” Critique that definition if it creates problems and
propose a precise alternative; distinguish reference from existence. Do not
silently assume materialism, Platonism, or an exhaustive abstract/concrete split.

Provide the root, its children, grandchildren, and great-grandchildren: at most
three subclass edges below Entity. Expand every proposed branch through that
scope wherever defensible; do not invent categories merely to fill a level.
Deeper branches may be indicated as unexpanded. Do not compress ancestry to
make deeper categories fit this display boundary. Do not generate an entire
domain ontology or leaf inventory.

Every primary edge must mean is-a/subclass inclusion, not instance-of, part-of,
location, use, or association. Specify what the nodes denote and how classes,
individuals, predicates, reified specifications, realizations, and values are
related. A single navigation parent may coexist with additional semantic
superclasses. State which sibling groups overlap, which are disjoint, and which
are exhaustive; assume none of these properties merely from tree layout.

For every node, give a short discriminating definition. For each important split,
give its organizing axis, strongest justification, strongest objection, and at
least one boundary case. Compare plausible alternatives. Explain any distinction
between semantic ancestry and preferred navigation placement.

Explicitly examine the placement and meaning of Property and Relation, their
shared predicate character, whether a visible Predicate layer earns its cost,
and how kind specifications relate to unary properties. Distinguish an arity
criterion from a metaphysical criterion. Specify when fixing a value or context
turns a multiargument relation into a unary condition; do not change arity
silently to obtain a preferred placement.

Stress-test the proposal with properties versus particular features and values;
dispositions versus capabilities; purposes, goals, preferences, norms and
obligations; kinds versus contextual roles; objects, processes, states, regions
and dependent features; texts versus carriers and content; organizations and
institutional entities; numbers and mathematical structures; and fictional or
impossible referents. Include concrete counterexamples, not just assurances.

Write a standalone Markdown document named UpperOntologyModelName.md
(replace ModelName with your model label, such as Astra or Gemini),
available as a downloadable file if supported; otherwise return its complete
Markdown in the response. Include the upper tree with definitions, the
architectural argument, sources consulted, and unresolved decisions. State the
model and reasoning setting only if known; do not invent metadata. Separate demonstrable category errors from
reasonable design choices. Cite authoritative sources for external factual
claims when available; do not use model confidence or conventional terminology
as a substitute for an argument. Stop after this independent proposal and wait
for the project packet.

## Prompt 2 — project critique with repository context

The repository and your preserved UpperOntologyModelName.md are now
available. Examine the ontology project as an independent critic. Your saved
initial proposal is evidence of your starting position, not a commitment you
must defend. Critique the incumbent Omniversal Ontology and the GPT/Sol proposal
equally, including definitions, subclass edges, sibling organization, specification
and bearer distinctions, crosswalks, coverage claims, reference use, documentation,
validation, rendering, and the human audit/merge workflow. Evaluate the
project's ontology claims rather than adopting their conclusions. Follow the
applicable repository access and file-write rules. Do not modify ontology data,
source documents, renderers, tests, or your preserved initial response. The only
requested repository write is your separate critique artifact.

Inventory what you actually inspected. Identify omitted or inaccessible material
and the resulting limits. Evaluate distinct issues once rather than repeating
them for every generated copy. Claims about source coverage or executable test
results require inspection or execution; otherwise label them unverified.

Prioritize defects by their consequences. For each major finding provide the
exact file/node or edge, the problematic definition or claim, a concrete
counterexample or inconsistency, a proposed remedy, and its cost or strongest
objection. Also identify useful distinctions that should survive reconciliation.
Do not call a placement wrong merely because another formal ontology differs.
Distinguish semantic defects from navigation preferences and deliberate scope
limitations. Do not assume the incumbent, Sol, or your own first proposal is the
winner; agreement among models is not independent evidence of correctness.

Give particular attention to Property/Relation reconciliation. Determine which
children genuinely satisfy their parent definitions. Examine unary kind
predicates, quality values, bearer-specific qualities, dispositions and capacities,
roles, normative content and binding instances, goals, purpose assignments and
preference orderings. Test relation groupings, including classification versus
instantiation, institutional versus social, and equivalence across domains.
Explain what must be renamed, split, relocated, cross-linked, or retained and
why. Require explicit argument types and interpretation where arity matters.

Assess whether the existing mappings preserve meanings or merely account for
labels. Recommend how to reconcile additions, omissions, splits, mergers,
broadened meanings, alternate parents, and disagreements while preserving stable
identifiers and traceable decisions. Do not assemble a union of all candidates
or let one-to-one mappings conceal incompatible definitions.

Finish with your recommended upper tree, again only through Entity's
great-grandchildren, with discriminating definitions and explicit split policies.
List material departures from your saved independent proposal and explain the
project evidence or better argument that motivated each. For unresolved choices,
state what example, evidence, or intended-use decision would discriminate between
alternatives. Recommend an audit sequence and bounded branch changes, not another
complete replacement tree. Avoid arbitrary branching or depth limits beyond the
requested reporting scope.

Write the critique and revised upper tree as a standalone Markdown document
named CritiqueByModelName.md, replacing ModelName with your model label, for
example CritiqueByAstra.md or CritiqueByGemini.md. If you can write to the
repository, save it alongside CriticPrompt.md using the repository's coordination
and write rules. Otherwise provide a downloadable file or the complete Markdown
response; I will save and commit it there manually. Identify the repository revision and files inspected, model
and session where known, tools or tests actually run, external sources used,
limitations, and unresolved findings. Do not overwrite the independent proposal.
