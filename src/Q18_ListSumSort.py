# Program to take a list of numbers from user, calculate sum, and sort the list
print('Q18_ListSumSort.py')

# Get numbers from user
numbers_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, numbers_input.split()))

# Calculate sum
total_sum = sum(numbers)
print(f"Sum of numbers: {total_sum}")

# Sort the list
sorted_numbers = sorted(numbers)
print(f"Sorted list: {sorted_numbers}")
