# Write a program to count the occurrence of the user - entered words in a sentence.

# Get input from user
sentence = input("Enter a sentence: ")
word = input("Enter the word to count: ")

# Convert to lowercase for case-insensitive comparison
sentence_lower = sentence.lower()
word_lower = word.lower()

# Split sentence into words
words_list = sentence_lower.split()

# Count occurrences
count = 0
for w in words_list:
    if w == word_lower:
        count += 1

# Display result
print(f"The word '{word}' appears {count} times in the sentence")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
