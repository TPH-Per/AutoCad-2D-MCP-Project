import os
import sys
import time
import win32com.client

# Import the new Calculation Engine
from calc_engine import BracketCalcEngine

def main():
    print("=== AutoCAD V2: Hybrid 3D & Calculation Demo ===")
    
    # 1. Engineering Calculations (V2 Upgrade)
    print("\n[1/3] Running Engineering Calculations...")
    weight = BracketCalcEngine.calculate_weight(100, 60, 80, 8)
    print(f" -> Bracket Weight (SUS304): {weight:.2f} kg")
    
    stress_check = BracketCalcEngine.check_bending_stress(load_kg=100, lever_arm_mm=80, section_width_mm=80, thickness_mm=8)
    print(" -> Stress Check Results:")
    for k, v in stress_check.items():
        print(f"      {k}: {v}")
        
    if stress_check["status"] == "FAIL":
        print(" -> ERROR: Stress check failed. Bracket is unsafe.")
        sys.exit(1)
    
    # 2. Connect to AutoCAD
    print("\n[2/3] Connecting to AutoCAD...")
    try:
        acad = win32com.client.GetActiveObject("AutoCAD.Application")
        try:
            doc = acad.ActiveDocument
        except Exception:
            doc = acad.Documents.Add()
        print(f" -> Connected to: {doc.Name}")
    except Exception as e:
        print(f" -> ERROR: AutoCAD COM connection failed: {e}")
        import traceback
        traceback.print_exc()
        # We don't exit here so the script can at least be tested up to the connection point in CI
        return

    # 3. Load C# .NET Plugin and Execute 3D Draw (V2 Upgrade)
    print("\n[3/3] Loading C# 3D Plugin and executing...")
    dll_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "AutoCad3DPlugin", "bin", "Release", "net8.0", "AutoCad3DPlugin.dll"))
    
    # Format the path for AutoCAD (replace \ with /)
    dll_path_acad = dll_path.replace("\\", "/")
    
    if not os.path.exists(dll_path):
        print(f" -> ERROR: DLL not found at {dll_path}")
        print(" -> Did you run 'dotnet build -c Release' in AutoCad3DPlugin?")
        return

    try:
        # We use SendCommand to load the DLL and trigger the custom command
        doc.SendCommand(f'(command "NETLOAD" "{dll_path_acad}")\n')
        time.sleep(1) # Wait for load
        doc.SendCommand("DRAW3DBRACKET\n")
        
        # Change view to Southwest Isometric to see the 3D solid
        doc.SendCommand("-VPOINT -1,-1,1\n")
        doc.SendCommand("SHADEMODE C\n") # Conceptual shading
        doc.SendCommand("ZOOM E\n")
        
        print(" -> SUCCESS: 3D Bracket generated via C# Plugin!")
    except Exception as e:
        print(f" -> ERROR executing 3D Command: {e}")

if __name__ == "__main__":
    main()
