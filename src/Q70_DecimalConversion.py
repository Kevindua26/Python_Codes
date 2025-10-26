# Write a program to convert decimal numbers to binary, octal and hexadecimal.
print('Q70_DecimalConversion.py')

def decimal_to_binary(num):
    """Convert decimal to binary"""
    return bin(num)[2:]  # [2:] removes '0b' prefix

def decimal_to_octal(num):
    """Convert decimal to octal"""
    return oct(num)[2:]  # [2:] removes '0o' prefix

def decimal_to_hexadecimal(num):
    """Convert decimal to hexadecimal"""
    return hex(num)[2:]  # [2:] removes '0x' prefix

# Get input from user
decimal_num = int(input("Enter a decimal number: "))

# Convert to different number systems
binary = decimal_to_binary(decimal_num)
octal = decimal_to_octal(decimal_num)
hexadecimal = decimal_to_hexadecimal(decimal_num)

# Display results
print("\n" + "="*40)
print(f"Decimal Number: {decimal_num}")
print("="*40)
print(f"Binary: {binary}")
print(f"Octal: {octal}")
print(f"Hexadecimal: {hexadecimal.upper()}")
print("="*40)

# Manual conversion for binary (optional demonstration)
def manual_decimal_to_binary(num):
    """Manual method to convert decimal to binary"""
    if num == 0:
        return "0"
    
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary

print(f"\nManual Binary Conversion: {manual_decimal_to_binary(decimal_num)}")
