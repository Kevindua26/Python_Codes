# Program to check if a number is divisible by 2 and 3

# Get number from user
number = int(input("Enter a number: "))

# Check if divisible by both 2 and 3
if number % 2 == 0 and number % 3 == 0:
    print(f"{number} is divisible by both 2 and 3")
else:
    print(f"{number} is not divisible by both 2 and 3")
