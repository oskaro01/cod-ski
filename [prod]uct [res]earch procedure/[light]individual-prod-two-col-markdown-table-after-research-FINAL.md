# Prompt 2: Individual Product Deep Research and Sheet Update

**Version:** 1.5
**Revises:** v1.4; v3.0 rates GCC purchasing evidence without social weighting and reports UAE validation separately. Existing commercial weights, financial safeguards, staged execution and detailed deliverables are preserved; regional buying evidence is distinguished from UAE launch proof.

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
| P2-2 Market and customer reviews | Competitor comparison, country-tagged GCC buying evidence, positive and negative review themes, quality concerns and positioning gap | Main competitor and marketplace tasks |
| P2-3 Demand and UGC | Four evidence layers, source records, v3.0 buying-evidence rating/reasons, GCC scope, UAE validation and separate creative support and compact creative proposals | `optional-tools/[UGC]-Search-and-Demand-Validation.md` |
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

For buying evidence, extend the same register with evidence type, briefly transcribed observed wording/metric, buyer-geography basis, purchase-status basis and independence group/reason. Use stable per-product group IDs for the underlying dataset/customer population; uncertain independence cannot count as proven additional corroboration. Purchase labels: PLATFORM-REPORTED PURCHASE, SELF-REPORTED PURCHASE, OWNERSHIP ONLY, GIFT OR SAMPLE or UNKNOWN. Labels describe source support, not guaranteed authenticity. Ownership, gifts and samples alone do not establish paid buying activity. Reuse these records throughout the stages; do not generate a second buying ledger.

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
  purchasing feedback and social-commerce evidence.

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

First pass per accessible relevant listing: inspect up to five recent and five low-rated written reviews, deduplicating overlaps. Inspect fewer when fewer are readable; record actual counts, source references, buyer-geography/purchase-status basis and purchase/use context. These are limits, not review quotas. A headline rating is not written-review inspection. Zero inspected reviews needs an access/availability explanation and a recovery action when decision-changing; inspect more only for a named material conflict. Sampled complaint shares are not population defect/return rates.

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

Choose routes appropriate to the business model. For branded resale, prioritize the brand's distributor/dealer programme and supported authorized supply; a similar-looking OEM offer is not the branded model. For private label, compare manufacturers against required specifications without borrowing the branded reference's sales/performance claims. Record seller role, authorization evidence, exact variant/quantity tier and quote dependencies. A programme verifies an inquiry route, not an exact-SKU price, factory identity or a shipping commitment. Do not substitute retail-to-retail price differences for wholesale economics. Missing quotations may be acceptable at screening, but the SAMPLE requirements below still need supported price and cost inputs or defensible bounded estimates.

Compare competitor specifications against supplier specifications field
by field. Mark each field **match**, **difference**, or **unknown**.

### 4. UGC and demand research

Evaluate four layers: exact product/model, direct comparable competitors,
product category, and customer problem/use case. Include useful English
and Arabic terms. A problem video can reveal interest without proving
purchase intent; a competitor demonstration cannot establish the
candidate's performance, safety or exact-model sales.

Default launch market is UAE; opportunity research spans the GCC. Seek useful
buying evidence across the GCC without six complete country studies by default.
Label supported countries and leave others NOT ASSESSED. Other-GCC buying evidence
can support a UAE opportunity hypothesis, not proven UAE demand. Assess UAE
customer fit, price, compatibility, channel and fulfilment separately.

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

Collection order within the demand-search budget: inspect explicit marketplace bought/sold wording and its model/country/period/rounding, then the bounded written-review sample. Rankings alone are context, not purchasing evidence. If material independent corroboration is missing, search accessible original buyer discussions for an author/date, model, country basis and actual purchase/use statement; recommendations and intentions are not purchases. Do not add a mandatory discussion quota or repeat adequate P2-2 checks at P2-3.

If only private evidence can close a decision-changing gap, record a redacted merchant-record request, owner and timing as EXTERNAL INPUT NEEDED; do not contact anyone automatically. Specify SKU, country, period, units versus orders, returns/cancellations basis and wholesale shipments versus end-customer sales. Supplier assertions remain SUPPLIER-REPORTED, not independent consumer-demand proof. Private documentation is not mandatory when public evidence already supports the decision. Keep buying activity, satisfaction/quality and creative popularity separate.

For a defensible GCC case, seek two independent relevant GCC demand signals,
including at least one recent purchasing signal or credible recent buyer-feedback
proxy. They need not come from UAE or different countries. Disclose actual country
and exact/comparable/category scope. Where UAE evidence is absent, document the
transfer rationale, customer/price/compatibility differences and a named UAE
validation check; absence of UAE proof does not establish weak regional demand.
Copied listings, syndicated reviews, reposts and a search result pointing
to the same listing count as one underlying source, not independent proof.
Positive ratings alone cannot establish sales velocity or profitability.

### Source discovery and access limits

Do not use Google Trends, Keyword Planner, keyword volume, autocomplete, CPC or search-result visibility as demand inputs. Ordinary English/Arabic web searches may locate direct marketplace, customer, supplier and creator sources; finding a result does not establish interest or purchases. No search-interest score, account creation or ads verification is required.

For the demand pass, use up to four new source-finding queries across the GCC in total per product and start with up to two accessible source types overall, reusing P2-2 records. These are focused first-pass limits, not per-country quotas or limits on the separate supplier/competitor tasks. Follow the evidence without six compulsory country studies. A follow-up needs a named conflict or decision-changing gap. After an access failure, use an accessible alternative, then disclose the limitation instead of repeatedly retrying. Record source, country, checked date, source snapshot/measurement period and exact/comparable/category/problem relevance. Old cached prices and reviews retain their original scope; today's retrieval does not make them current.

For each task, distinguish INSPECTED, LIMITED, ACCESS BLOCKED, EXTERNAL INPUT NEEDED and NOT ATTEMPTED, with counts/reasons. If readable reviews exist, inspect them; a headline rating is not a completed complaint check. Zero inspected reviews requires an explanation and recovery action when material. At P2-6, prioritize missing checks that could change the decision; requests requiring private quotes/documents/tests receive an owner and timing rather than endless public searching.

### UGC, global evidence and creative potential

Research useful accessible TikTok, Instagram, YouTube, Snapchat or creator
sources. Aim for three strong demonstrations when available; stop after a
focused pass if access is blocked or results repeat. Missing creator links
remain a gap; do not fabricate them or fill quotas with unrelated content.

Label every reference EXACT PRODUCT, COMPARABLE PRODUCT, CATEGORY,
CUSTOMER PROBLEM or GENERAL TREND, plus its supported GCC country or INTERNATIONAL.
Record direct URL, creator, date, visible metrics, hook, demonstration,
sponsorship status and the basis for country/audience relevance. Creator
location alone does not establish audience geography. Mark unavailable
metrics NOT CAPTURED, inaccessible destinations NOT VERIFIED and content
older than 12 months HISTORICAL. Negative/safety material belongs in risks.

A destination returning only a title, metadata or an empty player is NOT INSPECTED for the demonstration claim. Record what was actually read/viewed. An original inspectable hands-on article with product-use evidence may support creative assessment, labelled EDITORIAL HANDS-ON rather than creator video. Manufacturer demonstrations are BRAND DEMO, not independent customer proof. Do not infer audience geography from a creator's location or convert inaccessible videos into endorsements.

Calculate `(likes + comments + shares) / views * 100` only when all metrics
exist and views > 0. Do not infer sales or advertising performance from it.

International exact/comparable demonstrations may support global solution
interest and creative potential, not GCC purchasing. Report creative support as
STRONG, LIMITED or NOT ESTABLISHED. GCC UGC helps localization but is not required
for demand or high demand confidence. No creator quota applies. Relevant inspected
editorial or brand demonstrations can support U1 with provenance/limits disclosed;
promotional footage is not independent customer proof.

Create three hooks, three demonstrations, one objection-handling idea,
one Arabic-friendly angle and one English-friendly angle. Base ideas on
supported functionality and label untested creative as proposals.

### Demand Index v3.0: GCC purchasing evidence, UAE validation separate

This is an evidence-strength screening heuristic, not a validated demand model, sales forecast or probability of success. Use the purchasing-evidence rating below without an 80/20 marketplace/social blend. A high score cannot override identity, quality, economics or safety gates. Preserve v1.2/v2.0 scores as historical; methodology changes are not market growth.

Do not use Google Trends, Keyword Planner, keyword volume, autocomplete, CPC or search visibility as demand inputs. Ordinary English/Arabic searches locate evidence only; ranking/results earn no demand points.

Eligible buying evidence:
- Platform-reported sold/bought indicators or supplied merchant/order records: preserve exact model/variant, country, period and source limitations. Never invent a time window or precise sales from a rounded badge.
- Recent dated written product reviews or first-person purchasing feedback: capture dates, model, country basis and review-pool scope. These proxy buying activity, not unit sales. High average ratings describe reported satisfaction; cumulative counts alone do not establish current demand.
- Independent comparable offers with their own purchasing/feedback evidence: explain functional and price comparability. Multiple listings, seller counts, stockouts, ads and store ratings alone prove neither purchases nor profitable demand.
- Dated review/sold-counter changes, documented restocks and customer purchase discussions may corroborate buying evidence. One snapshot cannot prove growth. Call an increase in comparable dated buying indicators OBSERVED MOMENTUM, with source, country, model and period; otherwise report MOMENTUM NOT ESTABLISHED. Do not infer a market-wide trend or future growth, wait days or repeatedly scrape to construct a time series.

Recency: prefer written buyer reviews and first-person purchasing discussions from the preceding 12 months relative to the research date. Treat older evidence as HISTORICAL; a justified longer buying-cycle window must be stated explicitly. Preserve older safety/quality concerns rather than dismissing them by age. Review dates proxy feedback timing, not exact purchase dates. For sales badges record the current snapshot and exact displayed measurement period; undisclosed dates/periods are NOT CAPTURED and cannot be assumed recent. Price/stock records need the actual check date and any cached-source date; today's retrieval does not refresh old evidence.

Independence concerns the underlying merchant dataset or customer population, not the number of URLs, sites or screenshots. Copied listings, shared review pools/data feeds, syndicated merchant records, reposts and the same buyer count once. Two distinct merchant datasets or independently collected customer populations may corroborate each other; explain the basis. A sales badge and reviews on one listing are not automatically independent.

Global reviews with unknown buyer geography may inform quality, complaints and feature preferences, but cannot establish GCC purchasing. A GCC storefront alone does not establish buyer location. Complaints can indicate buying while revealing serious quality risks; retain both findings.

For candidate advancement, at least one qualifying buying signal must concern the exact product or an identified direct comparable with justified functional/price relevance. Category/problem-only signals cannot satisfy the candidate demand gate: report broader interest separately and candidate buying evidence UNKNOWN. Comparable-only evidence supports the solution opportunity, not proven purchases of the candidate's exact model; label the rating basis accordingly.

Purchasing-evidence rating, 0-100:
- UNKNOWN: insufficient accessible evidence to assess buying activity; never substitute zero.
- 0: affirmative, adequately scoped evidence of negligible current buying activity; absence of data is not enough.
- 25: weak, isolated or stale purchasing clues; historical evidence does not establish current buying.
- 50: relevant current GCC purchasing/feedback evidence with limited independent corroboration.
- 75: at least two independent relevant GCC signals, including recent purchasing/credible buyer feedback, with country/model/period limits clear.
- 100: strong independently corroborated current GCC buying evidence across sources and periods, with geography and model limits understood.
Explain intermediate ratings with sources; these are ordinal evidence-strength anchors, not statistically meaningful differences in demand size. Listing presence, stock and displayed prices alone are market-presence observations: purchasing-evidence rating UNKNOWN, not 25. Strong evidence in one GCC country can support 75/100 only for that stated scope. Never average unequally evidenced countries into a GCC-wide rating or transfer a country's rating to another. Multiple supported countries mean multi-country evidence, not automatically GCC-wide validation.

Always report separately:
1. GCC finding: rating or UNKNOWN explicitly labelled by supported country/model scope (for example, 75 - KSA-supported, direct-comparable evidence); recency, independent signal count, source IDs and limitations. In the existing record, tag researched/transfer countries SUPPORTED, REGIONAL TRANSFER HYPOTHESIS, INSUFFICIENT EVIDENCE or CONTRADICTED; mark unresearched countries NOT ASSESSED collectively. No extra six-country study or table is required.
2. UAE validation: use the same country statuses. SUPPORTED means relevant country-attributed buying evidence exists for the labelled product/comparable scope, not launch approval; REGIONAL TRANSFER HYPOTHESIS means another GCC market supports a documented opportunity rationale with a named validation check; INSUFFICIENT EVIDENCE means research was attempted but buying evidence remains inadequate; CONTRADICTED needs an adverse finding, not missing access; NOT ASSESSED means meaningful country-specific assessment was not completed. Buying evidence outside UAE is not UAE proof.
3. Demand confidence: HIGH / MEDIUM / LOW for the stated GCC finding, based on purchasing-source independence, recency, identity and country attribution. High confidence in regional demand can coexist with unvalidated UAE demand.
4. Creative assessment: relevant GCC/international UGC, editorial hands-on or brand demonstrations, with inspection status and creative limits. Missing UGC does not lower demand rating/confidence. Views, likes and promotional footage alone do not prove buying. First-person purchase discussions can count as purchasing evidence only with their actual scope; never count the same discussion twice.

There is no weighted demand-coverage percentage or required creator quota. State inspected evidence and missing buying checks directly. Core checklist coverage below is a different measure. At P2-2, creative checks may be NOT YET DUE; that does not make an otherwise assessed buying case provisional. Uncertainty about UAE transfer remains visible in readiness and the next action.

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

Assess six dimensions: GCC demand/UAE relevance, competition, sourcing, creative
demonstration, economics, and safety/fulfilment. Use these fixed item IDs;
do not split supported items or combine missing ones to inflate coverage.

| Dimension | Required core items |
|---|---|
| GCC demand / UAE relevance | D1: current GCC product/comparable offers, identity, price and country scope, plus UAE offer/price context or an explicit sourced transfer assessment; D2: two independent relevant GCC buying signals including recent purchasing/credible buyer feedback, at least one for the exact product or identified direct comparable (not category/problem-only), model/country limits, separate UAE validation status and a concrete UAE validation plan when regional-only |
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

Report creative evidence separately with sources and inspection limits. Missing UGC affects neither demand rating/confidence nor the core denominator; U1 still requires a relevant inspected demonstration, not necessarily GCC creator content. Buying discussions may support demand with scope disclosed, counted once. Search interest is excluded, not missing. Report GCC scope, UAE validation and core coverage separately; no weighted demand-coverage percentage applies. Preserve historical scores/denominators; core coverage is not full research completeness.

### Commercial score: existing weights, v3.0 demand input

| Dimension | Weight | Rating basis / anchors |
|---|---:|---|
| GCC market demand | 20 | Assessed v3.0 purchasing-evidence rating / 20 gives the 0-5 rating; preserve country/model scope and separate UAE validation. Regional-only evidence does not force a low rating. If buying evidence cannot be assessed, rating UNKNOWN |
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
Label the commercial total PROVISIONAL for material unresolved inputs. Missing
data cannot earn a high score. A strong regional demand rating is not UAE launch approval.

Keep confidence separate: A requires current corroborated evidence with no material
unresolved commercial gap; B supports a bounded sample with disclosed gaps; C
means mainly indirect, stale or inferred evidence needing more research. Missing
GCC UGC does not automatically cap confidence. Demand confidence concerns its
stated GCC scope; overall commercial confidence also considers UAE transfer,
sourcing and economics. Regional demand may be highly credible while UAE demand
remains unvalidated. A material transfer risk may warrant B/C or HOLD; explain
the risk rather than penalizing a missing UAE creator or review automatically.

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

For SAMPLE, explicitly verify: established product identity; D1/D2 GCC buying
evidence and UAE relevance/validation plan; S1/S2 relevant supplier/specification and price basis; U1 relevant
demonstration; E1-E4 credible economics with positive base-case contribution
after a stated plausible CAC; R1-R3 sample-stage requirements; no critical
pre-sample gate FAIL or unresolved blocker. Explain any missing noncritical
core item and the Stage 3 action to resolve it. Global UGC can satisfy U1
but cannot satisfy D2. A single listing plus global views cannot pass SAMPLE.
Regional-only buying evidence can support a bounded SAMPLE for physical validation
when all entry gates pass, UAE fit is defensible and a concrete UAE demand check
is recorded. This is not UAE launch approval. Confirmed UAE incompatibility or an
unresolved material transfer/safety/economic blocker requires HOLD, RESEARCH MORE
or DROP as appropriate. Carry the UAE validation dependencies to Stage 3 and
resolve them before a UAE commercial pilot; never relabel regional sales as UAE proof.

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
7.  Demand evidence: v3.0 purchasing-evidence rating, supported GCC country/model scope, UAE validation status/plan and separate creative support.
8.  Creative hooks and demonstration concepts.
9.  Conservative, base, and optimistic unit economics.
10. Commercial score using existing weights and v3.0 demand input, confidence, core item-by-item coverage, UAE validation and separate creative assessment. Preserve historical scores/versions separately.
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
| Trend / Demand                 | v3.0 buying-evidence rating, supported GCC scope, UAE validation status/plan and demand confidence; global evidence labelled separately |
| Research Decision              | SAMPLE, RESEARCH MORE, HOLD, or DROP                                                |
| Notes                          | Compact summary using the labels below                                              |

Keep Notes at 180-240 words, maximum 280, using these labels in order:
PRODUCT; EVIDENCE; ECONOMICS; DEMAND / SCORE; PROMISING; RISKS;
COLLECT; DECISION / NEXT. Include exact variant/match, the strongest
GCC/supplier/creative facts, financial basis, buying-evidence rating/GCC scope/UAE validation,
commercial and demand methodologies, confidence/core coverage, up to three promising
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
- Demand methodology v3.0, existing commercial weights, GCC demand rating/scope, UAE validation dependencies, separate creative assessment, core coverage and confidence.
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
