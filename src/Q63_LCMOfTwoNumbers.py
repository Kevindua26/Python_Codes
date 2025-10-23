# Write a program in python to find the lcm of 2 numbers.

def find_gcd(a, b):
    """Find GCD using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    """Find LCM using formula: LCM = (a * b) / GCD"""
    gcd = find_gcd(a, b)
    lcm = (a * b) // gcd
    return lcm

# Get input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate and display LCM
lcm = find_lcm(num1, num2)
print(f"\nLCM of {num1} and {num2} is {lcm}")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
