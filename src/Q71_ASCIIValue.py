# Write a program to find the ASCII value of a character.

def get_ascii(char):
    """Return ASCII value of a character"""
    return ord(char)

def get_char_from_ascii(ascii_value):
    """Return character from ASCII value"""
    return chr(ascii_value)

# Get input from user
print("=== ASCII Value Finder ===\n")
char = input("Enter a character: ")

# Get ASCII value
ascii_value = get_ascii(char)
print(f"\nASCII value of '{char}' is {ascii_value}")

# Demonstrate reverse conversion
print(f"\n=== Reverse Conversion ===")
print(f"Character for ASCII {ascii_value} is '{get_char_from_ascii(ascii_value)}'")

# Display ASCII values for common characters
print("\n=== Common ASCII Values ===")
characters = ['A', 'Z', 'a', 'z', '0', '9', ' ', '@']
for ch in characters:
    print(f"'{ch}' = {get_ascii(ch)}")

# Display ASCII range for alphabets
print("\n=== ASCII Range ===")
print(f"Uppercase A-Z: {get_ascii('A')} to {get_ascii('Z')}")
print(f"Lowercase a-z: {get_ascii('a')} to {get_ascii('z')}")
print(f"Digits 0-9: {get_ascii('0')} to {get_ascii('9')}")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
