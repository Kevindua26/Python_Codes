# Write a program to find the sum of natural numbers.
print('Q41_SumOfNaturalNumbers.py')

# Get input from user
n = int(input("Enter a number: "))

# Calculate sum of natural numbers
sum_natural = 0
for i in range(1, n + 1):
    sum_natural += i

# Display result
print(f"Sum of first {n} natural numbers is {sum_natural}")
