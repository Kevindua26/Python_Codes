# Write a program to handle exceptions in list operations.
print('Q101_ExceptionsListOperations.py')

my_list = [10, 20, 30, 40, 50]

try:
    # Try to access element
    index = int(input("Enter index: "))
    print(f"Element at index {index}: {my_list[index]}")
    
    # Try to remove element
    value = int(input("Enter value to remove: "))
    my_list.remove(value)
    print(f"Updated list: {my_list}")
    
except IndexError:
    print("Error: Index out of range!")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
