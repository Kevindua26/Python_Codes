# Write a program for user - defined exceptions.

# Define custom exception
class InvalidMarksError(Exception):
    def __init__(self, marks):
        self.marks = marks
        self.message = f"Invalid marks: {marks}. Marks must be between 0 and 100"
        super().__init__(self.message)

# Function that uses custom exception
def check_marks(marks):
    if marks < 0 or marks > 100:
        raise InvalidMarksError(marks)
    else:
        print(f"Marks {marks} is valid")

# Test the custom exception
try:
    marks = int(input("Enter marks: "))
    check_marks(marks)
except InvalidMarksError as e:
    print(f"Error: {e}")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
