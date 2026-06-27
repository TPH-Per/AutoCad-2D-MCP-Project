import math

class BracketCalcEngine:
    """
    Engineering Calculation Engine for Curtain Wall Brackets
    Material: SUS304 Stainless Steel
    """
    DENSITY_SUS304 = 7930  # kg/m^3
    YIELD_STRENGTH_SUS304 = 205.0  # MPa (N/mm^2)
    SAFETY_FACTOR = 1.5

    @classmethod
    def calculate_weight(cls, width: float, height: float, depth: float, thickness: float) -> float:
        """
        Calculate the approximate weight of an L-bracket.
        Dimensions are in mm. Returns weight in kg.
        """
        # Volume of L-shape = (width * thickness + (height - thickness) * thickness) * depth
        w_m = width / 1000.0
        h_m = height / 1000.0
        d_m = depth / 1000.0
        t_m = thickness / 1000.0
        
        volume_m3 = (w_m * t_m + (h_m - t_m) * t_m) * d_m
        weight_kg = volume_m3 * cls.DENSITY_SUS304
        return weight_kg

    @classmethod
    def check_bending_stress(cls, load_kg: float, lever_arm_mm: float, section_width_mm: float, thickness_mm: float) -> dict:
        """
        Calculates bending stress at the root of the bracket arm.
        Returns dict with stress, status, and utilization.
        """
        # Force in Newtons
        force_n = load_kg * 9.81
        
        # Bending Moment M = F * d
        moment_n_mm = force_n * lever_arm_mm
        
        # Section Modulus Z = (b * h^2) / 6
        # Here, b = section_width_mm, h = thickness_mm
        z_mm3 = (section_width_mm * (thickness_mm ** 2)) / 6.0
        
        # Stress = M / Z
        stress_mpa = moment_n_mm / z_mm3
        
        allowable_stress = cls.YIELD_STRENGTH_SUS304 / cls.SAFETY_FACTOR
        utilization = stress_mpa / allowable_stress
        
        status = "PASS" if utilization <= 1.0 else "FAIL"
        
        return {
            "applied_load_kg": load_kg,
            "max_stress_mpa": round(stress_mpa, 2),
            "allowable_stress_mpa": round(allowable_stress, 2),
            "utilization_percent": round(utilization * 100, 2),
            "status": status
        }

if __name__ == "__main__":
    # Test calculation
    weight = BracketCalcEngine.calculate_weight(100, 60, 80, 8)
    print(f"Bracket Weight: {weight:.2f} kg")
    
    stress_check = BracketCalcEngine.check_bending_stress(load_kg=200, lever_arm_mm=80, section_width_mm=80, thickness_mm=8)
    print("Stress Check Result:")
    for k, v in stress_check.items():
        print(f"  {k}: {v}")
