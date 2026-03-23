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

- Which of the BrianThinks epistemic commandments does the specimen specifically violate, and where?

## Silence: Things Unsaid, Implications, Counterfactuals

- Cite where the specimen should have considered alternative evidence/arguments but didn't
- Whether claimants engage the best critical forums/champions

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
