# Program to get user input and save report to a file
print('Q26_SaveReportToFile.py')

# Get user input
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

# Create report content
report = f"User Report\n"
report += f"-----------\n"
report += f"Name: {name}\n"
report += f"Age: {age}\n"
report += f"City: {city}\n"

# Save report to file
with open("user_report.txt", "w") as file:
    file.write(report)

print("Report saved to user_report.txt")
