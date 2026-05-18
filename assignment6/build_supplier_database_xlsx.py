from __future__ import annotations

import csv
import html
import struct
import zlib
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parent
CSV_PATH = ROOT / "Supplier-Database-Sheet.csv"
XLSX_PATH = ROOT / "Supplier-Database-Sheet-With-Images.xlsx"
IMAGE_DIR = ROOT / "product-images"


def xml_escape(value: object) -> str:
    return html.escape(str(value), quote=True)


def png_chunk(kind: bytes, data: bytes) -> bytes:
    return (
        struct.pack(">I", len(data))
        + kind
        + data
        + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)
    )


def save_png(path: Path, width: int, height: int, pixels: bytearray) -> None:
    raw = bytearray()
    stride = width * 4
    for y in range(height):
        raw.append(0)
        raw.extend(pixels[y * stride : (y + 1) * stride])
    png = (
        b"\x89PNG\r\n\x1a\n"
        + png_chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0))
        + png_chunk(b"IDAT", zlib.compress(bytes(raw), 9))
        + png_chunk(b"IEND", b"")
    )
    path.write_bytes(png)


def hex_to_rgba(color: str) -> tuple[int, int, int, int]:
    color = color.lstrip("#")
    return int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16), 255


def draw_rect(pixels: bytearray, width: int, height: int, x0: int, y0: int, x1: int, y1: int, color: str) -> None:
    r, g, b, a = hex_to_rgba(color)
    x0, y0 = max(0, x0), max(0, y0)
    x1, y1 = min(width, x1), min(height, y1)
    for y in range(y0, y1):
        for x in range(x0, x1):
            i = (y * width + x) * 4
            pixels[i : i + 4] = bytes((r, g, b, a))


def draw_outline(pixels: bytearray, width: int, height: int, x0: int, y0: int, x1: int, y1: int, color: str, thickness: int = 3) -> None:
    draw_rect(pixels, width, height, x0, y0, x1, y0 + thickness, color)
    draw_rect(pixels, width, height, x0, y1 - thickness, x1, y1, color)
    draw_rect(pixels, width, height, x0, y0, x0 + thickness, y1, color)
    draw_rect(pixels, width, height, x1 - thickness, y0, x1, y1, color)


def make_canvas(bg: str = "#f5ead8", width: int = 420, height: int = 300) -> tuple[int, int, bytearray]:
    pixels = bytearray(width * height * 4)
    draw_rect(pixels, width, height, 0, 0, width, height, bg)
    return width, height, pixels


def draw_dishcloth_image(path: Path) -> None:
    width, height, pixels = make_canvas()
    draw_rect(pixels, width, height, 52, 232, 368, 254, "#dfc9aa")
    cloths = [
        (82, 78, 286, 218, "#1f9f8a", "#0f766e"),
        (106, 60, 310, 208, "#f2b84b", "#c27c0e"),
        (130, 42, 334, 198, "#cfe8d8", "#6aa586"),
    ]
    for x0, y0, x1, y1, fill, border in cloths:
        draw_rect(pixels, width, height, x0 + 8, y0 + 8, x1 + 8, y1 + 8, "#c9b294")
        draw_rect(pixels, width, height, x0, y0, x1, y1, fill)
        draw_outline(pixels, width, height, x0, y0, x1, y1, border, 4)
        for y in range(y0 + 16, y1 - 8, 24):
            for x in range(x0 + 14, x1 - 10, 30):
                draw_rect(pixels, width, height, x, y, x + 5, y + 5, "#ffffff")
    draw_rect(pixels, width, height, 114, 124, 350, 166, "#fff7ed")
    draw_outline(pixels, width, height, 114, 124, 350, 166, "#c9a66b", 3)
    save_png(path, width, height, pixels)


def draw_gap_cover_image(path: Path) -> None:
    width, height, pixels = make_canvas("#eef6ff")
    draw_rect(pixels, width, height, 48, 210, 372, 242, "#cbd5e1")
    draw_rect(pixels, width, height, 72, 72, 196, 214, "#f8fafc")
    draw_outline(pixels, width, height, 72, 72, 196, 214, "#94a3b8", 4)
    draw_rect(pixels, width, height, 224, 72, 348, 214, "#f8fafc")
    draw_outline(pixels, width, height, 224, 72, 348, 214, "#94a3b8", 4)
    draw_rect(pixels, width, height, 190, 66, 230, 224, "#111827")
    draw_rect(pixels, width, height, 176, 96, 244, 132, "#0f172a")
    draw_rect(pixels, width, height, 172, 104, 248, 124, "#2563eb")
    draw_rect(pixels, width, height, 183, 138, 237, 170, "#0f172a")
    save_png(path, width, height, pixels)


def draw_pillowcase_image(path: Path) -> None:
    width, height, pixels = make_canvas("#fdf2f8")
    draw_rect(pixels, width, height, 62, 220, 358, 250, "#e9d5ff")
    draw_rect(pixels, width, height, 86, 82, 334, 208, "#f9a8d4")
    draw_outline(pixels, width, height, 86, 82, 334, 208, "#be185d", 5)
    draw_rect(pixels, width, height, 114, 108, 306, 186, "#fbcfe8")
    draw_outline(pixels, width, height, 114, 108, 306, 186, "#db2777", 3)
    draw_rect(pixels, width, height, 250, 91, 319, 199, "#f472b6")
    draw_rect(pixels, width, height, 260, 102, 309, 188, "#f9a8d4")
    save_png(path, width, height, pixels)


def create_images() -> dict[str, Path]:
    IMAGE_DIR.mkdir(exist_ok=True)
    images = {
        "Swedish dishcloths / reusable kitchen cleaning cloths": IMAGE_DIR / "swedish-dishcloth.png",
        "Silicone stove gap covers, 2-pack": IMAGE_DIR / "silicone-stove-gap-cover.png",
        "Satin pillowcase 2-pack": IMAGE_DIR / "satin-pillowcase.png",
    }
    draw_dishcloth_image(images["Swedish dishcloths / reusable kitchen cleaning cloths"])
    draw_gap_cover_image(images["Silicone stove gap covers, 2-pack"])
    draw_pillowcase_image(images["Satin pillowcase 2-pack"])
    return images


def column_name(index: int) -> str:
    name = ""
    while index:
        index, remainder = divmod(index - 1, 26)
        name = chr(65 + remainder) + name
    return name


def inline_cell(ref: str, value: object, style: int = 0) -> str:
    return f'<c r="{ref}" t="inlineStr" s="{style}"><is><t>{xml_escape(value)}</t></is></c>'


def build_sheet_xml(rows: list[dict[str, str]]) -> str:
    headers = [
        "Product Image",
        "Product Name",
        "Supplier Name",
        "Platform",
        "Trust Score",
        "MOQ",
        "Unit Price Range",
        "Verification Basis",
        "Source URL",
    ]
    widths = [24, 38, 42, 14, 14, 18, 22, 58, 52]
    cols = "".join(
        f'<col min="{i}" max="{i}" width="{width}" customWidth="1"/>'
        for i, width in enumerate(widths, start=1)
    )
    sheet_rows = ['<row r="1" ht="32" customHeight="1">']
    for index, header in enumerate(headers, start=1):
        sheet_rows.append(inline_cell(f"{column_name(index)}1", header, 1))
    sheet_rows.append("</row>")
    for row_index, row in enumerate(rows, start=2):
        sheet_rows.append(f'<row r="{row_index}" ht="126" customHeight="1">')
        values = [
            "",
            row["product"],
            row["supplier_name"],
            row["platform"],
            row["trust_score"],
            row["moq"],
            row["unit_price_range"],
            row["verification_basis"],
            row["source_url"],
        ]
        for col_index, value in enumerate(values, start=1):
            if col_index == 1:
                continue
            sheet_rows.append(inline_cell(f"{column_name(col_index)}{row_index}", value, 2))
        sheet_rows.append("</row>")
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheetViews><sheetView workbookViewId="0"/></sheetViews>
  <sheetFormatPr defaultRowHeight="18"/>
  <cols>{cols}</cols>
  <sheetData>{"".join(sheet_rows)}</sheetData>
  <drawing r:id="rId1"/>
</worksheet>'''


def build_drawing_xml(rows: list[dict[str, str]]) -> str:
    product_to_rid = {
        "Swedish dishcloths / reusable kitchen cleaning cloths": "rId1",
        "Silicone stove gap covers, 2-pack": "rId2",
        "Satin pillowcase 2-pack": "rId3",
    }
    anchors = []
    for index, row in enumerate(rows, start=1):
        pic_id = index
        anchors.append(
            f'''<xdr:oneCellAnchor>
  <xdr:from><xdr:col>0</xdr:col><xdr:colOff>114300</xdr:colOff><xdr:row>{index}</xdr:row><xdr:rowOff>95250</xdr:rowOff></xdr:from>
  <xdr:ext cx="1371600" cy="952500"/>
  <xdr:pic>
    <xdr:nvPicPr>
      <xdr:cNvPr id="{pic_id}" name="Product Image {pic_id}"/>
      <xdr:cNvPicPr/>
    </xdr:nvPicPr>
    <xdr:blipFill>
      <a:blip r:embed="{product_to_rid[row["product"]]}"/>
      <a:stretch><a:fillRect/></a:stretch>
    </xdr:blipFill>
    <xdr:spPr><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></xdr:spPr>
  </xdr:pic>
  <xdr:clientData/>
</xdr:oneCellAnchor>'''
        )
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<xdr:wsDr xmlns:xdr="http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing"
 xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
{"".join(anchors)}
</xdr:wsDr>'''


def build_xlsx() -> None:
    with CSV_PATH.open(newline="", encoding="utf-8-sig") as file:
        rows = list(csv.DictReader(file))
    images = create_images()

    content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Default Extension="png" ContentType="image/png"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
  <Override PartName="/xl/drawings/drawing1.xml" ContentType="application/vnd.openxmlformats-officedocument.drawing+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>'''
    root_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>'''
    workbook = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets><sheet name="Supplier Database" sheetId="1" r:id="rId1"/></sheets>
</workbook>'''
    workbook_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>'''
    sheet_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/drawing" Target="../drawings/drawing1.xml"/>
</Relationships>'''
    drawing_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/swedish-dishcloth.png"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/silicone-stove-gap-cover.png"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/satin-pillowcase.png"/>
</Relationships>'''
    styles = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <fonts count="2">
    <font><sz val="11"/><name val="Calibri"/></font>
    <font><b/><sz val="11"/><color rgb="FFFFFFFF"/><name val="Calibri"/></font>
  </fonts>
  <fills count="3">
    <fill><patternFill patternType="none"/></fill>
    <fill><patternFill patternType="gray125"/></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FF1F4E78"/></patternFill></fill>
  </fills>
  <borders count="2">
    <border><left/><right/><top/><bottom/><diagonal/></border>
    <border><left style="thin"/><right style="thin"/><top style="thin"/><bottom style="thin"/><diagonal/></border>
  </borders>
  <cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
  <cellXfs count="3">
    <xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyBorder="1"/>
    <xf numFmtId="0" fontId="1" fillId="2" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment horizontal="center" vertical="center" wrapText="1"/></xf>
    <xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyBorder="1" applyAlignment="1"><alignment vertical="center" wrapText="1"/></xf>
  </cellXfs>
  <cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>
</styleSheet>'''
    app = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"><Application>Codex</Application></Properties>'''
    core = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
 xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:title>Supplier Database Sheet</dc:title><dc:creator>Codex</dc:creator></cp:coreProperties>'''

    with ZipFile(XLSX_PATH, "w", ZIP_DEFLATED) as xlsx:
        xlsx.writestr("[Content_Types].xml", content_types)
        xlsx.writestr("_rels/.rels", root_rels)
        xlsx.writestr("xl/workbook.xml", workbook)
        xlsx.writestr("xl/_rels/workbook.xml.rels", workbook_rels)
        xlsx.writestr("xl/worksheets/sheet1.xml", build_sheet_xml(rows))
        xlsx.writestr("xl/worksheets/_rels/sheet1.xml.rels", sheet_rels)
        xlsx.writestr("xl/drawings/drawing1.xml", build_drawing_xml(rows))
        xlsx.writestr("xl/drawings/_rels/drawing1.xml.rels", drawing_rels)
        xlsx.writestr("xl/styles.xml", styles)
        xlsx.writestr("xl/media/swedish-dishcloth.png", images["Swedish dishcloths / reusable kitchen cleaning cloths"].read_bytes())
        xlsx.writestr("xl/media/silicone-stove-gap-cover.png", images["Silicone stove gap covers, 2-pack"].read_bytes())
        xlsx.writestr("xl/media/satin-pillowcase.png", images["Satin pillowcase 2-pack"].read_bytes())
        xlsx.writestr("docProps/app.xml", app)
        xlsx.writestr("docProps/core.xml", core)


if __name__ == "__main__":
    build_xlsx()
    print(f"Created {XLSX_PATH}")
