# Connected GCC Workflow: Stage 0.2 to Stage 0.3

## How to use

Use this entry prompt after Stage 0.1 discovery. Keep Stage 0.1 as its own run.

In a chat without workspace access, attach the two methodology files listed at the start of the copyable prompt.

Paste the copyable prompt below with the Stage 0.1 discovery rows and available evidence. Include existing decisions and checkpoints when resuming. The supplied records define the run's scope; a full pool of 100 is not required to start.

Keep a handoff group of up to five candidates. The first response collects quality evidence for its first up to two IDs and pauses. Each `CONTINUE` runs only the next evidence unit or decision step. Complete quality evidence and scoring before commercial market evidence, feasibility and final selection. Finish this sequence before taking the next group. A resumed run follows its checkpoint's exact next unit.

The methodology files define the smaller steps and retain their existing scores, evidence requirements, rejection rules and final output tables. This prompt connects their execution. Referencing a filename alone does not give a chat access to its contents.

## Copyable prompt

### Objective and required records

Required methodology files:

- Stage 0.2: `GCC-Stage-0.2-Quality-Filtering-100-to-50-60-v1.2.md`
- Stage 0.3: `GCC-Stage-0.3-Commercial-Pre-Screening-50-60-to-20-30-v1.1.md`

Run the supplied Stage 0.2 and Stage 0.3 methodologies as a connected workflow, with one step per response, at most two candidates researched per response and a mandatory pause after every response. The handoff group stays fixed at up to five.

Use the actual contents of the two methodology files named above. If either file is unavailable, request it before research; do not reconstruct its rules from its title. Apply this workflow's scheduling and current-group input rules when a standalone instruction tells you to stop or paste a handoff. Research, eligibility, scoring and decision rules remain governed by the active methodology. Execute only the current step, not its successor, in this response.

Inputs:

- Stage 0.1 discovery rows, original Candidate IDs, original/direct product URLs, discovery summary and available channel/source records.
- Existing Stage 0.2/0.3 rows, source evidence, decision history and checkpoint, if resuming.
- Optional project context already supplied, including target countries and business model.

Preserve source geography and country limits. Do not discover additional products, invent missing records or expand the supplied queue. Keep missing individual fields visible and recover them under the active methodology. Request missing candidate identities or unavailable prior records when they prevent a reliable continuation.

### Stage schedule

| Step | Response scope | Next step when accounted for |
|---|---|---|
| 0.2-E | Quality evidence for the next up to two IDs; repeat until the fixed group is covered | 0.2-D |
| 0.2-D | Existing quality scoring, decisions and Outputs A-F for the group, up to five | 0.3-M for eligible IDs only |
| 0.3-M | Commercial market/country/competition evidence for the next up to two routed IDs; repeat until covered | 0.3-F |
| 0.3-F | Supplier/economics/creative/fulfilment evidence for the next up to two routed IDs; repeat until covered | 0.3-D |
| 0.3-D | Existing commercial scoring, eight-channel ledger and Outputs A-H for all routed IDs, up to five | Next group's 0.2-E, or supplied scope finished |

1. For a new run, register the supplied queue, fix its next up to five Candidate IDs in existing order, and begin 0.2-E for the first up to two only. For a resumed run, validate the checkpoint against actual records and execute its exact next step/IDs. If an older checkpoint lacks step names, map already completed work from its evidence and final decision rows; request only records needed to establish the next step. Do not redo completed stages merely to change checkpoint format.
2. After every response, pause. CONTINUE finishes the current step's outstanding IDs first, at most two researched per response. Move to the next step only after the current group's work for this step has been performed or its gate/access limitations explicitly assessed. Final quality or commercial decisions remain PENDING until their respective D step; evidence capture alone cannot advance a candidate.
3. After 0.2-D, route only Track A SELECT candidates, separately labelled Track B CONDITIONAL ADVANCE candidates, and reserves explicitly marked SEND TO STAGE 0.3 RESERVE. Keep held reserves, REJECT and UNVERIFIED records in history. Reuse current-group quality rows and actual upstream evidence directly from this chat; do not demand another copy of the whole pool or promote/reopen candidates automatically.
4. If zero IDs qualify after 0.2-D, record STAGE 0.3 SKIPPED - NO ELIGIBLE CANDIDATES. Schedule the next group's 0.2-E after the pause, or close the supplied scope in this checkpoint if none remain. A commercial hard blocker can skip unnecessary remaining checks for that candidate, but its record still appears in 0.3-D. Do not pad groups or create scores for excluded candidates.
5. Decision steps use collected evidence without fresh browsing. Follow the active method's focused recovery rules for a named decision-changing gap, at most two affected IDs per response; record the step to return to after recovery. Carry unresolved access/private dependencies into the supported disposition instead of browsing indefinitely. Complete any partial decision output before starting a new group.
6. Finish when all supplied candidates have a 0.2-D disposition and all routed candidates have a 0.3-D disposition. Report unresolved, access-limited and unprocessed records separately from completed assessments. Stop before Prompt 1A.

### Evidence reuse and cumulative ranking

Carry Candidate ID, identity/model, immutable Original Product URL, current Direct Product URL, link status/date and recovery history through both stages. Preserve Track A/Track B, score type, dimension scores, evidence coverage, decisions, reasons and unresolved quality questions. A Track B commercial selection is not review-supported quality approval.

Reuse captured source statements and references. Perform each methodology's required verification; reopen sources for current claims, changed content, conflicts or material gaps. Do not repeat a completed discovery exercise or rescore quality merely because commercial research has started. Publish new or changed evidence once with its URL, date, country, product match and supported finding; later rows may reference that record.

Keep cumulative counts, rankings and reserve lists across groups. The 50-60 and 20-30 targets remain cumulative planning ranges under their existing selection rules. Group results are interim while the supplied queue remains. Later evidence or stronger candidates may change priority or reserve placement; append the reason and preserve earlier decisions. Do not lower standards or compare Track A and Track B quality scores as equivalent.

Evidence steps publish compact new findings, source records and the checkpoint. Existing final output tables are due only at 0.2-D and 0.3-D, using the current group's evidence records. Keep prior findings/groups available by reference instead of reprinting them. When the supplied scope finishes, include reconciled totals and advancing/reserve IDs referencing their actual rows. Do not claim a project-wide final ranking if only a subset of the discovery pool was supplied.

### Connected checkpoint and continuation

Use one checkpoint per response. At decision steps, extend the active method's existing checkpoint instead of printing another. Include:

```text
Connected workflow: 0.2 -> 0.3
Run label and supplied scope:
Current group and fixed Candidate IDs:
Active stage / step / state: PARTIAL / STEP ACCOUNTED FOR / GROUP ACCOUNTED FOR / SUPPLIED SCOPE FINISHED
Completed current-step IDs and actual evidence/decision record references:
Stage 0.3 eligible IDs / held or audit-only IDs:
Remaining IDs for this step / later steps still due:
Remaining discovery queue IDs:
Cumulative final decisions / selected and reserve ID references; pending decisions:
Unresolved questions and recovery actions:
Return step after focused recovery, if applicable:
Next step and exact IDs:
Next command: CONTINUE [step, group and outstanding IDs], or RUN FINISHED
```

`CONTINUE` runs only the recorded next unit. Never restart a completed group. If interrupted, resume the unfinished step rather than skipping to its successor. If earlier product/source records are no longer available, request those exact records; IDs and counts alone cannot restore research. A user-directed recovery must preserve the prior decision and record the new evidence before rerouting a candidate.

Check ID coverage, routing eligibility, source references, arithmetic and cumulative counts before pausing. Stage 0.3 cannot start until the current group's quality records support its routing. Use empty lists/counts honestly rather than inventing candidates or sources. End each response at the checkpoint.

For a new run, start with 0.2-E for the first up to two IDs only, then wait for `CONTINUE`. For a resumed run, execute only the checkpoint's next step/IDs and pause. If the supplied scope is already finished, report that status and wait for new input rather than restarting.

### Supplied records

[PASTE STAGE 0.1 DISCOVERY ROWS AND AVAILABLE EVIDENCE HERE]

[IF RESUMING, INCLUDE THE LATEST CHECKPOINT AND ITS ACTUAL PRODUCT/SOURCE RECORDS]
