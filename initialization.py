# initialization.py

import numpy as np
from config import *

class EspressoSimulation:
    def __init__(self, 
                 time_step=DEFAULT_TIME_STEP,
                 pressure=DEFAULT_PRESSURE,
                 water_temperature=DEFAULT_WATER_TEMPERATURE,
                 flow_rate=DEFAULT_FLOW_RATE,
                 dose=DEFAULT_DOSE,
                 grind_size=DEFAULT_GRIND_SIZE,
                 roast_level=DEFAULT_ROAST_LEVEL):
        
        self.time_step = time_step
        self.pressure = pressure
        self.water_temperature = water_temperature
        self.flow_rate = flow_rate
        self.dose = dose
        self.grind_size = grind_size
        self.roast_level = roast_level
        
        self.initialize_puck()
        self.initialize_water()
        self.initialize_extraction()
        
    def initialize_puck(self):
        self.puck_volume = np.pi * (PUCK_DIAMETER/2)**2 * PUCK_DEPTH
        self.puck_mass = self.dose / 1000  # convert grams to kg
        self.puck_density = self.puck_mass / self.puck_volume
        self.porosity = 1 - (self.puck_density / COFFEE_PARTICLE_DENSITY)
        
        # Initialize layers
        self.layer_depth = PUCK_DEPTH / NUMBER_OF_LAYERS
        self.layers = np.zeros(NUMBER_OF_LAYERS)
        
        # Kozeny-Carman equation for permeability
        dp = self.grind_size / 1e6  # convert micrometers to meters
        self.permeability = (dp**2 * self.porosity**3) / (180 * (1 - self.porosity)**2)
        
    def initialize_water(self):
        self.water_volume = 0
        self.water_mass = 0
        self.water_in_puck = np.zeros(NUMBER_OF_LAYERS)
        
    def initialize_extraction(self):
        self.coffee_concentration = INITIAL_COFFEE_CONCENTRATION * np.ones(NUMBER_OF_LAYERS)
        self.extracted_coffee = 0
        self.extraction_yield = 0
        
    def get_state(self):
        return {
            "time": 0,
            "water_volume": self.water_volume,
            "water_mass": self.water_mass,
            "water_in_puck": self.water_in_puck.copy(),
            "coffee_concentration": self.coffee_concentration.copy(),
            "extracted_coffee": self.extracted_coffee,
            "extraction_yield": self.extraction_yield,
            "pressure": self.pressure,
            "water_temperature": self.water_temperature,
            "flow_rate": self.flow_rate
        }

def create_simulation(user_inputs=None):
    if user_inputs is None:
        return EspressoSimulation()
    else:
        return EspressoSimulation(**user_inputs)