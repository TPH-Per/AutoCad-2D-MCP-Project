# Loop Triage State - V2 Upgrade

## High-Priority Items (Act on these)
- **V2 Architecture Planning**: Break down the abstract V2 requirements (C# integration, 3D modeling, Calc Engine) into concrete `.md` planning files.
  - Action: Create `plans/09-v2-architecture.md`, `plans/10-csharp-integration.md`, `plans/11-calc-engine.md`.
- **Implement Engineering Calculation Engine**: 
  - Action: Write `calc_engine.py` to calculate structural load, stress analysis, and material weight.
- **Implement C# .NET AutoCAD Plugin**:
  - Action: Create a C# project (`CsharpPlugin`) using AutoCAD ObjectARX / .NET API to handle 3D solid operations and mass properties calculations.
- **Enhance Python MCP Server (v2)**:
  - Action: Update `autocad_mcp_server.py` to include new 3D COM tools, PDF export, and integration with the Calc Engine and C# plugin.
- **Create 3D Execution Scripts**:
  - Action: Write `scripts/draw_dwg_3d_bracket.py` to demonstrate the V2 capabilities (extruding 3D profile, boolean ops).

## Watch Items
- **AutoCAD Runtime Dependencies**:
  - Why: The C# plugin requires AutoCAD assemblies (`acmgd.dll`, `acdbmgd.dll`, `accoremgd.dll`) to compile. Since AutoCAD might not be installed in the CI/CD environment, we must use mock references or nuget packages (like `AutoCAD.NET`) to compile successfully.
- **MCP Server Compatibility**: Ensure the new v2 tools don't break the existing v1 2D scripts.

## State Updates
- Project v1 (2D pure COM) completed successfully with 6 DWG planning files and execution scripts.
- Transitioning to Project v2: Hybrid Architecture (Python MCP + C# .NET Plugin + 3D + Calculations).
