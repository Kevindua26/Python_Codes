# Write a program to demonstrate positional parameters.
print('Q75_PositionalParameters.py')

def student_info(name, roll, branch, marks):
    """Function with positional parameters"""
    print(f"Name: {name}")
    print(f"Roll Number: {roll}")
    print(f"Branch: {branch}")
    print(f"Marks: {marks}")

def calculate_result(marks1, marks2, marks3):
    """Calculate total and percentage with positional parameters"""
    total = marks1 + marks2 + marks3
    percentage = (total / 300) * 100
    return total, percentage

def display_book_info(title, author, price, pages):
    """Display book information using positional parameters"""
    print(f"\nBook: {title}")
    print(f"Author: {author}")
    print(f"Price: ₹{price}")
    print(f"Pages: {pages}")

def power(base, exponent):
    """Calculate power using positional parameters"""
    return base ** exponent

# Demonstrating positional parameters
print("=== Example 1: Student Information ===\n")
student_info("Kaivalaya Dua", 205, "BCA", 85)

print("\n=== Example 2: Calculate Result ===\n")
total, percentage = calculate_result(85, 90, 78)
print(f"Total Marks: {total}/300")
print(f"Percentage: {percentage:.2f}%")

print("\n=== Example 3: Book Information ===")
display_book_info("Python Programming", "John Smith", 499, 350)
display_book_info("Data Structures", "Jane Doe", 599, 420)

print("\n=== Example 4: Power Calculation ===\n")
print(f"2^3 = {power(2, 3)}")
print(f"5^2 = {power(5, 2)}")
print(f"10^4 = {power(10, 4)}")

# Note: Order matters in positional parameters!
print("\n=== Note: Order of arguments matters! ===")
print("\nCorrect order:")
student_info("Alice", 101, "CSE", 92)

print("\nWrong order (will give wrong output):")
student_info(101, "Alice", 92, "CSE")  # Wrong order!
