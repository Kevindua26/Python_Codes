# Program to check if a single character is vowel or not

# Get character from user
char = input("Enter a single character: ").lower()

# Check if vowel
if char in "aeiou":
    print(f"'{char}' is a vowel")
else:
    print(f"'{char}' is not a vowel")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
