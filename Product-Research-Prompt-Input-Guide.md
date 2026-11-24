# Product Research Prompt Input Guide

## Quick Workflow

```text
Stage 0.1 (separate discovery run)
 > Connected 0.2: quality evidence > scores/routing
 > Connected 0.3: market > feasibility > decisions/handoff
 > Connected 1A: preparation
 > Connected 1B: market > feasibility > 11-column decisions
 > Individual Prompt 2 > Stage 3 > Pilot Test > Results Review
```

Pause after every step or research unit above. 0.2, 0.3 and 1B research at most two products per response, repeating the current evidence step until their fixed group of up to five is covered. Their decision step then handles the group. 1A preparation remains up to five per response.

## Connected Entry Prompts

| Use after | Open this entry prompt | Work per response |
|---|---|---|
| Stage 0.1 discovery | [Connected 0.2 to 0.3](<./[prod]uct [res]earch procedure/GCC-Connected-0.2-to-0.3.md>) | One evidence unit of up to 2, or one group decision step, per `CONTINUE` |
| Stage 0.3 selection | [Connected 1A to 1B](<./[prod]uct [res]earch procedure/GCC-Connected-1A-to-1B.md>) | Prepare up to 5; then one 1B evidence unit of up to 2, or one group decision step, per `CONTINUE` |

For a chat without workspace access, attach the two methodology files named in the entry prompt and provide its required candidate/source records. Paste its copyable prompt once, then reply `CONTINUE` for each next step or research unit. The next response resumes unfinished work first. A filename alone does not supply a file's contents.

| Method | Internal steps, with a pause after every response |
|---|---|
| 0.2 | `0.2-E` quality evidence, repeated for all group IDs > `0.2-D` scores and routing |
| 0.3 | `0.3-M` market evidence, repeated > `0.3-F` feasibility evidence, repeated > `0.3-D` scores and handoff |
| 1B | `1B-M` market evidence, repeated > `1B-F` feasibility evidence, repeated > `1B-D` final table and decisions |

For five products, an evidence step normally runs as 2 + 2 + 1 before moving on. Decision steps use the collected records; a named decision-changing gap schedules focused recovery. Evidence records alone do not advance a product or finalize its score.

Each group completes both stages before the next group starts. Groups can contain fewer than five; empty downstream groups are skipped. Preserve the actual product/source records with the checkpoint when changing chats. Cumulative rankings remain interim until the supplied pool is processed; a partial pool is not the whole project.

The original stage files remain the methodology and can still be run separately using the same internal pauses. Their research criteria, scores and final table formats are preserved. Optional 2A still checks one competitor alternative after it is noticed during individual Prompt 2 research.

## Keeping Research Between Steps

The 15-product staged prompt, both connected workflows, standalone 0.2/0.3/1B and individual Prompt 2 include the same saved-state rules. These rules are inside the prompts; there is no additional methodology file to attach.

When file tools are available, the agent creates a versioned `research-state-[RUN_ID]-vNNN.xlsx` with three sheets:

- `Products`: actual findings, identities/URLs, comparisons, calculations, decisions and their revision history.
- `Sources`: complete source URLs/documents, captured claims, dates, country/model scope and verification limits.
- `Progress`: the input registry/scope, current unit, completed/remaining IDs and exact next step.

A versioned JSON file with the same collections is the fallback when file tools work but workbook tools do not.

```text
Open latest state > Run one unit > Save new version > Reopen and check > PAUSE
```

Download each checkpoint version when offered. Continue in the same chat normally; reattach the latest version if the agent cannot reopen it. Before a final decision, consolidation or export, the agent must read the saved records again. In a new chat, provide the usual prompt/module files plus the latest research-state file. The state file is research output, not another prompt. Keep earlier checkpoint versions as backups.

For example: `Use the attached research-state file. Reopen and validate it, then resume only its recorded next unit. Preserve prior products and sources.`

If file creation is unavailable, the agent must say `TEXT EXPORT ONLY` and return a self-contained unit export using its normal output blocks. Retain those blocks and provide the relevant product/source exports before later consolidation. IDs and an instruction to remember them are insufficient. A failed file write must not be described as saved; its pending update must be recovered before dependent work. Missing earlier records must be requested, never guessed.

Prompt 2's supporting modules return changes to the main controller, which is the sole file writer. The saved records preserve the detailed dossier, three economic scenarios, Notes and exports; compact checkpoint messages do not replace those findings. A storage check preserves recorded evidence and limitations, not a guarantee that every source claim is true.

## Input Capacity

| Stage or Prompt | Input per Run | Main Purpose |
|---|---:|---|
| Stage 0.1 - Raw Discovery | Up to 15 new products | Discover raw product opportunities; build toward a cumulative list of 100 |
| Stage 0.2 - Quality Filtering | Up to 5 in the group; research up to 2 per response | Collect quality evidence, then score and route the group |
| Stage 0.3 - Commercial Pre-Screening | Up to 5 in the group; research up to 2 per response | Market evidence, feasibility evidence, then group scoring and selection |
| Prompt 1A - Candidate Verification | Up to 5 products | Verify and prepare the strongest candidates for full screening |
| Prompt 1B - Full Screening | Up to 5 prepared products; research up to 2 per response | Market evidence, feasibility evidence, then the group's final 11-column table |
| Prompt 2 - Individual Commercial Validation | 1 product | Perform detailed commercial, supplier, demand, UGC, and unit-economics validation |
| Optional Prompt 2A - Competitor Alternative | 1 alternative product | Compare a potentially stronger competitor or product variation |
| UGC and Demand Validation Tool | 1 product | Assess marketplace traction, creator content and named evidence gaps |
| Evidence Gap Closure Tool | 1 product | Research specific missing or unverified evidence |
| Product Decision Summary Tool | 1 product | Produce a short final decision summary |
| Standardized Notes Tool | 1 product | Convert research into consistent compact notes |
| Stage 3 - Supplier and Sample Validation | 1 SAMPLE product | Verify the supplier, order and test a sample, and update economics |
| Pilot or Stage 4 Testing | 1 product or test | Run a controlled pilot and review real performance |

## Reading Demand Results

The 15-product route and Individual Prompt 2 now report observed traction ENCOURAGING / MIXED / WEAK / UNASSESSABLE, supporting facts and separate HIGH/MEDIUM/LOW evidence confidence, not a 0-100 Demand Index. ENCOURAGING with LOW confidence means a plausible research opportunity with limitations, not approved inventory. One credible buying/activity source can justify more research; a second source strengthens confidence but is not a fixed quota. Individual Prompt 2's other four commercial weights total 80; demand stays separate and old /100 scores are not converted. Keep the existing review, supplier, economics and sample-risk checks. Earlier discovery/1A/1B methods retain their own criteria. Historical state files are not rewritten by this change.

## Easy Way to Remember

`Discover up to 15 at a time > groups of up to 5 through connected checks > every advancing product validated individually > each approved sample tested individually`

## Important Rule

Prompt 1B handles every eligible prepared candidate in its current handoff, up to five across multiple responses. Five is a group size, not a cap on total advancing products or a requirement to research five in one response. After Prompt 1B, Prompt 2 and every later validation stage run separately for each advancing product. A screening YES advances research; it does not approve a sample or inventory purchase.
