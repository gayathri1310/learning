studentGrades = {"XYZ": "A","ABC": "B"}

studentGrades["PQR"] = "C"

if "XYZ" in studentGrades:
    studentGrades["XYZ"] = "D"
if "ABC" in studentGrades:
    studentGrades["ABC"] = "C"
else:
    print("Student not found.")

print("studentGrades :",  studentGrades)