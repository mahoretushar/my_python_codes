# Basic Data Types Challenge 3: Temperature Conversion App

print("Welcome to the Temperature Conversion App")

# Gather user input
temp_f = float(input("\nWhat is the given temperature in degrees Fahrenheit: "))

# Convert temps
temp_c = (5 / 9) * (temp_f - 32)
temp_k = temp_c + 273.15

# Round temps
temp_f = round(temp_f, 4)
temp_c = round(temp_c, 4)
temp_k = round(temp_k, 4)

# Summary table
print(f"\nDegrees Fahrenheit:\t{temp_f}")
print(f"Degrees Celsius:\t{temp_c}")
print(f"Degrees Kelvin:\t\t{temp_k}")
