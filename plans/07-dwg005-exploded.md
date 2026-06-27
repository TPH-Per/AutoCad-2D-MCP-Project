# 07 - DWG-005: 3D Exploded View (2D Isometric)

## Objective
Provide a visual assembly guide for the shop floor and installation team.

## Drawing Contents
1.  **Isometric Projections:** 2D drawing of 3D parts aligned along 30-degree isometric axes.
2.  **Exploded Arrangement:** Show the Bracket Arm, Backplate, Shims, Washers, and Bolts separated along assembly axes.
3.  **Part Balloons:** Numbered balloons corresponding to the Bill of Materials.

## Technical Details
*   **Scale:** NTS (Not To Scale).
*   **Drafting Technique:** Use isometric snap/grid angles (30°, 150°, 90°) to draw the outlines. Use `acad_draw_line` and `acad_draw_arc` (ellipses might be required, or simplified circles) to fake 3D.

## Agent Execution Prompt

```text
[AGENT PROMPT: DWG-005]
Create DWG-005 Exploded View.
Scale: NTS.
Steps:
1. Draw an isometric view of the bracket arm using 30-degree lines on 0-OUTLINE.
2. Draw isometric representations of a bolt and washer displaced along the insertion axis.
3. Draw dashed trailing lines on 0-HIDDEN to show the path of assembly.
4. Draw circular balloons (using acad_draw_circle) with numbers (1, 2, 3...) inside them using acad_add_text on 0-TEXT-MAIN.
5. Draw leader lines pointing from the balloons to the parts.
6. Insert Title Block (DWG-005, Part: EXPLODED VIEW, Scale: NTS).
7. Save as DWG-005_Exploded-View.dwg.
```
