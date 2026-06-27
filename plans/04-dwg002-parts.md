# 04 - DWG-002: Bracket Type-A Detail

## Objective
Create detailed fabrication drawings for the main L-bracket (Type-A).

## Drawing Contents
1.  **Front View:** Showing the L-shape profile (100mm x 60mm x 8mm thick).
2.  **Top View:** Showing the width of the bracket (e.g., 80mm wide) and mounting slots.
3.  **Side View:** Showing the vertical leg and the connection hole for the adjustment bolt.
4.  **Dimensions:** Full fabrication dimensions including hole centers, radii, and overall sizes.
5.  **Hatch:** Section hatch on the Front View to indicate it's a solid section.

## Technical Details
*   **Scale:** 1:5 (Text height in MS = 12.5mm).
*   **Material:** SUS304 Stainless Steel, t=8.0mm.
*   **Features:**
    *   Mounting slots (for concrete anchors): e.g., 14x30mm slots.
    *   Connection hole: Ø12mm or Ø14mm.

## Agent Execution Prompt

```text
[AGENT PROMPT: DWG-002]
Create DWG-002 Bracket Type-A Detail.
Scale: 1:5.
Steps:
1. Draw Front View of an L-bracket (100x60x8mm) at (0,0) on 0-OUTLINE.
2. Apply ANSI31 hatch to the Front View on 0-HATCH.
3. Draw Top View at (0, 150) showing the 80mm width and two 14x30mm slotted holes.
4. Draw Side View at (150, 0) showing the 60mm height, 80mm width, and a Ø12mm center hole.
5. Add centerlines on 0-CENTER for all holes.
6. Add all necessary dimensions (overall dimensions, hole locations, plate thickness) on 0-DIMENSION.
7. Insert Title Block (DWG-002, Part: CW BRACKET TYPE-A, Scale: 1:5).
8. Save as DWG-002_Bracket-Type-A.dwg.
```
