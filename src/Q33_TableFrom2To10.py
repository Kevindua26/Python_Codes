# Write a program to print the table from 2 to 10.
print('Q33_TableFrom2To10.py')

# Loop through numbers 2 to 10
for num in range(2, 11):
    print(f"\nTable of {num}:")
    # Print multiplication table for each number
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
