# Write a program to create and use different generators in python.
print('Q59_DifferentGenerators.py')

print("=== Generator 1: Number Generator ===\n")

def number_generator(start, end):
    """Generate numbers from start to end"""
    for num in range(start, end + 1):
        yield num

print("Numbers 1 to 10:")
for num in number_generator(1, 10):
    print(num, end=" ")

print("\n\n=== Generator 2: Even Number Generator ===\n")

def even_generator(limit):
    """Generate even numbers up to limit"""
    num = 0
    while num <= limit:
        yield num
        num += 2

print("Even numbers up to 20:")
for num in even_generator(20):
    print(num, end=" ")

print("\n\n=== Generator 3: Factorial Generator ===\n")

def factorial_generator(n):
    """Generate factorials from 1 to n"""
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        yield factorial

print("Factorials 1 to 5:")
for fact in factorial_generator(5):
    print(fact, end=" ")

print("\n\n=== Generator 4: Power Generator ===\n")

def power_generator(base, max_power):
    """Generate powers of base"""
    for power in range(max_power + 1):
        yield base ** power

print("Powers of 2 (up to 2^8):")
for power in power_generator(2, 8):
    print(power, end=" ")

print("\n\n=== Generator 5: String Generator ===\n")

def char_generator(text):
    """Generate characters from string"""
    for char in text:
        yield char

print("Characters in 'Python':")
for char in char_generator("Python"):
    print(char, end=" ")

print("\n\n=== Generator 6: List Element Generator ===\n")

def list_generator(my_list):
    """Generate elements from list"""
    for item in my_list:
        yield item

fruits = ["Apple", "Banana", "Cherry", "Date"]
print("Fruits:")
for fruit in list_generator(fruits):
    print(fruit, end=" ")
