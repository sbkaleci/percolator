# ui.py

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from brew import brew_espresso
from config import *

class EspressoSimulatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Espresso Simulator")
        
        self.create_input_fields()
        self.create_run_button()
        self.create_output_area()
        
    def create_input_fields(self):
        ttk.Label(self.master, text="Pressure (bar):").grid(row=0, column=0)
        self.pressure_entry = ttk.Entry(self.master)
        self.pressure_entry.insert(0, str(DEFAULT_PRESSURE))
        self.pressure_entry.grid(row=0, column=1)
        
        ttk.Label(self.master, text="Water Temperature (°C):").grid(row=1, column=0)
        self.temp_entry = ttk.Entry(self.master)
        self.temp_entry.insert(0, str(DEFAULT_WATER_TEMPERATURE))
        self.temp_entry.grid(row=1, column=1)
        
        ttk.Label(self.master, text="Dose (g):").grid(row=2, column=0)
        self.dose_entry = ttk.Entry(self.master)
        self.dose_entry.insert(0, str(DEFAULT_DOSE))
        self.dose_entry.grid(row=2, column=1)
        
        ttk.Label(self.master, text="Grind Size (μm):").grid(row=3, column=0)
        self.grind_entry = ttk.Entry(self.master)
        self.grind_entry.insert(0, str(DEFAULT_GRIND_SIZE))
        self.grind_entry.grid(row=3, column=1)
        
        ttk.Label(self.master, text="Roast Level:").grid(row=4, column=0)
        self.roast_var = tk.StringVar(value=DEFAULT_ROAST_LEVEL)
        ttk.Combobox(self.master, textvariable=self.roast_var, values=["light", "medium", "dark"]).grid(row=4, column=1)
        
    def create_run_button(self):
        ttk.Button(self.master, text="Run Simulation", command=self.run_simulation).grid(row=5, column=0, columnspan=2)
        
    def create_output_area(self):
        self.output_text = tk.Text(self.master, height=10, width=50)
        self.output_text.grid(row=6, column=0, columnspan=2)
        
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().grid(row=0, column=2, rowspan=7)
        
    def run_simulation(self):
        user_inputs = {
            'pressure': float(self.pressure_entry.get()),
            'water_temperature': float(self.temp_entry.get()),
            'dose': float(self.dose_entry.get()),
            'grind_size': float(self.grind_entry.get()),
            'roast_level': self.roast_var.get()
        }
        
        time_points, states, analysis = brew_espresso(user_inputs)
        
        self.display_results(analysis)
        self.plot_results(time_points, states)
        
    def display_results(self, analysis):
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, f"Brew time: {analysis['brew_time']:.2f} seconds\n")
        self.output_text.insert(tk.END, f"Final volume: {analysis['final_volume']:.2f} mL\n")
        self.output_text.insert(tk.END, f"Extraction yield: {analysis['extraction_yield']*100:.2f}%\n")
        self.output_text.insert(tk.END, f"TDS: {analysis['tds']*100:.2f}%\n")
        self.output_text.insert(tk.END, f"Average flow rate: {analysis['flow_rate']:.2f} mL/s\n")
        self.output_text.insert(tk.END, f"Evaluation: {analysis['shot_evaluation']}\n")
        
    def plot_results(self, time_points, states):
        self.ax.clear()
        self.ax.plot(time_points, [state['water_volume'] for state in states], label='Volume (mL)')
        self.ax.plot(time_points, [state['extraction_yield']*100 for state in states], label='Extraction Yield (%)')
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Value')
        self.ax.legend()
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    gui = EspressoSimulatorGUI(root)
    root.mainloop()