# Write a program to demonstrate usage of map() and filter() on a list.
print('Q53_MapFilter.py')

# Original list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List:", numbers)

print("\n=== map() Function ===\n")

# 1. Square each number using map
squared = list(map(lambda x: x ** 2, numbers))
print("1. Squared numbers:", squared)

# 2. Double each number
doubled = list(map(lambda x: x * 2, numbers))
print("2. Doubled numbers:", doubled)

# 3. Add 10 to each number
add_ten = list(map(lambda x: x + 10, numbers))
print("3. Add 10 to each:", add_ten)

print("\n=== filter() Function ===\n")

# 1. Filter even numbers
even = list(filter(lambda x: x % 2 == 0, numbers))
print("1. Even numbers:", even)

# 2. Filter odd numbers
odd = list(filter(lambda x: x % 2 != 0, numbers))
print("2. Odd numbers:", odd)

# 3. Filter numbers greater than 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print("3. Numbers > 5:", greater_than_5)

print("\n=== Combining map() and filter() ===\n")

# Filter even numbers and then square them
even_squared = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print("Even numbers squared:", even_squared)
