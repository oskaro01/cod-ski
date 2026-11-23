# Connected GCC Workflow: Prompt 1A to Prompt 1B

## How to use

Use this entry prompt for candidates selected by Stage 0.3, plus any reserves the user explicitly promotes.

In a chat without workspace access, attach the two methodology files listed at the start of the copyable prompt.

Paste the copyable prompt below with Stage 0.3 Output E, its supporting records and the cumulative Product ID registry. Reuse the prior research-state file when available; keep its earlier products and append the new ID mappings and findings. For a new run, the first response prepares up to five candidates through 1A and pauses. Each `CONTINUE` then runs one 1B evidence unit, researching at most two products, or its final decision step. Download checkpoint versions when supplied and reattach the latest if it cannot be reopened. A resumed run follows its checkpoint's exact next unit. The saving rules are included here; no extra methodology file is required.

This workflow preserves 1A's preparation output and 1B's compact 11-column screening table. Individual Prompt 2 remains the next, separate deep-research step. Prompt 2A remains a separate check for a competitor alternative. Referencing a filename alone does not give a chat access to its contents.

## Copyable prompt

### Objective and required records

Required methodology files:

- Prompt 1A: `GCC-UGC-Prompt-1A-Candidate-Verification-and-Screening-Preparation-FINAL.md`
- Prompt 1B: `GCC-UGC-Prompt-1B-Full-Screening-and-Decision-Completion-FINAL.md`

Run the supplied Prompt 1A and Prompt 1B methodologies as a connected workflow, with one step per response and a mandatory pause after every response. 1A prepares up to five candidates as before. Each 1B research response covers at most two of those candidates; the final handoff remains up to five.

Use the actual contents of the two methodology files named above. If either file is unavailable, request it before research; do not reconstruct its rules from its title. Apply this workflow's scheduling and current-group input rules when a standalone instruction tells you to stop or paste a handoff. Research, eligibility, scoring, decision and output requirements remain governed by the active methodology. Execute only the current step, not its successor, in this response.

Inputs:

- Stage 0.3 Output E selected candidates, referenced source records and checkpoint; include the applicable Stage 0.2/0.3 track, scores, coverage, decisions and unresolved questions.
- Any explicitly user-promoted reserve candidates and their promotion records.
- Cumulative Product ID registry, including Candidate ID-to-Product ID mappings. If this is a new project, explicitly confirm an empty registry. If its state is unknown, request it before assigning IDs.
- Latest research-state file, or actual 1A/1B product/source exports and connected checkpoint, if resuming.

The supplied records define the run's scope. Preserve the candidate order and all existing IDs. Do not discover replacements, create another shortlist, promote reserves automatically or import the supplied-list screening method into this workflow. Missing individual fields are recoverable or disclosed gaps under the active methodology; absent candidate identities or inaccessible prior records must be recovered before claiming continuation.

### Stage schedule

| Step | Response scope | Next step when accounted for |
|---|---|---|
| 1A | Existing preparation outputs for the fixed group, up to five | 1B-M for PREPARED FOR FULL SCREEN candidates only |
| 1B-M | Market evidence for the next up to two prepared IDs; repeat until covered | 1B-F |
| 1B-F | Supplier/UGC/economics/risk evidence for the next up to two prepared IDs; repeat until covered | 1B-D |
| 1B-D | Existing decisions, 11-column table and summary for every candidate handed to 1B, up to five | Next group's 1A, or supplied scope finished |

1. For a new run, register the supplied eligible queue and take its next up to five candidates. Apply 1A only, using the registry to preserve/assign IDs. Keep its existing preparation outputs, 1,500-word target and brief limits. For a resumed run, validate the actual checkpoint and records, then execute the exact next step/IDs. Map older stage-only checkpoints from completed evidence/decision records; request missing records when the next step cannot be established. Do not redo completed work merely to change checkpoint format.
2. After every response, pause. CONTINUE finishes outstanding work in the current step first; each 1B research response covers at most two IDs. Only after all group members have a preparation disposition can PREPARED FOR FULL SCREEN records enter 1B-M. Preparation BLOCKED/UNPROCESSED records remain outside 1B; preserve them in the registry and exclusion history.
3. Run 1B-M units for all prepared candidates, then 1B-F units, then 1B-D in separate responses. Load the actual 1A intake rows, gap log, Output C, briefs, upstream decisions and sources from the validated state or complete portable exports. Do not ask for another copy of available records. Keep final screening decisions PENDING until 1B-D; a hard blocker may skip unnecessary later research, with the reason preserved in its final row.
4. Apply all original 1B checks and decision rules. Research responses contain compact evidence deltas and source records. Keep the group's shared 2,400-word presentation target, exactly 11 final table columns and existing Notes guidance; do not write dossiers or duplicate findings at every pause. Decision steps do not browse. Follow 1B's focused recovery rules for a named decision-changing gap, at most two IDs, and record the step to return to afterward. Complete any partial decision output before preparing another group.
5. If 1A prepares zero eligible candidates, record PROMPT 1B SKIPPED - NO PREPARED CANDIDATES. After the pause, CONTINUE starts the next 1A group. If none remain, close the supplied scope in this checkpoint. Do not pad groups or convert a preparation block into a 1B NO decision.
6. Finish when every supplied candidate has a preparation disposition and every prepared candidate has a 1B-D disposition. Reconcile all received records, preparation exclusions and screening decisions. Report unresolved records separately from fully screened products. Stop before individual Prompt 2.

### Evidence reuse and product handoff

Preserve Candidate ID-to-Product ID mappings and the latest registry state across groups. Keep immutable Original Product URL, current Direct Product URL, model/variant, country, link dates, recovery history, source IDs, Stage 0.2 track/coverage and Stage 0.3 scores/decisions. A changed link never authorizes a changed product identity.

Reuse captured evidence and 1A's preparation work. Perform each methodology's required verification; reopen sources for current claims, changed content, conflicts or material gaps. Preserve verification limitations and distinctions between exact, comparable and category evidence. Do not count a reused source as new independent corroboration. Publish new or changed source records once with their URLs and supported findings.

1A prepares candidates and records gaps; it does not assign final screening decisions or a new preparation score. 1B assigns YES / MAYBE / NO / UNPROCESSED under its own rules. A preparation block does not authorize a replacement or automatic rejection for weak demand.

Keep the cumulative screening record and every YES candidate's direct product URL, decision basis, sources and open questions for individual Prompt 2. Do not cap or force YES results. At the end of the supplied scope, give reconciled totals and YES/MAYBE/NO/UNPROCESSED lists plus preparation exclusions, referencing the actual records without reprinting earlier reports. The user selects one advancing product for a separate Prompt 2 run. Never run Prompt 2 or 2A automatically.

### Durable research state

State protocol: research-state-1. At intake create or reuse one downloadable research-state-[RUN_ID]-vNNN.xlsx with Products, Sources and Progress sheets. If workbook tools are unavailable but file tools work, use one versioned JSON file with those same collections. Inspect relevant records with tools rather than pasting the entire file into chat.

- Products: preserve the input registry and supplied upstream handoff records, Candidate/Product ID mappings, exact identity and original/current URLs. Store actual stage findings, comparisons, review observations, calculations/assumptions, risk checks, decisions, Notes and exports as they are produced. Use unique record IDs and stage/revision labels; retain superseded values and reasons. An ID/status list alone is not a research record.
- Sources: preserve full URLs or document references, captured claims/values, dates/periods, country/model scope, evidence labels, purchase/independence basis where relevant and access limits. Keep original source IDs plus unique source-record IDs scoped to the product/capture revision so reused labels cannot collide. Reference the applicable record/revision; do not save only source IDs.
- Progress: preserve run ID, schema/revision, active workflow and product scope, fixed group, completed/remaining units and IDs, next step/IDs, recovery return step, unresolved/stale dependencies and record counts. Keep other products and earlier workflow records when the active scope narrows.

Before each unit, reopen the latest file and validate run, revision and active scope. If an existing file is missing or unreadable, request that version or the actual unit exports before dependent work. Never rebuild missing earlier findings from memory. After the unit, use file tools to preserve previous records mechanically and append only new findings or explicit dated corrections. A retried unit must not duplicate completed records. New evidence can change an assessment; preserve its reason and mark affected older calculations/decisions STALE until reassessed.

Save a new version without overwriting the last good file, then reopen it. Verify prior record IDs/values and history are retained, record IDs are unique, source references resolve or are explicitly missing, counts reconcile and the next unit matches actual progress. Recorded UNKNOWN/NOT CAPTURED values are valid limitations, not failed storage or zero values. Publish a real download link and the version, counts, validation status and next step in the existing checkpoint. Do not claim SAVED from an intended write or an unchecked filename. On write/validation failure, keep the last good version, return the unit as a portable export and mark it uncommitted. Before dependent work, merge/check that export or explicitly continue from complete text exports; never silently use the older file as if the update succeeded.

Before scoring, final decisions, consolidation or exports, reopen the latest state and read the required product/source records. Check the expected unique IDs against the active scope; multiple historical rows are not extra products. List missing/conflicting records explicitly and pause dependent conclusions instead of inventing them. Stored evidence retains its original date and verification limits; storage does not prove source accuracy.

If file creation is unavailable, label TEXT EXPORT ONLY and make the unit's factual output a self-contained portable export: run/revision and unit IDs, exact identities/URLs, actual findings, complete referenced source records, changes and next action. Reuse the normal output blocks; do not add another dossier. Repeated URLs are allowed here when necessary for portability. The user must retain/re-supply these exports for later units or final consolidation; do not promise hidden file persistence. If an export cannot fit the response budget, return labelled parts with remaining record IDs and pause until the export is complete.

The outer connected or Prompt 2 controller is the sole state writer. An invoked methodology/module returns records and changes to it without creating competing versions. When this prompt runs standalone, it owns the state update. State files supplement the existing deliverables and require no extra methodology attachment.

### Connected checkpoint and continuation

Use one checkpoint per response. Extend 1A's existing checkpoint or 1B-D's summary checkpoint rather than printing another. Keep the active output budget. Include:

```text
Connected workflow: 1A -> 1B
Run label and supplied scope:
Current group and fixed Candidate IDs / Product IDs:
State file/revision, record counts, validation status and actual download link, or TEXT EXPORT ONLY:
Active stage / step / state: PARTIAL / STEP ACCOUNTED FOR / GROUP ACCOUNTED FOR / SUPPLIED SCOPE FINISHED
Prepared IDs / preparation-blocked or unprocessed IDs:
Completed current-step IDs and actual evidence/decision record references:
Remaining IDs for this step / later steps still due:
Remaining preparation queue IDs:
Cumulative final screening decisions / preparation exclusions; pending decisions:
Candidate-to-Product ID registry reference and latest assigned Product ID:
Source-record references / unresolved questions and recovery actions:
Return step after focused recovery, if applicable:
Next step and exact IDs:
Next command: CONTINUE [step, group and outstanding IDs], or RUN FINISHED
```

`CONTINUE` runs only the recorded next unit after reopening its validated state or actual portable exports. Never restart a completed group or reassign a Product ID. If interrupted, finish the outstanding step before advancing. If earlier product/source records are no longer available, request the saved state or those exact exports; an ID-only checkpoint cannot restore evidence. A user-directed recovery must preserve prior history and re-establish preparation eligibility before a blocked candidate enters 1B.

Check ID mappings, handoff eligibility, source-to-claim matches, arithmetic, table columns and cumulative counts before pausing. Every supplied candidate must be accounted for, even when no candidates advance. End each response at the checkpoint.

For a new run, start with Prompt 1A only, then wait for `CONTINUE`. For a resumed run, execute only the checkpoint's next step/IDs and pause. If the supplied scope is already finished, report that status and wait for new input rather than restarting.

### Supplied records

[PASTE STAGE 0.3 OUTPUT E AND ITS SUPPORTING RECORDS HERE]

[PASTE THE PRODUCT ID REGISTRY, OR EXPLICITLY CONFIRM AN EMPTY NEW-PROJECT REGISTRY]

[IF RESUMING, ATTACH THE LATEST RESEARCH-STATE FILE OR COMPLETE RELEVANT UNIT EXPORTS AND CHECKPOINT]
