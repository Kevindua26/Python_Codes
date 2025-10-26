# Program to perform math operations using math module
print('Q17_MathModule.py')
import math

# Basic math operations using math module
print("Math Module Operations")
print("=" * 30)

# Sample numbers
numbers = [10, 5, 8, 20, 3, 15]
print(f"Numbers: {numbers}")

# Min and Max
min_value = min(numbers)
max_value = max(numbers)
print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")

# Sum function
total_sum = sum(numbers)
print(f"Sum of all numbers: {total_sum}")

# Average using math module
total = sum(numbers)
average = total / len(numbers)
print(f"Average: {average}")

# Using math.fsum for more precise floating point sum
precise_sum = math.fsum(numbers)
precise_average = precise_sum / len(numbers)
print(f"Precise sum using math.fsum: {precise_sum}")
print(f"Precise average using math.fsum: {precise_average}")
