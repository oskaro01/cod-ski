# Editable Sheet Fix

The earlier `.xlsx` file used embedded placeholder drawings. Use this file instead for Google Sheets:

`Supplier-Database-Sheet-Editable-Google-Sheets.csv`

Why this version is better:

- It is fully editable after import.
- The product images use real public product image URLs.
- The first column uses Google Sheets `IMAGE()` formulas.
- The second column keeps the raw image URL in case the image formula needs to be reinserted.
- The `Product Page URL` column shows the page where the product image/source was found.

Recommended workflow:

1. Open Google Sheets.
2. Import `Supplier-Database-Sheet-Editable-Google-Sheets.csv`.
3. Choose "Replace spreadsheet" or "Insert new sheet."
4. Resize the rows and first column if the images appear small.

Image sources:

- Swedish dishcloth product photo page: https://www.zulaykitchen.com/products/zulay-kitchen-reusable-eco-friendly-swedish-dishcloth-6-pack
- Stove gap cover product photo page: https://www.stovesdirect.com/silicone-stove-gap-covers-2-pack-essentials-stove-gap-filler-heat/
- Satin pillowcase product photo page: https://illwishes.com/vetted/best-satin-pillowcase/
