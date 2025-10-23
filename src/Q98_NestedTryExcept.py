# Write a program for nested try - except.

try:
    num = int(input("Enter a number: "))
    
    try:
        result = 10 / num
        print(f"Result: {result}")
        
        try:
            my_list = [1, 2, 3]
            print(f"Element at index {num}: {my_list[num]}")
        except IndexError:
            print("Index out of range!")
    
    except ZeroDivisionError:
        print("Cannot divide by zero!")

except ValueError:
    print("Invalid input! Please enter a number")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
