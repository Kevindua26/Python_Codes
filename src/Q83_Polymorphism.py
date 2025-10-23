# Write a program to demonstrate polymorphism.

# Parent class
class Shape:
    def area(self):
        pass

# Child classes with same method name but different implementation
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Create objects
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Same method name, different behavior (polymorphism)
print(f"Circle area: {circle.area()}")
print(f"Rectangle area: {rectangle.area()}")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
