# Program to perform basic mathematical operations
print('Q15_BasicMathOperations.py')

def perform_math_operations(a, b):
    # Addition
    addition = a + b

    # Subtraction
    subtraction = a - b

    # Multiplication
    multiplication = a * b

    # Division
    division = a / b

    # Floor Division (removes decimal part)
    floor_division = a // b

    # Modulus (remainder)
    modulus = a % b

    # Exponentiation (power)
    power = a ** b

    # Print all results
    print(f"\nMathematical Operations with {a} and {b}:")
    print(f"Addition: {a} + {b} = {addition}")
    print(f"Subtraction: {a} - {b} = {subtraction}")
    print(f"Multiplication: {a} * {b} = {multiplication}")
    print(f"Division: {a} / {b} = {division:.2f}")
    print(f"Floor Division: {a} // {b} = {floor_division}")
    print(f"Modulus: {a} % {b} = {modulus}")
    print(f"Power: {a} ** {b} = {power}")

# Get input from user
print("Enter two numbers to perform basic math operations:")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operations
perform_math_operations(num1, num2)
