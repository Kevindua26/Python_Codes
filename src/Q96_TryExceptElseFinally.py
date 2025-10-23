# Write a basic program try - except - else - finally.

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

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
