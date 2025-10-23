# Write a program to perform different operations on strings.

# Create a string
text = "Hello World"

print("Original String:", text)
print("\n--- String Operations ---\n")

# 1. Convert to uppercase
print("1. Uppercase:", text.upper())

# 2. Convert to lowercase
print("2. Lowercase:", text.lower())

# 3. String length
print("3. Length:", len(text))

# 4. Replace word
print("4. Replace 'World' with 'Python':", text.replace("World", "Python"))

# 5. Split string
print("5. Split into words:", text.split())

# 6. Find substring
print("6. Find 'World':", text.find("World"))

# 7. Count character
print("7. Count 'o':", text.count('o'))

# 8. Check if starts with
print("8. Starts with 'Hello':", text.startswith("Hello"))

# 9. Check if ends with
print("9. Ends with 'World':", text.endswith("World"))

# 10. String concatenation
print("10. Concatenation:", text + " from Python")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
