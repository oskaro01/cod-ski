---
name: marketplace-database-architect
description: Design database schemas for multi-vendor ecommerce marketplaces with vendors, stores, products, categories, carts, orders, payments, commissions, payouts, shipments, reviews, wishlists, admin approvals, and bilingual Arabic/English content. Use for Khaleeja database, Supabase/Postgres planning, migrations, or schema review.
metadata:
  short-description: Multi-vendor marketplace database design
---

# Marketplace Database Architect

Use this skill for database design and schema planning.

## Core Tables

- users
- vendor_profiles
- stores
- categories
- products
- product_images
- inventory_movements
- carts
- cart_items
- orders
- order_items
- payments
- shipments
- reviews
- wishlists
- commissions
- payouts
- admin_audit_logs

## Marketplace Rules

- One order can contain products from many vendors.
- Commission belongs on order_items, not only orders.
- Vendors should have approval states.
- Products should have draft, pending_review, active, rejected, archived states.
- Arabic and English product fields should be separate when possible.
- Store slugs and product slugs must be unique.
- Keep payment provider IDs and shipment tracking IDs for reconciliation.

## Recommended MVP Stack

- PostgreSQL or Supabase Postgres.
- Supabase Auth if no existing auth exists.
- Supabase Storage or platform storage for product images.

## Output Style

For beginners, explain each table in plain language and include fields only when needed for the current step.

