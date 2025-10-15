def temperature(**unit):
    if "C" in unit:
        celsius = unit["C"]
        kelvin = celsius + 273.15
        fahrenheit = (1.8 * celsius) + 32
    elif "K" in unit:
        kelvin = unit["K"]
        celsius = kelvin - 273.15
        fahrenheit = (1.8 * celsius) + 32
    elif "F" in unit:
        fahrenheit = unit["F"]
        celsius = (fahrenheit - 32) / 1.8
        kelvin = celsius + 273.15
    else:
        return None
    return {"C": celsius, "K": kelvin, "F": fahrenheit}

def input_temperature():
    value = input("Enter temperature value: ")
    unit = input("Enter unit (C, K, or F): ").strip().upper()
    try:
        value = float(value)
    except ValueError:
        return "non-numeric", None, None
    if unit not in ["C", "K", "F"]:
        return "invalid-unit", None, None
    return "ok", value, unit

def print_temperature(values):
    print("TEMPERATURE CONVERSION")
    print("----------------------")
    print(f"Celsius: {values['C']:.2f}")
    print(f"Kelvin: {values['K']:.2f}")
    print(f"Fahrenheit: {values['F']:.2f}")

def main():
    status, temp_value, temp_unit = input_temperature()
    if status == "ok":
        if temp_unit == "C":
            result = temperature(C=temp_value)
        elif temp_unit == "K":
            result = temperature(K=temp_value)
        elif temp_unit == "F":
            result = temperature(F=temp_value)
        print()
        print_temperature(result)
    elif status == "non-numeric":
        print("Invalid input: please enter a numeric value.")
    elif status == "invalid-unit":
        print("Invalid unit: please enter C, K, or F.")

while True:
    main()