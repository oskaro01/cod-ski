# Connected GCC Workflow: Prompt 1A to Prompt 1B

## How to use

Use this entry prompt for candidates selected by Stage 0.3, plus any reserves the user explicitly promotes.

In a chat without workspace access, attach the two methodology files listed at the start of the copyable prompt.

Paste the copyable prompt below with Stage 0.3 Output E, its supporting records and the cumulative Product ID registry. For a new run, the first response prepares up to five candidates through 1A and pauses. Each `CONTINUE` then runs one 1B evidence unit, researching at most two products, or its final decision step. Finish screening this group before preparing the next. A resumed run follows its checkpoint's exact next unit.

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
- Existing 1A/1B rows, source evidence and connected checkpoint, if resuming.

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
3. Run 1B-M units for all prepared candidates, then 1B-F units, then 1B-D in separate responses. Use the actual 1A intake rows, gap log, Output C, briefs, upstream decisions and sources already available in this chat. Do not ask for another copy of available records. Keep final screening decisions PENDING until 1B-D; a hard blocker may skip unnecessary later research, with the reason preserved in its final row.
4. Apply all original 1B checks and decision rules. Research responses contain compact evidence deltas and source records. Keep the group's shared 2,400-word presentation target, exactly 11 final table columns and existing Notes guidance; do not write dossiers or duplicate findings at every pause. Decision steps do not browse. Follow 1B's focused recovery rules for a named decision-changing gap, at most two IDs, and record the step to return to afterward. Complete any partial decision output before preparing another group.
5. If 1A prepares zero eligible candidates, record PROMPT 1B SKIPPED - NO PREPARED CANDIDATES. After the pause, CONTINUE starts the next 1A group. If none remain, close the supplied scope in this checkpoint. Do not pad groups or convert a preparation block into a 1B NO decision.
6. Finish when every supplied candidate has a preparation disposition and every prepared candidate has a 1B-D disposition. Reconcile all received records, preparation exclusions and screening decisions. Report unresolved records separately from fully screened products. Stop before individual Prompt 2.

### Evidence reuse and product handoff

Preserve Candidate ID-to-Product ID mappings and the latest registry state across groups. Keep immutable Original Product URL, current Direct Product URL, model/variant, country, link dates, recovery history, source IDs, Stage 0.2 track/coverage and Stage 0.3 scores/decisions. A changed link never authorizes a changed product identity.

Reuse captured evidence and 1A's preparation work. Perform each methodology's required verification; reopen sources for current claims, changed content, conflicts or material gaps. Preserve verification limitations and distinctions between exact, comparable and category evidence. Do not count a reused source as new independent corroboration. Publish new or changed source records once with their URLs and supported findings.

1A prepares candidates and records gaps; it does not assign final screening decisions or a new preparation score. 1B assigns YES / MAYBE / NO / UNPROCESSED under its own rules. A preparation block does not authorize a replacement or automatic rejection for weak demand.

Keep the cumulative screening record and every YES candidate's direct product URL, decision basis, sources and open questions for individual Prompt 2. Do not cap or force YES results. At the end of the supplied scope, give reconciled totals and YES/MAYBE/NO/UNPROCESSED lists plus preparation exclusions, referencing the actual records without reprinting earlier reports. The user selects one advancing product for a separate Prompt 2 run. Never run Prompt 2 or 2A automatically.

### Connected checkpoint and continuation

Use one checkpoint per response. Extend 1A's existing checkpoint or 1B-D's summary checkpoint rather than printing another. Keep the active output budget. Include:

```text
Connected workflow: 1A -> 1B
Run label and supplied scope:
Current group and fixed Candidate IDs / Product IDs:
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

`CONTINUE` runs only the recorded next unit. Never restart a completed group or reassign a Product ID. If interrupted, finish the outstanding step before advancing. If earlier product/source records are no longer available, request those exact records; an ID-only checkpoint cannot restore evidence. A user-directed recovery must preserve prior history and re-establish preparation eligibility before a blocked candidate enters 1B.

Check ID mappings, handoff eligibility, source-to-claim matches, arithmetic, table columns and cumulative counts before pausing. Every supplied candidate must be accounted for, even when no candidates advance. End each response at the checkpoint.

For a new run, start with Prompt 1A only, then wait for `CONTINUE`. For a resumed run, execute only the checkpoint's next step/IDs and pause. If the supplied scope is already finished, report that status and wait for new input rather than restarting.

### Supplied records

[PASTE STAGE 0.3 OUTPUT E AND ITS SUPPORTING RECORDS HERE]

[PASTE THE PRODUCT ID REGISTRY, OR EXPLICITLY CONFIRM AN EMPTY NEW-PROJECT REGISTRY]

[IF RESUMING, INCLUDE THE LATEST CHECKPOINT AND ITS ACTUAL PRODUCT/SOURCE RECORDS]
