# Epistemic Evaluation Template

A framework for critically evaluating any specimen — interview, podcast, video, book, essay, report, theory, advocacy, testimony, manifesto, post, or movement.

**Style:**
- Terse and bullet-heavy
- Prioritize scan-ability — readers should be able to skip sections without losing the thread
- Prefer short labeled bullets over narrative paragraphs
- Use prose only when compression would sacrifice clarity

**Organization:**
- All evaluations live in `evaluations/`
- File naming: `YYYYMMDD_MixedCaseEvalTitle.md` (e.g. `20260322_HoganKnightsTemplar.md`)
- Supporting material (transcripts, source PDFs, clips, etc.) goes in a sibling folder: `YYYYMMDD_MixedCaseEvalTitle/`
- Maintain `evaluations/index.md` — one-line summary + link per eval, newest first

## Summary

### Specimen

- Title(s)
  - Format (interview, essay, documentary, thread, lecture, etc.)
  - Date published, accessed
  - Size (pages / minutes / words / MB)
- Sources: authors, claimants, wtnesses, presenters, promoters
- Meta-sources: platform, venue, outlet, channel
- Evaluated by: BrianThinks + [model/version]

### Synopsis

- Bulleted neutral description of what the specimen says

### Score

- BrianThinks evaluation, predictions, probabilities

## Sources

- For each source
  - Credentials: claimed vs verified
  - Incentives: financial, status, tribal
  - Record: notable past claims
  - History: summary of how the source's origin and evolution
  - Transparency: what notable facts above does the specimen leave unsaid?
- This section is the heavy lifting for the AI agent. It needs to dig deep into each 

## Stakes: Most Notable Predictions

- Quoted with context and verifiable citation

## Strengths: Most Credible Claims

- Probabilities, falsification, counterfactuals, implications

## Stumbles: Least Credible Claims

- Probabilities, falsification, counterfactuals, implications

## Sins: Epistemic Hygiene

Active violations — errors in what the specimen *said*, argued, or reasoned. Each violation names the commandment, quotes the instance, and explains the failure. Native commandments (violations of what was *said* or *concluded*):

- **Vide Cui Bono** — undisclosed incentives shaping the argument
- **Avoid Rage Bait** — anecdotes and strawmen substituted for aggregate data
- **Be Charitable** — opponents' positions misrepresented or bad-faithed
- **Beware Bias** — motivated reasoning, anchoring, tribal favoritism unreflected
- **Converge On Facts** — evidence not converging is treated as converging
- **Be Falsifiable** — claims immunized against any possible disconfirmation
- **Argue Your Best** — weakest argument led; stronger ones abandoned without examination
- **Test The Best** — quantity of claims substituted for quality of best evidence
- **Audit Luxury Beliefs** — beliefs held at zero personal cost, signaling loyalty over truth

## Silence: Things Unsaid

Omission violations — what a forthright, informed, non-conflicted speaker *should have surfaced* but didn't. For each item ask: what did they know or should have known, and why wasn't it said? Native commandments (violations of what was *withheld*):

- **Falsus Vel Tacitus** — source is wrong or silent about something they should have known or admitted
- **Follow the Money** — undisclosed financial conflicts or unexploited market implications
- **Master the Literature** — existing scholarship that contradicts the claim, omitted
- **Also Assess Answers** — implied conclusions hidden behind "just asking questions"
- **Steelman First** — best opposing argument not presented to the audience
- **Believe Your Beliefs** — market/prediction implications of the claim, not surfaced
- **Explain Consensus** — expert disagreement not accounted for in the argument
- **Question Revelation** — contradicting sources exist and were not tested against
- **Bet On It** — no odds offered; evasion of epistemic accountability
- **Predict It** — no testable predictions stated; unfalsifiable future left implicit

## Steelman

- The strongest possible version of the claimant's overall thesis
- Evaluation/probabilities for it

## Scorecard

- Expand the evaluation and least credible claims with evidence, arguments
- Give qualitative/quantitative judgments about sources

## Evidence

All empirical claims are cited inline with `†` linking to entries here. See [`~/bin/AgentRules.md`](~/bin/AgentRules.md) § Evidence for the full standard.

**MDwiki note:** Do not use raw `<a id>` tags — MDwiki breaks on them. Use the heading text as the anchor: `### My Claim Title` → link as `[†](#my-claim-title)` (lowercase, spaces→hyphens, parens dropped).

Each entry follows this structure:

### description-as-slug

- **Claim:**
- **Source:**
- **Dates:**
- **Quote/data:**

## History

- 2026.03.22 Created

## References

- The best references for each side
- Whether they were omitted/engaged by the specimen

## TODOs

- Improvements needed in this document
