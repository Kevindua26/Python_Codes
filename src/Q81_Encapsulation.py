# Write a program to demonstrate encapsulation.
print('Q81_Encapsulation.py')

class Student:
    def __init__(self, name, marks):
        self.__name = name  # Private variable
        self.__marks = marks  # Private variable
    
    # Getter methods
    def get_name(self):
        return self.__name
    
    def get_marks(self):
        return self.__marks
    
    # Setter methods
    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks!")
    
    def display(self):
        print(f"Name: {self.__name}, Marks: {self.__marks}")

# Create object
student = Student("Kaivalaya", 85)

# Access using getter
print(f"Name: {student.get_name()}")
print(f"Marks: {student.get_marks()}")

# Modify using setter
student.set_marks(90)
student.display()

# Direct access won't work (encapsulated)
# print(student.__marks)  # This will give error
