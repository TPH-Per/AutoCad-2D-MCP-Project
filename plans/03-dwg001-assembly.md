# 03 - DWG-001: General Arrangement (Mặt đứng tổng thể)

## Objective
Create the General Arrangement (GA) drawing showing the overview of the curtain wall bracket system installed on a building floor edge.

## Drawing Contents
1.  **Concrete Floor Slab / Edge Beam:** Section view of the concrete slab.
2.  **Bracket Assembly:** Placement of the curtain wall bracket anchored to the slab.
3.  **Mullion (Khung nhôm):** Indication of the vertical aluminum mullion attached to the bracket.
4.  **Glass Panels:** Reference lines showing the glass facade position.
5.  **Dimensions & Annotations:** Overall height, offset from slab to glass, and part callouts.

## Technical Details
*   **Scale:** 1:50 (Note: Scale text heights and dimension sizes by 50x in Model Space if drawing purely in MS).
*   **Geometry:**
    *   Floor Slab: 200mm thick.
    *   Edge distance: Bracket face to glass face is typically 150mm - 200mm.

## Agent Execution Prompt

```text
[AGENT PROMPT: DWG-001]
Create DWG-001 General Arrangement.
Scale: 1:50.
Steps:
1. Draw a section of the concrete slab (e.g., 1000x200mm) on 0-OUTLINE.
2. Add concrete hatch (AR-CONC or ANSI31) on 0-HATCH.
3. Draw a simplified bracket assembly attached to the edge.
4. Draw a vertical line representing the Aluminum Mullion and Glass plane.
5. Add dimensions showing the slab thickness and the distance from the slab edge to the glass.
6. Add callout MText for "CONCRETE SLAB", "CW BRACKET ASSEMBLY", "ALUMINUM MULLION".
7. Insert Title Block (DWG-001, Part: GENERAL ARRANGEMENT, Scale: 1:50).
8. Save as DWG-001_General-Arrangement.dwg.
```
