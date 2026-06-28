import win32com.client
import pythoncom
import math
import sys

# Try to connect to AutoCAD
try:
    acad = win32com.client.GetActiveObject("AutoCAD.Application")
    doc = acad.ActiveDocument
    msp = doc.ModelSpace
except Exception as e:
    # We will raise errors inside the functions if it's not connected, but let's try to add a document if ActiveDocument fails
    try:
        acad = win32com.client.GetActiveObject("AutoCAD.Application")
        doc = acad.Documents.Add()
        msp = doc.ModelSpace
    except Exception:
        acad = None
        doc = None
        msp = None

def get_msp():
    if msp is None:
        raise Exception("Not connected to AutoCAD")
    return msp

def get_doc():
    if doc is None:
        raise Exception("Not connected to AutoCAD")
    return doc

def aDouble(pts_list):
    import pythoncom
    import win32com.client
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, pts_list)

async def acad_add_layer(name: str, color: int, linetype: str = None):
    d = get_doc()
    try:
        layer = d.Layers.Item(name)
    except:
        layer = d.Layers.Add(name)
    layer.color = color
    if linetype:
        try:
            layer.Linetype = linetype
        except Exception:
            pass # Ignore if linetype isn't loaded

async def acad_draw_polyline(pts: list, closed: bool = False, layer: str = "0"):
    m = get_msp()
    flat_pts = []
    # 2D points for AddLightWeightPolyline
    for p in pts:
        flat_pts.extend([float(p[0]), float(p[1])])
    
    # Flatten point list
    pts_var = aDouble(flat_pts)
    pline = m.AddLightWeightPolyline(pts_var)
    pline.Closed = closed
    pline.Layer = layer
    return pline

async def acad_add_hatch(pts: list, pattern: str = "AR-CONC", scale: float = 10.0, layer: str = "0"):
    m = get_msp()
    # Create the hatch object (PatternType 1 = PreDefined)
    hatch = m.AddHatch(1, pattern, True)
    
    # Create boundary
    flat_pts = []
    for p in pts:
        flat_pts.extend([float(p[0]), float(p[1])])
    pts_var = aDouble(flat_pts)
    pline = m.AddLightWeightPolyline(pts_var)
    pline.Closed = True
    
    # Append outer loop using an array containing the polyline
    import pythoncom
    import win32com.client
    outer_loop = win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, [pline])
    hatch.AppendOuterLoop(outer_loop)
    hatch.PatternScale = scale
    hatch.Evaluate()
    hatch.Layer = layer
    # Optional: Delete boundary pline if we just wanted hatch, but usually keeping it or moving to hatch layer is fine
    pline.Delete()
    return hatch

async def acad_draw_line(x1, y1, x2, y2, layer: str = "0"):
    m = get_msp()
    pt1 = aDouble([float(x1), float(y1), 0.0])
    pt2 = aDouble([float(x2), float(y2), 0.0])
    line = m.AddLine(pt1, pt2)
    line.Layer = layer
    return line

async def acad_add_dimension_linear(x1, y1, x2, y2, offset: float, layer: str = "0", text_override: str = None):
    m = get_msp()
    pt1 = aDouble([float(x1), float(y1), 0.0])
    pt2 = aDouble([float(x2), float(y2), 0.0])
    
    # Calculate text position (offset perpendicularly or roughly by offset value)
    # This is a simplified positioning logic
    if abs(x2 - x1) > abs(y2 - y1):
        # Horizontal
        text_pt = aDouble([float((x1+x2)/2), float(y1 + offset), 0.0])
    else:
        # Vertical
        text_pt = aDouble([float(x1 + offset), float((y1+y2)/2), 0.0])
        
    dim = m.AddDimAligned(pt1, pt2, text_pt)
    dim.Layer = layer
    if text_override:
        dim.TextOverride = text_override
    return dim

async def acad_add_text(x, y, text: str, height: float, layer: str = "0"):
    m = get_msp()
    pt = aDouble([float(x), float(y), 0.0])
    txt = m.AddText(text, pt, height)
    txt.Layer = layer
    return txt

async def acad_draw_circle(cx, cy, radius, layer: str = "0"):
    m = get_msp()
    pt = aDouble([float(cx), float(cy), 0.0])
    circle = m.AddCircle(pt, float(radius))
    circle.Layer = layer
    return circle

async def acad_add_arc(cx, cy, radius, start_angle_deg, end_angle_deg, layer: str = "0"):
    m = get_msp()
    pt = aDouble([float(cx), float(cy), 0.0])
    # Convert deg to rad
    sa = math.radians(start_angle_deg)
    ea = math.radians(end_angle_deg)
    arc = m.AddArc(pt, float(radius), sa, ea)
    arc.Layer = layer
    return arc

async def acad_zoom_extents():
    if acad is not None:
        acad.ZoomExtents()

async def acad_save(path: str):
    d = get_doc()
    d.SaveAs(path)

