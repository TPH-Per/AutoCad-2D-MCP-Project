# 02 - Drawing Environment Setup

## Objective
Establish the standard AutoCAD drawing environment (Layers, Linetypes, Dimension Styles, and Title Block structure) required for all JIS-compliant shop drawings in this package.

## Standard Specifications (JIS B 0001 / JIS B 3402)

### 1. Layers and Linetypes
A CAD operator must setup these layers before beginning any drawing:
*   `0-OUTLINE`: Color 7 (White), Linetype `Continuous`, Lineweight 0.50
*   `0-HIDDEN`: Color 4 (Cyan), Linetype `HIDDEN2`, Lineweight 0.25
*   `0-CENTER`: Color 1 (Red), Linetype `CENTER2`, Lineweight 0.18
*   `0-DIMENSION`: Color 2 (Yellow), Linetype `Continuous`, Lineweight 0.18
*   `0-HATCH`: Color 3 (Green), Linetype `Continuous`, Lineweight 0.18
*   `0-TEXT-MAIN`: Color 7 (White), Linetype `Continuous`, Lineweight 0.18
*   `0-TEXT-NOTE`: Color 6 (Magenta), Linetype `Continuous`, Lineweight 0.18
*   `0-TITLEBLOCK`: Color 7 (White), Linetype `Continuous`, Lineweight 0.70
*   `0-CONSTRUCTION`: Color 8 (Gray), Linetype `Continuous`, Lineweight 0.09
*   `0-WELD`: Color 5 (Blue), Linetype `Continuous`, Lineweight 0.18

*Note: The script must load `HIDDEN2` and `CENTER2` from `acad.lin`.*

### 2. Title Block Frame (A3 Sheet)
*   Sheet Size: 420 x 297 mm
*   Drawing Area Frame: 400 x 277 mm (Offset 10mm from edges).
*   Title Block Box: Typically placed at the bottom right corner (e.g., width 190mm, height 55mm).
*   Standard Fields to populate (JP / EN):
    *   図面番号 (DWG No.)
    *   品名 (Part Name)
    *   材質 (Material)
    *   表面処理 (Finish)
    *   縮尺 (Scale)
    *   作成日 (Date)
    *   作成者 (Drawn by)

### 3. Coordinate System & Scale
*   Model Space is drawn at 1:1 scale (1 unit = 1 mm).
*   For a 1:5 scaled viewport on an A3 layout, dimensions and text sizes must be scaled appropriately in Model space if layout space is not used for annotations.
    *   *Example: If printing at 1:5, a 2.5mm text height on paper needs to be drawn at 12.5mm height in Model Space.*

## Agent Execution Prompt

```text
[AGENT PROMPT: DRAWING SETUP]
Configure the AutoCAD environment for JIS standards.
Using the MCP server, ensure you have a Python script to:
1. Iterate through the standard layer list and call `acad_add_layer` to create them.
2. Setup text sizes and standard dimension offset factors to match the target scale.
3. Keep the `0-CONSTRUCTION` layer handy for drawing layout boundaries before finalizing.
```
