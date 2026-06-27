# 11 - Engineering Calculation Engine (calc_engine.py)

## Objective
Provide a structural and material calculation engine that validates the bracket design before it is drawn. This ensures the shop drawings reflect physically viable and safe designs.

## Core Features
1. **Material Weight Calculation**: 
   * Input: Dimensions (L, W, H, thickness), hole diameters, material density (SUS304 = 7.93 g/cm³).
   * Output: Total mass in kg.
2. **Bending Stress (Cantilever Load)**:
   * Input: Dead load of the glass panel, wind load, lever arm length, moment of inertia of the section.
   * Output: Maximum bending stress ($\sigma = M \cdot y / I$).
   * Validation: Compare against SUS304 yield strength (approx 205 MPa).
3. **Anchor Bolt Shear/Pull-out**:
   * Calculate required shear capacity per bolt based on load distribution.

## MCP Server Integration
The MCP server will expose a tool `calc_evaluate_bracket(width, height, thickness, load_kg)` that the AI can call. If the stress exceeds safety factors, the AI can propose a thicker bracket before drafting.
