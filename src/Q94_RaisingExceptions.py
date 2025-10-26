# Write a program for raising exceptions.
print('Q94_RaisingExceptions.py')

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    elif age < 18:
        raise Exception("Age must be 18 or above!")
    else:
        print(f"Age {age} is valid")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except ValueError as e:
    print(f"ValueError: {e}")
except Exception as e:
    print(f"Error: {e}")
