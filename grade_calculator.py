grade1 = float(input("Enter your first grade: "))
grade2 = float(input("Enter your second grade: "))
oral = float(input("Enter your oral score: "))

average = (grade1 + grade2 + oral) / 3

if average >= 85:
    grade = 5
elif average >= 70:
    grade = 4
elif average >= 55:
    grade = 3
elif average >= 40:
    grade = 2
else:
    grade = 1

print("Your average", average)
print("Your grade", grade)