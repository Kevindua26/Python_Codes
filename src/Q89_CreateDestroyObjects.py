# Write a program to create and destroy multiple objects.
print('Q89_CreateDestroyObjects.py')

class Student:
    count = 0  # Class variable to count objects
    
    def __init__(self, name):
        self.name = name
        Student.count += 1
        print(f"Object created: {self.name} (Total objects: {Student.count})")
    
    def __del__(self):
        Student.count -= 1
        print(f"Object destroyed: {self.name} (Remaining objects: {Student.count})")

# Create multiple objects
print("=== Creating Objects ===")
s1 = Student("Alice")
s2 = Student("Bob")
s3 = Student("Charlie")

print(f"\nTotal objects: {Student.count}")

# Destroy objects
print("\n=== Destroying Objects ===")
del s1
del s2

print(f"\nRemaining objects: {Student.count}")

# Destroy remaining object
del s3

print(f"\nFinal count: {Student.count}")
