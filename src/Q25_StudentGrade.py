# Program to grade the student according to the percentage

# Get marks for 5 subjects from user
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
subject4 = float(input("Enter marks for subject 4: "))
subject5 = float(input("Enter marks for subject 5: "))

# Calculate total marks and percentage
total_marks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = (total_marks / 500) * 100

print(f"Total marks: {total_marks}")
print(f"Percentage: {percentage}%")

# Grade according to percentage
if percentage > 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "D"

print(f"Grade: {grade}")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
