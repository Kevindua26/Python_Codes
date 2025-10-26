# Write a basic try - finally program.
print('Q92_TryFinally.py')

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except:
    print("Error occurred!")
finally:
    print("This always executes!")
