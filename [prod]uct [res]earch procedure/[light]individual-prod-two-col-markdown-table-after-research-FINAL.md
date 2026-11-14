# Prompt 2: Individual Product Deep Research and Sheet Update

## Purpose

Use this prompt for one product at a time after Prompt 1 classifies the product as **YES**. A **MAYBE** product may be researched only when the user explicitly promotes it.

Prompt 2 must challenge the original screening result. A Prompt 1 YES means the product deserves investigation; it does not prove demand, supplier quality, profitability, or readiness to purchase.

Preserve the original Product ID, product name, URLs, Prompt 1 row, decision, and unresolved question. Do not silently replace the original screening record.

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

## Required input

Collect or confirm:

- Product ID, for example `P-007`.
- Original Prompt 1 row.
- Product name and variant.
- Original competitor, supplier, and UGC links.
- Target GCC country or countries.
- Sales channel.
- Fulfilment model.
- Testing budget and target selling price.
- The main question that caused Prompt 1 to classify the product as YES.

State assumptions when inputs are missing.

## Research tasks

### 1. Recheck the original claim

For every important Prompt 1 claim, mark it:

- **Confirmed** with a current direct source.
- **Changed** because the current evidence differs.
- **Indirect** because it only applies to a similar product or category.
- **Unverified** because evidence could not be found.

Explain whether the original YES decision became stronger, weaker, or uncertain.

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

### 3. Supplier deep research

Find at least three supplier leads when practical. For each supplier, record:

- Direct product URL and supplier name.
- Exact match, comparable match, discovery lead, or not found.
- Product material, dimensions, weight, variant, and included accessories.
- Unit price, price breaks, MOQ, and sample availability.
- Supplier history and transaction evidence.
- Production time and handling time.
- Shipping options to the target country.
- Incoterm, estimated delivery time, and tracking.
- Packaging, customization, and documentation.
- Warranty, defect, replacement, and after-sales terms.

Compare competitor specifications against supplier specifications field by field. Mark each field **match**, **difference**, or **unknown**.

### 4. UGC and demand research

Research relevant TikTok, Instagram Reels, Snapchat Spotlight, YouTube Shorts, TikTok Creative Center, Google Trends, marketplaces, and local creator sources.

### Search-Interest Research Protocol

Search interest is a separate demand-evidence component. Do not rely exclusively on Google Trends.

For each target GCC country, prioritize Saudi Arabia and UAE, then investigate other GCC countries where evidence is available.

Build a search-query set covering:

1. Exact product name and model.
2. Common product synonyms and alternative names.
3. Product category and subcategory.
4. Customer problem and use-case searches.
5. Product features and benefit-related searches.
6. Arabic equivalents and commonly used transliterations.

Use the following sources:

**A. Google Trends**
- Check country-specific interest rather than global interest.
- Use the latest 12 months to assess recent direction.
- Use a five-year view when seasonality or long-term movement matters.
- Compare exact product terms, synonyms, category terms and problem-related terms.
- Record rising, stable, declining, seasonal or insufficient-data signals.
- Treat Trends as relative search interest, never as absolute search volume or sales.

**B. Google Search**
- Check actual country-relevant search results.
- Identify commercial, transactional and informational search intent.
- Observe recurring retailers, product listings, competitors and buying-related results.
- Record relevant search queries and their country relevance.
- Do not interpret the number of search results as search volume.

**C. Google Autocomplete and Related Searches**
- Record suggested product searches, alternative names, problem-related phrases and purchase-intent wording.
- Check English and Arabic queries where possible.
- Treat suggestions as qualitative evidence of search behaviour, not proof of search volume or sales.

**D. Keyword Research Tools**
- Use Google Keyword Planner or another credible keyword research source when accessible.
- Capture country-specific monthly search volume, CPC, competition and language.
- Record the tool, date checked and available measurement period.
- Never invent missing keyword volumes or use global estimates as GCC-specific data.
- Treat CPC and keyword competition as supporting indicators of advertiser activity and the paid-search environment, not as direct proof of product sales, conversion rates, or customer demand.

**E. Google Shopping**
- Check product availability, merchant listings, visible prices, bundles and competing offers.
- Classify Google Shopping evidence under Marketplace evidence (40%), not Search Interest (30%).
- Do not double-count the same listing as independent search-demand evidence.

### Search-Interest Interpretation Rules

- Search for the exact product as well as its category, synonyms and underlying customer problem.
- Keep exact-product, similar-product, category-level and problem-level evidence separate.
- Low Google Trends interest for an exact product name does not automatically mean low customer demand.
- If exact-product search interest is weak, investigate whether customers search for the product using different names or search for the problem it solves.
- Do not present category-level interest as proof of exact-product demand.
- If Google Trends reports insufficient data, record `INSUFFICIENT DATA`, not a zero-demand score.
- Use multiple independent search sources where accessible. If only one usable source is available, score conservatively and disclose the limitation.
- If no usable country-specific search evidence is available, record `NOT CAPTURED` and mark the Demand Index `INCOMPLETE`.

For every search finding, preserve the query, language, country, source URL, date checked, measurement period, evidence type and actual finding.

A weak search-interest signal must be considered alongside marketplace demand and social traction. It must not independently trigger a product rejection.

Classify every source as:

1. Exact product or exact SKU.
2. Similar product with a similar benefit.
3. Category-level evidence.
4. General trend evidence.

Record direct links, country, date, views, likes, comments, shares, creator, hook, demonstration, and organic or paid signal when visible.

Calculate engagement only when all fields exist:

`(likes + comments + shares) / views * 100`

For the candidate, create three hooks, three demonstrations, one objection-handling idea, one Arabic-friendly angle, and one English-friendly angle. Treat creative potential separately from evidence of demand.

### Demand Index

When the evidence supports all three components, calculate a Demand Index out of 100:

| Component | Weight |
|---|---:|
| Marketplace evidence | 40 |
| Search interest | 30 |
| Social traction | 30 |

Score each component from 0 to 100 and explain the score. Use Google Trends as relative search interest, not as sales volume. If a component is missing, mark the Demand Index **INCOMPLETE** and do not silently redistribute the weights.

Use these scoring anchors unless the evidence justifies a different explanation:

| Score | General interpretation |
|---:|---|
| 0 | No credible evidence |
| 25 | Weak, isolated, indirect, or outdated evidence |
| 50 | Some relevant evidence, but limited or mixed |
| 75 | Multiple consistent and relevant signals |
| 100 | Strong, current, direct evidence from multiple independent sources |

Explain the evidence behind each component score. Do not assign a high score merely because the product has creative potential.

Calculate the Demand Index as:

`Demand Index = (Marketplace Score * 0.40) + (Search Interest Score * 0.30) + (Social Traction Score * 0.30)`

All component scores must be between 0 and 100. If any component is missing, keep the Demand Index **INCOMPLETE**. When multiple GCC countries are targeted, calculate country-specific Demand Indices where sufficient evidence exists. Do not combine country evidence in a way that hides differences between markets.

### 5. Unit economics

Model conservative, base, and optimistic scenarios. State every assumption.

```text
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

Show original currency, exchange-rate source and date, VAT treatment, shipping payer, discounts, and unknown costs. Never call gross spread or markup net profit.

### VAT and revenue basis

State the target country's VAT rate, whether the seller is VAT-registered, and whether the customer-facing selling price includes VAT.

- Show customer-facing price including VAT separately.
- For contribution analysis, use revenue excluding output VAT when the seller is required to collect VAT.
- Treat recoverable input VAT as a cash-flow item rather than a permanent product cost when the seller can legally recover it.
- Include non-recoverable import VAT, customs duty, brokerage, and other taxes as costs where applicable.
- Confirm whether platform, payment, BNPL, and advertising fees are calculated on the VAT-inclusive or VAT-exclusive amount.
- Use the same revenue basis when calculating break-even CAC and break-even ROAS.

If the seller's VAT status or the fee basis is unknown, show both the assumption and the sensitivity rather than presenting one precise profit number.

For break-even ROAS, state whether the advertising platform reports conversion revenue including or excluding VAT, shipping, discounts, refunds, and other adjustments. Use the same reported-revenue definition in the ROAS formula and the pilot result.

For order-level economics, multiply product and per-unit packaging costs by the actual quantity in the order. Account for bundles and multipacks, use average order value when appropriate, and calculate CAC per acquired order. Compare order-level CAC with order-level contribution before advertising. Avoid double-counting any landed-cost component.

Calculate one expected failed-delivery and reverse-logistics cost per order using the probability of failure and the applicable return-to-origin, reverse-shipping, refused-delivery, and handling charges. Include separate components only when they represent genuinely different costs. Keep payment collection fees separate.

Use this explicit basis: `expected failed-delivery cost = probability of failure x loss per failed order`. Show the probability and the applicable loss components before including the result in contribution.

### 6. Compliance, fulfilment, and rejection gates

Evaluate:

- Safety and compliance.
- Exact product match.
- Base-case economics.
- GCC shipping and delivery.
- Returns and customer support.
- Sample quality, marked **PENDING** until Prompt 3 tests it.

Use **PASS**, **FAIL**, or **PENDING**. A critical FAIL overrides a high score. PENDING means the candidate may be eligible for a sample only if the missing evidence is specifically identified.

### 7. Score and decision

Use the deep-research score only after the evidence threshold is met.

Assess these six evidence dimensions:

1. GCC demand.
2. Competitor landscape.
3. Supplier feasibility.
4. UGC evidence.
5. Unit economics.
6. Safety, compliance, and fulfilment.

For each dimension, record the evidence available, source quality, date checked, exact-product or category relevance, missing information, and whether the evidence is sufficient for a decision.

Calculate evidence coverage as:

`evidence coverage = adequately supported required evidence items / total applicable required evidence items * 100`

Do not count unsupported assumptions as completed evidence. If coverage is below the minimum needed for a defensible decision, return **RESEARCH MORE** and label the score as a screening score.

Use **80% evidence coverage as the default minimum**, with all six dimensions assessed and no critical safety, supplier-match, fulfilment, or economics gap left unlabelled. Lower or higher thresholds may be used only when the reason is stated.

Use this minimum evidence checklist and count each applicable requirement once:

| Evidence dimension | Required items to count |
|---|---|
| GCC marketplace evidence (GCC demand sub-requirement) | Current country-specific marketplace listings, visible demand signals, and customer feedback. Google Shopping belongs here and must not be double-counted as search-interest evidence. |
| Search-interest evidence (GCC demand sub-requirement) | Country-specific Google Trends, Google Search, Autocomplete/Related Searches, or keyword research; distinguish exact-product, category, and problem-level evidence. |
| Social traction evidence (GCC demand sub-requirement) | Relevant country-specific creator/content activity, audience response, engagement, and evidence freshness. |
| Country relevance (GCC demand sub-requirement) | Record which target GCC country each marketplace, search, and social signal actually supports; do not assume evidence transfers across countries. |
| Competitor landscape | Three meaningful comparisons when available, price, offer/specification, reviews or complaints, delivery/return signal |
| Supplier feasibility | Direct supplier, exact-match comparison, MOQ/unit price, shipping/lead-time signal, supplier evidence |
| UGC evidence | Three relevant references when available, evidence type, creative pattern, metrics or explicitly missing metrics |
| Unit economics | Product cost, inbound shipping, duties/taxes, fees, fulfilment/packaging, returns, CAC assumption |
| Safety/compliance/fulfilment | Applicable documents or restrictions, product risk, delivery feasibility, returns/support risk |

If an item is genuinely not applicable, mark it `N/A` with a reason and exclude it from the denominator. If it is relevant but unavailable, count it as missing. Keep evidence quality and freshness as separate fields; they do not replace coverage.

Evidence coverage measures research completeness across six top-level evidence dimensions. The GCC demand dimension contains four separately counted checklist sub-requirements (marketplace, search interest, social traction, and country relevance); these roll up to one GCC demand dimension and do not create additional commercial-score dimensions. The commercial score measures business attractiveness across five weighted dimensions. They are separate measures. Safety and compliance remain non-compensatory rejection gates, and fulfilment feasibility is represented within supplier and execution feasibility. A high commercial score must never override a critical safety or compliance failure.

| Dimension | Weight |
|---|---:|
| GCC market demand | 25 |
| UGC creative potential | 20 |
| Unit economics | 25 |
| Competition and differentiation | 10 |
| Supplier and execution feasibility | 20 |
| Total | 100 |

Rate each dimension from 0 to 5 and calculate:

`weighted points = (rating / 5) * dimension weight`

The commercial score supports comparison and prioritization. It does not independently determine SAMPLE, RESEARCH MORE, HOLD, or DROP. Apply the evidence threshold, financial criteria, and critical rejection gates when making the final decision.

Keep confidence separate:

- A: strong, current, product-specific GCC evidence.
- B: reasonably supported with some indirect or missing evidence.
- C: weak, old, category-level, or mostly inferred evidence.

Use these Prompt 2 decisions:

- **SAMPLE:** evidence threshold met, no critical gate fails, and the base-case contribution is positive enough to justify a sample.
- **RESEARCH MORE:** an important uncertainty can still change the decision.
- **HOLD:** interesting but not suitable for the current budget, timing, market, or channel.
- **DROP:** evidence or a critical gate makes the current candidate unsuitable.

Do not use GO at this stage. GO belongs to Prompt 3 after physical sample validation and means approval for a controlled pilot only.

## Output A: individual research dossier

Produce a detailed report with these sections:

1. Product ID and original Prompt 1 decision.
2. Executive decision and one-sentence reason.
3. Original claim audit: confirmed, changed, indirect, and unverified findings.
4. Target customer, problem, and positioning opportunity.
5. GCC marketplace and competitor evidence.
6. Supplier comparison and exact-match analysis.
7. UGC and demand evidence.
8. Creative hooks and demonstration concepts.
9. Conservative, base, and optimistic unit economics.
10. Confidence grade and evidence coverage.
11. PASS, FAIL, or PENDING rejection gates.
12. Risks and missing evidence.
13. Prompt 2 decision: SAMPLE, RESEARCH MORE, HOLD, or DROP.
14. Next action, owner, evidence required, and deadline.

Every material claim needs a direct source, research date, and evidence label: Verified, Estimate, Inference, or Unknown.

## Output B: vertical two-column export

After the dossier, produce exactly one table for the individual product:

| Column | Information to enter |
|---|---|
| Product ID / Name | Stable ID, complete product name, and meaningful variant or pack size |
| Category | Relevant category and subcategory |
| Original Prompt 1 Decision | YES or MAYBE, with the original screening date |
| Competitor/Product Link | Direct GCC competitor links, country, marketplace, and date checked |
| Supplier Link | Direct supplier links, exact-match status, and date checked |
| Product Cost (USD) | Unit price, MOQ, price break, original currency, and whether shipping is excluded |
| Competitor Selling Price (USD) | Current price, original currency, bundle size, conversion rate, and conversion date |
| UGC Video/Post Link | Direct UGC links with evidence type: exact, similar, category, or trend |
| UGC Views / Engagement | Metrics, engagement rate when calculable, sample size, and missing fields |
| Trend / Demand | Marketplace, search, and social evidence; Demand Index status |
| Research Decision | SAMPLE, RESEARCH MORE, HOLD, or DROP |
| Notes | Compact summary using the labels below |

Use these Notes labels:

`**PRODUCT:**` problem, buyer, specifications, and exact-match status.

`**MARKETPLACE:**` competitors, prices, ratings, reviews, delivery, and complaints.

`**SUPPLIER:**` supplier, MOQ, price, match status, shipping, and missing documents.

`**UGC:**` evidence type, hooks, demonstrations, metrics, sample size, and licensing.

`**ECONOMICS:**` landed-cost status, contribution, CAC assumption, break-even CAC/ROAS, and unknowns.

`**DEMAND:**` marketplace, search, social direction, and Demand Index status.

`**SCORE:**` final score, confidence grade, evidence coverage, and reason.

`**GATES:**` safety, exact match, economics, sample quality, fulfilment, and returns as PASS, FAIL, or PENDING.

`**RISKS:**` unresolved quality, compliance, delivery, return, competition, and creative risks.

`**NEXT ACTION:**` SAMPLE, RESEARCH MORE, HOLD, or DROP with owner, evidence, and deadline.

## Output C: horizontal update row for the original sheet

Also provide one horizontal Markdown row using the original 11-column sheet format:

```text
| Product Name | Category | Competitor/Product Link | Supplier Link | Product Cost (USD) | Competitor Selling Price (USD) | UGC Video/Post Link | UGC Views / Engagement | Trend / Demand | Research Decision | Notes |
|---|---|---|---|---:|---:|---|---|---|---|---|
| P-000 - Product name |  |  |  |  |  |  |  | SAMPLE / RESEARCH MORE / HOLD / DROP |  |
```

Use the same Product ID and sources as the dossier. The horizontal row is the compact update for the original 25-product sheet; the vertical table and dossier preserve the deeper research.

## Handoff to Prompt 3

Only a product with the Prompt 2 decision **SAMPLE** can enter:

[Stage-3-Supplier-and-Sample-Validation.md](Stage-3-Supplier-and-Sample-Validation.md)

Pass forward:

- Product ID and original Prompt 1 row.
- Prompt 2 dossier and vertical table.
- Horizontal update row.
- Supplier shortlist and unanswered supplier questions.
- Economic assumptions and break-even CAC/ROAS.
- Rejection-gate status.
- Product-specific sample pass/fail criteria.

Prompt 3 may return **GO FOR CONTROLLED PILOT**, **FIX AND RETEST**, or **NO-GO**. It must not be treated as permission for unrestricted inventory purchasing.

## Research integrity

- Use current sources and report the date checked.
- Never invent prices, sales counts, supplier facts, shipping quotes, UGC metrics, certifications, or links.
- Separate exact-product, similar-product, category, and trend evidence.
- State conflicting evidence instead of averaging it away.
- Treat missing sample evidence as PENDING.
- Do not recommend inventory from supplier photos alone.
- Keep the original Prompt 1 decision visible so the deeper research can be audited.
