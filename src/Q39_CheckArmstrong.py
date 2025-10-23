# Write a program to check if a number is armstrong or not.

# Get input from user
num = int(input("Enter a number: "))

# Convert to string to get digits
num_str = str(num)
num_digits = len(num_str)

# Calculate sum of digits raised to power
sum_of_powers = 0
for digit in num_str:
    sum_of_powers += int(digit) ** num_digits

# Check if armstrong number
if sum_of_powers == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
