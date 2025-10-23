# Write a program to handle multiple exceptions in one line.

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    my_list = [1, 2, 3]
    print(my_list[num])
except (ValueError, ZeroDivisionError, IndexError) as e:
    print(f"Error occurred: {e}")
    print(f"Error type: {type(e).__name__}")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
