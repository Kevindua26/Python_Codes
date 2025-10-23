# Write a program to print the factorial of numbers using recursive functions.

def factorial_recursive(n):
    """Calculate factorial using recursion"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def display_factorial_steps(n):
    """Display factorial calculation steps"""
    if n == 0 or n == 1:
        print(f"{n}! = 1")
    else:
        steps = []
        for i in range(n, 0, -1):
            steps.append(str(i))
        print(f"{n}! = {' × '.join(steps)} = {factorial_recursive(n)}")

# Get input from user
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers!")
else:
    # Calculate factorial
    result = factorial_recursive(num)
    print(f"\nFactorial of {num} is {result}")
    
    # Display steps
    print("\nCalculation:")
    display_factorial_steps(num)
    
    # Display factorials from 1 to num
    print(f"\nFactorials from 1 to {num}:")
    for i in range(1, num + 1):
        print(f"{i}! = {factorial_recursive(i)}")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
