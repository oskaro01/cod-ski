---
name: gcc-payment-gateway-advisor
description: Advise GCC ecommerce marketplaces on payment gateways, checkout methods, BNPL, Apple Pay, refunds, disputes, settlement, and UAE/Saudi/Qatar/Kuwait/Bahrain/Oman payment decisions. Use when comparing Stripe, Tabby, Tamara, PayTabs, Tap, Checkout.com, Network International, Amazon Payment Services, HyperPay, or payment integration strategy for Khaleeja or similar marketplaces.
metadata:
  short-description: GCC ecommerce payment gateway advisor
---

# GCC Payment Gateway Advisor

Use this skill for payment decisions in GCC ecommerce marketplaces.

## Providers To Consider

- Stripe: cards, Apple Pay, wallets, marketplace/payment infrastructure where available.
- Tabby: buy-now-pay-later popular in UAE/KSA/GCC.
- Tamara: buy-now-pay-later popular in KSA/UAE/GCC.
- PayTabs, Tap Payments, Checkout.com, Network International, Amazon Payment Services, HyperPay: regional alternatives.

## What To Compare

- Supported countries
- Supported currencies
- Apple Pay / Google Pay support
- Mada support for Saudi Arabia
- KNET support for Kuwait
- BNPL approval rates and customer fees
- Merchant fees and settlement timing
- Refund process
- Chargebacks and disputes
- Marketplace split payments or seller payout support
- Checkout UX
- Developer effort

## Rules

- Payment fees and country support change often. Verify against official provider docs or sales pages before giving final current numbers.
- Separate confirmed facts from assumptions.
- For Khaleeja MVP, recommend starting with the simplest reliable gateway first, then adding Tabby/Tamara after core checkout works.
- For marketplace commissions, calculate commission per order item because one order can include products from multiple vendors.

