# Write a program to determine whether the given string is a palindrome or not using slicing.
print('Q45_PalindromeSlicing.py')

# Get input from user
text = input("Enter a string: ")

# Convert to lowercase and remove spaces
text = text.replace(" ", "").lower()

# Check if palindrome using slicing
if text == text[::-1]:
    print(f"'{text}' is a PALINDROME")
else:
    print(f"'{text}' is NOT a palindrome")
