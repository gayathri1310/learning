Marks = int(input("Enter the Marks: "))
if Marks >= 90:
    grade = "A"
elif Marks >= 80:
    grade = "B"
elif Marks >= 70:
    grade = "C"
elif Marks >= 60:
    grade = "D"
else:
    grade = "F"

print("your grade is", grade)