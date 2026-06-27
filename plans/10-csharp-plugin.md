# 10 - C# .NET Plugin Specification (AutoCad3DPlugin)

## Objective
Build a C# Class Library that interfaces with AutoCAD's managed .NET API to perform 3D solid modeling operations that are either too slow or too complex for the win32com bridge.

## Core Responsibilities
1. **Parametric 3D Solid Generation**: Accept parameters (width, height, thickness) and generate a 3D solid representation of the Curtain Wall Bracket.
   * Method: Extrude a 2D profile.
   * Boolean Operations: Subtract cylindrical solids to create bolt holes and slotted holes.
2. **Mass Properties Extraction**: Calculate the exact volume, centroid, and weight of the 3D solid using AutoCAD's underlying geometric engine.
3. **2D View Extraction (Future/Bonus)**: Automatically generate FLATSHOT or section views from the 3D model.

## Implementation Details
*   **Project Type:** .NET Standard / .NET Framework Class Library (AutoCAD 2022+ typically uses .NET Framework 4.8).
*   **Dependencies:** `AutoCAD.NET` NuGet package.
*   **Command Exposure:** Use `[CommandMethod("DRAW3DBRACKET")]`.
*   **Integration:** The Python MCP server will use `doc.SendCommand("NETLOAD ... \n")` and then `doc.SendCommand("DRAW3DBRACKET \n")`.
