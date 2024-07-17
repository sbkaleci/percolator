# calculations.py

import numpy as np
from config import *


def calculate_flow(simulation):
    delta_p = simulation.pressure * 1e5  # Convert bar to Pa
    mu = WATER_VISCOSITY
    k = simulation.permeability
    L = PUCK_DEPTH
    A = np.pi * (PUCK_DIAMETER/2)**2

    Q = (k * A * delta_p) / (mu * L)  # m^3/s
    return min(Q * 1e6, 2.5)  # Convert to mL/s, cap at 2.5 mL/s


def update_water_distribution(simulation):
    flow_rate = calculate_flow(simulation)
    water_volume = flow_rate * simulation.time_step

    simulation.water_in_puck += water_volume / NUMBER_OF_LAYERS
    simulation.water_volume += water_volume
    simulation.water_mass += water_volume * WATER_DENSITY / 1e6  # Convert mL to kg

    return flow_rate


def calculate_extraction(simulation):
    R = 8.314  # Universal gas constant

    # Pressure and temperature effects (Arrhenius equation)
    temp_kelvin = simulation.water_temperature + 273.15
    k_temp = PRE_EXPONENTIAL_FACTOR * \
        np.exp(-ACTIVATION_ENERGY / (R * temp_kelvin))

    # Grind size and roasting level effects
    grind_factor = simulation.grind_size / DEFAULT_GRIND_SIZE
    roast_factor = ROAST_LEVEL_FACTORS[simulation.roast_level]

    # Decreasing extraction efficiency over time
    extraction_efficiency = 1 - \
        (simulation.extracted_coffee / (COFFEE_SOLUBILITY * simulation.dose))

    for i in range(NUMBER_OF_LAYERS):
        if simulation.water_in_puck[i] > 0:
            # Calculate concentration gradient (Fick's law)
            delta_concentration = k_temp * grind_factor * roast_factor * \
                extraction_efficiency * \
                simulation.coffee_concentration[i] * simulation.time_step

            # Adjust concentration based on flow rate and layer depth
            extracted = delta_concentration * \
                simulation.water_in_puck[i] * WATER_DENSITY / 1e6  # kg
            simulation.coffee_concentration[i] -= delta_concentration
            simulation.extracted_coffee += extracted

    simulation.extraction_yield = simulation.extracted_coffee / simulation.puck_mass


def calculate_heat_transfer(simulation):
    pass


def calculate_pressure_profile(simulation, time):
    if time < 5:  # Pre-infusion
        return 2 + (simulation.pressure - 2) * time / 5
    else:
        return simulation.pressure


def update_simulation(simulation, time):
    simulation.pressure = calculate_pressure_profile(simulation, time)
    flow_rate = update_water_distribution(simulation)
    calculate_extraction(simulation)
    calculate_heat_transfer(simulation)

    new_state = simulation.get_state()
    new_state['flow_rate'] = flow_rate
    return new_state
