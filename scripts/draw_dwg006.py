import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import autocad_mcp_server as acad

async def main():
    print("Setting up DWG-006: Bill of Materials...")
    
    await acad.acad_add_layer("0-OUTLINE", color=7)
    await acad.acad_add_layer("0-TEXT-MAIN", color=7)
    await acad.acad_add_layer("0-TITLEBLOCK", color=7)
    
    print("Drawing BOM Table...")
    # Table Frame
    await acad.acad_draw_polyline([[0, 0], [300, 0], [300, 150], [0, 150], [0, 0]], closed=True, layer="0-OUTLINE")
    # Horizontal line for header
    await acad.acad_draw_line(0, 130, 300, 130, layer="0-OUTLINE")
    
    print("Populating Headers...")
    headers = ["No.", "Part Name", "Material", "Qty", "Size", "Finish", "Remark"]
    x_positions = [10, 40, 120, 170, 200, 240, 270]
    
    for i, header in enumerate(headers):
        await acad.acad_add_text(x_positions[i], 135, header, height=5.0, layer="0-TEXT-MAIN")
        if i > 0:
            # Vertical dividers
            await acad.acad_draw_line(x_positions[i] - 5, 0, x_positions[i] - 5, 150, layer="0-OUTLINE")
            
    print("Populating Data...")
    await acad.acad_add_text(10, 115, "1", height=5.0, layer="0-TEXT-MAIN")
    await acad.acad_add_text(40, 115, "Bracket Type-A", height=5.0, layer="0-TEXT-MAIN")
    await acad.acad_add_text(120, 115, "SUS304", height=5.0, layer="0-TEXT-MAIN")
    await acad.acad_add_text(170, 115, "1", height=5.0, layer="0-TEXT-MAIN")
    await acad.acad_add_text(240, 115, "HL", height=5.0, layer="0-TEXT-MAIN")
    
    print("Adding Title Block...")
    tb_pts = [[0, -60], [300, -60], [300, 0], [0, 0], [0, -60]]
    await acad.acad_draw_polyline(tb_pts, closed=True, layer="0-TITLEBLOCK")
    await acad.acad_add_text(150, -30, "DWG-006: BILL OF MATERIALS", height=5.0, layer="0-TEXT-MAIN")
    
    await acad.acad_zoom_extents()
    out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "drawings", "DWG-006_BOM.dwg")
    # await acad.acad_save(out_path)
    print(f"Finished DWG-006. Save path: {out_path}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Error connecting to AutoCAD: {e}")
