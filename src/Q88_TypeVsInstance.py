# Write a program to differentiate between type() and instance().

class Animal:
    pass

class Dog(Animal):
    pass

# Create objects
dog = Dog()
num = 10
text = "Hello"

# type() - returns the exact type of object
print("=== type() function ===")
print(f"type(dog): {type(dog)}")
print(f"type(num): {type(num)}")
print(f"type(text): {type(text)}")

# isinstance() - checks if object is instance of class (includes inheritance)
print("\n=== isinstance() function ===")
print(f"isinstance(dog, Dog): {isinstance(dog, Dog)}")
print(f"isinstance(dog, Animal): {isinstance(dog, Animal)}")  # True (inheritance)
print(f"isinstance(num, int): {isinstance(num, int)}")
print(f"isinstance(text, str): {isinstance(text, str)}")

# Difference
print("\n=== Key Difference ===")
print(f"type(dog) == Dog: {type(dog) == Dog}")
print(f"type(dog) == Animal: {type(dog) == Animal}")  # False (exact type check)
print(f"isinstance(dog, Animal): {isinstance(dog, Animal)}")  # True (checks inheritance)

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
