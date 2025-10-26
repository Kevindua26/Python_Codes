# Write a program to perform file operations : write, read, search.
print('Q103_FileOperations.py')

# Write to file
def write_file():
    file = open("students.txt", "w")
    file.write("Alice,85\n")
    file.write("Bob,90\n")
    file.write("Charlie,78\n")
    file.close()
    print("Data written to file")

# Read from file
def read_file():
    file = open("students.txt", "r")
    content = file.read()
    print("\nFile content:")
    print(content)
    file.close()

# Search in file
def search_file(name):
    file = open("students.txt", "r")
    found = False
    for line in file:
        if name in line:
            print(f"Found: {line.strip()}")
            found = True
            break
    if not found:
        print(f"{name} not found!")
    file.close()

# Perform operations
write_file()
read_file()

print("\n=== Search Operation ===")
search_name = input("Enter name to search: ")
search_file(search_name)
