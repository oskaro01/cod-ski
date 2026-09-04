# Technical SEO Fixes Report

## Assignment Overview

**Assignment task:** Review the provided Google Search Console coverage/indexing exports and prepare technical SEO fixes.  
**Student note:** The assignment says to use Claude, but this report was completed with Codex as an AI-assisted alternative.  
**Primary site found in exports:** `https://abudhabistore.ae/`  
**Export date range:** January 3, 2026 to March 28, 2026  
**Report date:** August 27, 2026  
**Status:** Fixes researched and prepared. Live implementation requires store admin, theme, Search Console, and redirect access.

## What This Assignment Is Asking

In simple terms, this assignment is asking for three things:

1. Open the Google Sheets exports from Google Search Console.
2. Identify the technical SEO/indexing problems Google found.
3. Write the fixes that should be applied to the website, then validate them in Google Search Console.

The files are not normal spreadsheets with product content. They are Google Search Console "Coverage Drilldown" exports. Each file includes:

- A trend tab showing how many pages were affected over time.
- A URL examples tab showing sample affected URLs.
- A properties tab showing the exact Google Search Console issue name.

## Important Access Note

I cannot directly fix the live website without access to:

- Shopify/Ecommerized store admin
- Theme code editor
- URL redirect settings
- Google Search Console
- Robots.txt and sitemap settings
- Server/CDN logs for 5xx errors

This report therefore provides the technical SEO fix plan and exact implementation checklist.

---

# 1. Google Sheet Issue Summary

| # | Google Search Console Issue | Final Affected Pages | Trend | Priority | Main URL Patterns Found |
|---:|---|---:|---:|---|---|
| 1 | Not found (404) | 26,635 | +6.1% | High | Product URLs, collection URLs, Arabic `/ar/` URLs, filter/search URLs |
| 2 | Alternate page with proper canonical tag | 8,075 | -83.8% | Monitor | Product URLs inside collections, tracking parameters, filters |
| 3 | Blocked by robots.txt | 5,138 | +205.8% | High | Vendor pages, account/admin pages, search/filter URLs, web-pixel URLs |
| 4 | Excluded by `noindex` tag | 2,836 | +177.2% | Medium | Search/filter pages, `/ar/search`, web-pixel sandbox URLs |
| 5 | Page with redirect | 1,701 | -78.7% | Medium | Collection/product URL variants, older product paths |
| 6 | Soft 404 | 133 | +77.3% | High | Empty collections, out-of-stock collection filters, paginated collection pages |
| 7 | Blocked due to other 4xx issue | 119 | +153.2% | High | Product URLs, Arabic URLs, filtered search pages |
| 8 | Duplicate without user-selected canonical | 68 | +300.0% | Medium | `.atom` feed URLs and collection duplicates |
| 9 | Server error (5xx) | 9 | -74.3% | Critical | Product pages, search URLs, collection/product paths |
| 10 | Crawled - currently not indexed | 46,364 | -83.5% | High | Product pages, collection URLs, vendor URLs, filters, search, `.atom` feeds |
| 11 | Indexed, though blocked by robots.txt | 39 | +21.9% | High | Vendor pages, paginated collections, Arabic vendor URLs |

## Data Quality Note

One Sheet title mentions `khaleeja.ae`, but the sample URLs inside the exported tabs point to `abudhabistore.ae`. Because the URL examples are what Google Search Console uses for validation, this report treats the affected URL evidence as `abudhabistore.ae` and flags the title mismatch for review.

---

# 2. Main Diagnosis

The website appears to have crawl bloat from Shopify-style URL variants. Google is discovering many URLs that are not meant to become search landing pages, including:

- Product URLs inside collection paths
- Search result pages
- Filtered collection pages
- Vendor query URLs
- Arabic `/ar/` duplicates or translated paths
- Tracking-parameter URLs such as `_pos`, `_sid`, `_fid`, and `_ss`
- Paginated collection URLs
- `.atom` feed URLs
- Web-pixel sandbox URLs

The most important SEO goal is not to force Google to index every URL. The goal is to make Google index the correct canonical pages and ignore low-value duplicates, filters, feeds, tracking URLs, and private pages.

---

# 3. Fixes by Issue

## Issue 1: Not Found (404)

**Affected pages on March 28, 2026:** 26,635  
**Priority:** High

### Example patterns found

- Deleted or unavailable product URLs
- Old collection URLs
- Arabic product URLs
- Search/filter URLs that no longer resolve
- Tracking-parameter URLs

### Fix

| URL Type | Action |
|---|---|
| Deleted product with replacement | 301 redirect to the closest active product |
| Deleted product with no replacement | Return true 404 or 410 and remove internal links |
| Old collection URL | 301 redirect to the correct collection |
| Search/filter URL | Remove from internal links and sitemap; noindex or canonicalize if still accessible |
| Arabic URL with English equivalent | Redirect to Arabic equivalent if it exists, otherwise canonical product/category page |

### Implementation checklist

- Export 404 URLs from Search Console.
- Group URLs by product, collection, search, filter, and language path.
- Add redirects only where a close replacement exists.
- Remove broken links from menus, collection descriptions, product recommendations, blog posts, and feeds.
- Remove invalid URLs from any manually submitted sitemap.
- Validate top examples in Search Console.

---

## Issue 2: Alternate Page With Proper Canonical Tag

**Affected pages on March 28, 2026:** 8,075  
**Priority:** Monitor

### Why this may not be bad

Google says alternate pages with a proper canonical tag are usually working as intended. These URLs are alternate versions of another canonical URL.

### Example patterns found

- `/collections/.../products/...`
- URLs with `_pos`, `_fid`, `_sid`, and `_ss`
- Filtered collection URLs
- Product URLs shown under multiple collections

### Fix

This issue does not require fixing if the canonical URL is correct. The cleanup is:

- Keep the clean product URL as canonical: `/products/product-handle`
- Keep the clean collection URL as canonical: `/collections/collection-handle`
- Remove tracking and collection-path product variants from sitemaps.
- Update internal product links to clean product URLs where possible.

---

## Issue 3: Blocked by Robots.txt

**Affected pages on March 28, 2026:** 5,138  
**Priority:** High

### Example patterns found

- `/collections/vendors?...`
- `/admin`
- `/account`
- `/ar/account`
- Search/filter pages
- Web-pixel paths

### Fix

Review whether the blocked URLs should be indexed.

| If URL should be indexed | If URL should not be indexed |
|---|---|
| Remove the robots.txt block and make sure the page returns 200 | Keep blocked only for private/crawl-waste URLs |
| Add useful page content and internal links | Remove from sitemap and internal links |
| Submit the URL for validation in Search Console | If already indexed, use `noindex` before relying on robots.txt |

### Robots.txt cleanup example

Use this as a review model, not a blind copy-paste:

```text
User-agent: *
Disallow: /admin
Disallow: /account
Disallow: /cart
Disallow: /checkout
Disallow: /orders
Disallow: /search
Disallow: /web-pixels
Disallow: /*.atom

Sitemap: https://abudhabistore.ae/sitemap.xml
```

Important: robots.txt blocks crawling, but it does not always remove a URL from Google's index if other pages link to that URL.

---

## Issue 4: Excluded by `noindex` Tag

**Affected pages on March 28, 2026:** 2,836  
**Priority:** Medium

### Example patterns found

- Search URLs
- Filtered URLs
- Web-pixel sandbox URLs
- Arabic search pages

### Fix

This is acceptable for low-value pages such as internal search, filter combinations, and web-pixel sandbox URLs. The problem is only serious if important product, collection, or blog pages are accidentally tagged `noindex`.

### Implementation checklist

- Keep `noindex,follow` on search pages and low-value filters.
- Remove `noindex` from important product, collection, and blog pages.
- Remove noindexed URLs from XML sitemaps.
- Use Search Console URL Inspection on sample pages.

---

## Issue 5: Page With Redirect

**Affected pages on March 28, 2026:** 1,701  
**Priority:** Medium

### Example patterns found

- Old collection/product URLs
- Product URLs with tracking parameters
- Arabic collection/product paths

### Fix

Redirects are not always bad. The technical SEO problem happens when redirected URLs are still in sitemaps, internal links, ads, product feeds, or menus.

### Implementation checklist

- Keep 301 redirects for moved pages.
- Remove redirected URLs from sitemaps.
- Update internal links to point directly to the final URL.
- Avoid redirect chains.
- Avoid redirecting all deleted products to the homepage.

---

## Issue 6: Soft 404

**Affected pages on March 28, 2026:** 133  
**Priority:** High

### Example patterns found

- Empty brand/collection pages
- Out-of-stock filter pages
- Deep paginated collection pages such as `/collections/all?page=91`

### Fix

| URL Type | Recommended Fix |
|---|---|
| Empty collection that should exist | Add products, intro copy, internal links, and indexable content |
| Empty collection that should not exist | Return 404/410 or redirect to a relevant active collection |
| Out-of-stock filter URL | Noindex/canonicalize to clean collection |
| Deep pagination with no products | Remove internal links and return 404, 410, or canonicalize appropriately |

---

## Issue 7: Blocked Due to Other 4xx Issue

**Affected pages on March 28, 2026:** 119  
**Priority:** High

### Example patterns found

- Product URLs
- Arabic search URLs
- Filtered URLs

### Fix

Identify the exact HTTP status for each example URL:

- 400: fix malformed URL generation.
- 401: remove login requirement if the page should be public.
- 403: check bot/firewall/CDN rules.
- 410: acceptable only if permanently removed.
- 429: reduce bot throttling or verify Googlebot access.

Important product pages should return `200`, not 4xx.

---

## Issue 8: Duplicate Without User-Selected Canonical

**Affected pages on March 28, 2026:** 68  
**Priority:** Medium

### Example patterns found

- `.atom` feed URLs
- Collection duplicate URLs
- Arabic collection/feed URLs

### Fix

- Add canonical tags to duplicate HTML pages.
- Keep one canonical URL for every product and collection.
- Block or noindex feed URLs if they are not needed for search.
- Remove `.atom` URLs from internal links and sitemaps.

Canonical rule:

| Duplicate URL | Canonical Target |
|---|---|
| `/collections/all/products/product-handle` | `/products/product-handle` |
| `/collections/brand-name.atom` | `/collections/brand-name` or noindex/block feed |
| Filtered collection URL | Clean collection URL |
| Tracking-parameter URL | Clean product or collection URL |

---

## Issue 9: Server Error (5xx)

**Affected pages on March 28, 2026:** 9  
**Priority:** Critical

### Why this matters

Even though the count is low, 5xx errors are critical because they mean Google could not access the page due to a server-side failure.

### Fix

- Check server/CDN logs for the affected URLs and dates.
- Test URLs in an incognito browser and with Search Console URL Inspection.
- Fix theme/app errors causing product or search pages to fail.
- Check whether malformed filter/search URLs trigger timeouts.
- Set up uptime monitoring for important product, collection, and checkout pages.
- Validate fixes in Search Console.

---

## Issue 10: Crawled - Currently Not Indexed

**Affected pages on March 28, 2026:** 46,364  
**Priority:** High

### Example patterns found

- Product pages
- Collection pages
- Vendor URLs
- Search/filter URLs
- `.atom` feeds
- Arabic URLs

### Diagnosis

This issue often happens when Google crawls URLs but decides not to index them because they are duplicate, thin, low value, parameter-based, or not clearly useful as search landing pages.

### Fix

| Page Type | Action |
|---|---|
| Important product pages | Add unique product descriptions, specs, FAQs, reviews if real, image alt text, and internal links |
| Important collection pages | Add intro copy, useful filters, internal links, and unique SEO titles/descriptions |
| Search/filter pages | Noindex/canonicalize and remove from sitemap |
| Vendor pages | Index only if each vendor page has unique useful content |
| `.atom` feeds | Block/noindex/remove from internal discovery |
| Arabic pages | Add proper Arabic content and hreflang if targeting Arabic search |

### Content quality checklist for product pages

- Unique title tag
- Unique meta description
- One clear H1
- Product description not copied from supplier
- Product images with descriptive alt text
- Price and availability visible
- Internal links from related collections
- FAQ section for common buying questions
- Canonical tag pointing to the clean product URL

---

## Issue 11: Indexed, Though Blocked by Robots.txt

**Affected pages on March 28, 2026:** 39  
**Priority:** High

### Why this happens

Google may still index a blocked URL if other pages link to it. Because robots.txt blocks crawling, Google may index the URL with limited information.

### Fix

| Desired Outcome | Correct Action |
|---|---|
| Remove URL from Google | Temporarily allow crawl, add `noindex`, wait for removal, then optionally block again |
| Keep URL indexed | Remove the robots.txt block and make the page crawlable |
| Consolidate duplicate | Add canonical to the preferred URL and remove internal links to blocked duplicate |

Do not rely only on robots.txt to remove indexed URLs from Google.

---

# 4. Sitewide Technical SEO Fix Plan

## Fix 1: Clean Up Sitemaps

Only indexable canonical URLs should be in the sitemap.

Remove or prevent discovery of:

- Search result URLs
- Filtered URLs
- Tracking-parameter URLs
- `.atom` feed URLs
- Redirected URLs
- 404/410 URLs
- Noindexed URLs
- Private account/admin/checkout URLs

## Fix 2: Standardize Canonical Tags

Every product, collection, and blog page should have one canonical URL.

| Page Type | Canonical Should Point To |
|---|---|
| Product page | Clean `/products/product-handle` URL |
| Collection page | Clean `/collections/collection-handle` URL |
| Blog post | Clean `/blogs/blog-name/post-handle` URL |
| Filtered collection | Clean parent collection or noindex |
| Search page | Noindex, follow |
| Tracking URL | Clean base URL |

## Fix 3: Control Search and Filter Crawl Bloat

Search and filter URLs create many combinations that usually should not rank.

Recommended handling:

- Add `noindex,follow` to internal search pages.
- Canonicalize filtered collection URLs to the clean collection page unless a filter has unique search value.
- Avoid linking heavily to parameter URLs.
- Do not include parameter URLs in sitemaps.

## Fix 4: Fix Product and Collection URL Redirects

For each redirected URL:

- Keep the redirect if it serves users.
- Replace internal links with the final destination URL.
- Remove old URLs from feeds and sitemaps.
- Avoid redirect chains.

## Fix 5: Review Arabic URLs

Many examples contain `/ar/`. If Arabic pages are intentional:

- Make sure Arabic pages have Arabic content, not empty duplicate templates.
- Add hreflang tags between English and Arabic versions.
- Use correct canonical logic. Arabic pages should canonicalize to Arabic URLs if they are valid localized pages.

If Arabic pages are not ready:

- Keep them noindexed until translated content is complete.
- Remove them from sitemap until launch.

## Fix 6: Block or Remove Web-Pixel Sandbox URLs

Web-pixel sandbox URLs should not be search landing pages.

Recommended actions:

- Prevent internal links to `/web-pixels...` paths.
- Keep them blocked or noindexed depending on platform control.
- Check analytics/app settings that generated discoverable web-pixel URLs.

---

# 5. Validation Plan

After fixes are applied:

| Step | Tool | What to Check |
|---:|---|---|
| 1 | Google Search Console URL Inspection | Test sample URLs from each issue |
| 2 | Live URL test | Confirm fixed status: 200, 301, 404/410, noindex, or canonical |
| 3 | Sitemap report | Confirm sitemap contains only canonical indexable URLs |
| 4 | Robots.txt tester | Confirm important pages are not blocked |
| 5 | Coverage/Page indexing report | Click "Validate Fix" for resolved issues |
| 6 | Weekly monitoring | Track affected page count for 2-4 weeks |

## Success Criteria

| Issue | Success Target |
|---|---|
| 404 | Broken internal/sitemap URLs removed; valid redirects added where needed |
| Alternate canonical | Only expected alternates remain |
| Blocked by robots.txt | Only private or crawl-waste URLs remain blocked |
| Noindex | Only intentionally excluded URLs remain noindexed |
| Redirects | Redirected URLs removed from sitemap and internal links |
| Soft 404 | Empty pages either improved, redirected, or removed |
| Other 4xx | Important pages return 200 |
| Duplicate canonical | Preferred canonical declared |
| 5xx | No recurring server errors |
| Crawled not indexed | Important product/collection pages improved and resubmitted |
| Indexed though blocked | URLs either unblocked or removed via noindex/removal process |

---

# 6. Fix Status Tracker

| Issue | Status | Owner Needed | Evidence to Capture |
|---|---|---|---|
| Not found (404) | Ready for implementation | Store admin/developer | Redirect list and Search Console validation |
| Alternate canonical | Monitor and clean internal links | SEO/developer | Canonical URL inspection screenshots |
| Blocked by robots.txt | Ready for review | Developer | Robots.txt tester screenshots |
| Excluded by noindex | Ready for review | SEO/developer | URL Inspection screenshots |
| Page with redirect | Ready for cleanup | Store admin | Updated internal links and redirect export |
| Soft 404 | Ready for content/URL fix | SEO/content/store admin | Before/after URL Inspection |
| Other 4xx | Needs technical debugging | Developer | HTTP status test and fix screenshot |
| Duplicate without canonical | Ready for canonical fix | Developer | Canonical tag test |
| Server error 5xx | Needs urgent dev/server review | Developer/server admin | Server log or URL test |
| Crawled not indexed | Needs content and crawl cleanup | SEO/content/developer | Improved page examples |
| Indexed though blocked | Needs robots/noindex decision | SEO/developer | Removal or unblock validation |

---

# 7. Recommended Submission Summary

For the assignment, submit this report as the technical SEO fixes document.

If screenshots are required, include screenshots of:

- Google Sheet issue properties tabs
- Sample affected URL tabs
- Search Console Page indexing issue pages
- Robots.txt test
- URL Inspection test for one sample URL from each issue
- Redirect or theme settings after implementation, if available

## Sources Used

- Provided Google Sheets exports from Google Search Console:
  - https://docs.google.com/spreadsheets/d/1JTTz6zfJQNxrYh06hh-gsFLkpZ14c2Mn7t_bI2ItV_U/edit?usp=sharing
  - https://docs.google.com/spreadsheets/d/1kOBsS0vnq2cwuEWS8x7diKcr2Z7m1KozjoMae7QsG7w/edit?usp=sharing
  - https://docs.google.com/spreadsheets/d/18yYK3JgCrCjBxmYRuiFZaPNp2GqhouMgXPJ_eWufbsc/edit?usp=sharing
  - https://docs.google.com/spreadsheets/d/1pUkVezj0bZgtt-HAkQ1HMdP0GMv_fhfMjE17sWl0tKk/edit?usp=sharing
  - https://docs.google.com/spreadsheets/d/1sqf0w9J2J9ZYEtWLxPpOXLeVapfwupmTOgTbG-h9iUc/edit?usp=sharing
  - https://docs.google.com/spreadsheets/d/1uECTW5LeUHTveGRN2y4KplssRc5PWsNo00UpWw3-VBQ/edit?usp=sharing
  - https://docs.google.com/spreadsheets/d/1A-gb4gk6QYNryfKTq-OAX5qswEoH6CFesJJg5TGwL3g/edit?usp=sharing
  - https://docs.google.com/spreadsheets/d/1VFhbXCrYr9pd0USN3u-XLUnKEg9Es99gZyW-4Oyx2hM/edit?usp=sharing
  - https://docs.google.com/spreadsheets/d/1D0YbdAyGpOXfTqcUv3qZtVR-XWKb_RGecNdP4dMVM5E/edit?usp=sharing
  - https://docs.google.com/spreadsheets/d/13oD2sjTQuYj5lBx6YKcCU917yI3fADZ7iNIhcPQgU9M/edit?usp=sharing
  - https://docs.google.com/spreadsheets/d/1ippJsxmTOYdShE8hwOerxkyO1s7vAnxJCWFowIX0W5s/edit?usp=sharing
- Google Search Console Page indexing report documentation: https://support.google.com/webmasters/answer/7440203
- Google Search Central robots.txt guide: https://developers.google.com/search/docs/crawling-indexing/robots/intro
- Google Search Central sitemap guide: https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview
