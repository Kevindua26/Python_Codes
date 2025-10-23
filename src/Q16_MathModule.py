import math

# Demonstrating math module functions and constants
def demonstrate_math_operations():
    # Mathematical constants
    print("=== Mathematical Constants ===")
    print(f"Pi (π): {math.pi}")
    print(f"Euler's number (e): {math.e}")
    print(f"Tau (τ): {math.tau}")  # tau is 2*pi

    # Basic mathematical functions
    print("\n=== Basic Mathematical Functions ===")
    number = 16
    print(f"Square root of {number}: {math.sqrt(number)}")
    print(f"Factorial of 5: {math.factorial(5)}")
    print(f"GCD of 48 and 60: {math.gcd(48, 60)}")
    print(f"Absolute value of -7.8: {math.fabs(-7.8)}")

    # Trigonometric functions (input in radians)
    print("\n=== Trigonometric Functions ===")
    angle_deg = 45
    angle_rad = math.radians(angle_deg)  # Convert degrees to radians
    print(f"Angle: {angle_deg} degrees = {angle_rad:.4f} radians")
    print(f"sin({angle_deg}°): {math.sin(angle_rad):.4f}")
    print(f"cos({angle_deg}°): {math.cos(angle_rad):.4f}")
    print(f"tan({angle_deg}°): {math.tan(angle_rad):.4f}")

    # Logarithmic functions
    print("\n=== Logarithmic Functions ===")
    num = 100
    print(f"Natural logarithm of {num}: {math.log(num):.4f}")
    print(f"Base-10 logarithm of {num}: {math.log10(num):.4f}")
    print(f"Base-2 logarithm of {num}: {math.log2(num):.4f}")

    # Power and exponential functions
    print("\n=== Power and Exponential Functions ===")
    base = 2
    exp = 3
    print(f"{base} raised to power {exp}: {math.pow(base, exp)}")
    print(f"e raised to power 2: {math.exp(2):.4f}")

    # Ceiling and Floor
    print("\n=== Ceiling and Floor ===")
    decimal_num = 7.6
    print(f"Ceiling of {decimal_num}: {math.ceil(decimal_num)}")
    print(f"Floor of {decimal_num}: {math.floor(decimal_num)}")

# Run the demonstration
if __name__ == "__main__":
    demonstrate_math_operations()

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
