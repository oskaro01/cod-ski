# Product research workflow

Workspace integration: 2026-11-18. Existing active filenames are retained so open tabs and references continue to work. Some filenames contain older version numbers; the integrated content is based on the newer supplied revisions listed below.

```text
0.1 Discovery > 0.2 Quality > 0.3 Commercial pre-screen
 > 1A Preparation > 1B Screening > Individual Prompt 2
 > Stage 3 Sample validation > Controlled pilot > Actual results review

Optional alternative: user requests 2A > quick verdict > user approval
 > next unused Product ID > separate full Individual Prompt 2
```

| Stage | Active workspace file | Imported reference | Default work per execution |
|---|---|---|---|
| 0.1 | `GCC-Stage-0.1-100-Product-Raw-Discovery-v2.0.md` | v2.1 | Up to 15 new candidates; 100 cumulative |
| 0.2 | `GCC-Stage-0.2-Quality-Filtering-100-to-50-60-v1.2.md` | v1.3 | Up to 5 candidates |
| 0.3 | `GCC-Stage-0.3-Commercial-Pre-Screening-50-60-to-20-30-v1.1.md` | v1.2 | Up to 5 candidates |
| 1A | `GCC-UGC-Prompt-1A-Candidate-Verification-and-Screening-Preparation-FINAL.md` | v1.1 | Up to 5 selected or explicitly promoted reserve candidates |
| 1B | `GCC-UGC-Prompt-1B-Full-Screening-and-Decision-Completion-FINAL.md` | v1.1 | Up to 5 prepared candidates |
| Prompt 2 | `[light]individual-prod-two-col-markdown-table-after-research-FINAL.md` | Individual-product v1.1 | One YES, user-promoted MAYBE, or approved 2A alternative |
| Optional 2A | `GCC-UGC-Prompt-2A-Quick-Competitor-Opportunity-Validation-v1.0.md` | v1.0 | One alternative; quick check only |
| Stage 3 | `Stage-3-Supplier-and-Sample-Validation.md` | Existing workspace version | One SAMPLE product; physical evidence required |

## Using the handoffs

Pass the current group's rows, evidence references, decisions, unresolved questions and checkpoint to the next stage. Keep completed groups in a cumulative record. Do not reprint the entire project at every step. Partial checkpoints include actual completed evidence and the remaining IDs/action; an ID-only summary cannot restore lost research.

The Stage 0.1 export now has eleven columns: the original eight identity fields plus Original Product URL, Link Verification Status and Link Checked At. Stage 0.2 can begin from this log without a separate source register. Later stages append verification evidence and preserve the original record.

Candidate ID is the original discovery identity. Assign Product ID once using the cumulative project registry; preserve any already-existing legacy Discovery ID without requiring one. For a 2A alternative, preserve the parent Product ID and approval record rather than inventing a previous 1B YES. Check for duplicates before creating an alternative.

Original Product URL is immutable. Direct Product URL is the current verified page for the same product. When recovery is necessary, preserve both URLs with the match basis, source, date and reason. A category/search page cannot establish product identity. Temporary access failure is a verification dependency; it does not establish weak demand or poor quality.

## Supporting documents and preserved files

- `GCC-Selection-Sheet-and-Competitor-Opportunity-Tracker-Spec-v1.0.md` describes a future workbook update. No XLSX or Google Drive files were changed by this integration.
- `archive/2026-11-18-before-link-and-handoff-fixes/` contains exact backups of the seven replaced workspace documents.
- `archive/2026-11-18-reference-inputs/` contains untouched copies of all nine supplied reference documents, including the upstream revision notes. Their statements about workbook audits are upstream claims, not independently verified results of this integration.
- Master v2, Master v2.1 and Commercial Validation v2 remain reference methodologies, not extra mandatory executions.
- Existing Prompt 2.5, Stage 4 and the workflow image were preserved. The image may reflect an older workflow; the text flow here describes this integration. Forecasting prompts were not reviewed or revised in this task.

## Scope of this integration

Fixed direct-link provenance, Candidate/Product ID continuity, reserve admission, source-record handoffs, malformed/incomplete tables, Prompt 2A entry into deep research, duplicate handling, per-execution batch sizes and partial checkpoints.

The existing Google Trends/search protocol, 40/30/30 Demand Index, 80% evidence-coverage rule, commercial weights and SAMPLE decision criteria have not been changed. The missing-search-data bottleneck remains deliberately deferred.

Structural checks do not constitute live product validation, successful website access, a completed research run, supplier approval or a sample test.
