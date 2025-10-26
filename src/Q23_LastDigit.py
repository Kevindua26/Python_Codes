# Program to print the last digit of given integer number
print('Q23_LastDigit.py')

# Get number from user
number = int(input("Enter an integer number: "))

# Get last digit using modulo operator
last_digit = number % 10
print(f"The last digit of {number} is: {last_digit}")
