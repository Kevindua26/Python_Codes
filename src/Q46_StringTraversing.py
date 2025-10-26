# Write a program to demonstrate string traversing using the for loop.
print('Q46_StringTraversing.py')

# Get input from user
text = input("Enter a string: ")

print("\nTraversing string character by character:\n")

# Traverse string using for loop
for char in text:
    print(f"Character: {char}")

print("\nTraversing with index:")

# Traverse with index
for i in range(len(text)):
    print(f"Index {i}: {text[i]}")
