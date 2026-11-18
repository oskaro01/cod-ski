# GCC Selection Sheet and Competitor Opportunity Tracker — Update Specification

**Version:** 1.0  
**Purpose:** Implement the approved direct-product-link and
post-Prompt-2 competitor-opportunity rules in GCC research workbooks  
**Status:** Companion specification; does not modify the unused research
Master Prompt or the workbook-generation Master Prompt

------------------------------------------------------------------------

## 1. Scope

Apply this specification when the GCC selection workbook is next updated
or rebuilt.

It covers two separate workbook areas:

1.  The **main product selection sheet**, which contains active
    candidates/products moving through the normal GCC research pipeline.
2.  A separate **Competitor Opportunity Tracker**, which records real
    competitor products discovered during Prompt 2 and assessed through
    Prompt 2A.

Do not merge these two purposes. An unapproved competitor opportunity is
not an active selected product.

## 2. Main product selection sheet — mandatory fields

The main active selection sheet must contain these fields:

| Field                     | Requirement                                                                                |
|---------------------------|--------------------------------------------------------------------------------------------|
| Candidate ID / Product ID | Preserve the existing identifier; never recycle or overwrite it.                           |
| Product Name / Model      | Use the actual product name and meaningful model/variant shown on the direct product page. |
| Direct Product URL        | Mandatory product-specific URL for the actual product being researched.                    |
| Product Match Type        | `EXACT PRODUCT`, `COMPARABLE PRODUCT`, or `VARIANT / MODEL`.                               |
| Link Verification Status  | `VERIFIED`, `NOT VERIFIED`, `NOT DIRECT`, or `INACCESSIBLE`.                               |
| Original Product URL | Immutable first-recorded product URL; preserve even if a recovery page is used. |
| Link Checked At | Actual verification date; include provenance/record reference. |
| URL Recovery History | Previous/current URLs, same-product identity basis, date, source and reason. |

Direct Product URL means the current verified page. Original Product URL remains unchanged. A current access failure removes the row from eligible active counts until resolved, while the original record and previous verification evidence remain in history. This is an access/identity status, not a negative demand score. The Stage 0.1 export is eleven columns; downstream workbook sheets may have additional fields. Retain optional legacy Discovery IDs only when they already exist; Candidate ID is sufficient discovery provenance.

Preserve all existing workbook columns, formulas, source references,
scores, decisions and history. Add the required fields without silently
changing the meaning of existing fields.

If an existing column is labelled `Product / Source URL`, rename it to
`Direct Product URL` only when it is being used to store the candidate’s
actual product page. Keep the discovery source separately in the
existing Discovery Source field.

## 3. Main-sheet eligibility rule

Only products with all of the following may appear in the **active
selection pool**:

- A direct, product-specific URL.
- `Link Verification Status = VERIFIED`.
- A product name/model that matches the linked page.
- A valid Product Match Type.
- No category, search, collection, generic homepage, social post,
  advertisement, or generic campaign URL used as the candidate’s product
  page.

A direct product page may be an individual retailer/marketplace listing,
official manufacturer product page, DTC product page, or
product-specific crowdfunding page that identifies the actual product.

A comparable product is eligible only when it is a real product with its
own direct product page and is itself the product being researched. Do
not use a comparable listing to disguise a missing link for the original
product.

Rows marked `NOT VERIFIED`, `NOT DIRECT`, or `INACCESSIBLE` must not be
counted in active candidate totals or included in the active selection
pool. If a same-product direct page cannot be found, the candidate is
not eligible. Do not retain category/search leads as candidate rows or
create a separate discovery-leads register.

For previously completed/historical records, preserve the original
record in the audit/history area as required for traceability; do not
present it as an active eligible candidate.

## 4. Product Match Type definitions

Use these values consistently:

- **EXACT PRODUCT:** The linked page identifies the same product and
  model/variant being researched.
- **COMPARABLE PRODUCT:** The linked page identifies a different product
  that solves substantially the same customer problem. The comparable
  product itself is the research subject and has its own direct product
  page; record the reference product/opportunity in the Notes or Problem
  / Use Case field.
- **VARIANT / MODEL:** The linked page identifies the specific model or
  variant being researched. Use a separate candidate/product record only
  when the difference materially changes the product opportunity.

Do not transfer ratings, reviews, supplier prices, UGC metrics, or
conclusions from an exact product to a comparable product or different
model.

## 5. Competitor Opportunity Tracker — separate worksheet

Create a separate worksheet named:

`Competitor Opportunity Tracker`

This worksheet is for real, identifiable competitor products noticed
during Prompt 2 and submitted to Prompt 2A. It is not a general
discovery-leads register. Do not add category-only, search-only,
generic-homepage, or unidentified product concepts.

Recommended columns:

| Column | Field                           | Purpose                                                                                                                         |
|-------:|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
|      1 | Opportunity Reference           | Internal tracker row reference only; not a GCC Candidate ID or Product ID.                                                      |
|      2 | Alternative Product Name        | Actual name shown on the product page.                                                                                          |
|      3 | Brand / Model                   | Brand and meaningful model/variant, where visible.                                                                              |
|      4 | Direct Product URL              | Mandatory product-specific URL.                                                                                                 |
|      5 | Product Match Type              | `EXACT PRODUCT`, `COMPARABLE PRODUCT`, or `VARIANT / MODEL`.                                                                    |
|      6 | Link Verification Status        | `VERIFIED`, `NOT VERIFIED`, `NOT DIRECT`, or `INACCESSIBLE`; only VERIFIED alternatives may be assessed as valid opportunities. |
|      7 | Original Product ID             | Product ID whose Prompt 2 research led to the discovery.                                                                        |
|      8 | Original Product Name           | Name of the product being researched when the alternative was noticed.                                                          |
|      9 | Reason for Interest             | Why the user noticed or liked the alternative.                                                                                  |
|     10 | Early GCC Signal                | Brief evidence note with country/source; do not treat it as full demand validation.                                             |
|     11 | UGC URL(s)                      | Direct links to exact or comparable creator/customer content.                                                                   |
|     12 | UGC Evidence Type               | Exact product, comparable product, category, or general trend.                                                                  |
|     13 | UGC Visible Metrics             | Views, likes, comments, shares, or `NOT CAPTURED`.                                                                              |
|     14 | Quick Sourcing Signal           | Brief initial exact/comparable sourcing signal; not a supplier approval.                                                        |
|     15 | Prompt 2A Verdict               | `PROMOTE TO PROMPT 2`, `HOLD — NEED MORE EVIDENCE`, or `REJECT`.                                                                |
|     16 | Prompt 2A Date Checked          | Date the quick validation was completed.                                                                                        |
|     17 | Key Risks / Evidence Gaps       | Main issue(s) that could change the decision.                                                                                   |
|     18 | User Approval for Full Prompt 2 | `PENDING`, `APPROVED`, or `DECLINED`.                                                                                           |
|     19 | New Product ID                  | Assign only after the user approves the alternative for a separate Prompt 2 cycle.                                              |
|     20 | Notes / Evidence References     | Concise provenance and supporting references.                                                                                   |
|     21 | Original Product URL | Immutable URL captured when the opportunity was first recorded. |
|     22 | Link Checked At | Actual date of the current link check. |
|     23 | URL Recovery History / Entry Record | Recovery evidence, approval reference and actual Prompt 2 entry route. |

The tracker may contain a `PROMOTE` verdict while user approval is still
pending. That alternative must remain outside the main product selection
sheet until the user approves full Prompt 2 research.

## 6. ID and provenance rules

- Keep the original Product ID unchanged.
- Record the original Product ID that led to each competitor discovery.
- Do not reuse the original Product ID for the alternative.
- Check for the same product already in the tracker or active pool before creating an opportunity or assigning a new Product ID; a different seller page alone does not create a new product.
- Do not assign a new GCC100 Candidate ID to a post-Prompt-2 alternative
  unless the user explicitly routes it back through Stage 0.1.
- Once the user approves the alternative for full Prompt 2 research,
  assign the next unused Product ID from the authorized Product ID
  sequence.
- Carry PROMPT 2A - USER-APPROVED as its actual entry route, with the verdict, approval/date and evidence references. Do not fabricate a Prompt 1B YES, Candidate ID or original screening row. If the registry is not supplied, obtain it before assigning a global Product ID.
- Do not copy the original product’s scores, reviews, costs, supplier
  evidence, UGC metrics or conclusions to the alternative.
- Preserve the original research and the alternative’s independent
  research as separate records.

## 7. Workbook integrity and preservation

When implementing these changes:

1.  Preserve original worksheets and their historical records.
2.  Preserve existing Candidate IDs, Product IDs, formulas, links,
    decisions, score calculations, formatting and source references.
3.  Add the Competitor Opportunity Tracker as a separate worksheet; do
    not insert unapproved alternatives into the main selection pool.
4.  Do not delete historical rows merely because a later link check
    fails. Mark the eligibility/link status and keep the record in the
    appropriate audit/history area, while excluding it from active
    selection counts.
5.  Do not silently overwrite an existing product row when a comparable
    or alternative product is discovered.
6.  Keep the tracker append-only for new opportunities and decision
    updates. Preserve prior Prompt 2A verdicts and dates in history
    where the workbook supports decision history.

## 8. Workbook quality-control checks

Before delivering an updated workbook, confirm:

- Every active selection row has a direct product-specific URL.
- Every active selection row has `Link Verification Status = VERIFIED`.
- Every active selection row has a valid Product Match Type.
- Original Product URL, current Direct Product URL and Link Checked At remain separately traceable; every recovery records the same-product match and source.
- No category/search/homepage/social/ad URL is being used as a candidate
  product page.
- Unapproved competitor alternatives appear only in the Competitor
  Opportunity Tracker, not the main selection sheet.
- Every competitor opportunity records the Original Product ID when
  known.
- Every completed Prompt 2A assessment has a verdict and date checked.
- A new Product ID is assigned only after user approval for full Prompt
  2 research.
- Original IDs, formulas, scores, decisions, links and research history
  remain intact.

------------------------------------------------------------------------

## Implementation boundary

This specification is a companion to the revised Stage 0.1–0.3, Prompt
1A/1B, Prompt 2 and Prompt 2A documents. It does not replace those
research prompts and does not modify either Master Prompt.
