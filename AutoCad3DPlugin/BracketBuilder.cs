using System;
using Autodesk.AutoCAD.Runtime;
using Autodesk.AutoCAD.ApplicationServices;
using Autodesk.AutoCAD.DatabaseServices;
using Autodesk.AutoCAD.Geometry;
using Autodesk.AutoCAD.EditorInput;

namespace AutoCad3DPlugin
{
    public class BracketBuilder
    {
        [CommandMethod("DRAW3DBRACKET")]
        public void Draw3DBracket()
        {
            Document doc = Application.DocumentManager.MdiActiveDocument;
            Database db = doc.Database;
            Editor ed = doc.Editor;

            using (Transaction tr = db.TransactionManager.StartTransaction())
            {
                BlockTable bt = (BlockTable)tr.GetObject(db.BlockTableId, OpenMode.ForRead);
                BlockTableRecord btr = (BlockTableRecord)tr.GetObject(bt[BlockTableRecord.ModelSpace], OpenMode.ForWrite);

                // Create the 2D profile for the L-Bracket
                Polyline profile = new Polyline();
                profile.AddVertexAt(0, new Point2d(0, 0), 0, 0, 0);
                profile.AddVertexAt(1, new Point2d(100, 0), 0, 0, 0);
                profile.AddVertexAt(2, new Point2d(100, 8), 0, 0, 0);
                profile.AddVertexAt(3, new Point2d(8, 8), 0, 0, 0);
                profile.AddVertexAt(4, new Point2d(8, 60), 0, 0, 0);
                profile.AddVertexAt(5, new Point2d(0, 60), 0, 0, 0);
                profile.Closed = true;

                // Create a Region from the polyline
                DBObjectCollection objs = new DBObjectCollection();
                objs.Add(profile);
                DBObjectCollection regions = Region.CreateFromCurves(objs);
                Region reg = (Region)regions[0];

                // Extrude the Region to create a 3D Solid (Width = 80mm)
                Solid3d bracketSolid = new Solid3d();
                bracketSolid.Extrude(reg, 80.0, 0.0);
                
                // Add Hole (Subtract Cylinder)
                Solid3d holeSolid = new Solid3d();
                holeSolid.CreateFrustum(8, 6, 6, 6); // height=8, radius=6
                // Move hole to correct position: x=190 in top view -> x=50, y=4, z=40
                holeSolid.TransformBy(Matrix3d.Displacement(new Vector3d(50, 4, 40)));
                
                // Subtract hole
                bracketSolid.BooleanOperation(BooleanOperationType.BoolSubtract, holeSolid);

                // Calculate Mass Properties
                double volume = bracketSolid.MassProperties.Volume;
                // Density of SUS304 in kg/mm3 is 7.93e-6
                double massKg = volume * 7.93e-6;

                // Add solid to drawing
                btr.AppendEntity(bracketSolid);
                tr.AddNewlyCreatedDBObject(bracketSolid, true);

                ed.WriteMessage($"\n3D Bracket generated successfully.");
                ed.WriteMessage($"\nVolume: {volume:F2} mm^3");
                ed.WriteMessage($"\nEstimated Weight (SUS304): {massKg:F2} kg");

                tr.Commit();
            }
        }
    }
}
