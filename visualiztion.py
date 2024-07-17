# visualization.py

import matplotlib.pyplot as plt

def plot_extraction_over_time(time_points, states):
    """Plot extraction yield and volume over time."""
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Volume (mL)', color='tab:blue')
    ax1.plot(time_points, [state['water_volume'] for state in states], color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')
    
    ax2 = ax1.twinx()
    ax2.set_ylabel('Extraction Yield (%)', color='tab:orange')
    ax2.plot(time_points, [state['extraction_yield']*100 for state in states], color='tab:orange')
    ax2.tick_params(axis='y', labelcolor='tab:orange')
    
    plt.title('Extraction Progress')
    fig.tight_layout()
    return fig

def plot_flow_rate(time_points, states):
    """Plot flow rate over time."""
    flow_rates = [state['flow_rate'] for state in states]
    
    plt.figure(figsize=(10, 6))
    plt.plot(time_points, flow_rates)
    plt.xlabel('Time (s)')
    plt.ylabel('Flow Rate (mL/s)')
    plt.title('Flow Rate Over Time')
    return plt.gcf()

def plot_pressure_profile(time_points, states):
    """Plot pressure profile over time."""
    pressures = [state['pressure'] for state in states]
    
    plt.figure(figsize=(10, 6))
    plt.plot(time_points, pressures)
    plt.xlabel('Time (s)')
    plt.ylabel('Pressure (bar)')
    plt.title('Pressure Profile')
    return plt.gcf()