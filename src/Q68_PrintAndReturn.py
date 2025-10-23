# Write a program where you use both print and return in the same program (percentage calculation).

def calculate_percentage(marks_obtained, total_marks):
    """Calculate percentage and return it"""
    percentage = (marks_obtained / total_marks) * 100
    print(f"Marks Obtained: {marks_obtained}/{total_marks}")
    return percentage

def get_grade(percentage):
    """Get grade based on percentage and return it"""
    print(f"Percentage: {percentage:.2f}%")
    
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    
    print(f"Grade: {grade}")
    return grade

def display_result(name, roll, percentage, grade):
    """Display final result using print"""
    print("\n" + "="*40)
    print("        STUDENT REPORT CARD")
    print("="*40)
    print(f"Name: {name}")
    print(f"Roll Number: {roll}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print("="*40)
    
    if grade in ['A+', 'A', 'B']:
        print("Status: PASS - Excellent Performance!")
    elif grade in ['C', 'D']:
        print("Status: PASS - Need Improvement")
    else:
        print("Status: FAIL - Work Harder!")

# Get student details
name = input("Enter student name: ")
roll = input("Enter roll number: ")
marks_obtained = float(input("Enter marks obtained: "))
total_marks = float(input("Enter total marks: "))

print("\n--- Calculating Results ---\n")

# Calculate percentage (uses both print and return)
percentage = calculate_percentage(marks_obtained, total_marks)

# Get grade (uses both print and return)
grade = get_grade(percentage)

# Display complete result (uses print only)
display_result(name, roll, percentage, grade)

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
