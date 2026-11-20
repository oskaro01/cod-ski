# Prompt 2: Individual Product Deep Research and Sheet Update

**Version:** 1.3
**Revises:** v1.2 execution; checkpointed stages and separate supporting modules. Demand, commercial scoring and sample-entry methodology remain v1.2.

## Purpose

Use this prompt for one product at a time through a documented entry route: Prompt 1B YES; Prompt 1B MAYBE explicitly promoted by the user; Prompt 2A PROMOTE TO PROMPT 2 explicitly approved by the user; a user-selected 15-product staged screening record; or a product directly selected by the user for deep research. For a direct selection, a product URL is sufficient to begin identity verification; missing country, channel, budget and other business inputs remain explicit dependencies. For the Prompt 2A route, carry its verdict, date, sources, original-product reference and approval record. Never invent a prior screening result for any route.

Prompt 2 must challenge the original screening result. A Prompt 1 YES
means the product deserves investigation; it does not prove demand,
supplier quality, profitability, or readiness to purchase.

Preserve the original Product ID, product name, URLs, Prompt 1 row,
decision, and unresolved question. Do not silently replace the original
screening record.

## Stage controller and supporting modules

Run only ONE stage per response. Start at P2-1, publish its actual findings and checkpoint, then ask: `Proceed to P2-[next number]: [stage name]? Reply CONTINUE.` Wait for my reply. CONTINUE runs only the next stage; RECHECK [stage] [gap] updates that specific question and preserves the scheduled next stage. Do not interpret permission to continue as sample-payment or inventory approval.

| Stage | Work and required output | Supporting module |
|---|---|---|
| P2-1 Identity and intake | Actual entry record, original/current URL, model/variant, dated identity check, original-claim audit, target country/channel and missing business inputs | Main prompt identity rules |
| P2-2 Market and customer reviews | Competitor comparison, local purchasing evidence, positive and negative review themes, quality concerns and positioning gap | Main competitor and marketplace tasks |
| P2-3 Demand and UGC | Four evidence layers, source/query records, M/S/L scores and reasons, index/status/coverage, global creative support and compact creative proposals | `optional-tools/[UGC]-Search-and-Demand-Validation.md` |
| P2-4 Supplier comparison | Direct leads, specification comparison, exact-variant price/MOQ/tiers, shipping/lead-time basis, supplier claims and quote/document gaps | Main supplier tasks |
| P2-5 Economics and risks | Conservative/base/optimistic order economics, input sources/ranges, break-even measures, price/CAC/shipping/return sensitivities, risk gates and proposed sample test criteria | Main economics and compliance tasks |
| P2-6 Evidence-gap closure | Audit all 15 core items; research up to three decision-changing gaps, update affected inputs and list unresolved dependencies | `optional-tools/[Evidence-Gap]-Closure.md` |
| P2-7 Final decision | Current 15-item coverage ledger, supplemental demand gaps, five commercial ratings/points, confidence, gate references, canonical decision and short explanation | Main decision rules, then `optional-tools/Product-[Decision]-Summary.md` |
| P2-8 Notes and exports | Final Notes, vertical two-column table, horizontal 11-column row and Stage 3 handoff/readiness | `optional-tools/Standardized-[Notes].md` and Outputs B/C |

The tasks below define research standards; they are not instructions to execute every task in the first response. Output A is the cumulative published record from P2-1 through P2-7. Produce Outputs B/C only at P2-8. Before P2-7, label assessments PROVISIONAL / FINAL DECISION PENDING and never grant SAMPLE. A documented disqualifying finding may end research early with a sourced DROP and checkpoint; do not perform unnecessary remaining research. Ask whether to prepare exports. Final scoring cannot be inferred from unfinished stages.

After P2-8, report COMPLETE with unresolved later-stage actions. Do not ask for a nonexistent P2-9 or start Stage 3 automatically. For an early DROP, format only supported findings and mark skipped research NOT ASSESSED; no fabricated score or completed checklist.

### Using the separate modules

The supporting files remain separate. Their relevant functions are required at the stages above: demand assessment, gap audit, final explanation and Notes. Gap browsing is conditional on an actual material gap; the gap audit is always required. Reuse prior evidence and stop when the question is adequately resolved.

For a local agent, read the named module when its stage is reached. In a chat without workspace access, attach this prompt and the four module files at the start, or supply each module when requested. A local filename is not accessible merely because it appears in this prompt. If a module is absent, report MODULE NOT PROVIDED, execute the corresponding standards already specified here, and mark that its additional instructions were not applied; never pretend to have read it. Missing instructions needed for a defensible decision remain a dependency. No automatic merge or invented module contents.

Pass only the active Product ID, exact variant/country, actual source records, latest relevant findings and the named question to a module. In staged use, this controller determines timing and output: modules return findings/changes only until P2-7. They cannot independently approve SAMPLE, restart research, generate all exports or advance the next stage. Standalone module behavior remains available when the user requests it separately.

### Compact output and checkpoint contract

Use short factual records and source IDs; no product cards, images, decorative output or repeated dossiers. Use a compact comparison table only where it helps. P2-1 maximum 500 words; P2-2/3/4/6 maximum 900 each; P2-5 maximum 1,100; P2-7 maximum 900 including the core ledger and summary; P2-8 maximum 1,200 including both exports. Exclude URL strings; do not pad to these limits. These are stage limits, not a requirement to recreate a full report at every pause.

Keep one source register with stable IDs: direct URL or supplied-document reference, country/platform, date checked, publication/measurement period when available, exact/comparable/category/problem match, captured claim/value and verification limitation. Publish new records once; later stages cite their IDs. Reopen only for volatile/stale facts, conflicts or named gaps. Never infer local review geography solely from the storefront or count a syndicated review pool twice.

Every checkpoint contains Product ID/variant, target country, completed and next stage, actual new findings and source records, unresolved critical questions, changed assumptions/scores and current decision status. If a stage is unfinished, preserve completed work and resume that stage on CONTINUE. IDs alone cannot restore evidence. If switching chats, supply this prompt, required modules and the published stage/source records; if records are unavailable, disclose the gap rather than reconstruct them.

If a new finding changes an earlier model, price, risk or demand assumption, mark dependent scores/economics STALE and recompute only affected results before the final decision. Formatting never upgrades a decision. Pauses limit work per response; they do not reset conversation capacity or guarantee completion.

## GCC Market Scope and Research Rules

This research is specifically focused on the six GCC markets:

1.  United Arab Emirates (UAE)
2.  Saudi Arabia (KSA)
3.  Kuwait
4.  Qatar
5.  Bahrain
6.  Oman

All product research, market validation, demand assessment, competitor
analysis, pricing research, customer feedback analysis, and commercial
evaluation must be conducted with these GCC markets as the target
market.

- Prioritize GCC-specific marketplaces, retailers, suppliers, customers,
  search trends, and social-commerce evidence.

- Record the country, platform, currency, source URL, and research date
  for relevant findings.

- Do not treat non-GCC marketplace listings, ratings, reviews, sales
  figures, or popularity as proof of GCC demand or GCC customer
  satisfaction.

- International sources may be used for supporting technical
  specifications, manufacturer information, product documentation, and
  global supplier discovery. International demonstrations may support
  creative potential and global solution interest; clearly distinguish
  both uses from GCC demand evidence.

- Suppliers may be located outside the GCC, provided their ability to
  supply the target GCC market is properly evaluated.

- Assess GCC-specific shipping, landed costs, delivery feasibility,
  returns, warranty, product compliance, and applicable country
  requirements.

- Never assume that evidence from one GCC country automatically applies
  to all six countries.

- If GCC-specific evidence is unavailable, explicitly record the gap
  rather than substituting unrelated international evidence.

## Required input

Collect or confirm:

- Product ID, for example `P-007`.
- Actual entry record: Prompt 1B row, approved Prompt 2A opportunity, user-selected 15-product staged screening record, or direct user selection with its supplied URL. Mark nonexistent prior screening NOT AVAILABLE.
- Product name and variant.
- The candidate's own Direct Product URL, plus the immutable Original Product URL and current link-check date. A direct supplier/manufacturer product listing may establish identity if it matches the exact research subject; a generic supplier profile, unrelated comparable, category or search page cannot.
- Product Match Type: `EXACT PRODUCT`, `COMPARABLE PRODUCT`, or
  `VARIANT / MODEL`.
- Link Verification Status from the prior stage, if available.
- Original competitor, supplier, and UGC links.
- Target GCC country or countries.
- Sales channel.
- Fulfilment model.
- Testing budget and target selling price.
- The main question behind the original screening decision or approved Prompt 2A promotion, with the entry route recorded explicitly.

State assumptions when inputs are missing.

At P2-1, resolve the target country from the input or prior record. If absent, state UAE as the provisional first research market and invite correction at the pause; do not imply all six countries were assessed. Missing channel, fulfilment, budget and tax status remain named dependencies, not invented business facts.

Preserve Candidate ID if one exists and optional legacy Discovery ID if supplied. An approved Prompt 2A alternative may legitimately have neither; its new Product ID and opportunity record provide its provenance. Preserve Original Product URL exactly as received. If a recovery page for the same product is verified, update only Direct Product URL and record source, date and reason. Do not transfer scores, costs, reviews or conclusions from the parent product. Every alternative must pass the full research and existing decision gates independently.

## Direct product identity and link eligibility gate

Before beginning deep research, open the candidate’s own Direct Product
URL and confirm that it identifies the actual product and meaningful
model/variant being researched. Accept an individual marketplace or
retailer listing, official manufacturer product page, DTC product page,
or product-specific crowdfunding page that identifies the actual
product. A direct supplier product listing also qualifies when it establishes the same candidate and critical specifications; a supplier profile or similar-looking item does not. Do not use a category page, search result, collection page,
generic homepage, social post, advertisement, or generic campaign page
as the candidate’s product URL.

If the supplied URL is not product-specific or is inaccessible, search
for another accessible direct page for the **same product**. Do not
silently substitute a different comparable product. If the candidate
itself is a comparable product, use its own direct page and keep its
`COMPARABLE PRODUCT` classification visible throughout the dossier.

If no qualifying direct page can establish product identity after a
reasonable search, do not proceed as though the identity is verified:
record the gate as FAIL, explain the missing direct page, and use `DROP`
when the product cannot be established, or `HOLD` / `RESEARCH MORE` only
when a specific temporary access dependency can be resolved. Do not
assign or reuse a different Product ID to conceal an identity change.

## Research tasks

### 1. Recheck the original claim

For every important Prompt 1 claim, mark it:

- **Confirmed** with a current direct source.
- **Changed** because the current evidence differs.
- **Indirect** because it only applies to a similar product or category.
- **Unverified** because evidence could not be found.

Explain whether the original screening or promotion case became stronger, weaker or uncertain. For a Prompt 2A entrant, audit its actual quick-validation claims; do not describe them as a completed Prompt 1B screen.

### 2. Competitor deep research

Find at least three meaningful GCC competitors when available. Record:

- Direct product URL, country, marketplace, and date checked.
- Current price, currency, bundle size, and delivery promise.
- Rating and review count.
- Seller and fulfilment method.
- Exact or similar product specifications.
- Positive review themes.
- Repeated complaints and return risks.
- Main competitor USP.
- A differentiation opportunity for the candidate product.

Separate exact-product evidence from category-level evidence.

For written reviews, record actual inspected counts, selection method, dates, variant and local/global pool scope. Distinguish recurring product faults from delivery/seller problems. Use published 4-5/3/1-2-star shares only when available; never infer their distribution from the average rating. A targeted recent/low-rating sample is not a population defect or return rate. Evidence of credibility does not prove review authenticity. Unresolved serious quality concerns must appear in the risk gates and sample-test requirements.

### 3. Supplier deep research

Find at least three supplier leads when practical. For each supplier,
record:

- Direct product URL and supplier name.
- Exact match, comparable match, discovery lead, or not found.
- Product material, dimensions, weight, variant, and included
  accessories.
- Unit price, price breaks, MOQ, and sample availability.
- Supplier history and transaction evidence.
- Production time and handling time.
- Shipping options to the target country.
- Incoterm, estimated delivery time, and tracking.
- Packaging, customization, and documentation.
- Warranty, defect, replacement, and after-sales terms.

Compare competitor specifications against supplier specifications field
by field. Mark each field **match**, **difference**, or **unknown**.

### 4. UGC and demand research

Evaluate four layers: exact product/model, direct comparable competitors,
product category, and customer problem/use case. Include useful English
and Arabic terms. A problem video can reveal interest without proving
purchase intent; a competitor demonstration cannot establish the
candidate's performance, safety or exact-model sales.

Prioritize the actual target country; use UAE/KSA comparisons where
useful. Record other GCC countries as supported, unresearched or unknown.
Do not launch six complete country studies by default.

### Marketplace evidence first

Capture direct country-specific listings, price/currency, model/pack,
seller, ratings, review count, recent review dates/themes and visible
sales indicators. Record what each source proves:

- A listing establishes availability and an offer, not purchases.
- A visible sold counter is platform-reported purchasing evidence;
  preserve its period and variant scope when shown.
- Reviews are a purchasing proxy, not a sales count. Distinguish recent,
  relevant written feedback from cumulative or merged-variant ratings.
- Multiple sellers or countries improve distribution context but do not
  automatically establish multiple independent demand signals.

For a defensible local case, seek two independent demand signals for the
target country, including at least one purchasing signal or credible
recent customer-feedback proxy. Disclose comparable/category evidence.
Copied listings, syndicated reviews, reposts and a search result pointing
to the same listing count as one underlying source, not independent proof.
Positive ratings alone cannot establish sales velocity or profitability.

### Search-interest protocol and access limits

Use Google Trends or Keyword Planner when accessible; neither is mandatory.
Country-relevant Google Search, Autocomplete/Related Searches or credible
keyword data may supply qualitative search evidence. Inspect exact,
competitor, category and problem terms rather than insisting on brand
searches. Search visibility alone does not establish search volume;
Shopping listings belong to marketplace evidence, not a second demand signal.

Use a focused first pass: up to four relevant English/Arabic queries and
two accessible source types per target country. A second pass needs a
named conflict or decision-changing gap. After an access failure, use an
accessible alternative; do not repeatedly retry a blocked Trends page or
require a paid tool, account creation, ads verification or user screenshots
merely to finish. Record attempted queries/sources and the limitation.

For captured evidence, record query, language, country, URL, date checked,
measurement period and exact/comparable/category/problem relevance.
Trends measures relative interest: use 12 months and five years when
useful, never absolute volume or sales. Read supplied screenshots only for
visible terms/settings; mark hidden details NOT CAPTURED. CPC/competition
describe advertiser activity, not proven demand. Preserve conflicting signals.

Use NOT CAPTURED for inaccessible/unobserved data and INSUFFICIENT DATA
for an explicit source result with insufficient data. Neither means zero
demand. Low exact-brand interest does not independently reject a solution
with supported marketplace or category demand.

### UGC, global evidence and creative potential

Research useful accessible TikTok, Instagram, YouTube, Snapchat or creator
sources. Aim for three strong demonstrations when available; stop after a
focused pass if access is blocked or results repeat. Missing creator links
remain a gap; do not fabricate them or fill quotas with unrelated content.

Label every reference EXACT PRODUCT, COMPARABLE PRODUCT, CATEGORY,
CUSTOMER PROBLEM or GENERAL TREND, plus GCC/local or INTERNATIONAL.
Record direct URL, creator, date, visible metrics, hook, demonstration,
sponsorship status and the basis for country/audience relevance. Creator
location alone does not establish audience geography. Mark unavailable
metrics NOT CAPTURED, inaccessible destinations NOT VERIFIED and content
older than 12 months HISTORICAL. Negative/safety material belongs in risks.

Calculate `(likes + comments + shares) / views * 100` only when all metrics
exist and views > 0. Do not infer sales or advertising performance from it.

International exact/comparable demonstrations may support global solution
interest and UGC creative potential. They do not enter the GCC social
component or replace local marketplace evidence. Report global creative
support as STRONG, LIMITED or NOT ESTABLISHED with references; local UGC
adds localization confidence rather than serving as an automatic gate.

Create three hooks, three demonstrations, one objection-handling idea,
one Arabic-friendly angle and one English-friendly angle. Base ideas on
supported functionality and label untested creative as proposals.

### Demand Index v1.2

These are workflow prioritization weights, not a statistically validated
sales forecast. Preserve previous scores with their methodology/version;
do not compare v1.1 and v1.2 totals as if only market conditions changed.

| Component | Weight | Interpretation |
|---|---:|---|
| GCC marketplace demand | 60 | Observed purchasing signals and relevant customer feedback |
| GCC search interest | 20 | Country-specific search evidence, qualitative or quantitative |
| GCC social traction | 20 | Relevant local content/audience response with geographical support |

Score supported components 0-100 with evidence references and limitations.
Use NOT CAPTURED for unassessed components, never an invented zero.

| Anchor | Marketplace | Search | GCC social |
|---|---|---|---|
| 0 | Assessed evidence supports negligible current demand | Assessed sources support negligible relevant interest | Assessed evidence supports negligible relevant local traction |
| 25 | Isolated/stale availability or weak feedback | Isolated/stale qualitative signal | Isolated/stale relevant local content |
| 50 | Relevant recent feedback or purchasing proxy, but limited corroboration | Some relevant country-specific signals, mixed or indirect | Several relevant local signals with limited audience/recency support |
| 75 | Independent current purchasing/feedback signals, with repeat patterns | Consistent current country-specific signals across sources | Current independent local demonstrations and audience response |
| 100 | Strong corroborated recent purchasing evidence with clear scope | Strong corroborated current search evidence with scope/period known | Strong current independent local traction and supported audience relevance |

Explain intermediate scores. Listing presence alone is capped at 25.
High pooled review counts alone do not justify 75 or 100. Failure to find
evidence after a bounded search remains unknown; score 0 only with
affirmative supporting findings, not an access failure or a blank result.

```text
Full Demand Index = M * 0.60 + S * 0.20 + L * 0.20
Demand evidence coverage = sum of weights of adequately assessed components
Provisional Demand Index = sum(score * weight for assessed components)
                           / sum(weights of assessed components)
```

Use decimal weights in the formulas. When all components are assessed,
report FULL, coverage 100%. When marketplace is assessed and one or both
other components are unavailable, report PROVISIONAL, the available
components and coverage (60% or 80%). Otherwise report INSUFFICIENT EVIDENCE
without a numerical composite. Always include a weak or negative component
when it was assessed; do not drop it to improve the average.

A marketplace-only provisional 80/100 at 60% coverage is not equivalent
to a full 80/100. Never rank partial totals without showing coverage,
confidence and evidence scope. Report country-specific values where
supported; do not present a country score as GCC-wide validation.

An unavailable search/local-social component need not independently block
SAMPLE when the commercial evidence and sample-entry rules below pass.
Marketplace presence alone and international virality alone cannot pass them.

### 5. Unit economics

Model conservative, base, and optimistic scenarios. State every
assumption.

``` text
Calculation basis = per unit or per customer order; state which one is used.

If the customer-facing price includes VAT:
  Net revenue = gross customer price / (1 + VAT rate)
  Output VAT = gross customer price - net revenue

If the customer-facing price excludes VAT:
  Calculate the customer-facing gross price separately.

Landed product cost = product cost + inbound production freight
  + customs duty + non-recoverable import VAT
  + brokerage/clearance + production inspection allocation
  + per-unit packaging + other applicable sourcing costs

Contribution before advertising = net revenue
  - landed product cost
  - platform commission
  - payment or BNPL fee
  - fulfilment
  - expected return/refund cost
  - shipping subsidy
  - expected failed-delivery and reverse-logistics cost
  - payment collection fees

Contribution after advertising = contribution before advertising - CAC

Break-even CAC = contribution before advertising

Break-even ROAS per order = advertising-platform-reported conversion revenue per order / break-even CAC per order

Break-even ROAS for an aggregate campaign = total platform-reported conversion revenue for the same order cohort / total contribution before advertising for that same order cohort

Actual campaign ROAS = total platform-reported conversion revenue / actual advertising spend
```

If contribution before advertising is zero or negative, report no viable positive break-even CAC and break-even ROAS NOT APPLICABLE; do not divide by zero or interpret a negative ratio as a viable target. Contribution after advertising is not net profit after fixed overhead and other excluded business costs.

Show original currency, exchange-rate source and date, VAT treatment,
shipping payer, discounts, and unknown costs. Never call gross spread or
markup net profit.

### VAT and revenue basis

State the target country’s VAT rate, whether the seller is
VAT-registered, and whether the customer-facing selling price includes
VAT.

- Show customer-facing price including VAT separately.
- For contribution analysis, use revenue excluding output VAT when the
  seller is required to collect VAT.
- Treat recoverable input VAT as a cash-flow item rather than a
  permanent product cost when the seller can legally recover it.
- Include non-recoverable import VAT, customs duty, brokerage, and other
  taxes as costs where applicable.
- Confirm whether platform, payment, BNPL, and advertising fees are
  calculated on the VAT-inclusive or VAT-exclusive amount.
- Use the same revenue basis when calculating break-even CAC and
  break-even ROAS.

If the seller’s VAT status or the fee basis is unknown, show both the
assumption and the sensitivity rather than presenting one precise profit
number.

For break-even ROAS, state whether the advertising platform reports
conversion revenue including or excluding VAT, shipping, discounts,
refunds, and other adjustments. Use the same reported-revenue definition
in the ROAS formula and the pilot result.

For order-level economics, multiply product and per-unit packaging costs
by the actual quantity in the order. Account for bundles and multipacks,
use average order value when appropriate, and calculate CAC per acquired
order. Compare order-level CAC with order-level contribution before
advertising. Avoid double-counting any landed-cost component.

Calculate one expected failed-delivery and reverse-logistics cost per
order using the probability of failure and the applicable
return-to-origin, reverse-shipping, refused-delivery, and handling
charges. Include separate components only when they represent genuinely
different costs. Keep payment collection fees separate.

Use this explicit basis:
`expected failed-delivery cost = probability of failure x loss per failed order`.
Show the probability and the applicable loss components before including
the result in contribution.

### 6. Compliance, fulfilment, and rejection gates

Evaluate:

- Safety and compliance.
- Exact product match.
- Base-case economics.
- GCC shipping and delivery.
- Returns and customer support.
- Sample quality, marked **PENDING** until Prompt 3 tests it.

Use **PASS**, **FAIL**, or **PENDING**, with an evidence reference and the
stage when each check must pass. A critical FAIL overrides the score.
An unresolved pre-sample safety, identity, legal-import or financial
dependency blocks SAMPLE. Physical performance and later production QC
remain PENDING for Stage 3; they cannot be required to have passed before
a sample exists. Supplier payment verification is due before payment.

### 7. Score and decision

Separate commercial attractiveness, research completeness and confidence.
Unknown is not a failed product, and a high score is not sample approval.

### Sample-stage evidence coverage

Assess six dimensions: local demand, competition, sourcing, creative
demonstration, economics, and safety/fulfilment. Use these fixed item IDs;
do not split supported items or combine missing ones to inflate coverage.

| Dimension | Required core items |
|---|---|
| Local demand | D1: current target-country product/comparable listings, identity, price and country relevance; D2: two independent local demand signals, including a purchasing signal or credible recent customer-feedback proxy, with relevance limits |
| Competition | C1: meaningful comparable offers, specifications and positioning (aim for three when available); C2: customer complaints, support/returns signals and a defensible differentiation assessment |
| Sourcing | S1: direct supplier product lead and field-by-field specification match; S2: dated exact-variant unit price/MOQ/tiers with source and currency; S3: feasible target-country shipping, weight/lead-time basis and quote dependencies |
| Creative demonstration | U1: verified relevant exact/comparable demonstration and candidate-specific creative assessment; international evidence is acceptable here, with differences disclosed |
| Economics | E1: selling-price, tax and fee basis; E2: landed-cost components with sourced values or bounded estimates; E3: order-level fulfilment, returns, failed delivery and CAC assumptions with sources/ranges; E4: three scenarios, break-even measures and sensitivity to decision-changing inputs |
| Safety and fulfilment | R1: product-specific safety/compliance assessment and document requirements by stage; R2: delivery, returns, warranty and service feasibility; R3: target country/channel, fulfilment model, sample budget and written sample test criteria |

There are 15 core items before justified N/A exclusions. Return one compact
record per item: ID, SUPPORTED / MISSING / N/A, source IDs/date and any
limitation. A SUPPORTED assessment may identify an adverse finding; it
means assessed, not commercially attractive. Broad price ranges, unknown
costs treated as zero and unsupported guesses are not adequate support.
Defensible estimates can support sample-stage economics only with their
source, range, sensitivity and later verification action disclosed.

`Core coverage = SUPPORTED applicable core items / all applicable core items * 100`

Keep the 80% minimum for SAMPLE and assess all six dimensions. Missing
applicable core items stay in the denominator; N/A requires a reason.
Critical entry checks below must pass even if coverage exceeds 80%.

Report search evidence and GCC social evidence in a separate supplemental
ledger as SUPPORTED / NOT CAPTURED / INSUFFICIENT DATA with references.
They remain visible and affect demand coverage and confidence, but their
absence alone does not reduce core coverage. Report both figures, never
rename core coverage as full research completeness. Mark older coverage
calculations v1.1; this denominator changed and totals are not directly comparable.

### Commercial score v1.2

| Dimension | Weight | Rating basis / anchors |
|---|---:|---|
| GCC market demand | 20 | Assessed Demand Index / 20 gives the 0-5 rating; carry FULL/PROVISIONAL and coverage into the score. If no index is defensible, rating UNKNOWN |
| UGC creative potential | 15 | 0: assessed functionality or advertising constraints prevent a credible usable demonstration; 3: relevant observed demo and plausible differentiated hooks; 5: compelling repeatable candidate-relevant demonstration with supported localization plan |
| Unit economics | 30 | 0: credible base case nonviable; 3: plausible positive base case with explicit downside and acquisition assumptions; 5: resilient economics across tested price, CAC, shipping and return sensitivities |
| Competition and differentiation | 10 | 0: no viable offer advantage; 3: supported buyer/offer gap; 5: substantial supported differentiation with credible execution |
| Supplier and execution feasibility | 25 | 0: verified critical mismatch or no feasible supply route; 3: relevant supplier, price/MOQ, logistics and document plan; 5: well-corroborated supply/service feasibility with few material dependencies |
| Total | 100 | Comparison tool; gates determine the decision |

Use intermediate ratings with a brief evidence-based reason. Unknown
does not receive 0; use UNKNOWN and report supported weighted points out
of the assessed weight, plus the unassessed weight. Do not normalize
partial commercial points to /100. When every dimension is rateable,
calculate `weighted points = rating / 5 * weight` and sum to /100.
If the demand input is PROVISIONAL, label the commercial total PROVISIONAL
too. Do not award an automatic high demand rating for a missing channel.

Keep confidence separate: A requires current corroborated evidence with
no material demand-channel or commercial gap; B supports a bounded sample
decision with disclosed gaps; C indicates mainly indirect, stale or
inferred evidence and needs more research before SAMPLE. Missing search
or GCC social data caps confidence at B rather than automatically making
it C. A substantive local/sourcing/economics gap still warrants C.

### Decision rules

- **SAMPLE:** core coverage >=80%, all five commercial dimensions
  assessable, confidence A/B, and every sample-entry check below met.
- **RESEARCH MORE:** a recoverable, decision-changing evidence gap
  remains; name the gap and the next action. An access failure alone
  does not force this result when the remaining sample case is adequate.
- **HOLD:** viable possibility with a specific timing, budget, market or
  execution dependency; state what would release the hold.
- **DROP:** documented fundamental failure or nonviable economics;
  cite the decisive evidence. Missing data alone is not a DROP reason.

For SAMPLE, explicitly verify: established product identity; D1/D2 local
evidence; S1/S2 relevant supplier/specification and price basis; U1 relevant
demonstration; E1-E4 credible economics with positive base-case contribution
after a stated plausible CAC; R1-R3 sample-stage requirements; no critical
pre-sample gate FAIL or unresolved blocker. Explain any missing noncritical
core item and the Stage 3 action to resolve it. Global UGC can satisfy U1
but cannot satisfy D2. A single listing plus global views cannot pass SAMPLE.

Do not require all downside scenarios to be profitable; disclose loss
exposure, the sample budget and the evidence needed to test the assumptions.
If a plausible input range reverses the base-case decision and no credible
planning basis resolves it, use RESEARCH MORE. State the main price/CAC/
shipping/return sensitivity rather than hiding it in an optimistic total.

SAMPLE means proceed to Stage 3 supplier and sample validation. Payment
verification, physical tests, pilot-order approval and shipment release
occur at their relevant Stage 3 gates. GO is reserved for a controlled
pilot after validation, never unrestricted inventory purchasing.

## Output A: individual research dossier

Publish these findings across the assigned P2-1 through P2-7 stages under the stage budgets above. Together they form the dossier; do not reprint them all at the end. The executive/final commercial decision belongs to P2-7. Keep an index to actual stage/source records for export and handoff. If the user requests one consolidated report, produce it as a separate requested output using those records. Never call an unfinished dossier complete or approve SAMPLE from it.

1.  Product ID, actual entry route and original screening or Prompt 2A promotion record.
2.  Executive decision and one-sentence reason.
3.  Original claim audit: confirmed, changed, indirect, and unverified
    findings.
4.  Target customer, problem, and positioning opportunity.
5.  GCC marketplace and competitor evidence.
6.  Supplier comparison and exact-match analysis.
7.  UGC and demand evidence: component scores, FULL/PROVISIONAL/INSUFFICIENT EVIDENCE status, demand coverage and separate global creative support.
8.  Creative hooks and demonstration concepts.
9.  Conservative, base, and optimistic unit economics.
10. Commercial score v1.2, confidence, core item-by-item coverage and supplemental search/GCC social status. Preserve historical scores/versions separately.
11. PASS, FAIL, or PENDING rejection gates.
12. Risks and missing evidence.
13. Prompt 2 decision: SAMPLE, RESEARCH MORE, HOLD, or DROP.
14. Next action, owner, evidence required, and deadline.
15. **Potential Competitor Opportunity (optional):** only if an
    unusually interesting alternative naturally surfaced during the
    normal Prompt 2 research. Record the alternative’s product name,
    direct product URL, and concise reason it may deserve a separate
    quick validation. Do not conduct additional discovery solely to fill
    this section, do not replace the researched product, and do not
    automatically run Prompt 2A or full research on the alternative.

Every material claim needs a direct source or supplied-document reference,
research date and evidence label: VERIFIED, SUPPLIER-REPORTED, ESTIMATE,
INFERENCE, UNKNOWN, NOT CAPTURED or PENDING. Distinguish an accessible
supplier claim from independently supported performance. Store each source
once in the dossier, reuse its ID, and retain important direct links in exports.

## Output B: vertical two-column export

At P2-8, after P2-7 has recorded the supported final decision, produce exactly one table for the individual product:

| Column                         | Information to enter                                                                |
|--------------------------------|-------------------------------------------------------------------------------------|
| Product ID / Name              | Stable ID, complete product name, and meaningful variant or pack size               |
| Category                       | Relevant category and subcategory                                                   |
| Original Screening / Entry Route | Actual 1B, approved 2A, user-selected staged screening or direct user selection, with date and record reference |
| Competitor/Product Link        | Immutable Original Product URL, current Direct Product URL and important GCC competitor links with country/date; show identical original/current URL once |
| Supplier Link                  | Direct supplier links, exact-match status, and date checked                         |
| Product Cost (USD)             | Unit price, MOQ, price break, original currency, and whether shipping is excluded   |
| Competitor Selling Price (USD) | Current price, original currency, bundle size, conversion rate, and conversion date |
| UGC Video/Post Link            | Direct UGC links with evidence type: exact, similar, category, or trend             |
| UGC Views / Engagement         | Metrics, engagement rate when calculable, sample size, and missing fields           |
| Trend / Demand                 | v1.2 component scores, Demand Index/status and demand coverage; country and global/local distinction |
| Research Decision              | SAMPLE, RESEARCH MORE, HOLD, or DROP                                                |
| Notes                          | Compact summary using the labels below                                              |

Keep Notes at 180-240 words, maximum 280, using these labels in order:
PRODUCT; EVIDENCE; ECONOMICS; DEMAND / SCORE; PROMISING; RISKS;
COLLECT; DECISION / NEXT. Include exact variant/match, the strongest
local/supplier/UGC facts, financial basis, index status/demand coverage,
commercial methodology, confidence/core coverage, up to three promising
findings, risks and prioritized collection actions. Distinguish supplier
documents before payment from physical testing after receipt. State any
critical gate FAIL/PENDING and the exact next step. Refer to the dossier
for additional actions; do not hide a blocker to meet the limit.

Use the Standardized Notes module at P2-8 and for later formatting updates, with the same labels. Reuse the same Notes text in both exports; do not invent extra research merely to fill a Notes heading.

## Output C: horizontal update row for the original sheet

At P2-8, also provide one horizontal Markdown row using the original 11-column
sheet format:

``` text
| Product Name | Category | Competitor/Product Link | Supplier Link | Product Cost (USD) | Competitor Selling Price (USD) | UGC Video/Post Link | UGC Views / Engagement | Trend / Demand | Research Decision | Notes |
|---|---|---|---|---:|---:|---|---|---|---|---|
| P-000 - Product name |  |  |  |  |  |  |  |  | SAMPLE / RESEARCH MORE / HOLD / DROP |  |
```

Use the same Product ID and sources as the dossier. The horizontal row
is the compact update for the original 25-product sheet; the vertical
table and dossier preserve the deeper research.

## Handoff to Prompt 3

Only a product with the Prompt 2 decision **SAMPLE** can enter:

[Stage-3-Supplier-and-Sample-Validation.md](Stage-3-Supplier-and-Sample-Validation.md)

Pass forward:

- Product ID and actual entry record; never synthesize a missing screening row.
- Published Prompt 2 stage records/source register (the dossier), final decision and vertical table. Include actual records when moving chats; stage labels alone are insufficient.
- Horizontal update row.
- Supplier shortlist and unanswered supplier questions.
- Economic assumptions and break-even CAC/ROAS.
- Demand/Commercial methodology v1.2, FULL/PROVISIONAL status, separate demand/core coverage, supplemental gaps and confidence.
- Rejection-gate status.
- Product-specific sample pass/fail criteria.

Prompt 3 may return **GO FOR CONTROLLED PILOT**, **FIX AND RETEST**, or
**NO-GO**. It must not be treated as permission for unrestricted
inventory purchasing.

## Research integrity

- Use current sources and report the date checked.
- Missing access is not negative evidence. Preserve it as a visible gap,
  apply v1.2 sample-stage rules and never upgrade scores to manufacture a YES.
- Never invent prices, sales counts, supplier facts, shipping quotes,
  UGC metrics, certifications, or links.
- Separate exact-product, similar-product, category, and trend evidence.
- State conflicting evidence instead of averaging it away.
- Treat missing sample evidence as PENDING.
- Do not recommend inventory from supplier photos alone.
- Keep the actual original screening or approved Prompt 2A promotion record visible so the deeper research can be audited.
- Never use a category/search/homepage/social/ad URL as the candidate’s
  Direct Product URL.
- Never silently substitute a comparable product for the original
  candidate.
- If a different product is chosen for further research, preserve the
  original product record and create a separate product identity only
  after the user approves the alternative.

## Start instruction

Begin P2-1 only for the supplied product. Apply the identity gate, publish the intake/claim audit and actual source records, return the checkpoint and ask whether to continue to P2-2. Wait for the user's reply.
