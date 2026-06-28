import asyncio
import sys
import os

# Add parent directory to path to import autocad_mcp_server
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import autocad_mcp_server as acad

async def main():
    print("Setting up DWG-002: Bracket Type-A Detail...")
    
    # 1. Setup Layers
    await acad.acad_add_layer("0-OUTLINE", color=7)
    await acad.acad_add_layer("0-HIDDEN", color=4, linetype="HIDDEN2")
    await acad.acad_add_layer("0-CENTER", color=1, linetype="CENTER2")
    await acad.acad_add_layer("0-DIMENSION", color=2)
    await acad.acad_add_layer("0-HATCH", color=3)
    await acad.acad_add_layer("0-TEXT-MAIN", color=7)
    await acad.acad_add_layer("0-TEXT-NOTE", color=6)
    await acad.acad_add_layer("0-TITLEBLOCK", color=7)
    
    # 2. Draw Front View (100x60x8mm)
    print("Drawing Front View...")
    front_pts = [[0, 0], [100, 0], [100, 8], [8, 8], [8, 60], [0, 60], [0, 0]]
    await acad.acad_draw_polyline(front_pts, closed=True, layer="0-OUTLINE")
    await acad.acad_add_hatch(front_pts, pattern="ANSI31", scale=0.5, layer="0-HATCH")
    
    # 3. Draw Top View
    print("Drawing Top View...")
    top_pts = [[0, 150], [100, 150], [100, 230], [0, 230], [0, 150]]
    await acad.acad_draw_polyline(top_pts, closed=True, layer="0-OUTLINE")
    # Slot holes in top view
    await acad.acad_draw_circle(30, 190, 7, layer="0-OUTLINE")
    await acad.acad_draw_circle(70, 190, 7, layer="0-OUTLINE")
    
    # 4. Draw Side View
    print("Drawing Side View...")
    side_pts = [[150, 0], [230, 0], [230, 8], [230, 8], [158, 8], [158, 60], [150, 60], [150, 0]]
    await acad.acad_draw_polyline(side_pts, closed=True, layer="0-OUTLINE")
    await acad.acad_draw_circle(190, 30, 6, layer="0-OUTLINE") # Ø12 hole
    
    # 5. Add Dimensions
    print("Adding Dimensions...")
    await acad.acad_add_dimension_linear(0, 0, 100, 0, offset=-20, layer="0-DIMENSION")
    await acad.acad_add_dimension_linear(0, 0, 0, 60, offset=-20, layer="0-DIMENSION")
    await acad.acad_add_dimension_linear(0, 0, 8, 0, offset=-40, layer="0-DIMENSION", text_override="8 (t=8.0)")
    
    # 6. Title Block
    print("Adding Title Block...")
    tb_pts = [[250, 0], [450, 0], [450, 60], [250, 60], [250, 0]]
    await acad.acad_draw_polyline(tb_pts, closed=True, layer="0-TITLEBLOCK")
    await acad.acad_add_text(260, 45, "DWG-002: CW BRACKET TYPE-A", height=5.0, layer="0-TEXT-MAIN")
    await acad.acad_add_text(260, 30, "Material: SUS304", height=4.0, layer="0-TEXT-MAIN")
    await acad.acad_add_text(260, 15, "Scale 1:5", height=4.0, layer="0-TEXT-MAIN")
    
    # 7. Zoom and Save
    await acad.acad_zoom_extents()
    out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "drawings", "DWG-002_Bracket-Type-A.dwg")
    await acad.acad_save(out_path)
    print(f"Finished DWG-002. Save path: {out_path}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Error connecting to AutoCAD: {e}")
        print("Please ensure AutoCAD is open before running this script.")
