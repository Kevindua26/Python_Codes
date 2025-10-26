# Write a program to perform different operations on tuples.
print('Q50_TupleOperations.py')

# Create a tuple
my_tuple = (10, 20, 30, 40, 50, 20)

print("Original Tuple:", my_tuple)
print("\n--- Tuple Operations ---\n")

# 1. Access element by index
print("1. Element at index 2:", my_tuple[2])

# 2. Slicing tuple
print("2. Slice [1:4]:", my_tuple[1:4])

# 3. Length of tuple
print("3. Length:", len(my_tuple))

# 4. Count occurrences
print("4. Count of 20:", my_tuple.count(20))

# 5. Find index
print("5. Index of 30:", my_tuple.index(30))

# 6. Check if element exists
print("6. Is 40 in tuple?", 40 in my_tuple)

# 7. Maximum value
print("7. Maximum value:", max(my_tuple))

# 8. Minimum value
print("8. Minimum value:", min(my_tuple))

# 9. Sum of elements
print("9. Sum of elements:", sum(my_tuple))

# 10. Concatenate tuples
tuple2 = (60, 70)
print("10. Concatenation:", my_tuple + tuple2)

# 11. Convert tuple to list
print("11. Convert to list:", list(my_tuple))
