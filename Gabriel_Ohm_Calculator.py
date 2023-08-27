import tkinter as tk
import math

#Functions
def calculate():
    try:
        voltage = None
        current = None
        resistance = None
        
        if voltage_entry.get() and current_entry.get():
            voltage = float(voltage_entry.get())
            current = float(current_entry.get())
            resistance = voltage / current
            power = pow(voltage, 2) / resistance
        elif current_entry.get() and resistance_entry.get():
            current = float(current_entry.get())
            resistance = float(resistance_entry.get())
            voltage = current * resistance
            power = pow(current, 2) * resistance
        elif voltage_entry.get() and resistance_entry.get():
            voltage = float(voltage_entry.get())
            resistance = float(resistance_entry.get())
            current = voltage / resistance
            power = pow(voltage, 2) * resistance
        elif voltage_entry.get() and power_entry.get(): 
             voltage = float(voltage_entry.get())
             power = float(power_entry.get())
             current = power / voltage
             resistance = pow(voltage, 2) / power
        elif power_entry.get() and current_entry.get():
            power = float(power_entry.get())
            current = float(current_entry.get())
            voltage = power / current
            resistance = power / pow(current, 2)
        elif resistance_entry.get() and power_entry.get():
            power = float(power_entry.get())
            resistance = float(resistance_entry.get())
            current = math.sqrt(power / resistance)
            voltage = math.sqrt(power * resistance)
        else:
            result_label.config(text="Provide any two or more values")

        result_text = ""
        if voltage is not None:
            power = voltage * current
            result_text += f"Voltage (V): {voltage:.2f} V\n"
            result_text += f"Power (P): {power:.2f} W\n"
        if current is not None:
            power = pow(current, 2) * resistance
            result_text += f"Current (I): {current:.2f} A\n"
            result_text += f"Power (P): {power:.2f} W\n"
        if resistance is not None:
            power = pow(voltage, 2) / resistance
            result_text += f"Resistance (R): {resistance:.2f} Ω\n"
            result_text += f"Power (P): {power:.2f} W\n"

        result_label.config(text=result_text)
    except ValueError:
        result_label.config(text="Invalid input")

def reset():
    voltage_entry.delete(0, tk.END)
    current_entry.delete(0, tk.END)
    resistance_entry.delete(0, tk.END)
    power_entry.delete(0, tk.END)
    result_label.config(text="")

# User Interface
root = tk.Tk()
root.title("Gabriel's Ohm Calculator")
root.configure(bg="lightgray")

voltage_label = tk.Label(root, text="Voltage (V):", bg="lightgray")
current_label = tk.Label(root, text="Current (I):", bg="lightgray")
resistance_label = tk.Label(root, text="Resistance (R):", bg="lightgray")
power_label = tk.Label(root, text="Power (P):", bg="lightgray")
formulas_label = tk.Label(root, text="Voltage = I * R; P / I; √(P * R)\n"
                                     "Current = V / R; √(P / R); P / V\n"
                                     "Resistance = V / I; P / I²; V² / P\n"
                                     "Power = I² * R; V * I; V² / R",
                          font=("Arial", 12), justify="left")
voltage_entry = tk.Entry(root)
current_entry = tk.Entry(root)
resistance_entry = tk.Entry(root)
power_entry = tk.Entry(root)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left", wraplength=250)

voltage_label.grid(row=0, column=0, padx=10, pady=5)
voltage_entry.grid(row=0, column=1, padx=10, pady=5)
current_label.grid(row=1, column=0, padx=10, pady=5)
current_entry.grid(row=1, column=1, padx=10, pady=5)
resistance_label.grid(row=2, column=0, padx=10, pady=5)
resistance_entry.grid(row=2, column=1, padx=10, pady=5)
power_label.grid(row=3, column=0, padx=10, pady=5)
power_entry.grid(row=3, column=1, padx=10, pady=5)
formulas_label.grid(row=1, column=3, columnspan=2, padx=10, pady=5)  

calculate_button.grid(row=5, column=0, padx=10, pady=10)
result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.grid(row=5, column=1, padx=10, pady=10)

root.geometry("800x600")
root.mainloop()