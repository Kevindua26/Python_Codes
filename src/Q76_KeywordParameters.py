# Write a program to demonstrate keyword parameters.
print('Q76_KeywordParameters.py')

def student_info(name, roll, branch, marks):
    """Function demonstrating keyword parameters"""
    print(f"Name: {name}")
    print(f"Roll Number: {roll}")
    print(f"Branch: {branch}")
    print(f"Marks: {marks}")

def calculate_percentage(subject1, subject2, subject3, total_marks=300):
    """Calculate percentage with keyword parameters"""
    obtained = subject1 + subject2 + subject3
    percentage = (obtained / total_marks) * 100
    return percentage

def book_details(title="Unknown", author="Unknown", price=0, year=2025):
    """Function with default keyword parameters"""
    print(f"\nTitle: {title}")
    print(f"Author: {author}")
    print(f"Price: ₹{price}")
    print(f"Year: {year}")

def greet(name, message="Hello", time="Morning"):
    """Greeting function with keyword parameters"""
    print(f"{message}, {name}! Good {time}!")

# Demonstrating keyword parameters
print("=== Example 1: Using keyword parameters (order doesn't matter) ===\n")
student_info(name="Kaivalaya", roll=205, branch="BCA", marks=85)

print("\n=== Example 2: Different order with keywords ===\n")
student_info(marks=90, branch="CSE", name="Alice", roll=101)

print("\n=== Example 3: Mixed positional and keyword ===\n")
student_info("Bob", 102, marks=88, branch="IT")

print("\n=== Example 4: Default keyword parameters ===\n")
book_details(title="Python Programming", author="John Smith")
book_details(title="Data Science", price=599)
book_details()  # All defaults

print("\n=== Example 5: Calculate percentage ===\n")
per1 = calculate_percentage(subject1=85, subject2=90, subject3=78)
print(f"Percentage 1: {per1:.2f}%")

per2 = calculate_percentage(subject3=70, subject1=80, subject2=75, total_marks=300)
print(f"Percentage 2: {per2:.2f}%")

print("\n=== Example 6: Greeting with keywords ===\n")
greet(name="Kaivalaya")
greet(name="Alice", message="Hi", time="Evening")
greet(time="Night", name="Bob", message="Hey")
