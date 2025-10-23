# Write a program to count the total number of vowels, consonants and blanks in a string.

# Get input from user
text = input("Enter a string: ")

# Initialize counters
vowels = 0
consonants = 0
blanks = 0

# Define vowels
vowel_list = "aeiouAEIOU"

# Count vowels, consonants, and blanks
for char in text:
    if char == ' ':
        blanks += 1
    elif char.isalpha():  # Check if character is alphabet
        if char in vowel_list:
            vowels += 1
        else:
            consonants += 1

# Display results
print(f"\nResults:")
print(f"Total Vowels: {vowels}")
print(f"Total Consonants: {consonants}")
print(f"Total Blanks: {blanks}")

# Additional details
print(f"\nTotal Characters: {len(text)}")
print(f"Alphabets: {vowels + consonants}")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
