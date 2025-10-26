# Write a program to perform different range functions.
print('Q54_RangeFunctions.py')

print("=== Different Range Functions ===\n")

# 1. Range with single argument (stop)
print("1. range(10):")
for i in range(10):
    print(i, end=" ")
print()

# 2. Range with start and stop
print("\n2. range(5, 15):")
for i in range(5, 15):
    print(i, end=" ")
print()

# 3. Range with start, stop, and step
print("\n3. range(0, 20, 2) - Even numbers:")
for i in range(0, 20, 2):
    print(i, end=" ")
print()

# 4. Range with negative step (descending)
print("\n4. range(10, 0, -1) - Countdown:")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# 5. Range with negative numbers
print("\n5. range(-5, 5):")
for i in range(-5, 5):
    print(i, end=" ")
print()

# 6. Convert range to list
print("\n6. List from range(1, 11):")
range_list = list(range(1, 11))
print(range_list)

# 7. Convert range to tuple
print("\n7. Tuple from range(5, 50, 5):")
range_tuple = tuple(range(5, 50, 5))
print(range_tuple)

# 8. Check length of range
print("\n8. Length of range(1, 100):", len(range(1, 100)))

# 9. Access range element by index
print("\n9. Element at index 5 in range(10, 50):", range(10, 50)[5])
