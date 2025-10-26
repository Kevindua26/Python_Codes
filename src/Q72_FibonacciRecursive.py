# Write a program to print a fibonacci sequence using a recursive function.
print('Q72_FibonacciRecursive.py')

def fibonacci_recursive(n):
    """Generate Fibonacci number at position n using recursion"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def print_fibonacci_sequence(terms):
    """Print Fibonacci sequence using recursive function"""
    print(f"Fibonacci sequence with {terms} terms:")
    for i in range(terms):
        print(fibonacci_recursive(i), end=" ")
    print()

# Get input from user
n = int(input("How many Fibonacci terms do you want? "))

# Print Fibonacci sequence
print_fibonacci_sequence(n)

# Display individual terms with position
print("\nDetailed view:")
for i in range(n):
    print(f"F({i}) = {fibonacci_recursive(i)}")
