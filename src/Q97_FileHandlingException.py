# Write a program for file handling with exception.

try:
    # Try to open and read file
    file = open("data.txt", "r")
    content = file.read()
    print("File content:")
    print(content)
    file.close()
except FileNotFoundError:
    print("File not found! Creating new file...")
    # Create file if not exists
    file = open("data.txt", "w")
    file.write("Hello, this is sample data!")
    file.close()
    print("File created successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("File operation completed!")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
