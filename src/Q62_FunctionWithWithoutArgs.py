# Write a program for the def function definition with arguments and without arguments.
print('Q62_FunctionWithWithoutArgs.py')

# Function without arguments
def greet():
    print("Hello! Welcome to Python programming")

# Function with arguments
def greet_person(name):
    print(f"Hello {name}! Welcome to Python programming")

# Function with multiple arguments
def add_numbers(a, b):
    result = a + b
    print(f"Sum of {a} and {b} is {result}")

# Function with default argument
def greet_with_message(name, message="Good Morning"):
    print(f"{message}, {name}!")

print("=== Function without arguments ===")
greet()

print("\n=== Function with one argument ===")
greet_person("Kaivalaya")

print("\n=== Function with multiple arguments ===")
add_numbers(10, 20)
add_numbers(50, 75)

print("\n=== Function with default argument ===")
greet_with_message("Kaivalaya")
greet_with_message("Kaivalaya", "Good Evening")
