# Write a program to create a using the class keyword, and an object is created by calling the class.

# Define a class
class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll}")
        print(f"Marks: {self.marks}")

# Create objects (instances) of the class
student1 = Student("Kaivalaya", 205, 85)
student2 = Student("Alice", 101, 90)

# Use the objects
print("Student 1:")
student1.display()

print("\nStudent 2:")
student2.display()

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
