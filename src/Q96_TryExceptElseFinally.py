# Write a basic program try - except - else - finally.
print('Q96_TryExceptElseFinally.py')

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")
    print("Operation successful!")
finally:
    print("Execution completed!")
