# Write a program to raise and re - raise exceptions.

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error in divide function!")
        raise  # Re-raise the exception

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = divide(num1, num2)
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Caught re-raised exception: Cannot divide by zero!")
except Exception as e:
    print(f"Error: {e}")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
