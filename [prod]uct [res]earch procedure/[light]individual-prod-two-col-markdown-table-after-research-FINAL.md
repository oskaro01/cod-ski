# Prompt 2: Individual Product Deep Research and Sheet Update

**Version:** 1.7
**Revises:** v1.6; distinguishes sourced financial inputs from illustrative placeholders and uses conditional cost thresholds to guide missing-quote recovery. Qualitative traction, the four commercial weights totalling 80, detailed deliverables, staged execution and sample-risk safeguards remain unchanged.

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
| P2-3 Demand and UGC | Four evidence layers, source records, qualitative traction/facts, evidence confidence, GCC scope, UAE validation and separate creative support and compact creative proposals | `optional-tools/[UGC]-Search-and-Demand-Validation.md` |
| P2-4 Supplier comparison | Direct leads, specification comparison, exact-variant price/MOQ/tiers, shipping/lead-time basis, supplier claims and quote/document gaps | Main supplier tasks |
| P2-5 Economics and risks | Conservative/base/optimistic order economics, input sources/ranges, break-even measures, price/CAC/shipping/return sensitivities, risk gates and proposed sample test criteria | Main economics and compliance tasks |
| P2-6 Evidence-gap closure | Audit all 15 core items; research up to three decision-changing gaps, update affected inputs and list unresolved dependencies | `optional-tools/[Evidence-Gap]-Closure.md` |
| P2-7 Final decision | Current 15-item coverage ledger, qualitative traction/limits, four commercial ratings/points out of 80, confidence, gate references, canonical decision and short explanation | Main decision rules, then `optional-tools/Product-[Decision]-Summary.md` |
| P2-8 Notes and exports | Final Notes, vertical two-column table, horizontal 11-column row and Stage 3 handoff/readiness | `optional-tools/Standardized-[Notes].md` and Outputs B/C |

The tasks below define research standards; they are not instructions to execute every task in the first response. Output A is the cumulative published record from P2-1 through P2-7. Produce Outputs B/C only at P2-8. Before P2-7, label assessments PROVISIONAL / FINAL DECISION PENDING and never grant SAMPLE. A documented disqualifying finding may end research early with a sourced DROP and checkpoint; do not perform unnecessary remaining research. Ask whether to prepare exports. Final scoring cannot be inferred from unfinished stages.

After P2-8, report COMPLETE with unresolved later-stage actions. Do not ask for a nonexistent P2-9 or start Stage 3 automatically. For an early DROP, format only supported findings and mark skipped research NOT ASSESSED; no fabricated score or completed checklist.

### Using the separate modules

The supporting files remain separate. Their relevant functions are required at the stages above: demand assessment, gap audit, final explanation and Notes. Gap browsing is conditional on an actual material gap; the gap audit is always required. Reuse prior evidence and stop when the question is adequately resolved.

For a local agent, read the named module when its stage is reached. In a chat without workspace access, attach this prompt and the four module files at the start, or supply each module when requested. A local filename is not accessible merely because it appears in this prompt. If a module is absent, report MODULE NOT PROVIDED, execute the corresponding standards already specified here, and mark that its additional instructions were not applied; never pretend to have read it. Missing instructions needed for a defensible decision remain a dependency. No automatic merge or invented module contents.

Pass only the active Product ID, exact variant/country, actual source records loaded from state, latest relevant findings and the named question to a module. In staged use, this controller determines timing, output and state-file writes: modules return findings/changes without creating competing file versions. They cannot independently approve SAMPLE, restart research, generate all exports or advance the next stage. Standalone module behavior remains available when the user requests it separately.

### Compact output and checkpoint contract

Use short factual records and source IDs; no product cards, images, decorative output or repeated dossiers. Use a compact comparison table only where it helps. P2-1 maximum 500 words; P2-2/3/4/6 maximum 900 each; P2-5 maximum 1,100; P2-7 maximum 900 including the core ledger and summary; P2-8 maximum 1,200 including both exports. Exclude URL strings; do not pad to these limits. These are stage limits, not a requirement to recreate a full report at every pause.

Keep one source register with stable IDs: direct URL or supplied-document reference, country/platform, date checked, publication/measurement period when available, exact/comparable/category/problem match, captured claim/value and verification limitation. Publish new records once; later stages cite their IDs. Reopen only for volatile/stale facts, conflicts or named gaps. Distinguish marketplace-associated feedback from confirmed buyer geography and global/imported pools; never infer residency solely from the storefront or count a syndicated review pool twice.

For buying evidence, extend the same register with evidence type, briefly transcribed observed wording/metric, buyer-geography basis, purchase-status basis and independence group/reason. Use stable per-product group IDs for the underlying dataset/customer population; uncertain independence cannot count as proven additional corroboration. Purchase labels: PLATFORM-REPORTED PURCHASE, SELF-REPORTED PURCHASE, OWNERSHIP ONLY, GIFT OR SAMPLE or UNKNOWN. Labels describe source support, not guaranteed authenticity. Ownership, gifts and samples alone do not establish paid buying activity. Reuse these records throughout the stages; do not generate a second buying ledger.

Every checkpoint contains Product ID/variant, target country, completed and next stage, actual new findings and source references, unresolved critical questions, changed assumptions/scores and current decision status. Add the checked state filename/revision, record counts, validation status and actual download link, or TEXT EXPORT ONLY. If a stage is unfinished, preserve completed work and resume it on CONTINUE after reopening state. If switching chats, supply this prompt, required modules and the latest state file or complete relevant portable stage/source exports. Missing records are a named dependency; never reconstruct them from IDs or memory.

If a new finding changes an earlier model, price, risk or demand assumption, mark dependent scores/economics STALE and recompute only affected results before the final decision. Formatting never upgrades a decision. Pauses limit work per response; they do not reset conversation capacity or guarantee completion.

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

- Non-GCC buying/feedback can inform international traction, product-use/quality
  and a labelled transfer hypothesis, not confirmed GCC purchases or GCC
  satisfaction. Regional storefront context can support marketplace-associated
  activity; it does not independently establish each buyer's country.

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

Collection order within the demand-search budget: inspect explicit marketplace bought/sold wording and its model/country/period/rounding, then the bounded written-review sample. A documented sales-based marketplace rank can corroborate relative activity; generic rank labels and search position do not establish purchases. If material independent corroboration is missing, search accessible original buyer discussions for an author/date, model, country basis and actual purchase/use statement; recommendations and intentions are not purchases. Do not add a mandatory discussion quota or repeat adequate P2-2 checks at P2-3.

If only private evidence can close a decision-changing gap, record a redacted merchant-record request, owner and timing as EXTERNAL INPUT NEEDED; do not contact anyone automatically. Specify SKU, country, period, units versus orders, returns/cancellations basis and wholesale shipments versus end-customer sales. Supplier assertions remain SUPPLIER-REPORTED, not independent consumer-demand proof. Private documentation is not mandatory when public evidence already supports the decision. Keep buying activity, satisfaction/quality and creative popularity separate.

For a defensible research case, seek relevant exact-product or justified direct-comparable purchasing/customer activity and explain its GCC/UAE relevance. One credible source can justify continued commercial investigation; two independent signals strengthen confidence, not a mandatory source quota. Record marketplace-associated geography honestly when buyer countries are undisclosed. Explicit international/global pools support a transfer hypothesis, not confirmed GCC purchases. A promising research case is not SAMPLE approval; apply the sample-entry checks separately.

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

### Public-market traction assessment

Replace the numerical Demand Index with a qualitative assessment. It describes observed activity and a research opportunity, not exact sales volume, market size or success probability. Do not award demand points or translate the labels into numbers. Preserve earlier indices as historical; reassess from actual source records rather than converting 25/100 into a new label.

Use public evidence proportionately:
- Sold/bought badges and supplied order records indicate source-reported purchasing. Capture model, market, snapshot date, displayed period and rounding. An unspecified period stays NOT CAPTURED; a badge is not an exact monthly sales count.
- Dated purchase-labelled reviews and credible first-person buying/use accounts support customer activity. Cumulative product-review counts support historical traction; average stars describe reported satisfaction. Neither establishes current sales volume. Preserve genuine complaints separately as quality evidence.
- A documented sales-based marketplace rank can corroborate relative activity within its stated market/category. Generic bestseller labels and search positions are not equivalent. Never convert a rank into units or assume the same rank implies equal demand across categories.
- Exact-product or justified direct-comparable activity supports the candidate's research case, with differences disclosed. Category/problem interest supports exploration, not proven sales of this model. Listings, prices, stock, seller counts, ads, likes and views alone do not establish purchases.

Keep geography honest without demanding hidden buyer data. Label a regional storefront's own purchase indicators or product feedback MARKETPLACE-ASSOCIATED with its stated country and limitations when individual buyer countries are unavailable. This can support a preliminary regional opportunity; it is not independently confirmed buyer residency. Label explicitly global/imported review pools GLOBAL or POOLED and retain them for historical traction, product-use/quality and transfer hypotheses, not as confirmed GCC purchases. Missing buyer-country metadata lowers geographic confidence; it does not erase observed product activity. Never infer geography from names, language or creator location.

Count underlying datasets/customer populations, not URLs, sellers or country mirrors. Shared pools, syndicated reviews and reposts count once. Two independent relevant signals strengthen corroboration, but are not a quota for continuing research; one credible buying/customer-activity source can justify commercial investigation. This does not automatically satisfy sample-entry requirements or approve inventory.

Return one observed-traction label for an explicit product/model and geographic scope:
- ENCOURAGING: captured purchasing/customer-activity evidence supports a plausible case worth commercial validation. State whether support is current, historical, marketplace-associated or a transfer hypothesis. This is not proof of large or growing demand.
- MIXED: meaningful positive and adverse buying/activity evidence conflict. Name the conflict; do not turn quality complaints or geographic uncertainty alone into weak demand.
- WEAK: affirmative, appropriately scoped evidence indicates limited or declining activity against a stated relevant period/comparator. Missing access, few reviews or undisclosed sales alone do not justify this label.
- UNASSESSABLE: no usable purchasing/customer-activity evidence was captured. Availability, average stars and attention alone are insufficient. Record the gap without assigning zero or rejecting automatically.

Report evidence confidence separately: HIGH for coherent, current, well-matched and corroborated evidence with clear scope; MEDIUM for credible activity with disclosed limitations; LOW for mainly older, indirect, pooled or geographically uncertain evidence. ENCOURAGING with LOW confidence is valid. Confidence is not a multiplier or extra points deduction. Missing GCC UGC cannot lower traction or buying-evidence confidence.

Prefer buyer feedback from the preceding 12 months; older records remain HISTORICAL, not worthless or current. Preserve older safety complaints. Review dates are feedback dates, not exact purchase dates. Record cache/snapshot dates; today's retrieval does not refresh old data. Only comparable dated buying indicators support OBSERVED MOMENTUM; otherwise use MOMENTUM NOT ESTABLISHED. Do not wait or repeatedly scrape to manufacture a time series.

In the existing product record report: traction label and supporting facts/source IDs; current versus historical activity; exact/comparable and country/marketplace-associated/global scope; confidence and limitations; UAE validation and one next action. UAE/country statuses remain SUPPORTED / REGIONAL TRANSFER HYPOTHESIS / INSUFFICIENT EVIDENCE / CONTRADICTED / NOT ASSESSED. SUPPORTED requires evidence explicitly attributable to that market with its source-reported limits; a storefront alone does not establish buyer location. Do not relabel inferred review geography as SUPPORTED. A transfer hypothesis needs a fit rationale and named check. Other-country evidence is not UAE proof; unresearched countries remain NOT ASSESSED, with no compulsory six-country study.

Next action: continue commercial validation when the opportunity case is defensible, resolve one named decision-changing gap, or park/reject for a documented reason. Reuse completed checks and the existing research limits; make at most one focused demand follow-up for a material gap, then disclose the limitation or external action. Never require private competitor dashboards or continued browsing merely to improve a label. Keep creative assessment, quality, economics and sample/launch readiness separate. Do not use Google Trends, Keyword Planner, keyword volume, autocomplete, CPC or search visibility as demand inputs; source-finding searches locate evidence only.

### 5. Unit economics

Model conservative, base, and optimistic scenarios. State every
assumption.

### Financial input quality and decision use

Apply these rules within the existing economics tables and stage budget; do not add a separate report:

- Confirm or explicitly assume the channel, sourcing/fulfilment model, order quantity, shipping payer and acquisition method. Do not silently impose single-unit orders, free delivery or paid acquisition on every product, or switch models merely to make the result positive.
- For each material input, distinguish an actual quote/observed value, published benchmark, defensible estimate, ILLUSTRATIVE placeholder or UNKNOWN. Record its source/date and applicability; estimates need a rationale, range and verification action. A provider tariff is not a negotiated quote. No source means no claimed industry standard; do not reuse fixed supplier costs, CAC, failure/return probabilities or warranty reserves as universal defaults. Review complaint shares are not return/defect probabilities.
- Keep unsupported actual inputs UNKNOWN in the saved record. Clearly labelled ILLUSTRATIVE what-if values may explore exposure, but cannot replace missing facts or establish a most-likely base. Retain all three scenarios; when critical inputs lack a defensible planning basis, label the table ILLUSTRATIVE - ACTUAL ECONOMICS UNVERIFIED. Do not choose either cautious or optimistic guesses to force a decision.
- When a critical quote or acquisition cost is missing, first show one useful conditional affordability threshold using the available price and explicit operating assumptions: maximum landed/supplier cost at a stated CAC, or affordable CAC at a stated landed cost. Use the same quantity, return/write-off and tax basis as the scenarios. State what is held fixed and whether the target is break-even or a user-approved contribution buffer. Independently calculated cost and CAC maxima cannot both be spent at once. If the other inputs cannot support even a conditional threshold, report NOT CALCULABLE and name the next required input.
- Separate scenario outcome from economic readiness. With decision-changing unsupported inputs, actual economics remain PENDING / UNVERIFIED, not a confirmed economic FAIL. A negative illustrative base alone cannot justify DROP or a zero economics rating; a positive illustration cannot justify SAMPLE. Use RESEARCH MORE with a named quote/test action, or HOLD for an external timing/budget dependency. Credible evidence of nonviability for the selected offer/business model can justify DROP; all other critical rejection and SAMPLE gates still apply.

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

Build VAT-status sensitivities from each cost component's applicable tax basis; do not add a blanket VAT percentage to all costs or to already tax-inclusive amounts. Keep unresolved tax treatment explicit rather than inventing an exact alternative profit.

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

Confirm whether an RTO tariff is additional to outbound delivery or the total charge for the failed shipment. If unclear, show the conditional cost treatment and request clarification; do not silently charge outbound twice or assume return transport is free.

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
| GCC demand / UAE relevance | D1: current GCC product/comparable offers, identity, price and country scope, plus UAE offer/price context or an explicit sourced transfer assessment; D2: a source-supported exact-product/direct-comparable buying/customer-activity case with recency, country/marketplace-associated/global scope, confidence and limitations; an explicit reason the evidence is adequate for the proposed bounded sample, plus UAE fit and a concrete validation plan when country demand is unconfirmed. Independent corroboration strengthens the case, not a fixed two-source quota; listings/average stars/category attention alone cannot support it |
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

Report creative evidence separately with sources and inspection limits. Missing UGC affects neither observed traction/evidence confidence nor the core denominator; U1 still requires a relevant inspected demonstration, not necessarily GCC creator content. Buying discussions may support demand with scope disclosed, counted once. Search interest is excluded, not missing. Report GCC scope, UAE validation and core coverage separately; no weighted demand-coverage percentage applies. Preserve historical scores/denominators; core coverage is not full research completeness.

### Commercial score: four dimensions out of 80

Demand is a separate qualitative assessment, not a numerical input. Do not turn ENCOURAGING/MIXED/WEAK/UNASSESSABLE or evidence confidence into points. Keep the other weights unchanged; do not redistribute the retired 20 demand points.

| Dimension | Weight | Rating basis / anchors |
|---|---:|---|
| UGC creative potential | 15 | 0: assessed functionality or advertising constraints prevent a credible usable demonstration; 3: relevant observed demo and plausible differentiated hooks; 5: compelling repeatable candidate-relevant demonstration with supported localization plan |
| Unit economics | 30 | 0: credible base case nonviable; 3: plausible positive base case with explicit downside and acquisition assumptions; 5: resilient economics across tested price, CAC, shipping and return sensitivities |
| Competition and differentiation | 10 | 0: no viable offer advantage; 3: supported buyer/offer gap; 5: substantial supported differentiation with credible execution |
| Supplier and execution feasibility | 25 | 0: verified critical mismatch or no feasible supply route; 3: relevant supplier, price/MOQ, logistics and document plan; 5: well-corroborated supply/service feasibility with few material dependencies |
| Total | 80 | Comparison tool; the separate traction case and entry gates still determine the decision |

Use intermediate ratings with a brief evidence-based reason. Unknown is UNKNOWN, not 0. Report supported weighted points out of the assessed weight, plus unassessed weight out of 80. With all four dimensions assessable, calculate `weighted points = rating / 5 * weight` and sum to /80. Never normalize to /100 or present a partial score as a complete /80 score. Historical /100 totals and numerical demand indices remain historical and are not directly comparable; do not rescale them during formatting.

Label the commercial total PROVISIONAL for material unresolved inputs. A high /80 score does not compensate for missing buying activity, an indefensible UAE opportunity or any failed critical gate. Core coverage is a separate percentage, not the /80 commercial denominator.

Keep overall commercial confidence separate: A requires current corroborated evidence with no material unresolved commercial gap; B supports a bounded sample with disclosed, manageable limitations; C means material indirect/stale/inferred dependencies needing more work. Buying-evidence confidence concerns its stated scope; overall confidence also covers sourcing, economics and UAE transfer. One public source or missing buyer-residency metadata does not automatically force C; explain the actual decision risk. ENCOURAGING traction with LOW evidence confidence can justify research, but is not by itself enough for SAMPLE. Missing GCC UGC is not a demand penalty.

### Decision rules

- **SAMPLE:** core coverage >=80%, all four commercial dimensions
  assessable, a defensible D1/D2 market case, overall confidence A/B, and every sample-entry check below met.
- **RESEARCH MORE:** a recoverable, decision-changing evidence gap
  remains; name the gap and the next action. An access failure alone
  does not force this result when the remaining sample case is adequate.
- **HOLD:** viable possibility with a specific timing, budget, market or
  execution dependency; state what would release the hold.
- **DROP:** documented fundamental failure or nonviable economics;
  cite the decisive evidence. Missing data alone is not a DROP reason.

For SAMPLE, explicitly verify: established product identity; D1/D2 traction evidence,
source/geographic limits and UAE relevance/validation plan; S1/S2 relevant supplier/specification and price basis; U1 relevant
demonstration; E1-E4 credible economics with positive base-case contribution
after a stated plausible CAC; R1-R3 sample-stage requirements; no critical
pre-sample gate FAIL or unresolved blocker. Explain any missing noncritical
core item and the Stage 3 action to resolve it. Global UGC can satisfy U1
but cannot satisfy D2 alone. A single listing plus global views cannot pass SAMPLE. A promising traction label or unknown buyer country alone neither approves nor vetoes SAMPLE; assess the supported market case, material uncertainty and all remaining entry checks.
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
7.  Demand evidence: observed traction label/facts, current/historical and geographic/model scope, evidence confidence, UAE validation status/plan and separate creative support.
8.  Creative hooks and demonstration concepts.
9.  Conservative, base, and optimistic unit economics.
10. Four-dimension commercial score out of 80, separate qualitative traction/evidence confidence, overall confidence, core item-by-item coverage, UAE validation and creative assessment. Preserve historical scores/versions separately.
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

At P2-8, reopen the latest validated state or supplied portable stage/source records and confirm the supported P2-7 decision before producing exactly one table for the individual product. Preserve all detailed findings and calculation inputs in state; the compact export does not replace them:

| Column                         | Information to enter                                                                |
|--------------------------------|-------------------------------------------------------------------------------------|
| Product ID / Name              | Stable ID, complete product name, and meaningful variant or pack size               |
| Category                       | Relevant category and subcategory                                                   |
| Original Screening / Entry Route | Actual 1B, approved 2A, user-selected staged screening or direct user selection, with date and record reference |
| Competitor/Product Link        | Immutable Original Product URL, current Direct Product URL and important GCC competitor links with country/date; show identical original/current URL once |
| Supplier Link                  | Direct supplier links, exact-match status, and date checked                         |
| Product Cost (USD)             | Exact-candidate wholesale cost/status and any separate indicative comparable OEM prices; apply the cost-reporting contract below |
| Competitor Selling Price (USD) | Current price, original currency, bundle size, conversion rate, and conversion date |
| UGC Video/Post Link            | Direct UGC links with evidence type: exact, similar, category, or trend             |
| UGC Views / Engagement         | Metrics, engagement rate when calculable, sample size, and missing fields           |
| Trend / Demand                 | Observed traction label/facts, current/historical and country/model scope, evidence confidence, UAE validation status/plan; marketplace-associated/global evidence labelled separately |
| Research Decision              | SAMPLE, RESEARCH MORE, HOLD, or DROP                                                |
| Notes                          | Compact summary using the labels below                                              |

### Product-cost reporting for both exports

Use the same Product Cost cell text in Outputs B/C, without extra columns or new research:

- Show the exact-candidate wholesale price and its recorded evidence status. If unavailable, retain UNKNOWN; do not hide already captured comparable OEM prices behind that label. Append them separately as indicative alternative-sourcing evidence, not the exact candidate's cost or quality proof.
- Preserve each offer's supplier/source ID, product/specification match, unit/pack basis, MOQ/price tier, original currency, conversion source/date and shipping/tax inclusions or exclusions in the existing supplier records and concise Notes. Combine prices into a range only on a sufficiently comparable specification, quantity and cost basis; otherwise list offers separately.
- Keep source limitations visible in the cell: an inspected supplier-advertised price is not a confirmed quotation, and an inaccessible or snippet-only offer remains UNVERIFIED. Do not upgrade evidence during export.
- Exclude retail reference prices, illustrative target buying prices and calculated break-even ceilings from supplier-cost amounts. Keep affordability targets separately labelled in the economics/Notes. Indicative prices do not establish actual landed cost, profitability or SAMPLE readiness; all existing identity and decision gates remain unchanged.

Example structure, only when those findings exist: `Exact-model wholesale: UNKNOWN. Comparable OEM: USD [LOW]-[HIGH] [source IDs] - [recorded evidence status]; quotation pending.` If no usable comparable price was captured, report UNKNOWN with the actual gap instead of inventing a range. Do not populate a numerical cost input with this text or a convenient range endpoint; any scenario must retain its stated product/offer and input basis.

Keep Notes at 180-240 words, maximum 280, using these labels in order:
PRODUCT; EVIDENCE; ECONOMICS; DEMAND / SCORE; PROMISING; RISKS;
COLLECT; DECISION / NEXT. Include exact variant/match, the strongest
GCC/supplier/creative facts, financial basis, qualitative traction/facts/GCC scope/UAE validation,
commercial points with the /80 denominator, evidence/overall confidence and core coverage, up to three promising
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
- Latest validated research-state file or complete portable Prompt 2 stage/source records (the dossier), final decision and vertical table. Reopen the saved record before handoff; stage labels alone are insufficient.
- Horizontal update row.
- Supplier shortlist and unanswered supplier questions.
- Economic assumptions and break-even CAC/ROAS.
- Qualitative public-market traction/facts/scope and evidence confidence; four-dimension commercial points out of 80; UAE validation dependencies, separate creative assessment, core coverage and overall confidence.
- Rejection-gate status.
- Product-specific sample pass/fail criteria.

Prompt 3 may return **GO FOR CONTROLLED PILOT**, **FIX AND RETEST**, or
**NO-GO**. It must not be treated as permission for unrestricted
inventory purchasing.

## Research integrity

- Use current sources and report the date checked.
- Missing access is not negative evidence. Preserve it as a visible gap,
  apply the current sample-stage rules and never invent evidence or upgrade scores to manufacture a YES.
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

For a new run, begin P2-1 only for the supplied product. Load any supplied upstream research state while preserving its registry/history, apply the identity gate, publish the intake/claim audit and actual source records, then return the checked state version or portable export with the checkpoint. Ask whether to continue to P2-2 and wait for the user's reply. For an explicit resume, reopen the supplied state and execute only its recorded outstanding stage; do not restart P2-1 or infer a missing final decision from memory.
