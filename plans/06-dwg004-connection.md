# 06 - DWG-004: Connection & Anchor Detail

## Objective
Detail the mechanical connections between the bracket, the concrete structure, and the mullion.

## Drawing Contents
1.  **Concrete Anchor Detail:** Zoomed-in view of the wedge anchor or cast-in channel securing the backplate to the concrete.
2.  **Weld Detail:** If the bracket is welded to an embedment plate, show the weld symbols and fillet/butt weld profiles.
3.  **Adjustment Connection:** Detail of the slotted hole and adjustment bolt connecting the bracket to the mullion.

## Technical Details
*   **Scale:** 1:2 or 1:5.
*   **Standards:** JIS Z 3021 for welding symbols.
*   **Annotations:** Specific callouts for anchor bolt torque, washer sizes, and weld throat thickness.

## Agent Execution Prompt

```text
[AGENT PROMPT: DWG-004]
Create DWG-004 Connection & Anchor Detail.
Scale: 1:2.
Steps:
1. Draw a detailed view of an M12 anchor bolt expanding into concrete.
2. Draw a welded joint detail between a bracket plate and an embed plate.
3. Use 0-WELD layer to draw JIS Z 3021 weld symbols (e.g., Fillet weld triangle, 5mm throat).
4. Add multi-line text (MTEXT) specifying anchor pull-out requirements and weld inspection notes.
5. Insert Title Block (DWG-004, Part: CONNECTION DETAILS, Scale: 1:2).
6. Save as DWG-004_Connection-Detail.dwg.
```
