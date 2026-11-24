# Research modules and standalone tools

These files are separate modules used by Individual Prompt 2 v1.6. The folder name is retained for existing paths. Demand assessment, a gap audit, the decision explanation and Notes are part of the staged workflow. Additional browsing happens only when a material question needs it. Each file can also run independently for a later update.

| Need | File | Result |
|---|---|---|
| P2-3: marketplace, buyer, category/problem and creator evidence | `[UGC]-Search-and-Demand-Validation.md` | Demand assessment and focused evidence supplement; legacy filename retained |
| P2-6: audit and close decision-changing gaps | `[Evidence-Gap]-Closure.md` | Changes, unresolved dependencies and provisional readiness |
| P2-7: explain the fully assessed decision | `Product-[Decision]-Summary.md` | Decision, promising evidence, risks and next actions |
| P2-8: format final findings | `Standardized-[Notes].md` | Copy-ready Notes reused in both requested exports |

Typical use:

```text
P2-1 Identity > P2-2 Market/reviews > P2-3 Demand/UGC
 > P2-4 Suppliers > P2-5 Economics/risks > P2-6 Gap audit/closure
 > P2-7 Final decision > P2-8 Notes/exports
 > Stage 3 only when SAMPLE and the entry requirements pass
```

Each stage publishes findings and waits for CONTINUE. The main controller sets timing, output limits and approval gates. Reuse findings already captured; the modules do not launch repeated research automatically. P2-6 always audits gaps but can finish without browsing when none need research. The demand module can also support earlier screening as a standalone evidence tool; it cannot award that stage's YES.

## How to run

For the staged workflow, supply the main Individual Prompt 2 and these four files in a browsing-enabled chat. An agent with workspace access can read the modules at their assigned stage. ChatGPT cannot open a local path just because the prompt names it: attach the files at the start, or supply a requested module when needed. The controller discloses missing modules and follows its own available standards without pretending the missing file was read.

For standalone use, paste only the tool needed for the current question. Identify Product ID, exact variant and target country; reuse actual available records. In another conversation, supply the relevant stage findings, sources and latest supported decision. IDs alone cannot recover missing research.

Carry forward original/current product URLs, source references, dates and historical decisions. Each tool returns a bounded output and a checkpoint if unfinished. Use the main controller's research-state file or complete portable exports to preserve actual findings instead of relying on earlier chat messages.

## Saved-state ownership

The main Individual Prompt 2 contains the complete state-saving rules and is the sole writer of the versioned research workbook/JSON file. It reopens state before each stage, passes relevant records to a module, then saves and validates that module's findings with the stage output. Modules return complete changes and source records; they do not create competing versions or claim a write succeeded. No additional protocol attachment is required.

For standalone module use, provide the latest applicable state or actual product/source exports and keep the normal bounded output as a portable update. Request missing records when necessary; do not reconstruct facts from IDs or memory. Download the controller's checkpoint versions and reattach the latest if unavailable before later decisions/exports. If no file tools are available, `TEXT EXPORT ONLY` means the factual unit records must be retained and supplied for future work.

## Corrections made to the working notes

- Removed product-specific scores (70, 40 and 65), assumed screenshots and NIIMBOT/Baby Brezza facts from reusable instructions.
- Kept exact-product, competitor, category and problem evidence distinct. Related interest can reveal an opportunity but cannot prove the candidate's performance or sales.
- Separated research from summary/Notes formatting to reduce repeated browsing and output.
- Kept supplier documents before payment separate from physical tests after sample receipt; collection tasks state their timing.
- Preserved the existing 11-column sheet and canonical decisions: SAMPLE, RESEARCH MORE, HOLD and DROP. Plain-language summaries explain YES/MAYBE/NO alongside those decisions.

## Current methodology

Individual Prompt 2 execution is v1.6. Qualitative public-market traction replaces the numerical Demand Index: ENCOURAGING / MIXED / WEAK / UNASSESSABLE with facts and separate HIGH/MEDIUM/LOW evidence confidence. UAE is the default launch market; disclose actual country/model and current/historical scope. Regional storefront feedback may be MARKETPLACE-ASSOCIATED without proving buyer residency; explicitly global/imported pools are not GCC purchasing. One credible activity source can justify research; independent corroboration strengthens confidence rather than satisfying a fixed quota. Missing GCC UGC is not a traction/confidence penalty. Relevant inspected creative demonstrations remain part of U1, including international/editorial/brand evidence with limits disclosed.

Sample readiness retains 15 core items, 80% core minimum and all financial/safety/supplier entry gates. D1/D2 require a market case adequate for a bounded sample, with scope, confidence and UAE validation; an ENCOURAGING label alone does not approve SAMPLE. Resolve named UAE demand/fit dependencies before a UAE commercial pilot. Commercial weights remain creative 15, economics 30, competition 10 and supplier/execution 25, totalling 80 with no redistribution or normalization to /100. Keep the qualitative demand case separate. Preserve historical scores/denominators; formatting does not recalculate them. Detailed stages, Notes and both exports remain intact.

The pasted notes are design input, not verified product research. No example certification, price, review count, supplier relationship or screenshot is evidence for a new product.
