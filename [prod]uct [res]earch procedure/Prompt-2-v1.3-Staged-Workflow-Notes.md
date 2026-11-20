# Prompt 2 v1.3: Checkpointed Workflow

## What changed

Execution now runs one stage per response:

`P2-1 Identity > P2-2 Market/reviews > P2-3 Demand/UGC > P2-4 Suppliers > P2-5 Economics/risks > P2-6 Gap audit/closure > P2-7 Final decision > P2-8 Notes/exports`

Each stage publishes actual findings, source references, gaps and a checkpoint, then waits for CONTINUE. An unfinished stage resumes before advancing. RECHECK targets a named question; changes invalidate dependent calculations until recomputed. A documented disqualifying finding can end research early with a sourced DROP.

The four supporting files remain separate modules in `optional-tools`. Their demand, gap-audit, explanation and Notes functions are integrated; extra browsing is conditional. Attach the main prompt and modules to chats without workspace access. Missing module content is disclosed, never assumed read. Stage records form the dossier; the complete dossier is not reprinted at every pause.

P2-7 applies the full decision rubric before producing the plain-language summary. Earlier module outputs are provisional and cannot approve SAMPLE. P2-8 formats the supported decision into Notes and the existing two exports. Stage 3 still requires SAMPLE and the actual stage/source records.

The entry routes now explicitly include a user-selected 15-product screening record and direct user selection. Preserve the actual provenance; no fabricated 1B result is needed.

## What remains the same

- One product per Prompt 2 run.
- Demand methodology v1.2: marketplace 60%, search 20%, GCC social 20%.
- Commercial weights: demand 20, creative 15, economics 30, competition 10, supplier/execution 25.
- Fixed 15-item core checklist, 80% core minimum, confidence and explicit SAMPLE gates.
- Three economic scenarios, source-based assumptions, sensitivity checks and supplier specification comparisons.
- Sample testing, payment verification and inventory decisions belong to their later validation gates.

Execution version v1.3 is not a new score methodology. Prior v1.2 scores change only when evidence or assumptions change.

## 15-Product Demand Index Audit

The existing formulas were correct. Clarifications now specify component-specific evidence standards, the difference between not-yet-assessed and unavailable sources, and a MEDIUM demand-confidence cap when search/local social is missing. Zero requires affirmative evidence; a failed search is UNKNOWN. Global demonstrations remain creative evidence rather than local demand.

Illustrative arithmetic checks (synthetic inputs, not product research):

| M | S | L | Result | Coverage |
|---:|---:|---:|---|---:|
| 80 | 40 | 20 | FULL 60 | 100% |
| 80 | unavailable | 20 | PROVISIONAL 65 | 80% |
| 80 | unavailable | unavailable | PROVISIONAL 80 | 60% |
| 80 | 0, adequately assessed | unavailable | PROVISIONAL 60 | 80% |
| unavailable | 80 | 80 | INSUFFICIENT EVIDENCE, no composite | 40%, no marketplace assessment |

These checks verify arithmetic and branch behavior. They do not establish successful live model execution, source access, demand, supplier reliability or profitability.
