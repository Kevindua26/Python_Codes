# Write a program to print armstrong numbers from 1 to 1000.

print("Armstrong numbers from 1 to 1000:")

# Check each number from 1 to 1000
for num in range(1, 1001):
    # Convert to string to get digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate sum of digits raised to power
    sum_of_powers = 0
    for digit in num_str:
        sum_of_powers += int(digit) ** num_digits
    
    # Print if armstrong number
    if sum_of_powers == num:
        print(num, end=" ")

print('\This code is written and executed by Kaivalaya Dua 0231BCA205')
