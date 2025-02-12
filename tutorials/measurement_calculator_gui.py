import tkinter as tk
from tkinter import ttk, messagebox


def length_converter(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Miles": 0.000621371,
        "Feet": 3.28084,
        "Inches": 39.3701,
    }
    return value * (length_units[to_unit] / length_units[from_unit])


def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "Grams": 1,
        "Kilograms": 0.001,
        "Pounds": 0.00220462,
        "Ounces": 0.035274,
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])


def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9 / 5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5 / 9
        elif to_unit == "Kelvin":
            return (value - 32) * 5 / 9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9 / 5 + 32
    return value


def convert():
    try:
        value = float(input_value.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()
        conversion_type = conversion_type_var.get()

        if conversion_type == "Length":
            result = length_converter(value, from_unit, to_unit)
        elif conversion_type == "Weight":
            result = weight_converter(value, from_unit, to_unit)
        elif conversion_type == "Temperature":
            result = temperature_converter(value, from_unit, to_unit)
        else:
            raise ValueError("Invalid conversion type!")

        output_label.config(text=f"Result: {result:.2f} {to_unit}")
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid Input: {e}")


# Create the main application window
root = tk.Tk()
root.title("Measurement Calculator")
root.geometry("500x300")  # Set window size

# Define padding for all widgets
PAD_X = 10
PAD_Y = 5

# Conversion Type Selection
ttk.Label(root, text="Select Conversion Type:").grid(row=0, column=0, padx=PAD_X, pady=PAD_Y, sticky="w")
conversion_type_var = tk.StringVar(value="Length")
conversion_types = ["Length", "Weight", "Temperature"]
ttk.OptionMenu(root, conversion_type_var, *conversion_types).grid(row=0, column=1, padx=PAD_X, pady=PAD_Y, sticky="w")

# Input Value
ttk.Label(root, text="Enter Value:").grid(row=1, column=0, padx=PAD_X, pady=PAD_Y, sticky="w")
input_value = ttk.Entry(root, width=20)
input_value.grid(row=1, column=1, padx=PAD_X, pady=PAD_Y, sticky="w")

# From Unit
ttk.Label(root, text="From Unit:").grid(row=2, column=0, padx=PAD_X, pady=PAD_Y, sticky="w")
from_unit_var = tk.StringVar(value="Meters")
from_unit_menu = ttk.OptionMenu(root, from_unit_var, "Meters", "Meters", "Kilometers", "Miles", "Feet", "Inches", "Grams", "Kilograms", "Pounds", "Ounces", "Celsius", "Fahrenheit", "Kelvin")
from_unit_menu.grid(row=2, column=1, padx=PAD_X, pady=PAD_Y, sticky="w")

# To Unit
ttk.Label(root, text="To Unit:").grid(row=3, column=0, padx=PAD_X, pady=PAD_Y, sticky="w")
to_unit_var = tk.StringVar(value="Kilometers")
to_unit_menu = ttk.OptionMenu(root, to_unit_var, "Kilometers", "Meters", "Kilometers", "Miles", "Feet", "Inches", "Grams", "Kilograms", "Pounds", "Ounces", "Celsius", "Fahrenheit", "Kelvin")
to_unit_menu.grid(row=3, column=1, padx=PAD_X, pady=PAD_Y, sticky="w")

# Convert Button
convert_button = ttk.Button(root, text="Convert", command=convert)
convert_button.grid(row=4, column=1, padx=PAD_X, pady=PAD_Y, sticky="w")

# Output Label
output_label = ttk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
output_label.grid(row=5, column=0, columnspan=2, padx=PAD_X, pady=PAD_Y)

# Start the application
root.mainloop()
