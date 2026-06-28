import asyncio
import sys
import os
import math

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import autocad_mcp_server as acad

async def main():
    print("Setting up DWG-005: Exploded View...")
    
    await acad.acad_add_layer("0-OUTLINE", color=7)
    await acad.acad_add_layer("0-HIDDEN", color=4, linetype="HIDDEN2")
    await acad.acad_add_layer("0-TEXT-MAIN", color=7)
    await acad.acad_add_layer("0-TITLEBLOCK", color=7)
    
    print("Drawing Isometric Parts...")
    # Fake isometric bracket using lines at 30 degrees
    start_x, start_y = 100, 100
    dx, dy = 100 * math.cos(math.radians(30)), 100 * math.sin(math.radians(30))
    await acad.acad_draw_line(start_x, start_y, start_x + dx, start_y + dy, layer="0-OUTLINE")
    await acad.acad_draw_line(start_x, start_y, start_x, start_y + 100, layer="0-OUTLINE")
    
    print("Drawing Assembly Trails...")
    await acad.acad_draw_line(start_x - 50, start_y - 50, start_x, start_y, layer="0-HIDDEN")
    
    print("Drawing Part Balloons...")
    await acad.acad_draw_circle(start_x + dx + 20, start_y + dy + 20, 10, layer="0-OUTLINE")
    await acad.acad_add_text(start_x + dx + 17, start_y + dy + 16, "1", height=8.0, layer="0-TEXT-MAIN")
    
    print("Adding Title Block...")
    tb_pts = [[0, 0], [400, 0], [400, 277], [0, 277], [0, 0]]
    await acad.acad_draw_polyline(tb_pts, closed=True, layer="0-TITLEBLOCK")
    await acad.acad_add_text(250, 45, "DWG-005: EXPLODED VIEW", height=5.0, layer="0-TEXT-MAIN")
    
    await acad.acad_zoom_extents()
    out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "drawings", "DWG-005_Exploded-View.dwg")
    await acad.acad_save(out_path)
    print(f"Finished DWG-005. Save path: {out_path}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Error connecting to AutoCAD: {e}")
