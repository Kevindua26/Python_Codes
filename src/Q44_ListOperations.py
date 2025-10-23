# Write a program to perform different operations on the list.

# Create a list
my_list = [10, 20, 30, 40, 50]

print("Original List:", my_list)
print("\n--- List Operations ---\n")

# 1. Append element
my_list.append(60)
print("1. After append(60):", my_list)

# 2. Insert element at index
my_list.insert(2, 25)
print("2. After insert(2, 25):", my_list)

# 3. Remove element
my_list.remove(25)
print("3. After remove(25):", my_list)

# 4. Pop element (remove last)
popped = my_list.pop()
print("4. After pop():", my_list, "| Popped:", popped)

# 5. Index of element
print("5. Index of 30:", my_list.index(30))

# 6. Count occurrences
print("6. Count of 20:", my_list.count(20))

# 7. Sort list
my_list.sort()
print("7. After sort():", my_list)

# 8. Reverse list
my_list.reverse()
print("8. After reverse():", my_list)

# 9. List length
print("9. Length of list:", len(my_list))

# 10. Clear list
my_list.clear()
print("10. After clear():", my_list)

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
