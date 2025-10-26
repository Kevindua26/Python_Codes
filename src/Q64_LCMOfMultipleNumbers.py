# Write a program to find the lcm of multiple numbers.
print('Q64_LCMOfMultipleNumbers.py')

def find_gcd(a, b):
    """Find GCD of two numbers"""
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    """Find LCM of two numbers"""
    return (a * b) // find_gcd(a, b)

def find_lcm_multiple(numbers):
    """Find LCM of multiple numbers"""
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = find_lcm(lcm, num)
    return lcm

# Get input from user
n = int(input("How many numbers? "))
numbers = []

print("Enter the numbers:")
for i in range(n):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)

# Calculate and display LCM
result = find_lcm_multiple(numbers)
print(f"\nLCM of {numbers} is {result}")
