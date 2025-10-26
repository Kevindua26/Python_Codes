# Write a program to display calendar.
print('Q73_DisplayCalendar.py')

import calendar

def display_month_calendar(year, month):
    """Display calendar for a specific month"""
    print(calendar.month(year, month))

def display_year_calendar(year):
    """Display calendar for entire year"""
    print(calendar.calendar(year))

def get_day_name(year, month, day):
    """Get day name for a specific date"""
    day_number = calendar.weekday(year, month, day)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days[day_number]

def is_leap_year(year):
    """Check if year is leap year"""
    return calendar.isleap(year)

# Display menu
print("=== Calendar Program ===\n")
print("1. Display Month Calendar")
print("2. Display Year Calendar")
print("3. Get Day Name")
print("4. Check Leap Year")

choice = input("\nEnter your choice (1-4): ")

if choice == '1':
    # Display month calendar
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    print()
    display_month_calendar(year, month)

elif choice == '2':
    # Display year calendar
    year = int(input("Enter year: "))
    print()
    display_year_calendar(year)

elif choice == '3':
    # Get day name
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    day = int(input("Enter day: "))
    day_name = get_day_name(year, month, day)
    print(f"\n{day}/{month}/{year} is a {day_name}")

elif choice == '4':
    # Check leap year
    year = int(input("Enter year: "))
    if is_leap_year(year):
        print(f"\n{year} is a LEAP YEAR")
    else:
        print(f"\n{year} is NOT a leap year")

else:
    print("Invalid choice!")
