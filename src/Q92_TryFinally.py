# Write a basic try - finally program.

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except:
    print("Error occurred!")
finally:
    print("This always executes!")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
