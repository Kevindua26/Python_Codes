# Program to swap two variables without using a 3rd variable or any control statement
print('Q19_SwapNumbers.py')

# Get two numbers from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"Before swapping: a = {a}, b = {b}")

# Swap without 3rd variable using arithmetic operations
a = a + b
b = a - b
a = a - b

print(f"After swapping: a = {a}, b = {b}")
