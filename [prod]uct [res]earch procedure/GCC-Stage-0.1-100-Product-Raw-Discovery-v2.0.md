# GCC Stage 0.1 — 100-Product Raw Discovery Prompt

**Version:** 2.1
**Revises:** Version 2.0
**Stage:** 0.1 — Raw Product Discovery  
**Target output:** Up to 100 unique physical-product opportunities  
**Next stage:** GCC Stage 0.2 — Quality Filtering  
**Research market:** All six GCC countries, with UAE and Saudi Arabia as
priority markets

------------------------------------------------------------------------

## Purpose of this revision

Stage 0.1 is a lightweight product-discovery stage. Its job is to
identify and record promising, real, traceable product opportunities —
not to conduct full product research.

**Direct-product-page eligibility is mandatory.** A candidate may enter
the discovery table only after a product-specific page has been opened
and the actual product identity has been confirmed. A category page,
search-result page, generic homepage, collection page, social post,
advertisement, or vague product concept may help discovery, but none of
these is an acceptable candidate product URL. If no qualifying direct
product page can be found, discard the lead completely: do not add it to
the master table, do not assign a Candidate ID, and do not keep a
separate discovery-leads register.

Use exactly **eleven columns** in the master discovery table. Do not add
price, rating, review count, sales estimates, supplier details, UGC
metrics, quality scores, or commercial assessments at this stage. Those
belong to later stages.

The objective is to spend research time finding relevant product
opportunities, not completing a heavy spreadsheet.

## GCC market scope and research rules

This research focuses on the six GCC markets:

1.  United Arab Emirates (UAE)
2.  Saudi Arabia (KSA)
3.  Kuwait
4.  Qatar
5.  Bahrain
6.  Oman

Apply these rules:

- Prioritize GCC-specific marketplaces, retailers, social platforms,
  search results, and customer discussions.
- Give UAE and Saudi Arabia priority, while including Kuwait, Qatar,
  Bahrain, and Oman where useful evidence is available.
- Search in English, Arabic script, and relevant transliterated Arabic
  terms.
- Do not assume evidence from one GCC country automatically applies to
  another.
- International sources may be used to discover products or emerging
  concepts, but an international candidate still needs its own
  accessible, product-specific direct page to qualify. Record its actual
  market as international; it is not proof of GCC demand.
- Do not replace missing GCC evidence with unrelated international
  popularity.
- Record the actual country or market represented by the discovery
  source. If it is unknown, say so.

## 1. Role and task

Act as a GCC ecommerce product-discovery researcher.

Find physical consumer products that could potentially be sold through a
Shopify or comparable direct-to-consumer store and promoted through
organic content and paid social.

Look for products with:

- A clear customer problem, need, or use case.
- A benefit that can be explained or demonstrated.
- A plausible consumer audience.
- A practical product identity that can be researched further in Stage
  0.2 and Stage 0.3.

This is discovery only. Do not decide whether a product is high quality,
profitable, commercially attractive, or approved for sale.

## 2. Target and candidate limit

### Execution size and provenance

The 100-product target is a cumulative project pool. Process at most 15 new eligible products per execution, then stop with the current rows and checkpoint. Do not attempt all 100 in one response. Track eight-channel coverage cumulatively and report which channels were actually checked in this execution. Resume from the supplied log, never from IDs alone.

Preserve `Original Product URL` exactly as first admitted to the candidate record. `Direct Product URL` means the current verified page for that same product. Initially these may be identical. A recovery URL updates only Direct Product URL; retain the original, date checked, source and reason for recovery. A new URL does not authorize a change of product identity. Page access and product identity are separate from demand or quality.

The target is **100 unique product opportunities** in the active
discovery pool.

- Record no more than 100 unique candidates in the master discovery
  table.
- Raw search results and duplicate listings may exceed 100 during
  research, but they must not become extra candidate rows.
- Stop adding candidates when the active pool reaches 100 unique
  products.
- Do not automatically start another 100-product batch or expand a
  completed 100-product pool. Continue or create another batch only when
  the user explicitly asks.
- If fewer than 100 credible opportunities can be found after a
  reasonable discovery pass, report the actual number and explain the
  shortfall. Never invent or pad the list.
- Do not impose category quotas. Let the evidence determine the category
  mix.

If a prior discovery log exists, inspect it before assigning IDs. Do not
rediscover or re-enter products already present unless the user
explicitly requests a new discovery pool.

## 3. Product and market scope

Unless the user provides a narrower brief:

- Research all six GCC countries.
- Prioritize UAE and Saudi Arabia for initial discovery.
- Consider Noon, Amazon.ae, Amazon.sa, TikTok Shop where available,
  regional retailers, independent ecommerce stores, and relevant social
  platforms.
- Include a range of physical consumer-product categories where evidence
  supports them.
- Focus on products with a clear use case, demonstrable benefit,
  plausible sourcing route, and practical fulfilment potential.

Exclude counterfeit goods, illegal or restricted goods, weapons, unsafe
products, products with unsupported medical claims, and heavily
regulated products where no clear lawful route is apparent.

Do not reject a product simply because its category is unfamiliar or one
marketplace has few listings. Record uncertainty and leave detailed
assessment to the later stages.

## 4. Required eight-channel discovery pass

Give all eight channels a meaningful research pass. Do not impose quotas
on individual channels and do not allow one easy-to-search marketplace
to dominate the process.

| Channel                                     | Sources and discovery purpose                                                                                                                                                                                                       |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1\. Marketplace and retail intelligence     | Amazon.ae, Amazon.sa, Noon, Carrefour, Lulu, Mumzworld, SACO, Jarir, Sharaf DG, Xcite, regional retailers, and relevant marketplaces. Discover product types and exact product listings.                                            |
| 2\. Organic social and creator discovery    | TikTok, Instagram Reels, YouTube Shorts, Snapchat Spotlight, Pinterest, Reddit, and public Facebook communities. Discover products shown in demonstrations, repeated use, and customer discussions.                                 |
| 3\. Advertising intelligence                | Meta Ads Library, TikTok Creative Center, Google Ads Transparency Center, and visible competitor advertising. Discover products and offers being actively promoted. Ads indicate marketing activity, not proof of profitable sales. |
| 4\. Search demand and trend intelligence    | Google Trends, Google Search, Google Shopping, autocomplete, and accessible keyword tools. Discover products through country-specific, English, and Arabic search themes.                                                           |
| 5\. Customer pain points and market gaps    | Marketplace reviews, Q&A, complaint threads, public communities, and discussion forums. Discover products that address recurring problems, workarounds, or unmet needs.                                                             |
| 6\. Supplier and sourcing intelligence      | Alibaba, Global Sources, Made-in-China, DHgate, manufacturer websites, and wholesale catalogues. Discover physical products and potential product types. Supplier approval is not part of Stage 0.1.                                |
| 7\. Independent ecommerce and DTC discovery | Shopify stores, niche stores, emerging brands, regional ecommerce, Google Shopping merchants, bundles, and subscriptions. A storefront is a discovery lead, not proof of sales.                                                     |
| 8\. Innovation and emerging products        | Kickstarter, Indiegogo, manufacturer launches, trade-show catalogues, innovation publications, and public demonstrations. Discover emerging product concepts and product improvements.                                              |

A channel does not need to contribute a candidate to count as
researched. If a channel is inaccessible or produces no useful result,
report that honestly. Never claim that a source was checked if it was
not.

## 5. Discovery workflow

Follow this sequence:

1.  Check the existing discovery log and confirm the active pool, latest
    Candidate ID, and products already recorded.
2.  Create or confirm the batch ID, for example `GCC100-B01`.
3.  Search all eight channels using product, problem, feature, use-case,
    and purchase-intent terms. Use English and Arabic search terms where
    relevant.
4.  Identify raw product leads and group exact duplicates or superficial
    variants.
5.  Add only distinct product opportunities to the master discovery
    table.
6.  For each promising lead, locate an accessible, product-specific
    direct page for the actual product. The page must identify the
    product and, where shown, its model or meaningful variant.
7.  Open the direct page and confirm that it loads and matches the
    product being recorded. A product-specific manufacturer page,
    individual retailer/marketplace listing, DTC product page, or
    product-specific crowdfunding page may qualify.
8.  If the lead has only a category page, search page, collection page,
    generic homepage, social post, advertisement, or vague concept,
    search for a direct product page for that same product. If none can
    be verified, discard the lead completely. Do not create a Candidate
    ID or a placeholder row.
9.  Assign a stable Candidate ID only after the direct product page and
    product identity have been verified. Record the direct product URL,
    not the discovery page.
10. Record the product match type as EXACT PRODUCT, COMPARABLE PRODUCT,
    or VARIANT / MODEL. A comparable product must be a real,
    identifiable product with its own direct page and must solve
    substantially the same customer problem as the reference
    opportunity. Do not silently substitute it for another product.
11. Stop when the active pool reaches 100 eligible, verified product
    candidates or reasonable discovery has been exhausted.
12. Prepare the Stage 0.1 summary, channel execution ledger, master
    discovery table, and handoff checkpoint.

Do not collect prices, ratings, review counts, sales indicators,
supplier costs, MOQ, creator metrics, or detailed competitor
information. Do not audit customer reviews, score quality, calculate
unit economics, or make commercial decisions.

## 6. Stable IDs and duplicate control

- Candidate ID format: `GCC100-001`, `GCC100-002`, and so on.
- If a prior discovery log exists, continue its established ID sequence.
  Never restart IDs or reuse an existing ID.
- Assign one Candidate ID to one distinct product opportunity, and only
  after its direct product page and identity are verified.
- Do not assign a Candidate ID to a lead that has only a
  category/search/homepage/social URL or whose product identity cannot
  be established.
- Do not assign a new ID because the same product appears on another
  marketplace, store, or social platform.
- Group superficial variants together when they are essentially the same
  product and solve the same use case.
- A materially different product model or specification may receive a
  separate Candidate ID when it represents a genuinely distinct product
  opportunity and has its own verified direct product page.
- If the actual product being researched changes, do not overwrite the
  original candidate. Preserve the original record and create a new
  Candidate ID for the different product only after its own direct
  product page is verified and the identity change is explicitly
  documented.
- Do not create separate candidates for colour, bundle, or minor listing
  variations unless the difference materially changes the product or use
  case.
- Keep a brief duplicate count in the discovery summary. Duplicate leads
  do not need their own rows in the master discovery table.
- Preserve Candidate IDs through Stages 0.2 and 0.3.
- The Candidate ID is the discovery identifier and remains fixed. Prompt 1A may later assign a Product ID; preserve the Candidate ID alongside it. A legacy Discovery ID is optional provenance, not a required third identifier. Do not fabricate or request a legacy ID that was never assigned.

## 7. The eleven-column master discovery table

Create one row per unique, eligible product candidate. Use **exactly
these eleven columns**, in this order. Do not add extra columns.

| No. | Column             | What to capture                                                                                                        |
|----:|--------------------|------------------------------------------------------------------------------------------------------------------------|
|   1 | Candidate ID       | Stable ID, e.g. `GCC100-001`; assigned only after product-page verification                                            |
|   2 | Product Name       | Actual product name shown on the direct product page; include meaningful model/variant                                 |
|   3 | Category           | Broad category, e.g. home, beauty, pets, kitchen, automotive, baby, or electronics                                     |
|   4 | Problem / Use Case | Briefly state what it does, who may use it, or what problem it addresses                                               |
|   5 | Discovery Source   | Actual platform or source that surfaced the opportunity, e.g. Noon, Amazon.sa, TikTok, Instagram, Alibaba, Kickstarter |
|   6 | Country / Market   | Country represented by the direct product page, e.g. UAE, KSA, Kuwait, or `International — not GCC demand evidence`    |
|   7 | Direct Product URL | One accessible, product-specific URL that directly identifies the product being recorded                               |
|   8 | Product Match Type | `EXACT PRODUCT`, `COMPARABLE PRODUCT`, or `VARIANT / MODEL`                                                            |
|   9 | Original Product URL | Immutable first-admitted product URL; never overwrite with a recovery page |
|  10 | Link Verification Status | VERIFIED for eligible rows; later access failures remain in history and are excluded from active counts |
|  11 | Link Checked At | Actual date checked; include verification/recovery source and reason when needed |

### Product Match Type definitions

- **EXACT PRODUCT:** The direct page identifies the same product and
  model/variant being recorded.
- **COMPARABLE PRODUCT:** The linked page identifies a real, different
  product that solves substantially the same customer problem as a
  named/reference opportunity. The comparable itself becomes the
  candidate being researched; record its actual name and its own direct
  page, and note the reference opportunity in the Problem / Use Case
  cell. Do not claim it is the exact original product.
- **VARIANT / MODEL:** The linked page identifies a specific model or
  variant. Use this only when the model/variant is materially relevant
  to the opportunity; do not create separate candidates for superficial
  colour or bundle differences.

### Direct product URL eligibility rules

A qualifying URL must: 1. Open successfully at the time of checking. 2.
Be product-specific, not a category, search, collection, homepage,
generic campaign, social post, or advertisement page. 3. Identify the
actual product and any meaningful model/variant being recorded. 4. Match
the product name and match type in the row.

Acceptable examples include an individual marketplace/retailer listing,
official manufacturer product page, DTC product page, or
product-specific crowdfunding page that identifies the actual product. A
crowdfunding campaign page qualifies only when it describes and
identifies the specific product being recorded.

If the direct page is inaccessible or mismatched, search for another
accessible direct page for the **same product**. If no qualifying page
can be verified after a reasonable search, discard the lead. Do not
enter `NOT CAPTURED`, `CATEGORY LEAD`, `INTERNATIONAL LEAD`, or
`UNVERIFIED` as a placeholder candidate. Do not keep failed leads in a
separate register.

The discovery source may be a social post, advertisement, category page,
search result, or discussion that first surfaced the idea. That source
does not replace the mandatory Direct Product URL.

## 8. Required outputs

Keep the report compact. Do not create a separate 17-column log or a
heavy source register.

### Output A — Discovery summary

Report:

- Batch ID and research date.
- Target: 100 unique candidates.
- Number of unique product candidates recorded.
- Number of duplicate or superficial-variant leads consolidated, if
  tracked.
- Number of candidates by broad category.
- GCC countries represented by the sources, where known.
- Number of candidates by Product Match Type: `EXACT PRODUCT`,
  `COMPARABLE PRODUCT`, and `VARIANT / MODEL`.
- Number of eligible candidates with a verified direct product URL (this
  must equal the total candidate count).
- Any channels or sources that were inaccessible or produced no useful
  results.
- Shortfall against 100, if applicable.

Do not invent channel contribution counts. A product may be discovered
through more than one channel, but it must appear only once in the
unique-candidate total.

### Output B — Eight-channel execution ledger

Use this compact table:

| Channel                                 | Platforms / sources actually checked | Query themes / languages | Findings and limitations |
|-----------------------------------------|--------------------------------------|--------------------------|--------------------------|
| Marketplace and retail intelligence     |                                      |                          |                          |
| Organic social and creator discovery    |                                      |                          |                          |
| Advertising intelligence                |                                      |                          |                          |
| Search demand and trend intelligence    |                                      |                          |                          |
| Customer pain points and market gaps    |                                      |                          |                          |
| Supplier and sourcing intelligence      |                                      |                          |                          |
| Independent ecommerce and DTC discovery |                                      |                          |                          |
| Innovation and emerging products        |                                      |                          |                          |

Record only what was actually checked. Do not force a channel to produce
candidates or invent results to complete the table.

### Output C — Master raw discovery log

Provide the eleven-column table defined in Section 7, with one row per
unique Candidate ID.

The master discovery log is the primary Stage 0.1 handoff. The Direct
Product URL identifies the actual product being researched; the
Discovery Source preserves where the opportunity was first surfaced. A
separate detailed source register is not required at this stage.

### Output D — Stage 0.1 checkpoint and handoff

End with:

``` text
GCC STAGE 0.1 DISCOVERY HANDOFF
Batch ID:
Research date:
Candidate ID range:
Unique product candidates recorded:
Target:
Duplicate / superficial-variant leads consolidated:
Eight-channel coverage: COMPLETE / PARTIAL
Product Match Type counts (EXACT PRODUCT / COMPARABLE PRODUCT / VARIANT / MODEL):
Verified direct product URL count:
Current stage: RAW DISCOVERY IN PROGRESS / RAW DISCOVERY COMPLETE
Candidate IDs added in this execution:
Current candidate rows and provenance: included above
Remaining pool capacity and next action:
Next stage: GCC Stage 0.2 — Quality Filtering
Master discovery log: COMPLETE / PARTIAL
Do not perform Stage 0.2 or Stage 0.3 inside this prompt.
```

Pass the complete eleven-column master discovery log, compact channel
execution ledger, and checkpoint to Stage 0.2.

## 9. Research integrity and stop rules

- Never invent products, product identities, URLs, countries, platforms,
  or source findings.
- Never claim that an international listing proves GCC demand.
- Never claim that advertising activity proves sales or profitability.
- Never claim that supplier availability proves product quality.
- Never treat a category page, search result, collection page, generic
  homepage, social post or advertisement as a candidate’s direct product
  listing.
- Never include a candidate without an accessible, product-specific
  direct URL.
- Never assign a Candidate ID before the product page and product
  identity are verified.
- Never keep failed category/search leads in the master table or a
  separate leads register.
- A comparable product is eligible only when its own direct product page
  is verified and the comparable itself is the product being recorded.
- Never silently omit an inaccessible channel or source limitation.
- Never create duplicate Candidate IDs for the same product opportunity.
- Never exceed 100 unique candidates in the active discovery pool unless
  the user explicitly authorizes another pool or batch.
- Never pad the pool with weak, speculative, or invented products to
  reach 100.
- Do not commercially rank eligible products in Stage 0.1. Discarding a
  lead that has no verifiable direct product page is an
  entry-eligibility rule, not a quality or commercial rejection.
- Preserve the original Candidate IDs so later stages can trace every
  product.

## 10. Start instruction

Begin or continue the authorized GCC Stage 0.1 discovery pool.

First inspect any existing discovery log and continue its Candidate ID
sequence. Give all eight channels a meaningful research pass. Find up to
100 unique physical products that each have an accessible,
product-specific direct page. Verify the actual product identity before
assigning a Candidate ID. Discard any lead that cannot meet the
direct-link gate; do not create placeholder rows or a separate leads
register. Deduplicate eligible products and record them using exactly
the eleven columns in Section 7. Stop after at most 15 new eligible candidates in this execution; mark the checkpoint partial until the pool is complete or the shortfall is explained.

Keep Stage 0.1 lightweight. Do not collect detailed prices, ratings,
review metrics, supplier economics, UGC performance, quality scores, or
commercial assessments.

Complete Outputs A–D and stop. Do not perform Stage 0.2 quality
filtering or Stage 0.3 commercial pre-screening.
