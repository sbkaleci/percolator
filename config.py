# Physical constants
GRAVITY = 9.81  # m/s^2
WATER_DENSITY = 1000  # kg/m^3
WATER_VISCOSITY = 0.001  # Pa·s at 20°C

# Default simulation parameters
DEFAULT_TIME_STEP = 0.1  # seconds
TOTAL_SIMULATION_TIME = 30  # seconds

# Espresso machine parameters
DEFAULT_PRESSURE = 9  # bars
DEFAULT_WATER_TEMPERATURE = 93  # °C
DEFAULT_FLOW_RATE = 1.5  # mL/s

# Coffee parameters
COFFEE_SOLUBILITY = 0.3 # Maximum soluble portion of coffee (30%)
DEFAULT_DOSE = 16  # grams
DEFAULT_GRIND_SIZE = 275  # micrometers
DEFAULT_ROAST_LEVEL = 'light'  # options: light, medium, dark

# Puck parameters
PUCK_DIAMETER = 0.058  # m (58mm)
PUCK_DEPTH = 0.02  # m (20mm)
NUMBER_OF_LAYERS = 10  # for discretization

# Extraction parameters
COFFEE_PARTICLE_DENSITY = 1200  # kg/m^3
INITIAL_COFFEE_CONCENTRATION = 0.3  # mass fraction

# Heat transfer parameters
SPECIFIC_HEAT_CAPACITY_WATER = 4186  # J/(kg·K)
SPECIFIC_HEAT_CAPACITY_COFFEE = 1200  # J/(kg·K) (approximate)
THERMAL_CONDUCTIVITY_WATER = 0.6  # W/(m·K)
AMBIENT_TEMPERATURE = 23  # °C

# Chemical kinetics parameters
ACTIVATION_ENERGY = 40000  # J/mol (approximate)
PRE_EXPONENTIAL_FACTOR = 1e5  # 1/s (approximate)

# Simulation control
MAX_ITERATIONS = 1000
CONVERGENCE_TOLERANCE = 1e-6

# Output parameters
TDS_TARGET = 0.1  # 10% Total Dissolved Solids
IDEAL_EXTRACTION_YIELD = 0.2  # 20% extraction yield

# Extraction factors
GRIND_SIZE_FACTOR = 275  # Baseline for 275 micrometers
PRESSURE_FACTOR = 0.1  # Extraction increase per bar of pressure
ROAST_LEVEL_FACTORS = {
    'light': 1.1,
    'medium': 1.0,
    'dark': 0.9
}