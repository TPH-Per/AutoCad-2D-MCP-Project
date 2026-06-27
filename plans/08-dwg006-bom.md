# 08 - DWG-006: Bill of Materials (BOM) & Specifications

## Objective
Create the final sheet containing the material take-off, surface finish specs, and general notes.

## Drawing Contents
1.  **BOM Table:** A grid drawn with lines containing standard columns: Item No, Part Name, Material, Qty, Size, Finish, Remarks.
2.  **General Notes:** Bilingual (Japanese/English) notes regarding tolerances, standards, and QA/QC requirements.

## Technical Details
*   **Scale:** 1:1 or N/A (Drawn directly on the A3 sheet size).
*   **Table Layout:** Use `acad_draw_line` to draw a grid. Use `acad_add_text` for cell contents.

## Agent Execution Prompt

```text
[AGENT PROMPT: DWG-006]
Create DWG-006 Bill of Materials.
Scale: 1:1.
Steps:
1. Draw a rectangular table frame (e.g., 300mm wide x 150mm high) on 0-OUTLINE.
2. Draw horizontal and vertical grid lines to create 7 columns and 8 rows on 0-OUTLINE.
3. Populate headers using acad_add_text on 0-TEXT-MAIN:
   - 品番 / No.
   - 品名 / Part Name
   - 材質 / Material
   - 数量 / Qty
   - サイズ / Size
   - 表面処理 / Finish
   - 備考 / Remark
4. Fill in data for at least 3 items (e.g., Bracket Type-A, Anchor Bolt, Shim Plate).
5. Add General Notes using acad_add_mtext on 0-TEXT-NOTE detailing JIS B 0001 compliance.
6. Insert Title Block (DWG-006, Part: BILL OF MATERIALS, Scale: N/A).
7. Save as DWG-006_BOM.dwg.
```
