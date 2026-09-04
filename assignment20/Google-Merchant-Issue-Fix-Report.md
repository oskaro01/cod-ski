# Google Merchant Center Setup and Issue Fix Report

## Assignment Overview

**Assignment task:** Make the store live, connect it with Google Merchant Center, and try to fix Google Merchant issues.  
**Brand:** Your Product  
**Product:** Reusable Swedish Dishcloth 10-Pack  
**Report date:** August 30, 2026  
**Prepared by:** Student  
**Status:** Ready to complete in live store and Google Merchant Center.

## Access Note

Live setup and issue resolution require access to the store admin and Google Merchant Center. This report documents the required setup steps, checks, and fixes. Screenshots should be added after the student completes the live setup.

---

# 1. Store Live Checklist

| Requirement | Status | Evidence/Screenshot |
|---|---|---|
| Store homepage is public | Pending screenshot | `01-live-homepage.png` |
| Product page is public | Pending screenshot | `02-live-product-page.png` |
| Cart opens normally | Pending screenshot | `03-cart-or-checkout-test.png` |
| Checkout flow starts | Pending screenshot | `03-cart-or-checkout-test.png` |
| HTTPS/SSL works | Pending screenshot | Browser address bar |
| Contact page exists | Pending check | Footer or menu link |
| Shipping policy exists | Pending check | Footer or policy page |
| Returns/refund policy exists | Pending check | Footer or policy page |
| Privacy policy exists | Pending check | Footer or policy page |
| Terms of service exists | Pending check | Footer or policy page |

## Store Readiness Notes

The store should not be password-protected or in coming soon mode. Product, price, availability, image, shipping, return, and checkout information should be visible before connecting to Google Merchant Center.

---

# 2. Merchant Center Connection Checklist

| Requirement | Status | Evidence/Screenshot |
|---|---|---|
| Google Merchant Center account created/opened | Pending screenshot | `04-merchant-center-created.png` |
| Business name added | Pending check | Merchant Center business info |
| Store URL added | Pending check | Merchant Center online store section |
| Website verified | Pending screenshot | `05-website-verified-claimed.png` |
| Website claimed | Pending screenshot | `05-website-verified-claimed.png` |
| Product source/feed connected | Pending screenshot | `06-product-source-connected.png` |
| Products synced or uploaded | Pending screenshot | `07-products-synced.png` |
| Shipping settings added | Pending screenshot | `08-shipping-settings.png` |
| Return policy added | Pending screenshot | `09-return-policy-settings.png` |

---

# 3. Product Feed Review

## Primary Product

| Field | Recommended Value |
|---|---|
| `id` | `YP-SD10-001` |
| `title` | `Reusable Swedish Dishcloth 10-Pack` |
| `description` | `Reusable Swedish dishcloths for everyday kitchen wipe-downs, crumbs, coffee rings, sink splashes, and table resets.` |
| `link` | `https://yourstore.com/products/reusable-swedish-dishcloth-10-pack` |
| `image_link` | `https://yourstore.com/path-to-product-image.png` |
| `availability` | `in_stock` |
| `price` | `[PRICE] USD` |
| `brand` | `Your Product` |
| `condition` | `new` |
| `identifier_exists` | `no`, only if no real GTIN/MPN exists |
| `multipack` | `10` |
| `google_product_category` | `Home & Garden > Household Supplies > Household Cleaning Supplies` |

## Product Feed Quality Check

| Requirement | Status | Notes |
|---|---|---|
| Title matches product page | Pending | Product title should match landing page |
| Description matches product page | Pending | Avoid unsupported claims |
| Price matches product page | Pending | Same currency and sale price |
| Availability matches product page | Pending | In stock/out of stock must match |
| Image is public and clear | Pending | No promotional overlay or watermark |
| Product URL works | Pending | Product page must return 200 |
| Brand is included | Pending | Use `Your Product` |
| GTIN/MPN handled correctly | Pending | Do not invent values |

---

# 4. Merchant Center Issues and Fix Log

Use this table after checking `Products` > `Needs attention`.

| # | Issue Name | Affected Products | Severity | Where Fixed | Fix Attempted | Status |
|---:|---|---:|---|---|---|---|
| 1 | Website not verified/claimed | Account | Account issue | Merchant Center | Verify and claim online store URL | Pending |
| 2 | Missing shipping | Products/account | Warning/disapproval | Merchant Center shipping settings | Add shipping service and delivery time | Pending |
| 3 | Missing return policy | Products/account | Warning/disapproval | Merchant Center + store policy page | Add return policy and policy URL | Pending |
| 4 | Price mismatch | Product-level | Disapproval risk | Store/product feed | Match feed price to landing page | Pending |
| 5 | Availability mismatch | Product-level | Disapproval risk | Store/product feed | Match `availability` to product page inventory | Pending |
| 6 | Missing GTIN/MPN/brand | Product-level | Warning/disapproval | Product feed | Add real identifiers or use `identifier_exists=no` if appropriate | Pending |
| 7 | Bad image or promotional overlay | Product-level | Warning/disapproval | Product images/feed | Replace with clear product image | Pending |
| 8 | Landing page unavailable | Product-level | Disapproval | Store/product page | Make product page public and crawlable | Pending |
| 9 | Robots.txt blocks Google | Website issue | Account/product issue | Store/theme/robots settings | Allow Googlebot and Googlebot-image for product pages/images | Pending |
| 10 | Misrepresentation/trust issue | Account issue | Account risk | Store pages/business info | Add accurate contact, policies, pricing, and business info | Pending |

---

# 5. Fix Details

## Website Verification Fix

**Problem:** Google Merchant Center cannot confirm the student owns the store website.  
**Action:** Verify and claim the store URL using ecommerce platform, HTML tag, HTML file, Google Tag Manager, Google Analytics, or email verification.  
**Evidence:** Screenshot of verified/claimed website.

## Shipping Fix

**Problem:** Google cannot show accurate shipping information.  
**Action:** Add a shipping service in Merchant Center or submit the `shipping` attribute in the product feed. Use real delivery time and cost.  
**Evidence:** Screenshot of shipping settings.

## Return Policy Fix

**Problem:** Return information is missing or unclear.  
**Action:** Add return/refund policy page on the store and add return policy settings in Merchant Center.  
**Evidence:** Screenshot of return settings and store return policy page.

## Product Data Fix

**Problem:** Product data may be incomplete or inconsistent.  
**Action:** Check title, description, link, image, price, availability, brand, GTIN/MPN, condition, and multipack fields.  
**Evidence:** Screenshot of product feed/product details.

## Landing Page Fix

**Problem:** Google cannot access product landing page or product page does not match feed.  
**Action:** Make product page public, remove password protection, fix 404s, avoid generic redirects, and confirm price/availability match.  
**Evidence:** Screenshot of product page and Merchant Center product detail.

## Image Fix

**Problem:** Product image may be too small, blocked, generic, watermarked, or promotional.  
**Action:** Use a clear product image with no overlay text, no border, and no watermark. Make image URL public and crawlable.  
**Evidence:** Screenshot of product image on page/feed.

---

# 6. Final Status Summary

| Area | Status |
|---|---|
| Store made live | Pending live access |
| Google Merchant Center account | Pending live access |
| Website verified/claimed | Pending live access |
| Product source connected | Pending live access |
| Products reviewed | Pending live access |
| Merchant issues checked | Pending live access |
| Fixes attempted | Pending live access |
| Submission report prepared | Complete |

## Student Submission Note

Use this note if not all live fixes can be completed:

```text
I reviewed the store readiness requirements, prepared the store for Google Merchant Center connection, checked the required product feed fields, and documented the Merchant Center issue-fix process. Some live fixes require store admin or Google Merchant Center access, so I prepared the issue tracker and validation steps for completion after access is available.
```

## Sources Used

- Google Merchant Center: Online store URL verification: https://support.google.com/merchants/answer/11586344
- Google Merchant Center: Add products from an ecommerce platform: https://support.google.com/merchants/answer/12158210
- Google Merchant Center: Issues in Merchant Center: https://support.google.com/merchants/answer/12153802
- Google Merchant Center: Product data specification: https://support.google.com/merchants/answer/7052112
- Google Merchant Center: Free listings requirements: https://support.google.com/merchants/answer/13889434
