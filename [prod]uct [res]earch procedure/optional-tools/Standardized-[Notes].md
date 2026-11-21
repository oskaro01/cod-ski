# Standardized product research Notes

## Purpose and inputs

Format the latest available research for one product into a compact Notes cell. Use the dossier, latest decision, subsequent evidence updates and existing spreadsheet row when available. This is a formatting task; missing facts become named gaps rather than a new research assignment.

Preserve Product ID, exact variant, country, historical decision provenance and original/current URL records. Use only facts in the supplied records. A formatting example does not establish product facts.

In staged Individual Prompt 2, this is the P2-8 Notes module. Use the supported P2-7 final decision and latest source/financial records. The main controller requests Outputs B/C in this stage; generate Notes once and reuse it in both tables. That explicit controller instruction supplies the export request; do not require a separate request for each table. No new browsing, score changes or decision upgrades during formatting. Standalone formatting below still defaults to Notes only.

## Notes contract

Target 180-240 words; maximum 280 words excluding URL strings. Use these labels in order:

- PRODUCT: Product ID, exact variant, target country and material compatibility/specification limits.
- EVIDENCE: Strongest marketplace, supplier and UGC findings. Include dates, currencies and exact/comparable/category relevance where they affect interpretation. Include app, refill or competitor details here only when relevant.
- ECONOMICS: Landed-cost status, base-case contribution, CAC assumption and break-even measures when actually established; otherwise state the key unknown. Distinguish quoted costs, estimates and verified costs.
- DEMAND / SCORE: Current demand methodology v3.0, purchasing-evidence rating or UNKNOWN, supported GCC country/model scope, UAE validation status/next check, demand confidence, commercial score/overall confidence and separate core coverage. Include the assessment date. Existing commercial weights remain unchanged. No 80/20 social blend or weighted demand-coverage percentage applies; missing UGC is not a demand penalty. Global creator content supports creative assessment, not GCC buying proof. Preserve older scores and never recompute or upgrade during formatting.

- PROMISING: Up to three specific supported reasons.
- RISKS: Up to three material unresolved or confirmed problems. Move resolved concerns into the facts and preserve their resolution in the underlying evidence record.
- COLLECT: Up to three prioritized, decision-changing actions with owner/timing. Refer to the existing detailed gap register for additional required actions so compactness does not hide blockers.
- DECISION / NEXT: Preserve SAMPLE, RESEARCH MORE, HOLD or DROP and the exact next step. Distinguish Stage 3 entry from payment, pilot and inventory approval. If only a screening decision exists, label it as screening.

Use short statements and evidence IDs already present in the source register. Avoid repeating URLs stored in dedicated columns. Include material contradictory prices, original currencies, absent shipping costs and unverified supplier relationships. Never reuse an example's scores, supplier names, screenshots or product claims.

## Optional existing-row update

Default output is one copy-ready Notes cell only, with no report or introduction. If explicitly asked to update the complete row, require its existing values and return the same eleven columns:

```text
| Product Name | Category | Competitor/Product Link | Supplier Link | Product Cost (USD) | Competitor Selling Price (USD) | UGC Video/Post Link | UGC Views / Engagement | Trend / Demand | Research Decision | Notes |
```

Update only fields changed by supported new evidence. Preserve unaffected values, identity, original/current URLs and important competitor/supplier/UGC links. Keep historical values and change reasons in the supplied evidence/change record; do not silently overwrite a contradiction. Do not add columns, reconstruct missing old cells or invent currency conversions. If the row is absent, return Notes only and identify that dependency.

Return text for review. This prompt does not instruct an external spreadsheet write.
