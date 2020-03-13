import math

first_name = (str(input("type in your first name:")))
for i in first_name:
    if i != "":
        print("Invalid name. You have typed in a number within your name!!")
    exit()
surname = (str(input("type in your surname:")))
exam_mark = (int(input("type in your maths mark:")))


if exam_mark <= 49:
    print(first_name, surname, "Grade D - Fail")
elif (exam_mark >= 50) and (exam_mark <= 59):
    print(first_name, surname, "Grade C - Pass")
elif (exam_mark >= 60) and (exam_mark <= 79):
    print(first_name, surname, "Grade B - satisfactory")
elif (exam_mark >= 80) and (exam_mark <= 100):
    print(first_name, surname, "Grade A - Outstanding")
else :
    print("out of range")
