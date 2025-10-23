# Write a program to demonstrate variable length parameters.

# *args - variable length positional arguments
def calculate_sum(*numbers):
    """Calculate sum of variable number of arguments"""
    total = 0
    for num in numbers:
        total += num
    return total

# *args with normal parameters
def student_marks(name, *marks):
    """Calculate total marks with variable subjects"""
    print(f"\nStudent: {name}")
    print(f"Marks: {marks}")
    total = sum(marks)
    print(f"Total: {total}")
    print(f"Average: {total/len(marks):.2f}")

# **kwargs - variable length keyword arguments
def display_info(**details):
    """Display information using keyword arguments"""
    print("\nDetails:")
    for key, value in details.items():
        print(f"{key}: {value}")

# Combination of *args and **kwargs
def complete_info(name, *subjects, **details):
    """Demonstrate combination of all parameter types"""
    print(f"\nName: {name}")
    print(f"Subjects: {subjects}")
    print("Additional Details:")
    for key, value in details.items():
        print(f"  {key}: {value}")

# *args for multiplication
def multiply_all(*numbers):
    """Multiply all numbers"""
    result = 1
    for num in numbers:
        result *= num
    return result

# Demonstrating variable length parameters
print("=== Example 1: Sum with *args ===\n")
print(f"Sum of 2 numbers: {calculate_sum(10, 20)}")
print(f"Sum of 4 numbers: {calculate_sum(10, 20, 30, 40)}")
print(f"Sum of 6 numbers: {calculate_sum(5, 10, 15, 20, 25, 30)}")

print("\n=== Example 2: Student Marks ===")
student_marks("Kaivalaya", 85, 90, 78, 92, 88)
student_marks("Alice", 75, 80, 85)

print("\n=== Example 3: Display Info with **kwargs ===")
display_info(name="Kaivalaya", roll=205, branch="BCA", city="Delhi")
display_info(product="Laptop", price=50000, brand="Dell", warranty="2 years")

print("\n=== Example 4: Complete Info (all types) ===")
complete_info("Kaivalaya", "Python", "Java", "C++", roll=205, branch="BCA", year=2)

print("\n=== Example 5: Multiply All ===\n")
print(f"Multiply 2 numbers: {multiply_all(5, 4)}")
print(f"Multiply 4 numbers: {multiply_all(2, 3, 4, 5)}")
print(f"Multiply 6 numbers: {multiply_all(1, 2, 3, 4, 5, 6)}")

# List unpacking with *args
print("\n=== Example 6: List Unpacking ===\n")
numbers_list = [10, 20, 30, 40, 50]
print(f"Sum of list: {calculate_sum(*numbers_list)}")

dict_data = {"name": "Bob", "age": 20, "city": "Mumbai"}
display_info(**dict_data)

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
