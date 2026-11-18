# GCC Approved Prompt Revision Notes

**Version:** 1.0  
**Prepared from:** User-approved checklist selections  
**Scope:** Stage 0.1–0.3, Prompt 1A, Prompt 1B, Prompt 2, new Prompt 2A,
and a companion workbook specification

------------------------------------------------------------------------

## 1. Files prepared

| Revised file                                                                 | Version | Main changes                                                                                                                                                                                                                       |
|------------------------------------------------------------------------------|--------:|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GCC-Stage-0.1-100-Product-Raw-Discovery-v2.1.md`                            |     2.1 | Mandatory accessible direct product page; no category/search/homepage candidates; discard untraceable leads before assigning Candidate IDs; exact/comparable/variant match types; no quota padding.                                |
| `GCC-Stage-0.2-Quality-Filtering-100-to-50-60-v1.3.md`                       |     1.3 | Direct-product-page eligibility gate before Track A/B assignment or scoring; same-product link recovery; Q19 rejection reason; link-ineligible candidates excluded from Stage 0.3.                                                 |
| `GCC-Stage-0.3-Commercial-Pre-Screening-50-60-to-20-30-v1.2.md`              |     1.2 | Direct-product-page gate before scoring/selection; C16 rejection reason; direct URL, match type and link status added to screening and handoff tables; no target padding.                                                          |
| `GCC-UGC-Prompt-1A-Candidate-Verification-and-Screening-Preparation-v1.1.md` |     1.1 | Verification/preparation only; no autonomous discovery or replacements; direct-link eligibility gate; blocked candidates excluded from Prompt 1B handoff; revised handoff fields.                                                  |
| `GCC-UGC-Prompt-1B-Full-Screening-and-Decision-Completion-v1.1.md`           |     1.1 | Final YES/MAYBE/NO/UNPROCESSED screening; direct identity/link gate; no candidate replacement; optional competitor observation only.                                                                                               |
| `individual-prod-two-col-markdown-table-after-research-v1.1.md`              |     1.1 | Direct product identity gate; optional Potential Competitor Opportunity output section with product name, direct URL and reason; no automatic Prompt 2A execution.                                                                 |
| `GCC-UGC-Prompt-2A-Quick-Competitor-Opportunity-Validation-v1.0.md`          |     1.0 | New quick validation gate for competitor products discovered during Prompt 2; checks product identity, early GCC signals, UGC, creative potential, quick sourcing plausibility and obvious risks; returns PROMOTE / HOLD / REJECT. |
| `GCC-Selection-Sheet-and-Competitor-Opportunity-Tracker-Spec-v1.0.md`        |     1.0 | Companion workbook specification for mandatory URL/match/link-status fields and a separate Competitor Opportunity Tracker.                                                                                                         |

## 2. Approved workflow after these changes

``` text
Stage 0.1 — Raw Product Discovery
  Only real, identifiable products with verified direct product pages enter the candidate table.
        |
        v
Stage 0.2 — Quality Filtering
  Verify the same product page before assigning Track A / Track B or scoring.
        |
        v
Stage 0.3 — Commercial Pre-Screening
  Verify the same product page before commercial scoring and selection.
        |
        v
Prompt 1A — Candidate Verification and Preparation
  Verify and prepare the existing selected candidates; do not discover or replace.
        |
        v
Prompt 1B — Full Screening
  Make YES / MAYBE / NO / UNPROCESSED decisions; do not silently replace.
        |
        v
Prompt 2 — Individual Product Deep Research
  Deep research the approved product. Optionally note a particularly interesting
  competitor that surfaced naturally during the required research.
        |
        v
Prompt 2A — Quick Competitor Opportunity Validation (optional, user-triggered)
  Check whether the competitor is worth a separate full Prompt 2 cycle.
        |
        +---- REJECT: stop
        |
        +---- HOLD: resolve the stated gap
        |
        +---- PROMOTE TO PROMPT 2: user decides whether to proceed;
              approved alternative receives a new Product ID and its own
              independent Prompt 2 research.
```

## 3. Important policy details used in Prompt 2A

The final checklist selected UGC research, early GCC signals, comparable
products, and three verdicts, but did not separately select a hard
UGC/GCC threshold or numerical scoring. Therefore the prompt uses these
conservative defaults:

- UGC is explicitly investigated and is a strong positive signal, but
  absence of existing UGC is not an automatic rejection. The prompt also
  checks practical demonstration potential.
- Early GCC signals are checked, prioritizing UAE and KSA. No arbitrary
  minimum number of GCC signals is imposed at this quick stage; missing
  evidence is disclosed and can justify HOLD.
- Exact products and close comparable products are both eligible,
  provided the alternative has its own direct product page and solves
  substantially the same customer problem.
- No numerical composite score is used. The decision is evidence-based:
  PROMOTE TO PROMPT 2, HOLD — NEED MORE EVIDENCE, or REJECT.
- Prompt 2A does not automatically execute Prompt 2. The user decides
  whether to proceed.
- A new Product ID is assigned only after the user approves the
  alternative for full Prompt 2 research. The original Product ID and
  its research remain untouched.

## 4. Dependent consistency correction

The approved Prompt 1A edits define Prompt 1A as
verification/preparation only and remove autonomous replacement
discovery. The existing Stage 0.3 prompt also contained handoff wording
authorizing Prompt 1A to discover and replace candidates. That wording
was updated as a necessary consistency correction; otherwise the
approved Prompt 1A role would still conflict with the generated Stage
0.3 handoff.

Prompt 1B remains responsible for final YES / MAYBE / NO / UNPROCESSED
decisions. Prompt 1A may block a candidate from handoff when its direct
product identity cannot be verified, but it may not substitute another
product.

## 5. Workbook implementation boundary

The workbook changes are documented in the separate
`GCC-Selection-Sheet-and-Competitor-Opportunity-Tracker-Spec-v1.0.md`.

The existing source XLSX files were inspected but **not modified**. The
companion specification defines the next workbook update:

- Main active selection sheet: Direct Product URL, Product Match Type
  and Link Verification Status.
- Only verified product-specific pages qualify for the active selection
  pool.
- Unapproved competitor alternatives remain in a separate
  `Competitor Opportunity Tracker`.
- The tracker records the Original Product ID, alternative URL, match
  type, Prompt 2A verdict and date, risks/gaps, user approval and new
  Product ID after approval.
- Existing IDs, formulas, decisions and research history must be
  preserved.

### Existing workbook observations

The uploaded `GCC100-B01-Stage-0.1-Raw-Product-Discovery.xlsx` has a
100-row Discovery Log with 17 columns, while the Stage 0.1 prompt
specifies an eight-column master discovery table. A preliminary
URL-pattern check found 24 of the 100 rows using URLs that appear to be
category/search/collection pages. This is a URL-pattern flag only, not a
full live verification of those rows.

The B01 and B02 source workbooks have not been cleaned or rebuilt in
this revision. A separate workbook audit/rebuild is needed before
treating the historical rows as a fully compliant active selection pool.

## 6. Files intentionally not modified

- `GCC-UGC-Product-Research-Master-Prompt-v2.md`
- `GCC-UGC-Product-Research-Master-Prompt-v2.1.md`
- `GCC-Research-Workbook-Generation-Master-Prompt-v2.0.md`
- Existing XLSX workbooks

No Google Drive files were created or modified.
