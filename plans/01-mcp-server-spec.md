# 01 — MCP Server Specification
## AutoCAD Bridge via COM Automation

---

## Overview

The MCP server bridges the AI Agent to AutoCAD via Python COM automation (pywin32).
It uses the `FastMCP` pattern from the `mcp` Python SDK with stdio transport.

### Architecture
```
AI Agent (Claude/Antigravity) 
    → MCP Protocol (JSON-RPC over stdio)
        → Python MCP Server (FastMCP)
            → win32com.client → AutoCAD COM API
                → AutoCAD Application (acad.exe)
```

### Prerequisites
- Python 3.10+
- `pip install pywin32 "mcp[cli]"`
- AutoCAD 2022/2023/2024 must be running with a blank drawing open
- Windows OS (COM automation is Windows-only)

---

## Tool Inventory

### Category 1: Document Management

| # | Tool Name | Purpose | Parameters |
|---|---|---|---|
| 1 | `acad_new_drawing` | Create new drawing from template | `template: str = "acad.dwt"` |
| 2 | `acad_save` | Save active drawing | `filepath: str = ""` |
| 3 | `acad_zoom_extents` | Zoom to show all objects | None |
| 4 | `acad_regen` | Regenerate display | None |

### Category 2: Layer & Style Management

| # | Tool Name | Purpose | Key Parameters |
|---|---|---|---|
| 5 | `acad_add_layer` | Create/update layer | `name, color (ACI int), linetype (str), lineweight (int, hundredths of mm)` |
| 6 | `acad_set_active_layer` | Set current layer | `layer_name: str` |
| 7 | `acad_create_dimstyle` | Create JIS dimension style | `name, text_height, arrow_size, decimal_places, scale_factor` |
| 8 | `acad_create_text_style` | Create text style | `name, font, height` |
| 9 | `acad_load_linetype` | Load linetype from acad.lin | `name: str` |

### Category 3: Drawing Primitives

| # | Tool Name | Purpose | Key Parameters |
|---|---|---|---|
| 10 | `acad_draw_line` | Draw a line | `x1, y1, x2, y2, layer` |
| 11 | `acad_draw_polyline` | Draw 2D polyline | `points: [[x,y],...], closed: bool, layer` |
| 12 | `acad_draw_rectangle` | Draw rectangle (convenience) | `x, y, width, height, layer` |
| 13 | `acad_draw_circle` | Draw circle | `cx, cy, radius, layer` |
| 14 | `acad_draw_arc` | Draw arc | `cx, cy, radius, start_deg, end_deg, layer` |

### Category 4: Annotation

| # | Tool Name | Purpose | Key Parameters |
|---|---|---|---|
| 15 | `acad_add_text` | Single-line text | `x, y, content, height, layer, rotation_deg` |
| 16 | `acad_add_mtext` | Multi-line text | `x, y, content, width, height, layer` |
| 17 | `acad_add_dimension_linear` | Aligned dimension | `x1, y1, x2, y2, offset, layer, text_override` |
| 18 | `acad_add_leader` | Leader with text | `points: [[x,y],...], text, text_height, layer` |

### Category 5: Hatching

| # | Tool Name | Purpose | Key Parameters |
|---|---|---|---|
| 19 | `acad_add_hatch` | Add hatch pattern | `boundary_points, pattern, scale, angle, layer` |

### Category 6: Templates

| # | Tool Name | Purpose | Key Parameters |
|---|---|---|---|
| 20 | `acad_draw_a3_border` | Draw A3 sheet border with JIS margins | `scale_factor: float = 1.0` |
| 21 | `acad_draw_title_block` | Draw JIS title block | `dwg_no, part_name, material, finish, scale_text, drawn_by, date, x, y, sf` |
| 22 | `acad_draw_bom_table` | Draw BOM table | `x, y, sf, headers, rows` |
| 23 | `acad_purge_construction` | Freeze construction layer | None |

---

## Critical Implementation Notes

### Point Creation
All 3D points MUST be created as VARIANT arrays:
```python
import win32com.client
import pythoncom

def APoint(x, y, z=0):
    return win32com.client.VARIANT(
        pythoncom.VT_ARRAY | pythoncom.VT_R8, 
        (float(x), float(y), float(z))
    )
```

### Polyline Points (DIFFERENT from 3D points)
AddLightWeightPolyline uses FLAT 2D array (no z-coordinate):
```python
flat = [x1, y1, x2, y2, x3, y3, ...]
pts = win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, flat)
```

### Lineweight Values
Lineweight uses integer hundredths of mm:
- 0.09mm → `9`
- 0.18mm → `18`
- 0.25mm → `25`  
- 0.50mm → `50`
- 0.70mm → `70`

### Hatch Pattern Types
- `0` = PreDefined (ANSI31, SOLID, etc. from acad.pat) ← USE THIS
- `1` = UserDefined
- `2` = CustomDefined

**MUST** call `hatch.Evaluate()` and `doc.Regen(True)` after creating hatch.

### Dimension Style Variables (JIS)
Key DIMVAR settings:
- `DIMTXT` = text height (3.5mm on paper)
- `DIMASZ` = arrow size (2.5mm on paper)
- `DIMTAD` = 1 (text above dimension line — JIS standard)
- `DIMEXO` = 1.0 (extension line offset from object)
- `DIMEXE` = 2.0 (extension line extend beyond dim line)
- `DIMDEC` = 1 (one decimal place)
- `DIMSCALE` = overall scale factor (matches drawing scale)
- `DIMTIH` = 0 (text aligned with dimension line)

### MCP Server Pattern (FastMCP)
```python
from mcp.server.fastmcp import FastMCP
import sys

mcp = FastMCP("autocad-mcp")

@mcp.tool()
def my_tool(param: str) -> str:
    """Tool description visible to agent."""
    # NEVER print to stdout!
    print("debug info", file=sys.stderr)
    return "result string"

if __name__ == "__main__":
    mcp.run(transport='stdio')
```

### Common Pitfalls Checklist
- [ ] All coordinates as float, never int
- [ ] Never print() to stdout in MCP server  
- [ ] Wrap linetype loading in try/except (already loaded = error)
- [ ] Call hatch.Evaluate() after AppendOuterLoop
- [ ] Use VT_DISPATCH array for hatch boundary objects
- [ ] Angles in radians for AddArc and PatternAngle
- [ ] AutoCAD must be running before server starts
- [ ] Call doc.Regen(True) after major drawing changes
- [ ] "Continuous" linetype is always available (don't load it)
