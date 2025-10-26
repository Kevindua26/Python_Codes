# Write a program to demonstrate inheritance.
print('Q82_Inheritance.py')

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print(f"{self.name} makes a sound")

# Child class inheriting from Animal
class Dog(Animal):
    def sound(self):
        print(f"{self.name} barks: Woof Woof!")

# Another child class
class Cat(Animal):
    def sound(self):
        print(f"{self.name} meows: Meow Meow!")

# Create objects
animal = Animal("Generic Animal")
dog = Dog("Tommy")
cat = Cat("Kitty")

# Call methods
animal.sound()
dog.sound()
cat.sound()
