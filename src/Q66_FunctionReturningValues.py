# Write a program for usage of function returning values.

# Function returning single value
def square(num):
    return num ** 2

# Function returning calculation result
def calculate_area(length, width):
    area = length * width
    return area

# Function returning multiple values
def calculate_circle(radius):
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference

# Function returning boolean
def is_even(num):
    return num % 2 == 0

# Function returning string
def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"

# Using functions with return values
print("=== Square Function ===")
result = square(5)
print(f"Square of 5 is {result}")

print("\n=== Area Calculation ===")
area = calculate_area(10, 5)
print(f"Area of rectangle (10 x 5) is {area}")

print("\n=== Circle Calculations ===")
area, circumference = calculate_circle(7)
print(f"Circle with radius 7:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")

print("\n=== Even/Odd Check ===")
print(f"Is 10 even? {is_even(10)}")
print(f"Is 7 even? {is_even(7)}")

print("\n=== Grade System ===")
print(f"Marks 95: Grade {get_grade(95)}")
print(f"Marks 75: Grade {get_grade(75)}")
print(f"Marks 55: Grade {get_grade(55)}")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
