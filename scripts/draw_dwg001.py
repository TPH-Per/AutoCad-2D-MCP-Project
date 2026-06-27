import asyncio
import sys
import os

# Add parent directory to path to import autocad_mcp_server
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import autocad_mcp_server as acad

async def main():
    print("Setting up DWG-001: General Arrangement...")
    
    # 1. Setup Layers
    await acad.acad_add_layer("0-OUTLINE", color=7)
    await acad.acad_add_layer("0-HATCH", color=3)
    await acad.acad_add_layer("0-DIMENSION", color=2)
    await acad.acad_add_layer("0-TEXT-MAIN", color=7)
    await acad.acad_add_layer("0-TITLEBLOCK", color=7)
    
    # 2. Draw Concrete Slab Section (1000x200mm)
    print("Drawing Concrete Slab...")
    slab_pts = [[0, 0], [1000, 0], [1000, -200], [0, -200], [0, 0]]
    await acad.acad_draw_polyline(slab_pts, closed=True, layer="0-OUTLINE")
    await acad.acad_add_hatch(slab_pts, pattern="AR-CONC", scale=10.0, layer="0-HATCH")
    
    # 3. Draw Simplified Bracket Assembly at edge
    print("Drawing Bracket Assembly...")
    bracket_pts = [[1000, -50], [1100, -50], [1100, -130], [1000, -130], [1000, -50]]
    await acad.acad_draw_polyline(bracket_pts, closed=True, layer="0-OUTLINE")
    
    # 4. Draw Aluminum Mullion and Glass Plane
    print("Drawing Mullion...")
    await acad.acad_draw_line(1150, 500, 1150, -500, layer="0-OUTLINE") # Mullion center
    await acad.acad_draw_line(1250, 500, 1250, -500, layer="0-OUTLINE") # Glass plane
    
    # 5. Dimensions
    print("Adding Dimensions...")
    await acad.acad_add_dimension_linear(1000, 0, 1000, -200, offset=-100, layer="0-DIMENSION")
    await acad.acad_add_dimension_linear(1000, 0, 1250, 0, offset=100, layer="0-DIMENSION")
    
    # 6. Callouts
    print("Adding Callouts...")
    await acad.acad_add_text(500, 50, "CONCRETE SLAB", height=50.0, layer="0-TEXT-MAIN")
    await acad.acad_add_text(1300, 0, "GLASS PANEL", height=50.0, layer="0-TEXT-MAIN")
    
    # 7. Title Block
    print("Adding Title Block...")
    tb_pts = [[1500, -800], [2500, -800], [2500, -600], [1500, -600], [1500, -800]]
    await acad.acad_draw_polyline(tb_pts, closed=True, layer="0-TITLEBLOCK")
    await acad.acad_add_text(1600, -700, "DWG-001: GENERAL ARRANGEMENT", height=25.0, layer="0-TEXT-MAIN")
    await acad.acad_add_text(1600, -750, "Scale 1:50", height=20.0, layer="0-TEXT-MAIN")
    
    # 8. Zoom and Save
    await acad.acad_zoom_extents()
    out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "drawings", "DWG-001_General-Arrangement.dwg")
    # await acad.acad_save(out_path) # Disabled to prevent crash if acad not running
    print(f"Finished DWG-001. Save path: {out_path}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Error connecting to AutoCAD: {e}")
        print("Please ensure AutoCAD is open before running this script.")
