# brew.py

from initialization import create_simulation
from calculations import update_simulation
from config import TOTAL_SIMULATION_TIME, MAX_ITERATIONS

def run_simulation(user_inputs=None):
    simulation = create_simulation(user_inputs)
    
    time_points = [0]
    states = [simulation.get_state()]
    
    for i in range(1, MAX_ITERATIONS):
        current_time = i * simulation.time_step
        
        if current_time > TOTAL_SIMULATION_TIME:
            break
        
        new_state = update_simulation(simulation, current_time)
        
        time_points.append(current_time)
        states.append(new_state)
        
        if new_state['water_volume'] >= 60:  # Assuming a double shot
            break
    
    return time_points, states

def analyze_results(time_points, states):
    final_state = states[-1]
    
    analysis = {
        'brew_time': time_points[-1],
        'final_volume': final_state['water_volume'],
        'extraction_yield': final_state['extraction_yield'],
        'tds': final_state['extracted_coffee'] / final_state['water_mass'],
        'flow_rate': final_state['flow_rate']
    }
    
    # Simple shot evaluation
    if analysis['extraction_yield'] < 0.18:
        analysis['shot_evaluation'] = "Under-extracted. Consider using a finer grind or increasing brew time."
    elif analysis['extraction_yield'] > 0.22:
        analysis['shot_evaluation'] = "Over-extracted. Consider using a coarser grind or decreasing brew time."
    else:
        analysis['shot_evaluation'] = "Well extracted. Good balance achieved."
    
    return analysis

def brew_espresso(user_inputs=None):
    time_points, states = run_simulation(user_inputs)
    analysis = analyze_results(time_points, states)
    return time_points, states, analysis

if __name__ == "__main__":
    time_points, states, analysis = brew_espresso()
    
    print("Simulation complete. Summary:")
    for key, value in analysis.items():
        print(f"{key}: {value}")