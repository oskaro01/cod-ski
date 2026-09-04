# Google Merchant Product Feed Required Fields

## Purpose

Use this checklist when adding or fixing products in Google Merchant Center.

## Primary Product Example

**Product:** Reusable Swedish Dishcloth 10-Pack  
**Brand:** Your Product  
**Product URL:** `/products/reusable-swedish-dishcloth-10-pack`

| Attribute | Required? | Example Value | Notes |
|---|---|---|---|
| `id` | Yes | `YP-SD10-001` | Unique product ID; keep stable |
| `title` | Yes | `Reusable Swedish Dishcloth 10-Pack` | Match product page title |
| `description` | Yes | `Reusable Swedish dishcloths for everyday kitchen wipe-downs, crumbs, coffee rings, sink splashes, and table resets.` | Product-only info; no promo claims |
| `link` | Yes | `https://yourstore.com/products/reusable-swedish-dishcloth-10-pack` | Must use verified domain |
| `image_link` | Yes | `https://yourstore.com/path-to-product-image.png` | Public, clear product image |
| `availability` | Yes | `in_stock` | Must match landing page |
| `price` | Yes | `[PRICE] USD` | Must match landing page |
| `condition` | Required for used/refurbished; recommended here | `new` | Use `new` for new product |
| `brand` | Required when brand exists | `Your Product` | Use store/product brand |
| `gtin` | Required if real GTIN exists | `[GTIN]` | Do not guess |
| `mpn` | Required if no GTIN but real MPN exists | `[MPN]` | Do not guess |
| `identifier_exists` | Conditional | `no` | Use only if no GTIN/MPN exists and appropriate |
| `multipack` | Required for multipacks | `10` | Product is a 10-pack |
| `google_product_category` | Recommended | `Home & Garden > Household Supplies > Household Cleaning Supplies` | Helps product categorization |

## Safe Product Description

```text
Reusable Swedish dishcloths for everyday kitchen wipe-downs, crumbs, coffee rings, sink splashes, and table resets. This 10-pack makes it easier to keep fresh cloths ready through the week.
```

## Avoid in Merchant Feed

- Fake discounts
- Fake reviews
- "Best" or "guaranteed" claims
- "Zero waste" unless verified
- Promotional title text like "free shipping"
- Watermarked images
- Placeholder images
- Mismatched price or availability

## Quick Feed QA

| Check | Pass? |
|---|---|
| Product title matches landing page |  |
| Product description is accurate |  |
| Price is the same on page and feed |  |
| Availability is the same on page and feed |  |
| Product image is clear and public |  |
| Product link opens without login |  |
| No fake claims or fake urgency |  |
| GTIN/MPN are real or not submitted |  |
