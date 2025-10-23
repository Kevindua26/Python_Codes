# Write a program to handle exceptions with dictionary lookup.

student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

try:
    # Try to get marks
    name = input("Enter student name: ")
    marks = student_marks[name]
    print(f"{name}'s marks: {marks}")
    
except KeyError:
    print(f"Error: Student '{name}' not found in database!")
    print(f"Available students: {list(student_marks.keys())}")
except Exception as e:
    print(f"Error: {e}")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
