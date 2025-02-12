# measurement_calculator.py

def length_converter(value, from_unit, to_unit):
    length_units = {
        "meters": 1,
        "kilometers": 0.001,
        "miles": 0.000621371,
        "feet": 3.28084,
        "inches": 39.3701,
    }
    if from_unit in length_units and to_unit in length_units:
        return value * (length_units[to_unit] / length_units[from_unit])
    else:
        raise ValueError("Invalid length unit!")


def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "grams": 1,
        "kilograms": 0.001,
        "pounds": 0.00220462,
        "ounces": 0.035274,
    }
    if from_unit in weight_units and to_unit in weight_units:
        return value * (weight_units[to_unit] / weight_units[from_unit])
    else:
        raise ValueError("Invalid weight unit!")


def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    elif from_unit == to_unit:
        return value
    else:
        raise ValueError("Invalid temperature unit!")


def main():
    print("Measurement Calculator")
    print("======================")
    print("1. Length Conversion")
    print("2. Weight Conversion")
    print("3. Temperature Conversion")
    print("4. Exit")
    
    while True:
        choice = input("\nEnter your choice: ")
        if choice == "1":
            value = float(input("Enter value: "))
            from_unit = input("From unit (meters, kilometers, miles, feet, inches): ")
            to_unit = input("To unit (meters, kilometers, miles, feet, inches): ")
            try:
                result = length_converter(value, from_unit, to_unit)
                print(f"Converted value: {result} {to_unit}")
            except ValueError as e:
                print(e)
        elif choice == "2":
            value = float(input("Enter value: "))
            from_unit = input("From unit (grams, kilograms, pounds, ounces): ")
            to_unit = input("To unit (grams, kilograms, pounds, ounces): ")
            try:
                result = weight_converter(value, from_unit, to_unit)
                print(f"Converted value: {result} {to_unit}")
            except ValueError as e:
                print(e)
        elif choice == "3":
            value = float(input("Enter value: "))
            from_unit = input("From unit (Celsius, Fahrenheit, Kelvin): ")
            to_unit = input("To unit (Celsius, Fahrenheit, Kelvin): ")
            try:
                result = temperature_converter(value, from_unit, to_unit)
                print(f"Converted value: {result} {to_unit}")
            except ValueError as e:
                print(e)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
