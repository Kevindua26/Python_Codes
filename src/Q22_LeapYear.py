# Program to check whether the year is leap year or not

# Get year from user
year = int(input("Enter a year: "))

# Check if leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
