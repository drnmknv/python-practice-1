# a) Input & Variables
name = input("Enter student name: ")
math = float(input("Enter Math grade: "))
physics = float(input("Enter Physics grade: "))
python = float(input("Enter Python grade: "))

# b) Calculations
average = (math + physics + python) / 3

if average >= 90:
    letter_grade = 'A'
elif average >= 75:
    letter_grade = 'B'
elif average >= 60:
    letter_grade = 'C'
elif average >= 50:
    letter_grade = 'D'
else:
    letter_grade = 'F'

schlr = average >= 90 and math >= 70 and physics >= 70 and python >= 70

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
print("Letter hrade         :", letter_grade)
print("Scholarship :", schlr)
print("==============================")

# d) Comparison
print("Perfect score:", math == 100 and physics == 100 and python == 100)

grades = [math, physics, python]
subjects = ['math', 'physics', 'python']

for i in range(len(subjects)):
    cur_gr = grades[i]
    cur_sub = subjects[i]

    if cur_gr >= 90:
        comment = "Excellent"
    elif cur_gr >= 75:
        comment = "Good"
    elif cur_gr >= 60:
        comment = "satisfied"
    else :
        comment = "Fail"

    print("Subject :", cur_sub , "Grade : ", cur_gr , "---->" , comment)