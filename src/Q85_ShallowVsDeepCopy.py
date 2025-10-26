# Write a program to demonstrate differences between shallow copy and deep copy.
print('Q85_ShallowVsDeepCopy.py')

import copy

# Original list with nested list
original = [1, 2, [3, 4], 5]

# Shallow copy
shallow = copy.copy(original)

# Deep copy
deep = copy.deepcopy(original)

print("Original:", original)
print("Shallow copy:", shallow)
print("Deep copy:", deep)

# Modify nested list in original
original[2][0] = 999

print("\nAfter modifying original[2][0] to 999:")
print("Original:", original)
print("Shallow copy:", shallow)  # Changed (shares nested list)
print("Deep copy:", deep)  # Not changed (independent copy)
