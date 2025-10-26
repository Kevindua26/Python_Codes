# Write a program to perform set operations.
print('Q55_SetOperations.py')

# Create sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)
print("\n=== Set Operations ===\n")

# 1. Union - all elements from both sets
print("1. Union (set1 | set2):", set1 | set2)
print("   Union using union():", set1.union(set2))

# 2. Intersection - common elements
print("\n2. Intersection (set1 & set2):", set1 & set2)
print("   Intersection using intersection():", set1.intersection(set2))

# 3. Difference - elements in set1 but not in set2
print("\n3. Difference (set1 - set2):", set1 - set2)
print("   Difference using difference():", set1.difference(set2))

# 4. Symmetric Difference - elements in either set but not both
print("\n4. Symmetric Difference (set1 ^ set2):", set1 ^ set2)
print("   Using symmetric_difference():", set1.symmetric_difference(set2))

# 5. Add element to set
set1.add(6)
print("\n5. After adding 6 to set1:", set1)

# 6. Remove element
set1.remove(6)
print("6. After removing 6:", set1)

# 7. Discard element (doesn't raise error if not found)
set1.discard(10)
print("7. After discard(10):", set1)

# 8. Check if element exists
print("\n8. Is 3 in set1?", 3 in set1)

# 9. Length of set
print("9. Length of set1:", len(set1))

# 10. Clear set
set3 = {1, 2, 3}
set3.clear()
print("10. After clear():", set3)
