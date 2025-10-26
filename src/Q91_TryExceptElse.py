# Write a basic try - except - else program.
print('Q91_TryExceptElse.py')

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except:
    print("Error occurred!")
else:
    print(f"Result: {result}")
    print("No error occurred!")
