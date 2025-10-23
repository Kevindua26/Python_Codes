# Write a program to print the Fibonacci sequence.

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

print('\This code is written and executed by Kaivalaya Dua 0231BCA205')
