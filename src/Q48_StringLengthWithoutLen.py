# Write a program to calculate the length of a string without using the built-in len() function.
print('Q48_StringLengthWithoutLen.py')

# Get input from user
text = input("Enter a string: ")

# Calculate length without len()
length = 0
for char in text:
    length += 1

# Display result
print(f"Length of '{text}' is {length}")
