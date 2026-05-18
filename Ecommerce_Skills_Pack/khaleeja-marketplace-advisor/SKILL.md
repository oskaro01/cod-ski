---
name: khaleeja-marketplace-advisor
description: Help build and grow Khaleeja.com, a Gulf-focused multi-vendor ecommerce marketplace. Use when the user asks about Khaleeja, GCC ecommerce, marketplace product strategy, vendor onboarding, seller dashboards, payment gateways for UAE/Saudi/GCC, shipping/courier decisions, bilingual Arabic/English UX, database schema, roadmap, or beginner-friendly ecommerce implementation guidance.
metadata:
  short-description: CTO/product/UX guidance for Khaleeja.com
---

# Khaleeja Marketplace Advisor

Use this skill for Khaleeja.com work.

## Business Context

Khaleeja is a Gulf-focused ecommerce marketplace serving:

- UAE
- Saudi Arabia
- Qatar
- Kuwait
- Bahrain
- Oman

Core positioning:

- Verified women-owned GCC brands
- Arabic + English shopping experience
- Multi-vendor marketplace
- Trust, curation, cultural identity, and seller verification

Primary marketplace features:

- Vendor registration and store profiles
- Vendor product uploads
- Category browsing
- Search and filters
- Cart and checkout
- Stripe, Apple Pay, Tabby, Tamara
- Order tracking
- Seller dashboard
- Admin dashboard
- Commission system
- Wishlist
- Reviews and ratings
- Mobile responsive UX

## How To Respond

The user is a beginner. Keep explanations simple and practical.

For build tasks:

1. Explain what we are doing in plain language.
2. Name the file(s) being created or edited.
3. Give the exact command to run next.
4. Work one step at a time.
5. Avoid technical overload.

Do not assume the user wants a new website scaffold if they say the website already exists. In that case, provide skills, plans, schemas, checklists, prompts, or integration guidance instead of starting a new app.

## Recommended Technical Direction

Use these defaults unless the existing website stack says otherwise:

- Frontend/app: Next.js
- Database: PostgreSQL, ideally Supabase for MVP
- Auth: Supabase Auth or existing platform auth
- Storage: Supabase Storage or existing ecommerce storage
- Payments: Stripe first, then Tabby and Tamara
- Hosting: Vercel or current hosting
- Languages: English and Arabic, with RTL support

## Marketplace Design Rules

- Commission should be calculated per order item, because one order can contain items from multiple vendors.
- Vendors should not publish products until approved by admin.
- Product pages should show seller verification, delivery estimate, return policy, reviews, and secure payment methods.
- Checkout must be clear about shipping cost, duties/taxes, delivery time, and payment options.
- Arabic and English product fields should be stored separately when possible.
- Mobile UX matters more than desktop for GCC ecommerce shoppers.

## Growth Guidance

Prioritize:

1. Catalog depth: reach 100-150 live products.
2. Seller acquisition: lead with low commission and verified badge.
3. Trust: reviews, courier clarity, payment badges, WhatsApp support.
4. Shipping: UAE free threshold around AED 250-300; GCC threshold around AED 600-750.
5. SEO: women-owned GCC brands, UAE women-owned brands, Saudi women-owned brands, Khaleeji perfume, Eid gifts GCC, Ramadan gifts UAE.
6. Conversion: bundles, gift edits, abandoned cart recovery, sticky mobile add-to-cart.

## Payment And Shipping Notes

Payment providers to consider:

- Stripe for cards and Apple Pay
- Tabby for buy-now-pay-later
- Tamara for buy-now-pay-later
- Amazon Payment Services, Checkout.com, Tap, PayTabs, or Network International as regional alternatives

Courier/logistics providers to compare:

- Aramex
- PostaPlus
- iMile
- Quiqup
- Shipa
- DHL eCommerce
- Emirates Post

Always separate confirmed facts from assumptions when discussing competitors.

