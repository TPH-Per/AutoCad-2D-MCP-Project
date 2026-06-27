# 📋 MASTER PLAN — CW Bracket Shop Drawing Package (v2.0 — Corrected)
## Stainless Steel Curtain Wall Bracket System — Shop Drawing Package
### *Bộ Bản Vẽ Triển Khai: Hệ Thống Bracket Inox Mặt Dựng Kính*

---

## REVISION LOG

| Rev | Date | Changes |
|---|---|---|
| 1.0 | 2025-06 | Original plan |
| 2.0 | 2025-06 | Corrected geometry, enhanced MCP server, revised to 4 sheets, added realistic bracket specs |

---

## I. PROJECT SCOPE (REVISED)

### Deliverables: 4 sheets A3

| Sheet | Drawing No. | Title | Content | Scale |
|---|---|---|---|---|
| 1 | DWG-001 | Assembly Drawing | Front + Side + Top views, full dimensions, parts list | 1:2 |
| 2 | DWG-002 | Part Details | Individual part drawings: back plate, arm, gusset | 1:1 |
| 3 | DWG-003 | Connection & Weld Detail | Anchor detail, weld symbols, section cuts | 1:2 |
| 4 | DWG-004 | Installation GA | Bracket positions on curtain wall grid, typical bay | 1:20 |

### Product: CW Bracket Type-A

Total assembled: 150mm(H) x 120mm(projection) x 80mm(W)
Weight approx: 2.8 kg/piece

### Material Specification

| Property | Value |
|---|---|
| Material | SUS304 (JIS G 4305) |
| Back Plate | 150 x 80 x 8mm |
| Arm Plate | 120 x 80 x 8mm |
| Gusset Plate | ~60 x 60 x 6mm (right triangle) |
| Surface Finish | #400 Hairline Polish |
| Bolt Holes (Back) | 4x dia14 for M12 anchor bolts |
| Slotted Holes (Arm) | 2x 14x44mm for M12 adj. bolts |

---

## II. FILE STRUCTURE

```
autocad&mcp/
├── README.md
├── requirements.txt
├── mcp-server/
│   └── autocad_mcp_server.py
├── plans/
│   ├── 00-master-plan.md          <- This file
│   ├── 01-mcp-server-spec.md
│   ├── 02-drawing-setup.md
│   ├── 03-dwg001-assembly.md
│   ├── 04-dwg002-parts.md
│   ├── 05-dwg003-connection.md
│   ├── 06-dwg004-installation.md
│   ├── 07-bom-data.md
│   └── 08-finalize-export.md
├── drawings/
├── pdf-output/
├── reference/
└── scripts/
```

## III. EXECUTION ORDER

Phase 0: Setup -> Phase 1: DWG-001 -> Phase 2: DWG-002 -> Phase 3: DWG-003 -> Phase 4: DWG-004 -> Phase 5: Finalize
