# Write a program to print the characters which are common in 2 strings.
print('Q47_CommonCharacters.py')

# Get input from user
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

print("\nCommon characters:")

# Find common characters
common_chars = []
for char in string1:
    if char in string2 and char not in common_chars:
        common_chars.append(char)
        print(char, end=" ")

# If no common characters
if len(common_chars) == 0:
    print("No common characters found")
