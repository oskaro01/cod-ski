# Prompt 1A: GCC Product Discovery and Full-Screening Preparation

## Purpose

Discover promising physical ecommerce products for GCC markets and prepare a compact handoff pack for Prompt 1B.

This prompt stops before full product screening. It does not make the final YES, MAYBE, or NO decision. It selects five candidates and records the source links, basic market signals, supplier leads, UGC leads, economics inputs, risks, and unresolved questions that Prompt 1B needs to begin the full screen.

The research agent is responsible for discovery, crawling, source collection, URL checking, deduplication, and preparation of the handoff pack. Do not depend on a product list supplied by the user. User ideas may be used as optional seeds, but they must not replace autonomous discovery.

## Execution control

- Execute only discovery and handoff preparation in this prompt.
- Keep the final handoff compact and do not repeat the same source or finding in multiple sections.
- Preserve every completed Discovery ID and Product ID. Never restart a completed batch or assign a duplicate ID.
- If the response is approaching its limit, stop after the last completed research unit and emit a compact checkpoint listing completed IDs, remaining work, and the next action. Do not silently skip unfinished candidates.

## Fixed response and output control

- Target 1,200-1,500 words, excluding URLs and compact table cells.
- Use short factual statements and tables. Do not expand the report beyond the required content.
- Use these sections in order: discovery summary, eight-channel coverage ledger, raw discovery log, final selected products, and handoff checkpoint.
- Represent the shortlist through `SHORTLISTED` rows in the raw discovery log. Do not create a second shortlist table.
- Keep each selected-product explanation to 80-100 words maximum, excluding its links and table row.
- Do not repeat identical URLs or add unsolicited sections, commentary, introductions, or conclusions after the checkpoint.
- If the required work cannot fit, complete the current research unit, save the checkpoint, and state exactly what remains. Never invent findings or silently omit required work.

## Operating assumptions

Use these assumptions unless the user gives a more specific brief:

- Market: all six GCC countries, with Saudi Arabia and the UAE as priority validation markets.
- Channel: Shopify or similar DTC supported by social content and paid social; compare Noon, Amazon, TikTok Shop, and local retailers where relevant.
- Product scope: physical consumer products with a clear problem, demonstrable benefit, plausible sourcing, and practical GCC fulfilment.
- Price, testing budget, and final fulfilment model: unknown at this stage. Record visible evidence and assumptions without inventing final economics.
- Exclude counterfeit goods, unsafe products, unsupported medical claims, illegal goods, weapons, heavily regulated products, and products with no practical demonstration or fulfilment path.

## Discovery funnel

For each discovery batch:

1. Discover a target of 12-16 raw product opportunities.
2. Remove duplicates, superficial variants, inaccessible dead ends, and unsupported entries.
3. Shortlist approximately 7 opportunities.
4. Select the five strongest opportunities using the preparation score and evidence quality.
5. Prepare the complete handoff pack for those five.
6. Stop as soon as five candidates meet the minimum handoff evidence. Do not continue browsing only to fill a quota.
7. Do not perform the full screening in this prompt.

These are targets, not permission to invent findings. If evidence cannot support the target, report the shortfall.

## Preparation output boundary

Prompt 1A collects research inputs. Prompt 1B performs the detailed analysis.

For each selected candidate, keep the preparation brief concise: no more than 80-100 words, excluding URLs and tables. Use one line per source and one line per finding. Do not write a full competitor comparison, full supplier audit, detailed unit-economics model, creative strategy, or final decision in Prompt 1A.

The handoff must preserve enough information for Prompt 1B to start efficiently, but Prompt 1B must reopen, verify, compare, and challenge the evidence.

Use stable IDs:

- Raw discovery ID: `D-B01-001`.
- Selected candidate ID: `P-001`.

Do not cap the number of candidates selected across the project. The five selected in this batch are the five that receive the Prompt 1B screen.

## Discovery channels

Give all eight channels a light discovery pass where accessible. Use the four primary channels for the main search and use the four supporting channels for additional leads or gap resolution. Do not assign product quotas to channels or categories. Selection is based on evidence.

1. **Primary: Marketplace and retail intelligence:** Amazon.sa, Amazon.ae, Noon, Carrefour, Lulu, Mumzworld, SACO, Jarir, Sharaf DG, Xcite, Amazon US/UK/EU, Walmart, eBay, AliExpress, and Etsy where relevant. Search current listings, product variations, reviews, complaints, rankings, price signals, and products with limited GCC availability.
2. **Primary: Organic social and creator discovery:** TikTok, Instagram Reels, YouTube Shorts, Snapchat Spotlight, Pinterest, Reddit, and public Facebook communities. Search English, Arabic, transliterated Arabic, product, problem, feature, and use-case terms.
3. **Supporting: Advertising intelligence:** Meta Ads Library, TikTok Creative Center, Google Ads Transparency Center, and public competitor advertising. Use a light pass to identify repeated advertisers or useful creative-market evidence.
4. **Primary: Search demand and trend intelligence:** Google Trends, Google Search, Google Shopping, autocomplete, and public keyword tools. Record country, language, seasonality, related queries, and purchase-intent signals.
5. **Supporting: Customer pain points and market gaps:** public discussions, reviews, Q&A sections, complaint threads, and community feedback. Use a light pass when the product problem or market weakness is unclear.
6. **Primary: Global supplier and sourcing intelligence:** Alibaba, Global Sources, Made-in-China, DHgate, manufacturer websites, and wholesale catalogues. Record one practical supplier lead, visible specifications, MOQ, price, and sample signals.
7. **Supporting: Independent ecommerce and DTC discovery:** Shopify stores, niche stores, emerging brands, regional ecommerce, Google Shopping merchants, product bundles, and subscriptions. Treat attractive storefronts as leads, not proof of sales.
8. **Supporting: Innovation and emerging products:** Kickstarter, Indiegogo, manufacturer launches, trade-show catalogues, innovation publications, and public demonstrations. Use a light pass when the product is genuinely emerging or primary channels do not reveal enough variety.

Explore multiple categories during discovery, but do not use category diversity as a selection quota. If the strongest five belong to one category, select them when their evidence supports them.

## Preparation priority score

Use this score only for the approximately seven shortlisted opportunities to choose which receive the Prompt 1B full screen. It is not a final commercial approval score.

| Dimension | Weight |
|---|---:|
| Demand across independent sources | 25 |
| Problem and product appeal | 15 |
| UGC demonstration potential | 15 |
| Preliminary economics | 15 |
| Competition and differentiation | 10 |
| Supplier availability | 10 |
| GCC fulfilment and compliance potential | 10 |
| Total | 100 |

Calculate:

`Preparation Priority Score = sum of (dimension score x weight / 100)`

Rate each dimension from 0 to 100 using these anchors:

| Score | Meaning |
|---:|---|
| 0 | No credible evidence or the dimension is contradicted |
| 25 | Weak, isolated, indirect, or outdated evidence |
| 50 | Some relevant evidence, but limited or mixed |
| 75 | Multiple consistent and relevant signals |
| 100 | Strong, current, direct evidence from multiple independent sources |

Use the evidence for that specific dimension only. Do not award points for missing information or for the discovery channel itself.
Record the evidence for every score. Discovery source and category are not scoring dimensions.

## Evidence to collect before the handoff

For every one of the five selected candidates, collect the following. This is preparation evidence, not final approval. Stop at the minimum evidence needed for the handoff; Prompt 1B will reopen and deepen the research.

### Product identity and problem

- Product name, exact variant, pack size, and visible specifications.
- One-sentence customer problem or use case.
- Target buyer and relevant GCC market.
- Product or listing URL that directly represents the candidate.
- One short exact-match note.

### Competitor and GCC market signals

- One direct competitor or comparable product URL when available; add a second only when it is immediately available and materially useful.
- Country, platform, date checked, currency, and visible price for each.
- One-line delivery, rating, review, sales, search, social, or advertising signal when visible.
- One-line market weakness or unresolved concern.

### Supplier leads

- One direct supplier product URL when available.
- Supplier name, exact or comparable match, visible unit price, MOQ, variant, and sample signal.
- One-line shipping, production, packaging, documentation, or supplier-risk signal when visible.

Do not treat a supplier category page or search page as a verified supplier listing. Mark it `DISCOVERY LEAD` until the direct product page is found.

### UGC and creator evidence

- One relevant creator demonstration when available; add a second only when it is immediately available and materially useful.
- Direct video or post URL, platform, creator, date checked, visible metrics, product identity, and evidence type.
- Classify each source as exact product, similar product, category-level, general trend, negative experience, or safety complaint.
- Mark content older than 12 months `HISTORICAL`, missing metrics `NOT CAPTURED`, and inaccessible URLs `NOT VERIFIED`.

Do not write a full UGC analysis or create hooks here. Prompt 1B will do that.

Never use fires, explosions, injuries, charging failures, product failures, or negative experiences as positive UGC evidence. Move them into risks.

### Preliminary economics inputs

Collect visible inputs only and keep them as raw inputs:

- Supplier product cost and original currency.
- Competitor selling price and original currency.
- Exchange-rate source and conversion date for USD fields.
- One-line shipping, MOQ, packaging, duty, VAT, fulfilment, and fee signals when visible.
- Unknown costs that Prompt 1B must model.

Do not calculate final contribution, break-even CAC, or break-even ROAS here. Prompt 1B performs the full unit-economic model.

### Risk and unresolved-question register

Record up to three important safety, compliance, quality, shipping, fulfilment, or differentiation flags. List the exact questions Prompt 1B must answer.

## Direct-link verification gate

Before placing a link in the handoff pack:

1. Open the destination.
2. Confirm that it loads.
3. Confirm that it matches the product or claim.
4. Record country, platform, date checked, and source type.
5. Mark inaccessible or mismatched links `NOT VERIFIED`.

Never invent or reconstruct URLs. Preserve the original direct URL when it is a user seed. For autonomous discovery, preserve the direct product or listing URL that led to selection.

## Required output

### Output A: raw discovery log

Keep each raw discovery entry to one compact line and keep the total to 12-16 rows. Record one primary source URL or source domain for raw opportunities; preserve full direct URLs and verification details for shortlisted and selected products.

| Discovery ID | Product opportunity | Category | Source URLs | Signal captured | Preparation Priority Score | Status | Reason / next action |
|---|---|---|---|---|---:|---|---|
| D-B01-001 | Example product |  |  |  |  | REJECTED / SHORTLISTED / SELECTED / DUPLICATE / UNPROCESSED |  |

### Output B: channel execution report

Keep each of the eight channel rows concise. List no more than two representative URLs per channel and write `NOT USED - inaccessible or clearly irrelevant` only when a supporting channel could not contribute useful evidence.

| Channel | Platforms searched | Query themes | Opportunities found | Relevant URLs | Findings and limitations | Inaccessible sources |
|---|---|---|---:|---|---|---|
| Marketplace and retail |  |  |  |  |  |  |
| Organic social and creators |  |  |  |  |  |  |
| Advertising intelligence |  |  |  |  |  |  |
| Search demand and trends |  |  |  |  |  |  |
| Customer pain points and gaps |  |  |  |  |  |  |
| Supplier and sourcing |  |  |  |  |  |  |
| Independent ecommerce and DTC |  |  |  |  |  |  |
| Innovation and emerging products |  |  |  |  |  |  |

### Output C: five-candidate compact handoff pack

Create one complete section for each selected product. Use `PREPARED FOR FULL SCREEN` as the status. Do not use YES, MAYBE, or NO yet.

| Product ID | Discovery ID | Product and variant | Category | Opportunity type | Priority Score | Status | Direct product URL | Competitor URLs | Supplier URL | UGC URLs | Main missing questions |
|---|---|---|---|---|---:|---|---|---|---|---|---|
| P-001 | D-B01-001 |  |  |  |  | PREPARED FOR FULL SCREEN |  |  |  |  |  |
| P-002 | D-B01-002 |  |  |  |  | PREPARED FOR FULL SCREEN |  |  |  |  |  |
| P-003 | D-B01-003 |  |  |  |  | PREPARED FOR FULL SCREEN |  |  |  |  |  |
| P-004 | D-B01-004 |  |  |  |  | PREPARED FOR FULL SCREEN |  |  |  |  |  |
| P-005 | D-B01-005 |  |  |  |  | PREPARED FOR FULL SCREEN |  |  |  |  |  |

Each selected Product ID must map to exactly one original Discovery ID. Preserve this mapping in the handoff table and checkpoint. Do not merge opportunities, reuse a Discovery ID, or create a new Product ID during handoff.

Under the table, include one compact preparation brief per product containing only: product identity and problem, direct source links, one-line market signal, one supplier lead, one competitor or comparable, one UGC lead, raw economics inputs, one key risk, and one missing question. Do not repeat full competitor analysis, supplier auditing, detailed economics, creative concepts, or final decisions. Prompt 1B performs those tasks.

### Output D: handoff checkpoint

End with this exact marker and include the full handoff pack immediately after it:

```text
GCC PRODUCT RESEARCH HANDOFF PACK
Discovery batch:
Raw opportunities discovered:
Shortlisted opportunities:
Selected Product IDs:
Current stage: PREPARED FOR FULL SCREEN
Next script: GCC-UGC-Prompt-1B-Full-Screening-and-Decision-Completion.md
Do not perform full screening in Prompt 1A.
```

The handoff pack must be self-contained. Prompt 1B must be able to continue from it without the original discovery response.

## Start instruction

Begin autonomous discovery for one batch. Give all eight channels a light pass where accessible, discover 12-16 raw opportunities, shortlist approximately 7, and select five by evidence. Use deeper research only for the strongest candidates or material evidence gaps. Collect the minimum required handoff inputs, then stop as soon as five candidates are prepared. Do not perform full screening, final YES/MAYBE/NO decisions, detailed contribution modelling, or the final cumulative table.
