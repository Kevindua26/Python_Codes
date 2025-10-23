# Write a program on getting multiple inputs from users and print them in formatted way

# Getting multiple inputs from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
hobby = input("Enter your favorite hobby: ")
height = float(input("Enter your height in feet: "))

# Printing information in different formatted ways
print("\n=== User Information ===")

# Creating a summary
summary = (f"""
Age: {age} years
City: {city}
Favorite Hobby: {hobby}
Height: {height:.2f} meters""")

# .format(name=name, age=age, city=city, hobby=hobby, height=height))

print(summary)

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
