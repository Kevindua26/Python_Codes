# Write a program to find the factorial of a number.
print('Q32_Factorial.py')

# Get input from user
num = int(input("Enter a number: "))

# Calculate factorial
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i

# Display result
print(f"Factorial of {num} is {factorial}")
