from __future__ import annotations

import csv
import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CHART_DIR = ROOT / "charts"
DATA_DIR = ROOT / "data"


PRODUCTS = [
    {
        "rank": 1,
        "product": "Swedish dishcloths / reusable kitchen cleaning cloths",
        "short": "Swedish Dishcloths",
        "category": "Kitchen cleaning",
        "target_price": 14.99,
        "supplier_cost": 2.00,
        "packaging": 0.80,
        "fulfillment": 3.75,
        "fees": 0.90,
        "profit": 7.54,
        "margin_percent": 50.3,
        "break_even_ad_cost": 7.54,
        "monthly_sales_proof": 5000,
        "review_count": 12615,
        "rating": 4.7,
        "risk_level": "Low-medium",
        "decision": "GO",
        "recommendation": "Test first. Lowest risk profile.",
    },
    {
        "rank": 2,
        "product": "Silicone stove gap covers, 2-pack",
        "short": "Stove Gap Covers",
        "category": "Kitchen problem-solver",
        "target_price": 12.99,
        "supplier_cost": 1.50,
        "packaging": 0.75,
        "fulfillment": 3.50,
        "fees": 0.78,
        "profit": 6.46,
        "margin_percent": 49.7,
        "break_even_ad_cost": 6.46,
        "monthly_sales_proof": 8000,
        "review_count": 69034,
        "rating": 4.4,
        "risk_level": "Low-medium",
        "decision": "GO",
        "recommendation": "Test second. Add size guide.",
    },
    {
        "rank": 3,
        "product": "Satin pillowcase 2-pack",
        "short": "Satin Pillowcases",
        "category": "Bedding / beauty-adjacent",
        "target_price": 14.99,
        "supplier_cost": 2.40,
        "packaging": 0.85,
        "fulfillment": 3.75,
        "fees": 0.90,
        "profit": 7.09,
        "margin_percent": 47.3,
        "break_even_ad_cost": 7.09,
        "monthly_sales_proof": 10000,
        "review_count": 316733,
        "rating": 4.5,
        "risk_level": "Medium",
        "decision": "GO with controls",
        "recommendation": "Use safe beauty wording.",
    },
]


RISK_ROWS = [
    {
        "product": "Swedish Dishcloths",
        "Saturation": 3,
        "Quality": 2,
        "Fulfillment": 1,
        "Returns": 1,
        "Compliance/Fit": 2,
        "Overall": "Low-medium",
    },
    {
        "product": "Stove Gap Covers",
        "Saturation": 3,
        "Quality": 2,
        "Fulfillment": 1,
        "Returns": 2,
        "Compliance/Fit": 3,
        "Overall": "Low-medium",
    },
    {
        "product": "Satin Pillowcases",
        "Saturation": 4,
        "Quality": 3,
        "Fulfillment": 1,
        "Returns": 2,
        "Compliance/Fit": 3,
        "Overall": "Medium",
    },
]


COLORS = {
    "dishcloth": "#0f766e",
    "gap": "#2563eb",
    "satin": "#c2410c",
    "profit": "#16a34a",
    "supplier": "#0ea5e9",
    "packaging": "#a855f7",
    "fulfillment": "#f97316",
    "fees": "#64748b",
    "risk_low": "#22c55e",
    "risk_mid": "#f59e0b",
    "risk_high": "#ef4444",
    "ink": "#111827",
    "muted": "#6b7280",
    "grid": "#e5e7eb",
    "bg": "#ffffff",
}


def ensure_dirs() -> None:
    CHART_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for svg in CHART_DIR.glob("*.svg"):
        svg.unlink()


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def money(value: float) -> str:
    return f"${value:,.2f}"


def pct(value: float) -> str:
    return f"{value:.1f}%"


def compact_count(value: float) -> str:
    if value >= 1000:
        return f"{value / 1000:.1f}K"
    return f"{value:,.0f}"


def product_color(index: int) -> str:
    return [COLORS["dishcloth"], COLORS["gap"], COLORS["satin"]][index % 3]


def risk_color(value: int) -> str:
    if value <= 2:
        return COLORS["risk_low"]
    if value == 3:
        return COLORS["risk_mid"]
    return COLORS["risk_high"]


def text(
    x: float,
    y: float,
    value: object,
    size: int = 14,
    fill: str = COLORS["ink"],
    weight: str = "400",
    anchor: str = "start",
) -> str:
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="Arial, Helvetica, sans-serif" '
        f'font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">'
        f"{esc(value)}</text>"
    )


def wrap(value: str, max_chars: int) -> list[str]:
    words = value.split()
    lines: list[str] = []
    current: list[str] = []
    for word in words:
        candidate = " ".join([*current, word]).strip()
        if current and len(candidate) > max_chars:
            lines.append(" ".join(current))
            current = [word]
        else:
            current.append(word)
    if current:
        lines.append(" ".join(current))
    return lines


def multiline(
    x: float,
    y: float,
    lines: list[str],
    size: int = 14,
    fill: str = COLORS["ink"],
    weight: str = "400",
    anchor: str = "start",
    line_height: int = 18,
) -> str:
    parts = [
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="Arial, Helvetica, sans-serif" '
        f'font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">'
    ]
    for index, line in enumerate(lines):
        dy = 0 if index == 0 else line_height
        parts.append(f'<tspan x="{x:.1f}" dy="{dy}">{esc(line)}</tspan>')
    parts.append("</text>")
    return "".join(parts)


def rounded_rect(x: float, y: float, width: float, height: float, fill: str, stroke: str = "none", rx: int = 10) -> str:
    return (
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{width:.1f}" height="{height:.1f}" '
        f'rx="{rx}" fill="{fill}" stroke="{stroke}"/>'
    )


def save_svg(filename: str, body: str, width: int = 1300, height: int = 760) -> None:
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img">'
        f'<rect width="100%" height="100%" fill="{COLORS["bg"]}"/>'
        f"{body}</svg>"
    )
    (CHART_DIR / filename).write_text(svg, encoding="utf-8")


def title_block(title: str, subtitle: str) -> list[str]:
    return [
        text(60, 58, title, 30, COLORS["ink"], "700"),
        text(60, 88, subtitle, 15, COLORS["muted"]),
    ]


def write_csvs() -> None:
    product_fields = [
        "rank",
        "product",
        "category",
        "decision",
        "risk_level",
        "target_price",
        "supplier_cost",
        "packaging",
        "fulfillment",
        "fees",
        "profit",
        "margin_percent",
        "break_even_ad_cost",
        "monthly_sales_proof",
        "review_count",
        "rating",
    ]
    with (DATA_DIR / "product_summary.csv").open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=product_fields)
        writer.writeheader()
        for row in PRODUCTS:
            writer.writerow({field: row[field] for field in product_fields})

    risk_fields = list(RISK_ROWS[0].keys())
    with (DATA_DIR / "risk_scores.csv").open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=risk_fields)
        writer.writeheader()
        writer.writerows(RISK_ROWS)


def markdown_row(values: list[object]) -> str:
    return "| " + " | ".join(str(value) for value in values) + " |"


def create_data_tables() -> None:
    lines = [
        "# Product Validation Data Tables",
        "",
        "Research date: May 6, 2026",
        "",
        "These tables present the same data as the CSV files in a cleaner, submission-friendly format.",
        "",
        "## Product Summary",
        "",
        markdown_row([
            "Rank",
            "Product",
            "Category",
            "Decision",
            "Risk",
            "Price",
            "Profit",
            "Margin",
            "Sales Proof",
            "Reviews",
            "Rating",
        ]),
        "|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in PRODUCTS:
        lines.append(
            markdown_row([
                row["rank"],
                row["product"],
                row["category"],
                row["decision"],
                row["risk_level"],
                money(row["target_price"]),
                money(row["profit"]),
                pct(row["margin_percent"]),
                f"{compact_count(row['monthly_sales_proof'])}+",
                compact_count(row["review_count"]),
                f"{row['rating']:.1f}/5",
            ])
        )

    lines.extend(
        [
            "",
            "## Margin Calculation Detail",
            "",
            markdown_row([
                "Product",
                "Target Price",
                "Supplier Cost",
                "Packaging",
                "Fulfillment",
                "Fees",
                "Profit Before Ads",
                "Break-Even Ad Cost",
            ]),
            "|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in PRODUCTS:
        lines.append(
            markdown_row([
                row["short"],
                money(row["target_price"]),
                money(row["supplier_cost"]),
                money(row["packaging"]),
                money(row["fulfillment"]),
                money(row["fees"]),
                money(row["profit"]),
                money(row["break_even_ad_cost"]),
            ])
        )

    lines.extend(
        [
            "",
            "## Risk Assessment",
            "",
            "Scale: 1 = low risk, 5 = high risk.",
            "",
            markdown_row([
                "Product",
                "Saturation",
                "Quality",
                "Fulfillment",
                "Returns",
                "Compliance/Fit",
                "Overall",
            ]),
            "|---|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in RISK_ROWS:
        lines.append(
            markdown_row([
                row["product"],
                row["Saturation"],
                row["Quality"],
                row["Fulfillment"],
                row["Returns"],
                row["Compliance/Fit"],
                row["Overall"],
            ])
        )

    lines.extend(
        [
            "",
            "## CSV Sources",
            "",
            "- `data/product_summary.csv`",
            "- `data/risk_scores.csv`",
        ]
    )
    (ROOT / "data-tables.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def chart_validated_products() -> None:
    width, height = 1300, 650
    body = title_block(
        "Validated Products and Go / No-Go Recommendation",
        "Lower-risk replacement products selected after fresh demand and margin research.",
    )

    x0, y0 = 60, 135
    table_w = 1180
    row_h = 130
    columns = [
        ("Rank", x0 + 28),
        ("Validated product", x0 + 120),
        ("Margin", x0 + 585),
        ("Risk", x0 + 745),
        ("Go / No-Go", x0 + 915),
    ]
    body.append(rounded_rect(x0, y0, table_w, 58, "#eef2ff", COLORS["grid"], 12))
    for label, x in columns:
        body.append(text(x, y0 + 36, label, 14, COLORS["muted"], "700"))

    for index, row in enumerate(PRODUCTS):
        y = y0 + 76 + index * row_h
        fill = "#ffffff" if index % 2 == 0 else "#f8fafc"
        body.append(rounded_rect(x0, y, table_w, row_h - 18, fill, COLORS["grid"], 12))
        body.append(rounded_rect(x0 + 24, y + 34, 42, 42, product_color(index), "none", 21))
        body.append(text(x0 + 45, y + 61, row["rank"], 18, "#ffffff", "700", "middle"))
        body.append(multiline(x0 + 120, y + 43, wrap(row["product"], 42), 16, COLORS["ink"], "700", "start", 21))
        body.append(text(x0 + 120, y + 92, row["category"], 13, COLORS["muted"]))
        body.append(text(x0 + 585, y + 53, pct(row["margin_percent"]), 22, product_color(index), "700"))
        body.append(text(x0 + 585, y + 83, f"Profit {money(row['profit'])}", 13, COLORS["muted"], "700"))
        risk_fill = COLORS["risk_mid"] if row["risk_level"] == "Medium" else COLORS["risk_low"]
        body.append(rounded_rect(x0 + 745, y + 38, 145, 38, risk_fill, "none", 19))
        body.append(text(x0 + 817.5, y + 63, row["risk_level"], 13, "#ffffff", "700", "middle"))
        body.append(rounded_rect(x0 + 915, y + 32, 250, 48, product_color(index), "none", 24))
        body.append(text(x0 + 1040, y + 62, row["decision"], 15, "#ffffff", "700", "middle"))
        body.append(text(x0 + 915, y + 103, row["recommendation"], 13, COLORS["muted"]))

    save_svg("01_validated_products_go_no_go.svg", "".join(body), width, height)


def chart_demand_proof() -> None:
    width, height = 1300, 760
    body = title_block(
        "Demand Proof",
        "Observed marketplace sales proof and review depth for the new lower-risk products.",
    )

    x_label = 70
    x_bar = 380
    y_start = 145
    row_h = 170
    sales_max = 11000
    review_max = 330000
    bar_w = 700
    sales_h = 34
    review_h = 24

    body.append(text(x_bar, 125, "Monthly sales proof", 13, COLORS["muted"], "700"))
    body.append(text(x_bar, 167, "Review proof", 13, COLORS["muted"], "700"))

    for index, row in enumerate(PRODUCTS):
        y = y_start + index * row_h
        body.append(rounded_rect(55, y - 30, 1190, 132, "#ffffff" if index % 2 == 0 else "#f8fafc", COLORS["grid"], 12))
        body.append(multiline(x_label, y + 5, wrap(row["product"], 29), 15, COLORS["ink"], "700", "start", 20))
        body.append(text(x_label, y + 74, f"Rating {row['rating']:.1f}/5", 13, COLORS["muted"], "700"))

        sales_width = row["monthly_sales_proof"] / sales_max * bar_w
        body.append(rounded_rect(x_bar, y - 4, bar_w, sales_h, "#e5e7eb", "none", 17))
        body.append(rounded_rect(x_bar, y - 4, sales_width, sales_h, product_color(index), "none", 17))
        body.append(text(x_bar + min(sales_width + 16, bar_w + 8), y + 19, f"{compact_count(row['monthly_sales_proof'])}+ monthly sales", 14, product_color(index), "700"))

        review_width = row["review_count"] / review_max * bar_w
        body.append(rounded_rect(x_bar, y + 49, bar_w, review_h, "#e5e7eb", "none", 12))
        body.append(rounded_rect(x_bar, y + 49, max(review_width, 8), review_h, COLORS["ink"], "none", 12))
        body.append(text(x_bar + min(review_width + 16, bar_w + 8), y + 68, f"{compact_count(row['review_count'])} reviews", 13, COLORS["ink"], "700"))
        body.append(text(x_bar, y + 99, "Source basis: Amazon/retailer demand signal cited in report", 13, COLORS["muted"]))

    save_svg("02_demand_proof.svg", "".join(body), width, height)


def chart_margin_calculation() -> None:
    width, height = 1300, 760
    body = title_block(
        "Margin Calculation",
        "Stacked bars show target price split into costs and profit before ads.",
    )
    parts = [
        ("supplier_cost", "Supplier", COLORS["supplier"]),
        ("packaging", "Packaging", COLORS["packaging"]),
        ("fulfillment", "Fulfillment", COLORS["fulfillment"]),
        ("fees", "Fees", COLORS["fees"]),
        ("profit", "Profit", COLORS["profit"]),
    ]

    x_label = 70
    x_bar = 385
    x_notes = 1015
    y_start = 170
    row_h = 150
    max_price = 16
    bar_w = 580
    bar_h = 48

    for tick in [0, 4, 8, 12, 16]:
        x = x_bar + tick / max_price * bar_w
        body.append(f'<line x1="{x:.1f}" y1="135" x2="{x:.1f}" y2="595" stroke="{COLORS["grid"]}"/>')
        body.append(text(x, 625, money(tick), 12, COLORS["muted"], anchor="middle"))

    for index, row in enumerate(PRODUCTS):
        y = y_start + index * row_h
        body.append(multiline(x_label, y - 2, wrap(row["product"], 29), 15, COLORS["ink"], "700", "start", 20))
        body.append(text(x_label, y + 62, f"Target price {money(row['target_price'])}", 13, COLORS["muted"], "700"))
        x = x_bar
        for key, label, color in parts:
            value = row[key]
            segment_w = value / max_price * bar_w
            body.append(rounded_rect(x, y - 10, segment_w, bar_h, color, "none", 8))
            if segment_w >= 72:
                body.append(text(x + segment_w / 2, y + 20, money(value), 12, "#ffffff", "700", "middle"))
            x += segment_w
        body.append(text(x_notes, y - 4, f"Margin: {pct(row['margin_percent'])}", 20, product_color(index), "700"))
        body.append(text(x_notes, y + 27, f"Profit before ads: {money(row['profit'])}", 13, COLORS["ink"], "700"))
        body.append(text(x_notes, y + 53, f"Break-even ad cost: {money(row['break_even_ad_cost'])}", 13, COLORS["muted"]))

    legend_x = 70
    legend_y = 690
    for key, label, color in parts:
        body.append(rounded_rect(legend_x, legend_y - 14, 24, 16, color, "none", 4))
        body.append(text(legend_x + 34, legend_y, label, 13, COLORS["muted"], "700"))
        legend_x += 165

    save_svg("03_margin_calculation.svg", "".join(body), width, height)


def chart_risk_assessment() -> None:
    width, height = 1300, 720
    body = title_block(
        "Risk Assessment",
        "Scale: 1 = low risk, 5 = high risk. New products avoid electronics, plumbing, and fragile parts.",
    )
    cols = ["Saturation", "Quality", "Fulfillment", "Returns", "Compliance/Fit"]
    x0 = 295
    y0 = 160
    cell_w = 140
    row_h = 112

    for col_index, col in enumerate(cols):
        x = x0 + col_index * cell_w + cell_w / 2
        body.append(multiline(x, y0 - 45, wrap(col, 13), 13, COLORS["muted"], "700", "middle", 15))
    body.append(text(1075, y0 - 27, "Overall risk", 13, COLORS["muted"], "700", "middle"))

    for row_index, row in enumerate(RISK_ROWS):
        y = y0 + row_index * row_h
        body.append(rounded_rect(55, y - 26, 1190, 92, "#ffffff" if row_index % 2 == 0 else "#f8fafc", COLORS["grid"], 12))
        body.append(multiline(75, y + 8, wrap(row["product"], 20), 15, COLORS["ink"], "700", "start", 19))
        for col_index, col in enumerate(cols):
            value = int(row[col])
            x = x0 + col_index * cell_w
            body.append(rounded_rect(x, y - 10, cell_w - 16, 54, risk_color(value), "none", 10))
            body.append(text(x + (cell_w - 16) / 2, y + 25, value, 22, "#ffffff", "700", "middle"))
        overall_color = COLORS["risk_mid"] if row["Overall"] == "Medium" else COLORS["risk_low"]
        body.append(rounded_rect(1005, y - 10, 150, 54, overall_color, "none", 27))
        body.append(text(1080, y + 24, row["Overall"], 14, "#ffffff", "700", "middle"))

    legend_y = 640
    legend = [("Low", COLORS["risk_low"]), ("Medium", COLORS["risk_mid"]), ("High", COLORS["risk_high"])]
    for index, (label, color) in enumerate(legend):
        x = 70 + index * 150
        body.append(rounded_rect(x, legend_y - 16, 28, 18, color, "none", 5))
        body.append(text(x + 38, legend_y, label, 13, COLORS["muted"], "700"))

    save_svg("04_risk_assessment.svg", "".join(body), width, height)


def create_readme() -> None:
    content = """# Product Validation Visualizations

Research date: May 6, 2026

This folder contains only the required visualizations for `assignment5/Product-Validation-Report.md`.

## Charts

1. [Validated products and go / no-go recommendation](charts/01_validated_products_go_no_go.svg)
2. [Demand proof](charts/02_demand_proof.svg)
3. [Margin calculation](charts/03_margin_calculation.svg)
4. [Risk assessment](charts/04_risk_assessment.svg)

## Data Files

- [Product summary data](data/product_summary.csv)
- [Risk score data](data/risk_scores.csv)
- [Readable data tables](data-tables.md)

## Colab Notebook

Open `product_validation_visualizations_colab.ipynb` in Google Colab to regenerate the required charts with `pandas`, `matplotlib`, and `seaborn`.
"""
    (ROOT / "README.md").write_text(content, encoding="utf-8")


def notebook_cell(cell_type: str, source: str) -> dict:
    cell = {
        "cell_type": cell_type,
        "metadata": {},
        "source": [line + "\n" for line in source.rstrip().splitlines()],
    }
    if cell_type == "code":
        cell["outputs"] = []
        cell["execution_count"] = None
    return cell


def create_notebook() -> None:
    product_data = json.dumps(PRODUCTS, indent=2)
    risk_data = json.dumps(RISK_ROWS, indent=2)
    cells = [
        notebook_cell(
            "markdown",
            """# Product Validation Visualizations

This notebook regenerates only the required visuals:

- Validated products with go / no-go recommendation
- Demand proof
- Margin calculation
- Risk assessment

Research date: May 6, 2026""",
        ),
        notebook_cell(
            "code",
            """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", context="notebook")
plt.rcParams["axes.titleweight"] = "bold"
palette = ["#0f766e", "#2563eb", "#c2410c"]""",
        ),
        notebook_cell(
            "code",
            f"""product_data = {product_data}
risk_data = {risk_data}

df = pd.DataFrame(product_data)
risk_df = pd.DataFrame(risk_data).set_index("product")
df""",
        ),
        notebook_cell("markdown", "## 1. Validated Products and Go / No-Go Recommendation"),
        notebook_cell("code", """display(df[["rank", "product", "margin_percent", "risk_level", "decision"]])"""),
        notebook_cell("markdown", "## 2. Demand Proof"),
        notebook_cell(
            "code",
            """fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)

sns.barplot(data=df, y="short", x="monthly_sales_proof", palette=palette, ax=axes[0])
axes[0].set_title("Monthly Sales Proof")
axes[0].set_xlabel("Observed monthly sales")
axes[0].set_ylabel("")
axes[0].bar_label(axes[0].containers[0], labels=[f"{v/1000:.1f}K+" for v in df["monthly_sales_proof"]], padding=5)

sns.barplot(data=df, y="short", x="review_count", palette=palette, ax=axes[1])
axes[1].set_title("Review Proof")
axes[1].set_xlabel("Review count")
axes[1].set_ylabel("")
axes[1].bar_label(axes[1].containers[0], labels=[f"{v/1000:.1f}K" for v in df["review_count"]], padding=5)

plt.tight_layout()
plt.show()""",
        ),
        notebook_cell("markdown", "## 3. Margin Calculation"),
        notebook_cell(
            "code",
            """parts = ["supplier_cost", "packaging", "fulfillment", "fees", "profit"]
labels = ["Supplier", "Packaging", "Fulfillment", "Fees", "Profit"]
colors = ["#0ea5e9", "#a855f7", "#f97316", "#64748b", "#16a34a"]

fig, ax = plt.subplots(figsize=(13, 5.5))
left = np.zeros(len(df))
for part, label, color in zip(parts, labels, colors):
    ax.barh(df["short"], df[part], left=left, label=label, color=color)
    left += df[part]

for i, row in df.iterrows():
    ax.text(row["target_price"] + 0.2, i, f"Price ${row['target_price']:.2f} | Margin {row['margin_percent']:.1f}%", va="center", weight="bold")

ax.set_title("Margin Calculation: Unit Economics")
ax.set_xlabel("USD")
ax.set_ylabel("")
ax.legend(ncol=5, bbox_to_anchor=(0.5, -0.14), loc="upper center")
plt.tight_layout()
plt.show()""",
        ),
        notebook_cell("markdown", "## 4. Risk Assessment"),
        notebook_cell(
            "code",
            """risk_numeric = risk_df.drop(columns=["Overall"])
plt.figure(figsize=(12, 4.8))
sns.heatmap(risk_numeric, annot=True, cmap="RdYlGn_r", vmin=1, vmax=5, linewidths=0.8, cbar_kws={"label": "Risk score"})
plt.title("Risk Assessment")
plt.xlabel("")
plt.ylabel("")
plt.tight_layout()
plt.show()""",
        ),
    ]

    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.x"},
            "colab": {"provenance": []},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    (ROOT / "product_validation_visualizations_colab.ipynb").write_text(json.dumps(notebook, indent=2), encoding="utf-8")


def main() -> None:
    ensure_dirs()
    write_csvs()
    create_data_tables()
    chart_validated_products()
    chart_demand_proof()
    chart_margin_calculation()
    chart_risk_assessment()
    create_readme()
    create_notebook()
    print(f"Generated visualizations in {ROOT}")


if __name__ == "__main__":
    main()
