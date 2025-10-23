# Write a program to use list comprehension with condition, to use set comprehension.

print("=== List Comprehension ===\n")

# 1. Simple list comprehension
squares = [x ** 2 for x in range(1, 11)]
print("1. Squares of 1-10:", squares)

# 2. List comprehension with condition (even numbers)
evens = [x for x in range(1, 21) if x % 2 == 0]
print("2. Even numbers 1-20:", evens)

# 3. List comprehension with condition (odd numbers)
odds = [x for x in range(1, 21) if x % 2 != 0]
print("3. Odd numbers 1-20:", odds)

# 4. List comprehension with if-else
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 11)]
print("4. Even/Odd labels:", labels)

# 5. List comprehension - multiples of 3
multiples_of_3 = [x for x in range(1, 31) if x % 3 == 0]
print("5. Multiples of 3:", multiples_of_3)

print("\n=== Set Comprehension ===\n")

# 1. Simple set comprehension
squares_set = {x ** 2 for x in range(1, 11)}
print("1. Squares set:", squares_set)

# 2. Set comprehension with condition
even_set = {x for x in range(1, 21) if x % 2 == 0}
print("2. Even numbers set:", even_set)

# 3. Set comprehension - remove duplicates
numbers = [1, 2, 2, 3, 4, 4, 5, 5]
unique_set = {x for x in numbers}
print("3. Unique numbers:", unique_set)

# 4. Set comprehension with string
word = "programming"
unique_chars = {char for char in word}
print("4. Unique characters in 'programming':", unique_chars)

print("\n=== Dictionary Comprehension ===\n")

# 1. Dictionary comprehension
squares_dict = {x: x ** 2 for x in range(1, 6)}
print("1. Squares dictionary:", squares_dict)

# 2. Dictionary with condition
even_squares = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
print("2. Even squares dict:", even_squares)

print('\nThis code is written and executed by Kaivalaya Dua 0231BCA205')
