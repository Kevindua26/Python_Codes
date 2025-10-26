# Program to check if a single character is vowel or not
print('Q27_CheckVowel.py')

# Get character from user
char = input("Enter a single character: ").lower()

# Check if vowel
if char in "aeiou":
    print(f"'{char}' is a vowel")
else:
    print(f"'{char}' is not a vowel")
