import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import autocad_mcp_server as acad

async def main():
    print("Setting up DWG-004: Connection Detail...")
    
    await acad.acad_add_layer("0-OUTLINE", color=7)
    await acad.acad_add_layer("0-WELD", color=5)
    await acad.acad_add_layer("0-TEXT-NOTE", color=6)
    await acad.acad_add_layer("0-TITLEBLOCK", color=7)
    
    print("Drawing Anchor Bolt Detail...")
    bolt_pts = [[0, 0], [20, 0], [20, 100], [0, 100], [0, 0]]
    await acad.acad_draw_polyline(bolt_pts, closed=True, layer="0-OUTLINE")
    await acad.acad_add_text(30, 50, "M12 WEDGE ANCHOR", height=5.0, layer="0-TEXT-NOTE")
    
    print("Drawing Weld Detail...")
    weld_plate = [[100, 0], [150, 0], [150, 10], [100, 10], [100, 0]]
    await acad.acad_draw_polyline(weld_plate, closed=True, layer="0-OUTLINE")
    # Weld symbol
    await acad.acad_draw_line(125, 10, 150, 30, layer="0-WELD")
    await acad.acad_draw_line(150, 30, 200, 30, layer="0-WELD")
    await acad.acad_draw_polyline([[175, 30], [175, 35], [180, 30]], closed=True, layer="0-WELD")
    await acad.acad_add_text(160, 32, "5", height=4.0, layer="0-WELD")
    
    print("Adding Title Block...")
    tb_pts = [[250, 0], [450, 0], [450, 60], [250, 60], [250, 0]]
    await acad.acad_draw_polyline(tb_pts, closed=True, layer="0-TITLEBLOCK")
    await acad.acad_add_text(260, 45, "DWG-004: CONNECTION DETAIL", height=5.0, layer="0-TEXT-NOTE")
    
    await acad.acad_zoom_extents()
    out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "drawings", "DWG-004_Connection-Detail.dwg")
    await acad.acad_save(out_path)
    print(f"Finished DWG-004. Save path: {out_path}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Error connecting to AutoCAD: {e}")
