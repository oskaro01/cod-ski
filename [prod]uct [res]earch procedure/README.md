# Product research workflow

Workspace integration: 2026-11-18. Existing active filenames are retained so open tabs and references continue to work. Some filenames contain older version numbers; the integrated content is based on the newer supplied revisions listed below.

```text
0.1 Discovery (separate run)
 > Connected 0.2 Quality evidence > Scores/routing
 > Connected 0.3 Market > Feasibility > Decisions/handoff
 > Connected 1A Preparation
 > Connected 1B Market > Feasibility > Decisions/table
 > Individual Prompt 2
 > Stage 3 Sample validation > Controlled pilot > Actual results review

Optional alternative: user requests 2A > quick verdict > user approval
 > next unused Product ID > separate full Individual Prompt 2

Supplied-list alternative: 15-product staged screening
 > user selects one product > Individual Prompt 2

Inside Prompt 2 (pause after each stage):
Identity > Market/reviews > Demand/UGC > Suppliers > Economics/risks
 > Gap audit/closure > Final decision > Notes/exports
```

## Connected stage runs

Use these entry prompts to connect the methods, one internal step per response, with a pause after every response:

- [Connected 0.2 to 0.3](GCC-Connected-0.2-to-0.3.md): fix a group of up to five discovery candidates; collect quality evidence in units of up to two, score/route the group, then commercially research and score eligible candidates through their own steps.
- [Connected 1A to 1B](GCC-Connected-1A-to-1B.md): prepare up to five Stage 0.3-selected candidates, then screen prepared candidates through market and feasibility evidence units of up to two before their final group table.

| Method | Internal steps |
|---|---|
| 0.2 | `0.2-E` quality evidence > `0.2-D` scores and routing |
| 0.3 | `0.3-M` market > `0.3-F` feasibility > `0.3-D` scores and handoff |
| 1B | `1B-M` market > `1B-F` feasibility > `1B-D` final 11-column table and decisions |

Evidence steps repeat for the next up to two group IDs on each response; for five products that is normally 2 + 2 + 1. Reply `CONTINUE` for the recorded next unit or step. Finish both methods for the current group before starting another group. Partial work resumes first; empty downstream groups are skipped. Final scores and selections are due at decision steps, which assemble existing findings without new browsing. A named decision-changing gap schedules focused recovery under the method's rules.

Cumulative rankings stay interim while the supplied pool remains. Track labels, weights, thresholds, decisions, IDs, final table formats and source evidence are preserved. Standalone 0.2, 0.3 and 1B use the same internal pauses. Stage 0.1, 1A preparation and individual Prompt 2 were not subdivided by this update.

In a chat without workspace access, attach each entry prompt's two methodology files and provide its required candidate/source records. The entry prompt connects scheduling and current-group handoffs; the method files define their internal steps and govern research, scoring, eligibility and output requirements. Do not paste only filenames or expect an ID-only checkpoint to restore unavailable evidence. Stage 0.1, individual Prompt 2, optional 2A and Stage 3 retain their separate execution boundaries.

The following table lists the underlying methods, which can also be run separately.

| Stage | Active workspace file | Imported reference | Default work per execution |
|---|---|---|---|
| 0.1 | `GCC-Stage-0.1-100-Product-Raw-Discovery-v2.0.md` | v2.1 | Up to 15 new candidates; 100 cumulative |
| 0.2 | `GCC-Stage-0.2-Quality-Filtering-100-to-50-60-v1.2.md` | v1.3; staged execution | Group up to 5; evidence up to 2 per response, then group decisions |
| 0.3 | `GCC-Stage-0.3-Commercial-Pre-Screening-50-60-to-20-30-v1.1.md` | v1.2; staged execution | Group up to 5; market/feasibility units up to 2 per response, then group decisions |
| 1A | `GCC-UGC-Prompt-1A-Candidate-Verification-and-Screening-Preparation-FINAL.md` | v1.1 | Up to 5 selected or explicitly promoted reserve candidates |
| 1B | `GCC-UGC-Prompt-1B-Full-Screening-and-Decision-Completion-FINAL.md` | v1.1; staged execution | Group up to 5 prepared; market/feasibility units up to 2 per response, then final table |
| Supplied-list screening | `GCC-15-Product-Staged-Screening-Plain-Output.md` | Execution 1.3; checklist-first decisions; Demand v3.0 supporting comparison | Normally 15 supplied products; research groups up to 5, conditional recovery up to 2, with pauses |
| Prompt 2 | `[light]individual-prod-two-col-markdown-table-after-research-FINAL.md` | Execution v1.5; Demand v3.0; existing commercial weights | One product; one checkpointed stage per response; accepts 1B, approved 2A, selected staged record or direct user selection |
| Optional 2A | `GCC-UGC-Prompt-2A-Quick-Competitor-Opportunity-Validation-v1.0.md` | v1.0 | One alternative; quick check only |
| Stage 3 | `Stage-3-Supplier-and-Sample-Validation.md` | Existing workspace version | One SAMPLE product; physical evidence required |

## Using the handoffs

Pass the current group's rows, evidence references, decisions, unresolved questions and checkpoint to the next stage through the validated research-state file or complete portable exports. Keep completed groups in that cumulative record. Do not reprint the entire project at every step. An ID-only summary cannot restore lost research.

The Stage 0.1 export now has eleven columns: the original eight identity fields plus Original Product URL, Link Verification Status and Link Checked At. Stage 0.2 can begin from this log without a separate source register. Later stages append verification evidence and preserve the original record.

Candidate ID is the original discovery identity. Assign Product ID once using the cumulative project registry; preserve any already-existing legacy Discovery ID without requiring one. For a 2A alternative, preserve the parent Product ID and approval record rather than inventing a previous 1B YES. Check for duplicates before creating an alternative.

Original Product URL is immutable. Direct Product URL is the current verified page for the same product. When recovery is necessary, preserve both URLs with the match basis, source, date and reason. A category/search page cannot establish product identity. Temporary access failure is a verification dependency; it does not establish weak demand or poor quality.

## Saved research state

State protocol `research-state-1` is embedded in the 15-product staged prompt, both connected controllers, standalone 0.2/0.3/1B and Individual Prompt 2. No extra methodology attachment is required. In connected use, the outer controller handles saving, including the 1A preparation checkpoint; invoked methods/modules return findings and changes without competing file writes.

With file tools, each checkpoint publishes a checked version of `research-state-[RUN_ID]-vNNN.xlsx` containing `Products`, `Sources` and `Progress`, or JSON collections with the same roles if workbook support is unavailable. Store actual stage findings and calculation inputs, full source records, historical revisions and exact continuation state. Preserve upstream products when later research narrows to one product.

Before a unit, reopen the latest state. Afterward, preserve prior records with file tools, save a new version, reopen it and check record preservation, ID/source references, counts and progress before claiming SAVED. A failed update remains uncommitted with a portable recovery export. Before scoring/final decisions/exports, read the state again; list missing records instead of reconstructing them from conversation memory. UNKNOWN values remain recorded limitations, not zeros or automatic storage failures.

Download checkpoint versions when supplied. Reattach the latest if the agent cannot reopen it, and carry it with the normal prompts/modules when moving chats. If file creation is unavailable, require `TEXT EXPORT ONLY` self-contained unit records, retained and supplied for later work. Source IDs without their full records are insufficient. These files supplement existing dossiers and final table formats; they do not create live spreadsheet integrations or new commercial approval gates. No actual product-state workbook is generated merely by editing these prompts.

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



======

Yes use the, **three files together**:

1. Individual **Stage 0.2** file.
2. Individual **Stage 0.3** file.
3. **GCC-Connected-0.2-to-0.3.md**.

Also provide your **Stage 0.1 results and source records**.

Then tell the agent:

```text
Use the connected 0.2-to-0.3 file as the workflow controller.
Use the individual 0.2 and 0.3 files as methodology references.

Start with 0.2-E only. Pause afterward and wait for CONTINUE.
```

Upload the files once in that conversation. Afterward, reply `CONTINUE` to advance through the steps.

**Later**, use the same arrangement for **1A + 1B + Connected-1A-to-1B**, together with your Stage 0.3 results.


======

Yes, this reveals a weakness in our setup: **the checkpoints still depend on earlier chat messages being available.** More pauses won’t preserve those details by themselves.

What you describe is consistent with context or retrieval limitations, although I can’t confirm the exact cause in that chat. Models have a limited working context. [OpenAI’s explanation](https://developers.openai.com/api/docs/guides/conversation-state)

**We should give the research a saved record outside the conversation.** I recommend one research workbook containing:

- **Products:** IDs, names, findings, checklist results, decisions and unresolved questions.
- **Sources:** Full URLs, captured facts, dates, country/model scope and verification limits. Source IDs alone aren’t enough.
- **Progress:** Completed units, remaining IDs and the exact next step.

The flow becomes:

```text
Research one unit
 > Update the research file
 > Verify earlier records remain intact
 > Publish a downloadable checkpoint version
 > Pause
 > CONTINUE
```

Before updating it, the agent must **open the existing file**, preserve previous records and change only the relevant entries. It shouldn’t recreate the workbook from memory.

Before FINAL, you attach the latest version again—even in the same chat—and say:

```text
Read the attached research file before consolidating.

Check that all 15 product IDs are accounted for and that
their source references resolve to complete source records.

Use the recorded findings. List any missing or conflicting
data explicitly; never reconstruct it from memory.
```

This also lets you move to a fresh chat without restarting research. File creation depends on the tools available in that chat; plain-text batch exports are a fallback.

For your **already lengthy chat**, recover the earlier published outputs first. Asking it to create a complete file now cannot reliably recover facts it has already lost access to.

I’d add this file-saving layer to our workflow next. No prompt edits made yet.

===

Done. Added saved-state handling to:

- The **15-product staged prompt**.
- Both **connected workflows**, plus standalone 0.2, 0.3 and 1B.
- **Individual Prompt 2** and its supporting modules.

The prompts now require:

```text
Open saved state > Research one unit > Save a new version
> Reopen and validate > Pause
```

Final decisions and exports must read the saved findings and full source records again. If file tools are unavailable, the agent must provide a portable text export and clearly say `TEXT EXPORT ONLY`.

**No extra prompt attachment is needed.** The agent generates the research-state file during your research run. Download checkpoint versions and reattach the latest when moving chats or when it becomes unavailable.

Updated the [Input Guide](C:/Users/ASUS/Desktop/cod-ski/Product-Research-Prompt-Input-Guide.md:37). Existing scoring rules, detailed Prompt 2 tables, scenarios and Notes were preserved.

Document checks passed; live ChatGPT execution hasn’t been tested yet.