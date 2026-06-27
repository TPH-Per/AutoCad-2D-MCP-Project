# 05 - DWG-003: Bracket Type-B Detail

## Objective
Create detailed fabrication drawings for the corner bracket (Type-B).

## Drawing Contents
1.  **Front View:** Profile view of a modified bracket designed for corner mounting (e.g., an angle bracket or a T-shaped bracket).
2.  **Top / Side Views:** Corresponding projections.
3.  **Section Cuts:** A cross-section view showing welding or specific bending details.

## Technical Details
*   **Scale:** 1:5.
*   **Material:** SUS304 Stainless Steel.
*   **Features:** Asymmetrical design for edge/corner conditions.

## Agent Execution Prompt

```text
[AGENT PROMPT: DWG-003]
Create DWG-003 Bracket Type-B Detail.
Scale: 1:5.
Steps:
1. Draw Front View of a T-shaped or Corner bracket at (0,0) on 0-OUTLINE.
2. Draw the Top View showing the mounting geometry.
3. Add a section cut (A-A) to show the profile thickness and bend/weld locations.
4. Add hidden lines on 0-HIDDEN to show internal features.
5. Apply ANSI31 hatch to the section cut on 0-HATCH.
6. Add dimensions and centerlines.
7. Insert Title Block (DWG-003, Part: CW BRACKET TYPE-B (CORNER), Scale: 1:5).
8. Save as DWG-003_Bracket-Type-B.dwg.
```
