# Program to check login and password

# Set correct login credentials
correct_username = "admin"
correct_password = "password123"

# Get user input
username = input("Enter username: ")
password = input("Enter password: ")

# Check login credentials
if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid username or password")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
