# Write a basic program of string operations.
print('Q104_StringOperations.py')

text = "Hello World"

print("Original String:", text)
print("\n=== String Operations ===")

# 1. Uppercase
print("1. Uppercase:", text.upper())

# 2. Lowercase
print("2. Lowercase:", text.lower())

# 3. Length
print("3. Length:", len(text))

# 4. Replace
print("4. Replace:", text.replace("World", "Python"))

# 5. Split
print("5. Split:", text.split())

# 6. Find
print("6. Find 'World':", text.find("World"))

# 7. Count
print("7. Count 'l':", text.count('l'))

# 8. Starts with
print("8. Starts with 'Hello':", text.startswith("Hello"))

# 9. Ends with
print("9. Ends with 'World':", text.endswith("World"))

# 10. Concatenation
print("10. Concatenation:", text + " from Python")
