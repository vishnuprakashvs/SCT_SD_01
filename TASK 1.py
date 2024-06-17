def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, from_scale, to_scale):
    if from_scale == to_scale:
        return value
    
    if from_scale == 'C':
        if to_scale == 'F':
            return celsius_to_fahrenheit(value)
        elif to_scale == 'K':
            return celsius_to_kelvin(value)
    
    if from_scale == 'F':
        if to_scale == 'C':
            return fahrenheit_to_celsius(value)
        elif to_scale == 'K':
            return fahrenheit_to_kelvin(value)
    
    if from_scale == 'K':
        if to_scale == 'C':
            return kelvin_to_celsius(value)
        elif to_scale == 'F':
            return kelvin_to_fahrenheit(value)

    raise ValueError("Invalid temperature scales. Please use 'C', 'F', or 'K'.")

def main():
    print("Temperature Converter")
    value = float(input("Enter the temperature value to convert: "))
    from_scale = input("Enter the current scale of the temperature (C/F/K): ").upper()
    to_scale = input("Enter the scale to convert to (C/F/K): ").upper()
    
    try:
        result = convert_temperature(value, from_scale, to_scale)
        print(f"{value}°{from_scale} is {result:.2f}°{to_scale}")
    except ValueError as e:
        print(e)

if _name_ == "_main_":
    main()