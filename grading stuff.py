import math

first_name = (str(input("type in your first name:")))
if first_name is complex:
    print("name has a number in")
    first_name = (str(input("type in your first name:")))
else:
    first_name = (str(input("type in your first name:")))

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
