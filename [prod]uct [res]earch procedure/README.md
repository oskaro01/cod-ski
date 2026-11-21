# Product research workflow

Workspace integration: 2026-11-18. Existing active filenames are retained so open tabs and references continue to work. Some filenames contain older version numbers; the integrated content is based on the newer supplied revisions listed below.

```text
0.1 Discovery > 0.2 Quality > 0.3 Commercial pre-screen
 > 1A Preparation > 1B Screening > Individual Prompt 2
 > Stage 3 Sample validation > Controlled pilot > Actual results review

Optional alternative: user requests 2A > quick verdict > user approval
 > next unused Product ID > separate full Individual Prompt 2

Supplied-list alternative: 15-product staged screening
 > user selects one product > Individual Prompt 2

Inside Prompt 2 (pause after each stage):
Identity > Market/reviews > Demand/UGC > Suppliers > Economics/risks
 > Gap audit/closure > Final decision > Notes/exports
```

| Stage | Active workspace file | Imported reference | Default work per execution |
|---|---|---|---|
| 0.1 | `GCC-Stage-0.1-100-Product-Raw-Discovery-v2.0.md` | v2.1 | Up to 15 new candidates; 100 cumulative |
| 0.2 | `GCC-Stage-0.2-Quality-Filtering-100-to-50-60-v1.2.md` | v1.3 | Up to 5 candidates |
| 0.3 | `GCC-Stage-0.3-Commercial-Pre-Screening-50-60-to-20-30-v1.1.md` | v1.2 | Up to 5 candidates |
| 1A | `GCC-UGC-Prompt-1A-Candidate-Verification-and-Screening-Preparation-FINAL.md` | v1.1 | Up to 5 selected or explicitly promoted reserve candidates |
| 1B | `GCC-UGC-Prompt-1B-Full-Screening-and-Decision-Completion-FINAL.md` | v1.1 | Up to 5 prepared candidates |
| Supplied-list screening | `GCC-15-Product-Staged-Screening-Plain-Output.md` | Execution 1.3; checklist-first decisions; Demand v3.0 supporting comparison | Normally 15 supplied products; research groups up to 5, conditional recovery up to 2, with pauses |
| Prompt 2 | `[light]individual-prod-two-col-markdown-table-after-research-FINAL.md` | Execution v1.5; Demand v3.0; existing commercial weights | One product; one checkpointed stage per response; accepts 1B, approved 2A, selected staged record or direct user selection |
| Optional 2A | `GCC-UGC-Prompt-2A-Quick-Competitor-Opportunity-Validation-v1.0.md` | v1.0 | One alternative; quick check only |
| Stage 3 | `Stage-3-Supplier-and-Sample-Validation.md` | Existing workspace version | One SAMPLE product; physical evidence required |

## Using the handoffs

Pass the current group's rows, evidence references, decisions, unresolved questions and checkpoint to the next stage. Keep completed groups in a cumulative record. Do not reprint the entire project at every step. Partial checkpoints include actual completed evidence and the remaining IDs/action; an ID-only summary cannot restore lost research.

The Stage 0.1 export now has eleven columns: the original eight identity fields plus Original Product URL, Link Verification Status and Link Checked At. Stage 0.2 can begin from this log without a separate source register. Later stages append verification evidence and preserve the original record.

Candidate ID is the original discovery identity. Assign Product ID once using the cumulative project registry; preserve any already-existing legacy Discovery ID without requiring one. For a 2A alternative, preserve the parent Product ID and approval record rather than inventing a previous 1B YES. Check for duplicates before creating an alternative.

Original Product URL is immutable. Direct Product URL is the current verified page for the same product. When recovery is necessary, preserve both URLs with the match basis, source, date and reason. A category/search page cannot establish product identity. Temporary access failure is a verification dependency; it does not establish weak demand or poor quality.

## Supporting documents and preserved files

- `optional-tools/README.md` maps four separate supporting modules to the staged Prompt 2: demand/UGC, gap audit/closure, decision summary and Notes. They also work independently for later updates. Attach the files in chats without workspace access; a local filename alone does not supply module content.
- `GCC-Selection-Sheet-and-Competitor-Opportunity-Tracker-Spec-v1.0.md` describes a future workbook update. No XLSX or Google Drive files were changed by this integration.
- `archive/2026-11-18-before-link-and-handoff-fixes/` contains exact backups of the seven replaced workspace documents.
- `archive/2026-11-18-reference-inputs/` contains untouched copies of all nine supplied reference documents, including the upstream revision notes. Their statements about workbook audits are upstream claims, not independently verified results of this integration.
- Master v2, Master v2.1 and Commercial Validation v2 remain reference methodologies, not extra mandatory executions.
- Existing Prompt 2.5, Stage 4 and the workflow image were preserved. The image may reflect an older workflow; the text flow here describes this integration. Forecasting prompts were not reviewed or revised in this task.

## Scope of this integration

Fixed direct-link provenance, Candidate/Product ID continuity, reserve admission, source-record handoffs, malformed/incomplete tables, Prompt 2A entry into deep research, duplicate handling, per-execution batch sizes and partial checkpoints.

The current 15-product route and Individual Prompt 2 use Demand Index v3.0: an evidence-strength purchasing rating, not an 80/20 marketplace/social blend or validated sales forecast. Research GCC opportunity evidence while treating UAE as the default launch market. Report actual supported country/model scope and separate UAE validation status/plan. Strong other-GCC purchasing evidence can advance a defensible UAE opportunity, but cannot establish UAE buying proof. Missing GCC creator content does not lower demand rating/confidence; creative demonstrations are assessed separately. Google Trends, Keyword Planner and search-interest scoring remain excluded.

The fixed 15-item sample checklist and explicit financial/safety/sourcing gates remain. D1/D2 now assess GCC buying evidence and UAE relevance/validation. A bounded physical SAMPLE may investigate a regional opportunity; UAE commercial pilot dependencies must be resolved before launch. Existing commercial weights remain demand 20, creative 15, economics 30, competition 10, supplier/execution 25. Scores remain prioritization heuristics, not success probabilities.

In supplied-list screening, the five checks for identity, GCC purchasing activity, independent corroboration/UAE relevance, quality concerns and sourcing/offer route determine advancement. The numerical index is supporting comparison information and cannot override a material gap or failure. This initial checklist does not replace Individual Prompt 2's detailed research, Notes, two export tables or sample-readiness checklist.

`archive/2026-11-18-before-prompt-2-demand-revision/` preserves the earlier pre-v1.2 Prompt 2. The v1.2 and v1.3 revision notes describe historical methodology/execution changes. `Observable-Market-Demand-v2.0-Revision-Notes.md` records the historical v2.0 method; v3.0 replaces its social weighting and UAE-only evidence restrictions in the two current routes and their modules. Earlier discovery/1A/1B prompts and reference masters retain their own historical criteria; they are not required when using the supplied-list alternative. Do not import their old demand scores without recomputation under v3.0.

Structural checks do not constitute live product validation, successful website access, a completed research run, supplier approval or a sample test.
