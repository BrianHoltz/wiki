# Independent ontology critique and upper-tree proposal

## How to use the prompts

### Prompt 1 delivery

Send only Prompt 1 to a fresh conversation in the model's ordinary chat
interface, not a repo-connected coding agent or a chat inside a project with
attached repository files. Disable repository connectors and project context;
do not attach our trees, wiki links, design discussions, or Prompt 2. Where
possible, disable memories or personalization that expose our ontology. A fresh
chat interface alone does not guarantee the absence of that context.

Allow web research into external ontologies and primary literature. Keep our
project name, author name, repository address, and wiki address out of the
initial message. Prompt 1 explicitly excludes attempts to find our work without
supplying a locator. This is an instruction boundary, not a technical guarantee:
record any reported exposure and restart if independence matters.

Request a downloadable Markdown response named IndependentUpperOntology.md.
If the interface cannot create files, save the complete returned Markdown
verbatim. Import it unchanged into a model-specific review directory in the
repo, such as Ontology/Reviews/Astra/IndependentUpperOntology.md, and commit it
before proceeding. Record the actual model/version, reasoning setting, and
source conversation when known; do not infer undisclosed identifiers. Keep any
import metadata outside the model's original response.

### Prompt 2 delivery

Send Prompt 2 only after the initial response is preserved in a commit. The
same chat can then receive the repository, or a repo-enabled agent can receive
both the repository and that exact initial response. The latter offers better
file inspection and executable checks; identify any change of model or session.

Provide the full repository at a pinned revision, with an inventory of the
ontology project and any relevant uncommitted files included in the packet.
The inventory should distinguish maintained authority, historical references,
experiments, and generated artifacts. Include the frozen OO snapshot and
manifest, current OO sources, GPT/Sol proposal and coverage map, architecture
and validation documentation, design memoranda, categorization backlog,
reference ontologies and crosswalks, and relevant renderers and tests. The
critique concerns the ontology project and its dependencies, not unrelated
personal material elsewhere in the wiki.

Save the second response separately as ProjectCritique.md in the same
model-specific directory and commit it. Preserve the initial response unchanged;
revisions belong in the critique. Have repository write access limited to the
requested review artifact where practical. If the critic cannot access the
full packet or execute checks, require an explicit scope statement.

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

Write a standalone Markdown document named IndependentUpperOntology.md,
available as a downloadable file if supported; otherwise return its complete
Markdown in the response. Include the upper tree with definitions, the
architectural argument, sources consulted, and unresolved decisions. State the
model and reasoning setting only if known; do not invent metadata. Separate demonstrable category errors from
reasonable design choices. Cite authoritative sources for external factual
claims when available; do not use model confidence or conventional terminology
as a substitute for an argument. Stop after this independent proposal and wait
for the project packet.

## Prompt 2 — project critique with repository context

The repository and your preserved IndependentUpperOntology.md are now
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
named ProjectCritique.md. If repository writes are available, save it in the
specified model-specific review directory using the repository's coordination
and write rules. Otherwise provide a downloadable file or the complete Markdown
response for import. Identify the repository revision and files inspected, model
and session where known, tools or tests actually run, external sources used,
limitations, and unresolved findings. Do not overwrite the independent proposal.
