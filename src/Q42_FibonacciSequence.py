# Write a program to print the Fibonacci sequence.
print('Q42_FibonacciSequence.py')

# Get input from user
n = int(input("How many Fibonacci numbers do you want? "))

# Initialize first two numbers
a, b = 0, 1

# Print Fibonacci sequence
print(f"First {n} Fibonacci numbers:")
for i in range(n):
    print(a, end=" ")
    # Update values
    a, b = b, a + b
