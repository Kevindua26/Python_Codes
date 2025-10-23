# Write a program to perform different operations on dictionaries.

# Create a dictionary
student = {
    "name": "Kaivalaya",
    "roll": 205,
    "branch": "BCA",
    "marks": 85
}

print("Original Dictionary:", student)
print("\n--- Dictionary Operations ---\n")

# 1. Access value by key
print("1. Name:", student["name"])

# 2. Get method
print("2. Branch:", student.get("branch"))

# 3. Add new key-value pair
student["city"] = "Delhi"
print("3. After adding city:", student)

# 4. Update value
student["marks"] = 90
print("4. After updating marks:", student)

# 5. Get all keys
print("5. Keys:", student.keys())

# 6. Get all values
print("6. Values:", student.values())

# 7. Get all items (key-value pairs)
print("7. Items:", student.items())

# 8. Check if key exists
print("8. Is 'name' in dict?", "name" in student)

# 9. Remove item using pop
removed = student.pop("city")
print("9. After pop('city'):", student, "| Removed:", removed)

# 10. Length of dictionary
print("10. Length:", len(student))

# 11. Copy dictionary
student_copy = student.copy()
print("11. Copied dictionary:", student_copy)

# 12. Clear dictionary
student_copy.clear()
print("12. After clear():", student_copy)

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
