import numpy as np

def espresso_extraction(grind_size, pressure, tamp_force, coffee_mass, water_temp):
    # Constants
    D_l = 1e-9  # Estimated diffusivity of coffee solubles in water (m^2/s)
    viscosity = 0.001  # Viscosity of water at near-boiling temp (Pa.s)
    density = 1000  # Density of water (kg/m^3)
    bed_porosity = 0.4  # Porosity of the coffee bed, typical for packed beds

    # Fluid dynamics
    basket_radius = 0.057 / 2  # Radius of a typical espresso basket (m)
    flow_area = np.pi * basket_radius ** 2  # Cross-sectional area (m^2)
    hydraulic_conductivity = pressure * 1e5 / viscosity  # Simplified relation (m/s)
    velocity = hydraulic_conductivity * bed_porosity  # Fluid velocity (m/s)

    # Adjust extraction efficiency formula
    grind_effect = np.exp(-0.1 * (grind_size - 250) ** 2)  # Gaussian peak at 250 microns
    pressure_effect = pressure / 9  # Normalize to a baseline of 9 bars
    tamp_effect = np.clip(30 / tamp_force, 0.5, 2)  # Inversely proportional within limits
    temp_effect = np.clip((water_temp - 85) / (96 - 85), 0.5, 1.5)  # Normalized around typical brewing temps

    # Calculate extraction yield
    extraction_efficiency = 0.2 * grind_effect * pressure_effect * tamp_effect * temp_effect
    extraction_yield = extraction_efficiency * (coffee_mass / 18)  # Normalize to 18 grams baseline

    return extraction_yield

# Example usage
grind_size = 250  # in microns
pressure = 9  # in bar
tamp_force = 20  # in Newtons
coffee_mass = 17  # in grams
water_temp = 92  # in Celsius

yield_percent = espresso_extraction(grind_size, pressure, tamp_force, coffee_mass, water_temp)
print(f"Extraction Yield: {yield_percent:.2%}")
