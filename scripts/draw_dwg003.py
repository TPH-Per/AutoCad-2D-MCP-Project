import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import autocad_mcp_server as acad

async def main():
    print("Setting up DWG-003: Bracket Type-B Detail...")
    
    await acad.acad_add_layer("0-OUTLINE", color=7)
    await acad.acad_add_layer("0-HATCH", color=3)
    await acad.acad_add_layer("0-DIMENSION", color=2)
    await acad.acad_add_layer("0-TEXT-MAIN", color=7)
    await acad.acad_add_layer("0-TITLEBLOCK", color=7)
    
    print("Drawing Corner Bracket Front View...")
    front_pts = [[0, 0], [150, 0], [150, 8], [8, 8], [8, 100], [0, 100], [0, 0]]
    await acad.acad_draw_polyline(front_pts, closed=True, layer="0-OUTLINE")
    await acad.acad_add_hatch(front_pts, pattern="ANSI31", scale=0.5, layer="0-HATCH")
    
    print("Drawing Corner Bracket Top View...")
    top_pts = [[0, 150], [150, 150], [150, 230], [0, 230], [0, 150]]
    await acad.acad_draw_polyline(top_pts, closed=True, layer="0-OUTLINE")
    
    print("Adding Dimensions...")
    await acad.acad_add_dimension_linear(0, 0, 150, 0, offset=-20, layer="0-DIMENSION")
    await acad.acad_add_dimension_linear(0, 0, 0, 100, offset=-20, layer="0-DIMENSION")
    
    print("Adding Title Block...")
    tb_pts = [[200, 0], [400, 0], [400, 60], [200, 60], [200, 0]]
    await acad.acad_draw_polyline(tb_pts, closed=True, layer="0-TITLEBLOCK")
    await acad.acad_add_text(210, 45, "DWG-003: CW BRACKET TYPE-B (CORNER)", height=5.0, layer="0-TEXT-MAIN")
    await acad.acad_add_text(210, 30, "Material: SUS304", height=4.0, layer="0-TEXT-MAIN")
    await acad.acad_add_text(210, 15, "Scale 1:5", height=4.0, layer="0-TEXT-MAIN")
    
    await acad.acad_zoom_extents()
    out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "drawings", "DWG-003_Bracket-Type-B.dwg")
    # await acad.acad_save(out_path)
    print(f"Finished DWG-003. Save path: {out_path}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Error connecting to AutoCAD: {e}")
