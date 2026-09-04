# Google Merchant Center and Live Store Setup: Step-by-Step Guide

## Assignment Overview

**Assignment task:** Make your store live, connect it with Google Merchant Center, and try to fix Google Merchant issues.  
**Brand:** Your Product  
**Logo tagline:** Cleaner Home, Easier Life  
**Product focus:** Reusable Swedish Dishcloth 10-Pack  
**Primary product URL:** `/products/reusable-swedish-dishcloth-10-pack`  
**Guide date:** August 30, 2026  
**Important note:** This setup requires your store admin login and Google account login. Do not enter payment details for paid ads unless your instructor specifically asks you to run ads.

## What This Assignment Means

This assignment has three practical jobs:

1. Make sure the ecommerce store is public and ready for customers.
2. Create or open Google Merchant Center and connect the store/product feed.
3. Open Merchant Center's `Needs attention` area and fix or document the product/account issues.

Google Merchant Center is where ecommerce products are uploaded so they can appear on Google surfaces such as Search, Shopping, Images, YouTube, and ads/free listings when eligible.

---

# Part 1: Make the Store Live

## Step 1: Open Your Store Admin

Log in to your ecommerce platform or Ecommerized dashboard.

Look for sections like:

- `Store`
- `Website`
- `Online store`
- `Settings`
- `Domain`
- `Store status`
- `Publish`

The exact wording can change depending on the platform.

## Step 2: Remove Password or Coming Soon Mode

Check that the store is not hidden from visitors.

| Setting | What It Should Be |
|---|---|
| Password protection | Off |
| Coming soon mode | Off |
| Maintenance mode | Off |
| Store visibility | Public or Live |
| Search engine visibility | Enabled |

## Step 3: Connect or Confirm the Domain

Your store should open from a clean public URL.

Examples:

```text
https://yourstore.com/
https://yourproduct.store/
https://your-ecommerized-store.com/
```

Check:

| Domain Item | Requirement |
|---|---|
| HTTPS/SSL | Working |
| Homepage | Opens without login |
| Product page | Opens without login |
| Cart | Opens normally |
| Checkout | Starts normally |
| Mobile view | Loads correctly |

## Step 4: Check Required Store Pages

Google may reject or limit stores that look incomplete, misleading, or hard to trust.

Create or confirm these pages:

| Page | Purpose |
|---|---|
| Contact Us | Shows how customers can contact the business |
| Shipping Policy | Explains shipping cost, country, and delivery timing |
| Returns and Refund Policy | Explains return window, return cost, and refund process |
| Privacy Policy | Explains customer data handling |
| Terms of Service | Explains store terms |
| About Us | Adds trust and brand context |

Put links to these pages in the footer.

## Step 5: Check Product Page Readiness

Open the Reusable Swedish Dishcloth 10-Pack product page.

Confirm:

| Product Page Item | Requirement |
|---|---|
| Product title | Clear and matches feed title |
| Product description | Specific, useful, not copied filler |
| Price | Visible and same as Merchant feed |
| Availability | Visible and accurate |
| Product image | Real product image, not placeholder |
| Add to cart button | Working |
| Checkout path | Working |
| Shipping/returns info | Linked or visible |
| Mobile page | Easy to use |

## Step 6: Test the Live Store

Use an incognito/private browser window and open:

```text
https://yourstore.com/
https://yourstore.com/products/reusable-swedish-dishcloth-10-pack
https://yourstore.com/cart
```

If all pages open without login, the store is live enough for the assignment.

## Screenshot Needed

Save screenshots in:

`assignment20/screenshots/`

Use:

```text
01-live-homepage.png
02-live-product-page.png
03-cart-or-checkout-test.png
```

---

# Part 2: Create or Open Google Merchant Center

## Step 1: Open Merchant Center

Go to:

https://merchant.google.com/

Sign in with the Google account you use for business/assignments.

## Step 2: Create Merchant Center Account

If you do not have an account yet, follow the setup flow.

Google may ask for:

| Field | Recommended Entry |
|---|---|
| Business name | `Your Product` |
| Website URL | Your live store URL |
| Business country | Your store country |
| Time zone | Your working time zone |
| Customer service contact | Your business email |
| Phone number | Your business/customer support number, if available |

## Step 3: Add Online Store URL

Go to:

`Settings` > `Business info` > `Online store`

Enter your store URL starting with `https://`.

Example:

```text
https://yourstore.com
```

## Step 4: Verify and Claim Website

Google says website verification proves you own the site, and claiming links the site to your Merchant Center account.

Choose one method:

| Method | Use When |
|---|---|
| Ecommerce platform verification | Your platform provides a Google/Merchant connection |
| Email verification | You can receive email at an address linked to the site |
| HTML tag | You can add code to the homepage/head section |
| HTML file | You can upload files to the website server |
| Google Tag Manager | You are an admin of the GTM container |
| Google Analytics | You are an admin of the GA property connected to the site |

For most student ecommerce stores, the easiest methods are ecommerce platform connection, HTML tag, Google Tag Manager, or Google Analytics.

## Step 5: Confirm Website Status

After verification, Merchant Center should show the website as verified/claimed.

## Screenshot Needed

Save:

```text
04-merchant-center-created.png
05-website-verified-claimed.png
```

---

# Part 3: Connect Products to Google Merchant

## Recommended Method: Connect Ecommerce Platform

If your platform supports Google Merchant Center:

1. In Merchant Center, go to `Products`.
2. Open `Products & store`.
3. Under `All products`, click `Add products`.
4. If there is a dropdown, choose `Add another product source`.
5. Select the option to connect your ecommerce platform.
6. Continue to the platform login/connection screen.
7. Approve the connection.
8. Return to Merchant Center and wait for products to sync.

Google says ecommerce platform sync may take up to 3 days, and product changes should usually be managed inside the ecommerce platform after connection.

## Backup Method: Use a Product File or Google Sheet

If Ecommerized does not show as a platform option, use:

- `Add products from a file`
- `Use Google Sheets`
- `Add products one by one`, if available in the account

Use Google Sheets/file upload if the store has only a few assignment products.

## Minimum Product Feed Fields

Google's product data requirements commonly include:

| Attribute | Example for Your Product |
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
| `identifier_exists` | `no`, only if no GTIN or MPN exists |
| `multipack` | `10` |
| `google_product_category` | `Home & Garden > Household Supplies > Household Cleaning Supplies` |

Do not guess a GTIN or MPN. If the product has no real manufacturer GTIN/MPN, use `identifier_exists = no` only when appropriate.

## Screenshot Needed

Save:

```text
06-product-source-connected.png
07-products-synced.png
```

---

# Part 4: Add Shipping and Return Settings

Google requires shipping information in many countries, including the United States, and recommends adding return policy information.

## Shipping Setup

In Merchant Center, look for:

`Settings` > `Shipping and returns`

or:

`Business info` > `Shipping`

Add:

| Field | Example |
|---|---|
| Country | United States or your target country |
| Service name | Standard shipping |
| Delivery time | 3-7 business days |
| Shipping cost | Free, flat rate, or calculated |
| Currency | Same as product feed |

Use real store values. Do not claim free shipping unless the store actually offers it.

## Return Policy Setup

Add:

| Field | Example |
|---|---|
| Return window | 14 or 30 days, based on real policy |
| Return method | Mail return |
| Return cost | Customer pays or free returns |
| Refund processing time | Example: 5-10 business days |
| Return policy URL | Link to store return/refund page |

## Screenshot Needed

Save:

```text
08-shipping-settings.png
09-return-policy-settings.png
```

---

# Part 5: Find Merchant Center Issues

## Step 1: Open Needs Attention

In Merchant Center:

1. Go to `Products`.
2. Go to `Needs attention`.
3. Review account-level and product-level issues.

Google says product-level issues can happen when product data does not match the website, does not follow product data specifications, or violates Shopping policies.

## Step 2: Download or Screenshot Issues

For each issue, capture:

| Field | What to Write |
|---|---|
| Issue name | Example: Missing value `shipping` |
| Affected products | Number of products affected |
| Severity | Warning, disapproval, account issue |
| Product example | Product title or item ID |
| Where to fix | Store admin, feed, Merchant Center, website page |
| Fix attempted | What you changed or planned |
| Status | Fixed, pending review, needs admin access |

## Screenshot Needed

Save:

```text
10-needs-attention-overview.png
11-issue-detail-page.png
```

---

# Part 6: Common Google Merchant Issues and Fixes

## Issue: Website Not Verified or Claimed

**Where to fix:** Merchant Center > Settings > Business info > Online store

**Fix:**

- Enter the correct live store URL.
- Verify using ecommerce platform, HTML tag, HTML file, Google Tag Manager, or Google Analytics.
- Claim the website after verification.

## Issue: Missing Shipping

**Where to fix:** Merchant Center shipping settings or product feed

**Fix:**

- Add shipping service in Merchant Center.
- Make shipping cost and delivery time match the store.
- Add `shipping` attribute in the feed only if using feed-level shipping.

## Issue: Missing Return Policy

**Where to fix:** Store policy page and Merchant Center return settings

**Fix:**

- Add a real return/refund policy page to the store.
- Add the return policy in Merchant Center.
- Link the policy in the footer.

## Issue: Price Mismatch

**Where to fix:** Store product page and product feed

**Fix:**

- Make product feed price match the landing page price.
- Make currency match.
- Remove outdated sale prices.
- Re-sync or re-upload the product feed.

## Issue: Availability Mismatch

**Where to fix:** Store inventory and product feed

**Fix:**

- If product is in stock, both website and feed should say `in_stock`.
- If out of stock, both should say `out_of_stock`.
- Re-sync feed after inventory updates.

## Issue: Missing Product Identifier

**Where to fix:** Product feed or product details in store admin

**Fix:**

- Add real `brand`.
- Add real `gtin` if the manufacturer assigned one.
- Add real `mpn` if there is no GTIN but a manufacturer part number exists.
- If the product does not have GTIN/MPN, set `identifier_exists` to `no` when appropriate.

Do not invent GTIN or MPN values.

## Issue: Bad Product Image

**Where to fix:** Product page image and image feed field

**Fix:**

- Use a clear product image.
- Avoid watermarks, promotional text, borders, and placeholder images.
- Make sure the image URL is public and crawlable.
- Use JPG, PNG, WebP, GIF, BMP, or TIFF as accepted by Google.

## Issue: Landing Page Unavailable

**Where to fix:** Store product page

**Fix:**

- Make product URL public.
- Remove password/coming soon blocks.
- Fix 404 or redirect problems.
- Ensure Googlebot and Googlebot-image are not blocked by robots.txt.

## Issue: Promotional Text in Title or Image

**Where to fix:** Product title, description, and image

**Fix:**

- Remove phrases like `free shipping`, `limited offer`, `best deal`, and `discount`.
- Keep title focused on the product only.
- Remove image text overlays and watermarks.

## Issue: Misrepresentation or Trust Issue

**Where to fix:** Store pages and Merchant Center business details

**Fix:**

- Add accurate business name.
- Add contact information.
- Add shipping, returns, refund, privacy, and terms pages.
- Make price, availability, and checkout information consistent.
- Remove fake reviews, fake trust badges, fake urgency, and unsupported claims.

---

# Part 7: What to Submit

Submit these items:

1. Screenshot of live store homepage.
2. Screenshot of live product page.
3. Screenshot of Merchant Center account.
4. Screenshot showing website verified/claimed.
5. Screenshot showing product source/feed connected.
6. Screenshot showing product list or synced products.
7. Screenshot of `Needs attention` issues.
8. Issue-fix report showing what was fixed or attempted.

Use the file:

`Google-Merchant-Issue-Fix-Report.md`

## Short Submission Summary

Use this text if the assignment needs a short note:

```text
I made the store live, checked the main customer pages, connected the store/product source to Google Merchant Center, verified and claimed the website, reviewed Merchant Center's Needs attention section, and documented the Google Merchant issues with attempted fixes. Product feed fields, shipping, returns, product images, price, availability, and identifier issues were reviewed for compliance.
```

## Sources Used

- Google Merchant Center: Online store URL verification: https://support.google.com/merchants/answer/11586344
- Google Merchant Center: Add products from an ecommerce platform: https://support.google.com/merchants/answer/12158210
- Google Merchant Center: Issues in Merchant Center: https://support.google.com/merchants/answer/12153802
- Google Merchant Center: Product data specification: https://support.google.com/merchants/answer/7052112
- Google Merchant Center: Free listings requirements: https://support.google.com/merchants/answer/13889434
