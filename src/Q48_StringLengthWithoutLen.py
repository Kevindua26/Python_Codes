# Write a program to calculate the length of a string without using the built-in len() function.

# Get input from user
text = input("Enter a string: ")

# Calculate length without len()
length = 0
for char in text:
    length += 1

# Display result
print(f"Length of '{text}' is {length}")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
