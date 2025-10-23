# Write a program to use len(), del, remove(), and range() on list/tuple.

print("=== List Operations ===\n")

# Create a list
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)

# 1. len() - get length
print("1. Length of list:", len(my_list))

# 2. remove() - remove element by value
my_list.remove(30)
print("2. After remove(30):", my_list)

# 3. del - delete element by index
del my_list[1]
print("3. After del my_list[1]:", my_list)

# 4. range() - create list using range
range_list = list(range(1, 11))
print("4. List from range(1, 11):", range_list)

print("\n=== Tuple Operations ===\n")

# Create a tuple
my_tuple = (5, 10, 15, 20, 25)
print("Original Tuple:", my_tuple)

# 1. len() - get length
print("1. Length of tuple:", len(my_tuple))

# 2. del - delete entire tuple (can't delete individual elements)
temp_tuple = (1, 2, 3)
print("2. Before del:", temp_tuple)
del temp_tuple
print("   Tuple deleted successfully")

# 3. range() with tuple
range_tuple = tuple(range(5, 16, 2))
print("3. Tuple from range(5, 16, 2):", range_tuple)

# 4. Using range in loop with tuple
print("4. Accessing tuple elements using range:")
for i in range(len(my_tuple)):
    print(f"   Index {i}: {my_tuple[i]}")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
