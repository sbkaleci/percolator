# utils.py

import json
import os

def save_simulation_results(time_points, states, analysis, filename='simulation_results.json'):
    """Save simulation results to a JSON file."""
    results = {
        'time_points': time_points,
        'states': [state for state in states],  # Convert numpy arrays to lists
        'analysis': analysis
    }
    
    with open(filename, 'w') as f:
        json.dump(results, f, indent=4)

def load_simulation_results(filename='simulation_results.json'):
    """Load simulation results from a JSON file."""
    if not os.path.exists(filename):
        return None
    
    with open(filename, 'r') as f:
        results = json.load(f)
    
    return results['time_points'], results['states'], results['analysis']

def calculate_tds(extracted_coffee, water_mass):
    """Calculate Total Dissolved Solids (TDS)."""
    return extracted_coffee / water_mass

def calculate_extraction_ratio(extracted_coffee, dose):
    """Calculate the extraction ratio."""
    return extracted_coffee / dose