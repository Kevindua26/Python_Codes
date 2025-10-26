# Write a program for function definition with no return argument.
print('Q65_FunctionNoReturn.py')

# Function with no return (using print)
def display_welcome():
    print("Welcome to Python Programming!")
    print("Learning functions is fun!")

# Function that performs action but doesn't return
def print_table(num):
    print(f"\nTable of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Function to display student info
def display_student_info(name, roll, marks):
    print(f"\n--- Student Information ---")
    print(f"Name: {name}")
    print(f"Roll Number: {roll}")
    print(f"Marks: {marks}")

# Function to greet multiple times
def greet_multiple(name, times):
    for i in range(times):
        print(f"Hello {name}!")

# Calling functions
display_welcome()

print_table(5)

display_student_info("Kaivalaya", 205, 85)

print("\n=== Greeting 3 times ===")
greet_multiple("Kaivalaya", 3)
