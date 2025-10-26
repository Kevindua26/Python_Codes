# Program to perform list operations (sum and sort)
print('Q18_ListOperations.py')

# Get input from user
n = int(input("Enter how many numbers you want to add to the list: "))
numbers = []

# Input numbers into the list
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate sum and sort the list
list_sum = sum(numbers)
sorted_list = sorted(numbers)

# Display results
print("\nResults:")
print(f"Original list: {numbers}")
print(f"Sum of numbers: {list_sum}")
print(f"Sorted list: {sorted_list}")
