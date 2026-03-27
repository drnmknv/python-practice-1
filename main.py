# a) Input & Variables
name = input("Enter student name: ")
math = float(input("Enter Math grade: "))
physics = float(input("Enter Physics grade: "))
python = float(input("Enter Python grade: "))

# b) Calculations
average = (math + physics + python) / 3

scholarship = 0
if average >= 90:
    scholarship = 35000

gpa = average / 25

# c) Formatted Output
print("==============================")
print("STUDENT REPORT CARD")
print("==============================")
print("Student     :", name)
print("Math        :", math)
print("Physics     :", physics)
print("Python      :", python)
print("------------------------------")
print("Average     :", round(average, 2))
print("GPA         :", round(gpa, 2))
print("Scholarship :", scholarship, "KZT")
print("==============================")

# d) Comparison
print("Scholarship granted:", average >= 90)
print("Perfect score:", math == 100 and physics == 100 and python == 100)