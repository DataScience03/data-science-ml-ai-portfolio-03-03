"""
Project: Student Report Card Generator
Day: 01
Author: Krishna Priya
"""

# Student details
student_name = input("Enter student name: ")
student_class = input("Enter class: ")

# Marks input
maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

# Calculation
total_marks = maths + science + english
percentage = (total_marks / 300) * 100

# Grade logic
if percentage >= 85:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

# Output
print("\n--- REPORT CARD ---")
print("Name:", student_name)
print("Class:", student_class)
print("Total Marks:", total_marks)
print("Percentage:", round(percentage, 2))
print("Grade:", grade)
