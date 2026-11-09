# Prompt 1B: GCC Product Full Screening and Decision Completion

## Purpose

Use this prompt after Prompt 1A has discovered products and prepared the five-candidate handoff pack.

Prompt 1B performs the original master-prompt screening workflow for all five selected products. It uses the handoff from Prompt 1A instead of asking the user for a new candidate list.

The individual-product prompt remains separate and untouched. Prompt 1B produces the compact Prompt 1 screening table and decision summary. A product classified YES can later enter the individual-product deep-research prompt.

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

## Required input from Prompt 1A

Paste the complete output from:

`GCC-UGC-Prompt-1A-Discovery-and-Screening-Preparation.md`

The handoff must contain:

- Raw discovery log.
- Channel execution report.
- Five-candidate handoff table.
- Compact preparation brief for each selected product.
- Direct source links and their verification status.
- Preparation Priority Score.
- Risks and unresolved questions.
- Handoff checkpoint.

Treat the five selected Product IDs as fixed. Do not restart discovery, replace candidates, or assign duplicate IDs.

If a handoff field is missing, record the gap first and research it where possible. Never invent product names, URLs, prices, metrics, dates, or specifications.

## Execution control

- Execute only the full screening of the five fixed candidates in this prompt.
- Reuse verified handoff sources and do not repeat the same research unnecessarily.
- Preserve all Product IDs, source links, decisions, and unresolved questions.
- Complete a minimum evidence pass for all five products before deepening any one product. Do not let one difficult candidate consume the whole response.
- For each product, stop once the evidence is sufficient for a defensible decision. Research beyond the minimum only to resolve a conflict or a decision-changing gap.
- If the response is approaching its limit, stop after the last completed Product ID and provide a compact checkpoint listing completed IDs, remaining IDs, and the next action. Resume from that checkpoint without restarting completed products.

## Fixed response and output control

- Target 1,800-2,400 words, excluding URLs and compact table cells.
- Produce only the cumulative 11-column table and the decision summary. Do not create a separate mini-report for any product.
- Keep each product's Notes cell concise, normally no more than 80-120 words.
- Use the strongest relevant evidence rather than repeating every source discovered.
- Do not add unsolicited sections, introductions, conclusions, repeated URLs, creative scripts, full supplier audits, or Prompt 2 calculations.
- If the full screen cannot fit, complete the current product, save the checkpoint, and state exactly what remains. Never invent evidence or silently omit a product.

## Research market

Focus on all six GCC countries:

1. Saudi Arabia (KSA)
2. United Arab Emirates (UAE)
3. Kuwait
4. Qatar
5. Bahrain
6. Oman

Prioritize KSA and UAE for the first screening pass, then use other GCC evidence where available. Do not force a separate full-country investigation when no relevant evidence is accessible. Demand in one GCC country is not proof of demand in all GCC countries.

Check relevant local currency, price expectations, climate, lifestyle, seasonality, Arabic and English search language, delivery expectations, returns, COD, payment methods, BNPL, VAT, customs, product restrictions, and local fulfilment.

## Screening standard

Screen all five selected products using the same requirements. Keep every important statement labelled as:

- **Verified:** directly supported by a current source.
- **Estimate:** calculated from stated assumptions.
- **Inference:** a reasoned interpretation of evidence.
- **Unknown:** not yet verified.

Do not perform Prompt 2's detailed supplier validation, sample testing, final profitability approval, or full deep-research dossier here. Those remain in `individual-prod-two-col-markdown-table-after-research.md` after a product receives YES or is explicitly promoted.

## Research tasks for each selected product

### A. Problem and product fit

Investigate:

- Customer problem, desire, inconvenience, or purchase occasion.
- Whether the benefit is understandable in one sentence.
- Whether a creator can demonstrate the product in a short video.
- Whether the product fits the target GCC customer and channel.

### B. GCC market evidence

Check relevant marketplaces, retailers, search signals, and social platforms. Prefer direct KSA and UAE evidence when available.

Capture:

- Direct comparable listing URLs.
- Current visible price and original currency.
- Ratings, review counts, sales indicators, or rankings when disclosed.
- Delivery and return signals.
- Demand evidence across more than one independent source.
- Recurring complaints or obvious market weaknesses.
- Exact-product, category-level, and general-trend evidence separately.

Marketplace badges are directional unless the platform discloses the measurement period. Do not convert review counts into invented sales counts.

For USD spreadsheet fields, convert supplier costs and competitor prices using a reliable exchange-rate source. Record original currency, original amount, exchange-rate source, conversion date, and USD equivalent in Notes. Never invent or silently estimate an exchange rate.

### C. Initial supplier and sourcing signal

Find at least one supplier lead when possible. Record:

- Direct supplier URL.
- Supplier name.
- Visible unit price and MOQ.
- Product specification and apparent match level.
- Sample availability when visible.
- Shipping or fulfilment signal.
- Compliance or safety concern.

Label the supplier **exact match**, **comparable**, **discovery lead**, or **not found**. A category or search page is a discovery lead, not a verified supplier.

### D. UGC and creative signal

Check TikTok, Instagram Reels, Snapchat Spotlight, YouTube Shorts, TikTok Creative Center, and relevant creator sources where available.

Separate:

1. Exact product or exact SKU evidence.
2. Same product type with a similar benefit.
3. Category-level content.
4. General trend evidence.

Record direct URLs, views, likes, comments, shares, creator market, hook, demonstration, and date checked when available. Calculate engagement only when all required numbers exist:

`(likes + comments + shares) / views * 100`

Do not classify a product as YES because of one viral video.

### E. Preliminary economics

Use visible information to estimate commercial plausibility:

```text
Preliminary product spread = competitor selling price - visible supplier product cost
```

Label this as a preliminary spread, not profit. Note unknown shipping, duties, taxes, fees, fulfilment, returns, packaging, and advertising costs. Do not reject a product only because Prompt 1 lacks costs that Prompt 2 can verify, unless visible evidence already shows clearly impossible economics.

### F. Initial safety and risk check

Flag products that appear counterfeit, unsafe, heavily regulated, medically claimed, restricted, fragile, difficult to fulfil, or unsuitable for a clear UGC demonstration.

Do not make legal or compliance claims without a source. Mark documentation issues **PENDING VERIFICATION**.

## Direct-link and UGC verification gate

Before including evidence in the final table:

1. Open the actual destination.
2. Confirm that it loads.
3. Confirm that it matches the product and claim.
4. Record country, platform, publication date when available, and date checked.
5. Mark inaccessible or mismatched links `NOT VERIFIED`.

Never use a homepage, category page, search-result page, generic bestseller page, or official product page as a substitute for the exact product, supplier, or creator content being discussed.

For each shortlisted product, find at least two relevant positive creator demonstrations when available. If this cannot be verified, record the gap and do not award YES solely because marketplace demand is strong.

Classify UGC as exact product, similar product, category-level, general trend, negative experience, or safety complaint. Mark content older than 12 months `HISTORICAL`. Do not use safety complaints, product failures, injuries, fires, or negative experiences as positive UGC evidence.

If a metric is unavailable, state `NOT CAPTURED`. If a URL is inaccessible, state `NOT VERIFIED`. Never invent URLs, views, dates, creators, engagement, sales, or specifications.

## Evidence rules

Prefer evidence in this order:

1. Official manufacturer, regulator, marketplace, or platform source.
2. Direct product listing with visible product information.
3. Direct supplier listing.
4. Direct creator post or official creative library entry.
5. Search snippets or secondary pages as discovery leads only.

For each important finding, record source URL, source type, country, date checked, exact-product or category relevance, and what the source proves.

## Screening decisions

### YES: advance to Prompt 2

Classify YES when the product has:

- A clear customer problem or desire.
- At least two independent GCC demand signals when available, preferably from different source types. If only one weak or indirect signal is available, keep the product MAYBE unless the exception is explained.
- At least two relevant positive creator demonstrations when available, or a documented reason to keep it MAYBE instead.
- At least one directly accessible supplier lead with match status recorded.
- No visible critical safety or compliance blocker.
- Preliminary economics that are not obviously impossible.
- Enough evidence to justify individual deep research.

Write the exact reason for YES and the main question Prompt 2 must verify.

### MAYBE: keep in the review queue

Classify MAYBE when the product has a promising signal but important evidence is missing, conflicting, indirect, seasonal, or too weak for YES.

Write what looks promising, what is missing, the specific check that could change the decision, and whether it should later be promoted to Prompt 2.

### NO: do not advance

Classify NO when evidence shows:

- No recognizable customer need or usable positioning.
- Weak or contradictory market evidence with no credible angle.
- No feasible supplier or impossible fulfilment signal.
- Clearly negative preliminary economics.
- Unsafe, counterfeit, restricted, or unsolvable compliance risk.
- No practical UGC demonstration.
- Severe saturation with no credible differentiation.

Write the evidence-based rejection reason. When a NO depends on economics or another measurable threshold, include the relevant number, comparison, or calculation. Do not use NO for missing evidence; use MAYBE or UNPROCESSED.

### UNPROCESSED

Use UNPROCESSED only when a source, tool, or research dependency prevents completion. Record attempted sources, exact missing work, and the next recovery action.

## Required output

Keep the output in the original master-prompt style. Do not produce five full dossiers, five vertical tables, or repeated creative strategies.

### Output A: cumulative 11-column table

After screening all five selected products, produce one horizontal table:

| Product Name | Category | Competitor/Product Link | Supplier Link | Product Cost (USD) | Competitor Selling Price (USD) | UGC Video/Post Link | UGC Views / Engagement | Trend / Demand | Research Decision | Notes |
|---|---|---|---|---:|---:|---|---|---|---|---|
| P-001 - Product name |  |  |  |  |  |  |  |  | YES / MAYBE / NO / UNPROCESSED |  |
| P-002 - Product name |  |  |  |  |  |  |  |  | YES / MAYBE / NO / UNPROCESSED |  |
| P-003 - Product name |  |  |  |  |  |  |  |  | YES / MAYBE / NO / UNPROCESSED |  |
| P-004 - Product name |  |  |  |  |  |  |  |  | YES / MAYBE / NO / UNPROCESSED |  |
| P-005 - Product name |  |  |  |  |  |  |  |  | YES / MAYBE / NO / UNPROCESSED |  |

Use exactly these 11 columns. Preserve direct URLs and use `NOT VERIFIED`, `DISCOVERY LEAD`, `NOT CAPTURED`, `HISTORICAL`, `Pending verification`, or `UNPROCESSED: reason` where necessary.

Keep Notes concise using the following labels. Use one short sentence per label and omit a label only when it is genuinely not applicable:

`**PROBLEM:**` customer problem and buyer.

`**MARKET:**` countries, price, reviews, sales indicators, and date.

`**SUPPLIER LEAD:**` supplier, MOQ, price, match level, and missing details.

`**UGC:**` evidence type, direct links, freshness, hooks, and captured metrics.

`**ECONOMICS:**` preliminary spread and unknown costs.

`**RISKS:**` safety, compliance, fulfilment, competition, or quality concerns.

`**NEXT CHECK:**` the exact Prompt 2 question for YES or MAYBE products.

### Output B: decision summary

After the table, provide:

- Total products received from Prompt 1A.
- Total processed.
- Total YES.
- Total MAYBE.
- Total NO.
- Total UNPROCESSED, with reasons.
- Product IDs classified YES, MAYBE, and NO.
- Main evidence pattern behind the decisions.
- Prompt 2 handoff list for every YES product.

Do not cap the YES list or force category diversity. The five products were selected by Prompt 1A; this screen decides each product independently.

## Prompt 2 handoff

For every YES product, preserve:

- Product ID.
- The completed 11-column row.
- Original product, competitor, supplier, and UGC links.
- The unresolved verification question.

These are the inputs for `individual-prod-two-col-markdown-table-after-research.md`.

A Prompt 1B YES means the product deserves individual deep research. It is not permission to purchase.

## Teaching mode

Keep explanation concise. Briefly state what was checked, why the evidence matters, what remains unknown, and why each product received its decision. Do not duplicate the entire research record below the table.

## Start instruction

Read the complete Prompt 1A handoff pack. Confirm the five fixed Product IDs. Fully screen all five products using this prompt, preserve direct evidence, and produce the compact 11-column table and decision summary. Do not ask the user for a new candidate list. Do not use the individual-product prompt's detailed dossier format at this stage.
