import math
# Pythagorean Theorem Calculator
# Formula: c = sqrt(a^2 + b^2)
print("Pythagorean Theorem Calculator")
# Get user inputs (once)
a = float(input("Enter a: "))
b = float(input("Enter b: "))
# Basic validation for positive values
if a <= 0 or b <= 0:
    print("Error: a and b must be positive numbers.")
else:
    # Calculate using math.sqrt (preferred)
    pythagorean_formula = math.sqrt(a**2 + b**2)
    print("Pythagorean formula result:", pythagorean_formula)
    
    # Alternative using exponentiation (no import needed)
    # pythagorean_formula = (a**2 + b**2)**0.5