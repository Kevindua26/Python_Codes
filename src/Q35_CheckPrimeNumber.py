# Write a program to check whether the number is prime number or not.

# Get input from user
num = int(input("Enter a number: "))

# Prime number check
if num <= 1:
    print(f"{num} is not a prime number")
else:
    is_prime = True
    # Check if number has any divisor from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    # Display result
    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
