# Write a program to handle multiple exceptions.

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a number")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Some error occurred: {e}")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
