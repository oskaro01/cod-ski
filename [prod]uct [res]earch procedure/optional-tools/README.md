# Research modules and standalone tools

These files are separate modules used by Individual Prompt 2 v1.3. The folder name is retained for existing paths. Demand assessment, a gap audit, the decision explanation and Notes are part of the staged workflow. Additional browsing happens only when a material question needs it. Each file can also run independently for a later update.

| Need | File | Result |
|---|---|---|
| P2-3: category, problem, search and creator evidence | `[UGC]-Search-and-Demand-Validation.md` | Demand assessment and focused evidence supplement |
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

Carry forward original/current product URLs, source references, dates and historical decisions. Each tool returns a bounded output and a checkpoint if unfinished. A checkpoint must contain the completed findings, not only an instruction to remember them.

## Corrections made to the working notes

- Removed product-specific scores (70, 40 and 65), assumed screenshots and NIIMBOT/Baby Brezza facts from reusable instructions.
- Kept exact-product, competitor, category and problem evidence distinct. Related interest can reveal an opportunity but cannot prove the candidate's performance or sales.
- Separated research from summary/Notes formatting to reduce repeated browsing and output.
- Kept supplier documents before payment separate from physical tests after sample receipt; collection tasks state their timing.
- Preserved the existing 11-column sheet and canonical decisions: SAMPLE, RESEARCH MORE, HOLD and DROP. Plain-language summaries explain YES/MAYBE/NO alongside those decisions.

## Current methodology

Individual Prompt 2 execution is v1.3; its demand/commercial methodology remains v1.2. It uses 60/20/20 GCC marketplace/search/social weights. Missing search/local-social data permits a PROVISIONAL demand score with explicit 60%/80% demand coverage when marketplace evidence is adequately assessed. It does not count as zero or establish a fully validated demand case. Global UGC supports creative potential, separately from local demand.

Sample readiness uses the fixed 15-item core checklist, 80% core minimum and explicit sample-entry requirements. Supplemental search/local-social gaps stay visible and affect confidence. Commercial weights are demand 20, creative 15, economics 30, competition 10 and supplier/execution 25. Preserve old scores and denominators as historical; report methodology changes separately from new evidence. See the main Prompt 2 for the complete rubric and gates.

The pasted notes are design input, not verified product research. No example certification, price, review count, supplier relationship or screenshot is evidence for a new product.
