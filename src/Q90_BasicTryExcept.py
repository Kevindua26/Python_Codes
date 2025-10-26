# Write a basic try - except program.
print('Q90_BasicTryExcept.py')

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except:
    print("Error occurred!")
