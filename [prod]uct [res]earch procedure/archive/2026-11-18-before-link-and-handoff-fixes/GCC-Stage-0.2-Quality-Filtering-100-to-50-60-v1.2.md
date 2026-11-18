# GCC Stage 0.2 --- 100-to-50/60 Product Quality Filtering Prompt

**Version:** 1.2\
**Stage:** 0.2 --- Initial Quality Filtering\
**Input:** Complete Stage 0.1 discovery log and source register\
**Target output:** Approximately 50--60 qualified products\
**Next stage:** GCC Stage 0.3 --- Commercial Pre-Screening

------------------------------------------------------------------------
## GCC Market Scope and Research Rules

This research is specifically focused on the six GCC markets:

1. United Arab Emirates (UAE)
2. Saudi Arabia (KSA)
3. Kuwait
4. Qatar
5. Bahrain
6. Oman

All product research, market validation, demand assessment, competitor analysis, pricing research, customer feedback analysis, and commercial evaluation must be conducted with these GCC markets as the target market.

- Prioritize GCC-specific marketplaces, retailers, suppliers, customers, search trends, and social-commerce evidence.

- Record the country, platform, currency, source URL, and research date for relevant findings.

- Do not treat non-GCC marketplace listings, ratings, reviews, sales figures, or popularity as proof of GCC demand or GCC customer satisfaction.

- International sources may be used for supporting technical specifications, manufacturer information, product documentation, and global supplier discovery, but clearly distinguish them from GCC market evidence.

- Suppliers may be located outside the GCC, provided their ability to supply the target GCC market is properly evaluated.

- Assess GCC-specific shipping, landed costs, delivery feasibility, returns, warranty, product compliance, and applicable country requirements.

- Never assume that evidence from one GCC country automatically applies to all six countries.

- If GCC-specific evidence is unavailable, explicitly record the gap rather than substituting unrelated international evidence.
------------------------------------------------------------------------

## 1. Your role

Act as a senior marketplace quality analyst, customer-review researcher,
product-risk analyst and evidence auditor.

Your task is to evaluate the products discovered in Stage 0.1 and
identify which products show credible product-quality,
customer-satisfaction and practical-use signals.

This stage is a quality filter, not a full commercial validation. Do not
make final profitability decisions and do not perform Prompt 1A, Prompt
1B or Prompt 2 screening.

## 2. Required input and ID preservation

Use the complete Stage 0.1 handoff:

-   Discovery summary.
-   Eight-channel execution ledger.
-   Master raw discovery log.
-   Source register.
-   Candidate IDs and duplicate mapping.

Treat the Stage 0.1 Candidate IDs as fixed. Do not restart discovery,
rename candidates, merge distinct products without evidence or assign
duplicate IDs.

If a source or field is missing, record the gap and research it where
possible. Do not invent a missing rating, review count, product model or
customer complaint.

## 3. Objective

Filter the Stage 0.1 pool toward **50--60 quality-qualified products**.

The 50--60 target applies to **Track A SELECT products only**. It is a
planning range, not a quota. Do not keep weak products to fill it. If
only 43 products meet the quality standard, pass 43 and explain the
shortfall. If more than 60 qualify, rank them by evidence-backed quality
score and preserve the remaining quality-qualified products as a
separate reserve list rather than deleting them.

Track B products that meet the no-review conditional-advancement rule
may be handed to Stage 0.3 in a **separate conditional group**. Do not
count them as quality-qualified SELECT products or use them to inflate
the 50--60 target. The combined Stage 0.3 input may therefore contain
Track A SELECT products plus separately labelled Track B conditional
candidates and other reserve items.

Every product must receive an explicit decision, alongside a separate
evaluation-track label:

-   **SELECT — TRACK A:** review evidence supports a complete, evidence-
    based quality assessment and the product meets the SELECT threshold.
-   **CONDITIONAL ADVANCE — TRACK B:** no A--E review dimension could be
    adequately assessed after a reasonable search, but all F--H dimensions
    are supported, the separate suitability score is at least 70, and no
    critical blocker remains. This permits commercial pre-screening only;
    it does not establish or certify product quality.
-   **REVIEW:** promising, but a specific missing, incomplete or
    conflicting quality/suitability item needs checking.
-   **REJECT:** evidence shows weak quality, serious recurring
    complaints, duplicate identity, unsuitable product characteristics
    or a critical blocker.
-   **UNVERIFIED:** the listing or evidence could not be checked
    sufficiently to make a fair decision. Inaccessible evidence must not
    be mistaken for evidence that reviews do not exist.

Missing evidence alone is not proof of poor quality. Lack of reviews must
not automatically cause rejection. Use REVIEW or UNVERIFIED when the
available evidence is incomplete or inaccessible.


## 4. Evaluation-track classification and review-evidence gate

Classify every candidate into exactly one evaluation track before
calculating its score. The track is a research-path label, not a quality
rating.

### Track A --- Review evidence available

Assign **TRACK A — REVIEW EVIDENCE AVAILABLE** when at least one of the
five review-related dimensions (A--E) has enough relevant evidence to be
scored responsibly.

A dimension is `FOUND / ASSESSABLE` only when the evidence is sufficiently
specific and detailed to support an actual dimension score. A listing
existing, a review tab being visible, a bare star icon, or a search-result
snippet alone does not automatically qualify.

Use these minimum interpretations:

- **A — Rating strength and review depth:** rating scale, product/listing
  identity and a usable rating/review-count signal are visible. If the
  count or variant relationship is unclear, explain the limitation and
  do not overstate the sample.
- **B — Review freshness:** dated review evidence is visible and can be
  assessed for recency/activity.
- **C — Review credibility:** enough review content or platform indicators
  exist to assess verified-purchase signals, specificity, repetition or
  exact-variant relevance.
- **D — Negative-review/defect profile:** negative review content is
  available to identify and assess complaint or defect themes.
- **E — Usefulness and customer satisfaction:** positive or mixed review
  content describes actual use, benefits, repeat use, unmet expectations
  or customer satisfaction.

One dimension may be assessable even when the other four are not. Record
each A--E dimension separately as `FOUND / ASSESSABLE`, `NOT FOUND`,
`NOT ACCESSIBLE`, or `NOT CAPTURED`, with source IDs and a short reason.
Do not treat one dimension's evidence as proof of another dimension.

### Track B --- No review evidence found

Assign **TRACK B — NO REVIEW EVIDENCE** only when none of A--E has
sufficient evidence to assess after a reasonable search. At minimum:

1. Reopen the original direct product/listing URL.
2. Check review/rating sections on the original listing where present.
3. Search relevant GCC marketplace/retailer listings for the exact
   product and close product identity matches where accessible.
4. Check at least one additional relevant source or retailer where
   practical.
5. Record what was searched, the country/platform, date checked and
   result. Do not claim a source was checked if it was not.

If review sources exist but cannot be accessed, classify the relevant
fields `NOT ACCESSIBLE` and normally use `UNVERIFIED`, not Track B. If a
platform does not expose a particular metric, use `NOT CAPTURED`. Track B
means a reasonable search found no assessable A--E review evidence; it
does not mean the product has no customers, no demand or poor quality.

### Evidence geography

Record whether review evidence is GCC-specific or international. GCC
reviews may support GCC customer-satisfaction findings. International
reviews may support carefully labelled general product-quality signals,
but must never be presented as proof of GCC demand or GCC customer
satisfaction. Keep exact-product, comparable-product and category-level
evidence distinct.

### Track assignment rule

- If one or more A--E dimensions are assessable: Track A.
- If zero A--E dimensions are assessable after the reasonable search:
  Track B, provided the search was genuinely completed.
- If the search itself could not be completed because relevant sources
  were inaccessible or a dependency failed: `UNVERIFIED`; do not force a
  Track B classification.

Track assignment must be recorded before scoring and preserved through
Stage 0.3 and later handoffs.


## 5. Quality evaluation framework

Use the dimension definitions below according to the assigned track:
Track A scores only A–E; Track B scores only F–H. Do not combine the
tracks or calculate scores for dimensions outside the assigned track.
Use direct evidence and record the source.

### A. Rating strength and review depth --- 20 points

Check: - Average rating and rating scale. - Total review count. -
Whether the review count belongs to the exact model/variant or a
combined listing. - Review count relative to similar listings where
meaningful. - Whether the sample is too small to support a confident
conclusion.

Guidance, not a hard universal rule: - 4.2--5.0 with a meaningful review
base is a positive signal. - 4.0--4.19 requires closer review
analysis. - Below 4.0 is a warning, not automatic rejection. - 50+
reviews are preferred for an initial signal; 100+ is stronger when
reviews are genuine and product-specific. - A 4.8 rating from 12 reviews
is not automatically stronger than a 4.4 rating from 800 reviews.

Do not compare ratings across platforms as if their review systems are
identical.

### B. Review freshness and activity --- 10 points

Check: - Recent reviews within approximately 90--180 days where
available. - Whether reviews continue to appear. - Whether positive or
negative sentiment has changed. - Whether the listing is active and
currently available.

Do not infer review velocity if dated review data is unavailable. Mark
it `NOT CAPTURED`.

### C. Review credibility and exact-variant relevance --- 10 points

Check: - Verified-purchase indicators where shown. - Specific
descriptions of actual use. - Repetitive, generic or suspiciously
similar wording. - Sudden unexplained review bursts when visible. -
Whether reviews refer to the exact product, another variant or an
unrelated bundled item. - Whether the listing has combined ratings for
materially different products.

Do not accuse a seller of fake reviews without evidence. Use
`AUTHENTICITY CONCERN - UNCONFIRMED` when there are warning signs but no
proof.

### D. Negative-review and defect profile --- 20 points

Read negative reviews and identify recurring themes:

-   Product stops working.
-   Poor durability or short lifespan.
-   Performance below advertised claims.
-   Missing parts/accessories.
-   Battery, charging, overheating or electrical concerns.
-   Material, fit or sizing problems.
-   Difficult setup or confusing instructions.
-   Poor packaging or transit damage.
-   Warranty/refund or seller-support complaints.
-   Safety incidents or credible injury/fire reports.

Record the number or proportion only if it can be reliably calculated
from the accessible review sample. Otherwise describe the recurring
themes and mark the proportion `NOT CAPTURED`.

A single serious safety report must be investigated. Do not bury it in
an average rating.

### E. Product usefulness and customer satisfaction --- 15 points

Check: - Whether customers describe a real problem being solved. -
Whether the benefit matches the listing claim. - Whether positive
reviews describe repeat use or meaningful convenience. - Whether the
product is easy to understand and operate. - Whether the product appears
to meet a recurring need rather than a one-off novelty.

### F. UGC and demonstration suitability --- 10 points

Check: - Whether the product can be demonstrated in a short video. -
Whether the result is visible or measurable. - Whether creators or
customers show actual use. - Whether content is product-specific,
similar-product, category-level or general trend. - Whether comments
show questions, objections or purchase intent.

This is a feasibility check, not proof of demand. Do not reward a
product merely because one video is viral.

### G. Listing and specification clarity --- 5 points

Check: - Exact brand/model/variant. - Clear product photos and
description. - Key specifications and included accessories. -
Consistency between title, images and technical details. - Warranty and
return information where visible.

### H. Basic safety and operational suitability --- 10 points

Identify obvious: - Safety concerns. - Restricted or regulated product
issues. - Fragility and breakage risk. - Battery/chemical/shipping
complications. - Unusual storage or handling requirements. - High
likelihood of customer misuse. - Unsupported health or performance
claims.

This is an initial warning screen, not a legal certification. Detailed
compliance belongs to Stage 0.3 and later stages.

## 6. Quality score

Score each assessable dimension from 0 to 100. A score of 100 means the
strongest positive evidence; 0 means poor, contradicted or seriously
adverse evidence. For dimension D, a high score means few or no recurring
serious defects; a low score means repeated or severe complaints.

### Track A — A–E weighted quality score

Use ONLY dimensions A–E, with their original weights:

| Dimension | Weight |
|---|---:|
| A. Rating strength and review depth | 20 |
| B. Review freshness and activity | 10 |
| C. Review credibility and exact-variant relevance | 10 |
| D. Negative-review and defect profile | 20 |
| E. Usefulness and customer satisfaction | 15 |
| **Total** | **75** |

Calculate a weighted average using only the A–E dimensions that are
`FOUND / ASSESSABLE`:

```text
A–E Weighted Score =
SUM(dimension score × original dimension weight for assessable A–E dimensions)
/
SUM(original weights for assessable A–E dimensions)
```

This is a weighted average, not a simple average.

If at least one A–E dimension is assessable, calculate and report the
score. Missing dimensions are excluded from both the numerator and
denominator; they must NOT be scored as zero.

- Label the score `PROVISIONAL` when one to four A–E dimensions are
  assessable.
- Label the score `COMPLETE` only when all five A–E dimensions are
  assessable.
- Report A–E evidence coverage as the supported A–E weights divided by
  75, multiplied by 100.
- Report the dimension count, e.g. `3/5 dimensions; 73.3% coverage`.

A provisional score is useful for comparison and research prioritization,
but it does not automatically qualify a product for SELECT.

Score interpretation for Track A:
- 85–100: excellent quality signals.
- 75–84: strong quality signals.
- 65–74: mixed; review the specific gaps.
- 50–64: weak.
- Below 50: poor.

These bands describe the score; the evidence and decision requirements
below still determine whether the product can be selected.

**Track A decision requirements:**

- **SELECT — TRACK A:** score of at least 70/100, A, D and E
  assessable, and no critical blocker. A, D and E together provide at
  least 73.3% weighted A–E evidence coverage.
- **REVIEW:** score of 60–69; or a score of 70 or more when A, D and E
  are not all assessable; or evidence is promising but insufficient for
  a fair final decision.
- **REJECT:** score below 60 when A, D and E are assessable; or a
  critical safety, legal or counterfeit blocker is established.
- If the score is below 60 but the evidence is insufficient to judge
  fairly, use REVIEW / HOLD rather than rejecting by guess.
- If the research itself could not be completed, use UNVERIFIED.

### Track B — no-review preliminary suitability score

Track B applies only when none of A–E can be assessed after the
documented reasonable search in Section 4.

Score only F, G and H, using their original weights normalized to 100%:

| Dimension | Original weight | Track B normalized weight |
|---|---:|---:|
| F. UGC and demonstration suitability | 10 | 40% |
| G. Listing and specification clarity | 5 | 20% |
| H. Basic safety and operational suitability | 10 | 40% |
| **Total** | **25** | **100%** |

```text
No-Review Preliminary Product Suitability Score =
(F × 0.40) + (G × 0.20) + (H × 0.40)
```

All three dimensions must be supported to issue a complete Track B
score. If any is missing, mark the score `INCOMPLETE`; do not
redistribute the weights. Report Track B evidence coverage as the
supported original F–H weights divided by 25, multiplied by 100.

This score measures preliminary demonstration, listing and operational
suitability only. It is **not** a customer-demand score, a
customer-satisfaction score, a proven product-quality score or a
substitute for physical sample testing.

**Track B decision requirements:**

- **CONDITIONAL ADVANCE — TRACK B:** complete F/G/H score of 70–100,
  3/3 dimensions supported, 100% Track B weighted coverage, and no
  critical blocker. This permits Stage 0.3 commercial pre-screening only.
- **REVIEW / RESERVE:** score of 60–69, or a promising but incomplete
  F/G/H assessment.
- **REJECT:** complete score below 60, or a critical blocker. If evidence
  is too incomplete to judge, use REVIEW / UNVERIFIED as appropriate.

### Critical blockers

Any critical safety, counterfeit or legal blocker overrides every score
and prevents advancement. A high H score is not a compliance
certification and cannot cancel a known critical risk.

Do not compare Track A A–E quality scores directly with Track B F–H
suitability scores. These are different measures.

## 7. Decision reason codes

Use one or more codes for every REVIEW or REJECT decision.

  Code   Reason
  ------ ---------------------------------------------------------
  Q01    Low average rating
  Q02    Insufficient review sample
  Q03    Repeated product defects or durability complaints
  Q04    Performance does not match advertised claims
  Q05    Serious safety complaint or unresolved safety concern
  Q06    Review authenticity or exact-variant concern
  Q07    Poor customer support, warranty or refund experience
  Q08    Weak customer usefulness or unclear problem
  Q09    Weak practical demonstration/UGC suitability
  Q10    Incomplete or inconsistent product specifications
  Q11    Fragile or operationally unsuitable product
  Q12    Counterfeit, restricted or potentially unlawful product
  Q13    Duplicate or superficial variant
  Q14    Listing unavailable, inaccessible or not verifiable
  Q15    Other evidence-based reason --- explain
  Q16    Review evidence not found after documented reasonable search
  Q17    Review evidence inaccessible; verification incomplete
  Q18    Track B suitability evidence incomplete

Do not use a reason code without an explanation and supporting source.
Multiple codes may apply.

## 8. Required research and source handling

For each candidate:

1. Reopen the direct product listing and confirm exact product/variant
   identity.
2. Check each A--E review dimension separately using the review-evidence
   gate in Section 4. Record `FOUND / ASSESSABLE`, `NOT FOUND`,
   `NOT ACCESSIBLE` or `NOT CAPTURED` for each dimension.
3. Capture rating, review count, rating distribution and date checked
   where visible.
4. Read a balanced sample of positive and negative reviews where
   accessible; prioritize recent and verified-purchase reviews where
   shown.
5. Check Q&A, warranty, returns and seller signals where visible.
6. Search for product-specific complaints or safety issues.
7. Check at least one relevant independent source when practical.
8. Score only the dimensions for the assigned track: A–E for Track A,
   or F–H for Track B. Do not score or combine both routes for one
   candidate.
9. Assign Track A or Track B only after documenting the search outcome.
10. Capture relevant demonstration content, but do not treat it as proof
    of quality unless it shows the exact product being tested.
11. Record inaccessible sources, missing metrics, geography, evidence
    relevance and the date checked.
12. Preserve the track label, score type, evidence coverage and decision
    in every subsequent handoff.

Keep evidence labels: - **Verified** - **Estimate** - **Inference** -
**Unknown** - **NOT VERIFIED** - **NOT CAPTURED** - **PENDING**

Never invent review counts, review dates, verified-purchase status,
failure rates or customer sentiment percentages.

## 9. Required output

### Output A --- Quality-filter summary

Report:

- Number of Candidate IDs received and researched.
- Track A count and Track B count.
- Track A SELECT (quality-qualified) count.
- Track B CONDITIONAL ADVANCE count (not quality-qualified).
- REVIEW, REJECT and UNVERIFIED counts, split by track where applicable.
- Track A quality-qualified products passed to Stage 0.3.
- Track B conditional candidates passed separately to Stage 0.3.
- Number of other reserve products and total Stage 0.3 handoff count.
- Main reasons for rejection, main evidence gaps and any safety issues
  requiring escalation.

### Output B --- Product scoring and decision table

Show one row for every candidate received, not only selected products.

| Candidate ID | Product/model | Track | A–E individual scores (A/B/C/D/E) | A–E weighted score /100 (status) | F–H individual scores (F/G/H) | F–H suitability score /100 (status) | Evidence coverage | Decision | Reason code / explanation / evidence IDs | Missing evidence / next action |
|---|---|---|---|---:|---|---:|---|---|---|---|

Display each assessable dimension's score from 0–100. For a dimension
that is not assessable, show the correct status: `NOT FOUND`,
`NOT ACCESSIBLE`, `NOT CAPTURED` or `N/A`; do not enter zero.

- Track A: show A–E scores and the weighted A–E score. F–H must be `N/A`.
  Label the A–E score `PROVISIONAL` or `COMPLETE`.
- Track B: show the A–E search outcomes and F/G/H scores with the
  separate F–H suitability score. Use Track B only when none of A–E is
  assessable after the documented reasonable search.
- UNVERIFIED: do not force a Track A or Track B score.
- Show evidence coverage as both dimension count and percentage, e.g.
  `Track A: 3/5; 73.3%` or `Track B: 3/3; 100%`.
- Include a concrete decision reason, applicable reason code(s) and
  evidence/source IDs for every candidate.
- Record the country/geography and whether review evidence is
  exact-product, comparable-product or category-level.
- Keep the original Candidate ID and distinguish verified facts from
  inferences.

Do not combine the A–E score and F–H score into one final score.

### Output C --- Stage 0.3 handoff groups

### C1. Track A — quality-qualified SELECT products

Include only products classified `SELECT — TRACK A`. These are the
products counted toward the 50--60 quality-qualified target.

| Candidate ID | Product/model | Category | A–E Weighted Score /100 (PROVISIONAL/COMPLETE) | A–E evidence coverage | Strongest positive evidence | Main negative/defect evidence | Direct product URL | Supplier/UGC leads | Stage 0.2 decision |
|---|---|---|---:|---|---|---|---|---|---|
| GCC100-001 |  |  |  | 3/5; 73.3% |  |  |  |  | SELECT — TRACK A |

### C2. Track B — conditional Stage 0.3 candidates (not quality-qualified)

List only products classified `CONDITIONAL ADVANCE — TRACK B` with a
complete F/G/H score of at least 70 and no critical blocker. Keep them in
a separate table and do not count them as Track A SELECT products.

| Candidate ID | Product/model | Category | No-Review Suitability Score /100 | Evidence coverage | A–E search outcome | F/G/H evidence summary | Direct product URL | Main unresolved quality questions | Stage 0.2 decision |
|---|---|---|---:|---|---|---|---|---|---|
| GCC100-001 |  |  |  | 3/3; 100% | No assessable review evidence found after documented search |  |  |  | CONDITIONAL ADVANCE — TRACK B |

### C3. Other reserve products

List Track A REVIEW/INCOMPLETE products and Track B REVIEW products
separately, with the specific evidence needed to change their status.
For each reserve product, explicitly state whether it should enter the
Stage 0.3 active commercial research pool (`SEND TO STAGE 0.3 RESERVE`)
or remain on hold until the named quality/suitability gap is resolved
(`HOLD — RESOLVE STAGE 0.2 GAP`). Do not merge these reserve records
into either table above.

| Candidate ID | Track | Decision | Score type/value | Evidence coverage | Main unresolved gap | Stage 0.3 routing | Recovery action |
|---|---|---|---|---|---|---|---|

Do not create new Candidate IDs. The 50--60 target applies only to
Track A SELECT products; report the Track B conditional count separately.

### Output D --- Rejected and reserve log

List every REJECT, REVIEW, UNVERIFIED and non-selected reserve product
with: Candidate ID, track, decision, score type/value if supportable,
evidence coverage, reason code(s), exact evidence that caused the
decision, and what new evidence could change it. Keep Track A reserve
and Track B reserve records visibly separate. Track B conditional
candidates are listed in Output C2, not as quality-qualified SELECTs.

Rejected products remain in the master history. Do not delete them.

### Output E --- Append-only decision history

Add a new row for every candidate decision. Never overwrite a Stage 0.1
record. Include the evaluation track, evidence coverage and score type.

| Candidate ID | Stage | Track | Previous status | New status | Score type/value | Evidence coverage | Decision date | Reason code(s) | Evidence/source IDs | Missing evidence | Next action |
|---|---|---|---|---|---|---|---|---|---|---|---|

------------------------------------------------------------------------

### Output F --- Stage 0.2 checkpoint

End with:

``` text
GCC STAGE 0.2 QUALITY FILTER HANDOFF — VERSION 1.2
Input batch:
Candidate IDs received:
Products researched:
TRACK A — REVIEW EVIDENCE AVAILABLE:
TRACK B — NO REVIEW EVIDENCE:
TRACK A SELECT — QUALITY-QUALIFIED:
TRACK B CONDITIONAL ADVANCE — NOT QUALITY-QUALIFIED:
TRACK A REVIEW / RESERVE:
TRACK B REVIEW / RESERVE:
REJECT:
UNVERIFIED:
Track A quality-qualified products passed to Stage 0.3:
Track B conditional candidates passed separately to Stage 0.3:
Total Stage 0.3 handoff candidates:
Current stage: QUALITY FILTER COMPLETE
Next prompt: GCC Stage 0.3 — Commercial Pre-Screening
Do not perform Stage 0.3 or Prompt 1A/1B/2 inside this prompt.
```

Pass the complete screening log, Track A SELECT list, separate Track B
conditional list, separate Track A/Track B reserve lists, rejected and
unverified lists, source register and append-only decision history to
Stage 0.3. Preserve each product's track, evidence coverage, score type,
A–E search outcome and unresolved quality questions. Stage 0.3 may
commercially pre-screen Track B conditional candidates, but must never
relabel them as quality-qualified.

## 10. Research integrity and stop rules

-   Do not select products merely because they have a high rating.
-   Do not reject products merely because they have few or no reviews.
-   Do not classify inaccessible review sources as `NO REVIEW EVIDENCE`;
    use UNVERIFIED when the search could not be completed.
-   Do not treat a Track B suitability score as a Quality Score.
-   Do not label Track B conditional candidates `SELECT` or count them
    toward the 50--60 quality-qualified target.
-   Do not advance an incomplete Track B score automatically; all F/G/H
    dimensions must be supported for CONDITIONAL ADVANCE.
-   Do not compare Track A Quality Scores directly with Track B
    suitability scores.
-   Do not allow a high suitability score to offset a critical safety,
    legal or counterfeit blocker.
-   Do not treat combined-variant ratings as exact-product evidence.
-   Do not convert review counts into sales.
-   Do not ignore recurring negative reviews because the average rating
    is high.
-   Do not treat one viral video as quality proof.
-   Do not hide safety complaints.
-   Do not force 50--60 products if fewer meet the standard.
-   Do not delete rejected products or overwrite previous decisions.
-   Do not perform full supplier audits, detailed CAC modelling or final
    commercial approval.

## 11. Start instruction

Read the complete Stage 0.1 handoff. Preserve every Candidate ID.
Check A–E for every product and assign the track using Section 4. If at
least one A–E dimension is assessable, assign Track A and calculate the
weighted A–E average using only assessable dimensions; exclude missing
dimensions from the denominator and label the score PROVISIONAL unless
all five are assessable. If none of A–E is assessable after a documented
reasonable search, assign Track B and score F–H using 40/20/40. If the
search could not be completed, use UNVERIFIED. Never score F–H for Track
A or combine A–E with F–H. Show each product's dimension scores,
weighted score, evidence coverage, decision and reason. Apply the
critical rejection gates and prepare separate Track A SELECT, Track B
CONDITIONAL ADVANCE, reserve, rejected and unverified handoffs. Do not
count Track B as quality-qualified. Stop after Stage 0.2.
