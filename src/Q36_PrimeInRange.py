# Write a program to check prime numbers between the given range.

# Get range from user
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"\nPrime numbers between {start} and {end}:")

# Check each number in the range
for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        # Check if number is prime
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        
        # Print if prime
        if is_prime:
            print(num, end=" ")

print('\This code is written and executed by Kaivalaya Dua 0231BCA205')
