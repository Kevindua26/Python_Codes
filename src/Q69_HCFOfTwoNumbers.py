# Write a program to find the hcf of two numbers.
print('Q69_HCFOfTwoNumbers.py')

def find_hcf(a, b):
    """Find HCF/GCD using Euclidean algorithm"""
    # Store original values for display
    original_a, original_b = a, b
    
    # Euclidean algorithm
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    
    return a

# Get input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate HCF
hcf = find_hcf(num1, num2)

# Display result
print(f"\nHCF of {num1} and {num2} is {hcf}")

# Alternative method using recursion
def find_hcf_recursive(a, b):
    """Find HCF using recursion"""
    if b == 0:
        return a
    return find_hcf_recursive(b, a % b)

print(f"HCF using recursion: {find_hcf_recursive(num1, num2)}")
