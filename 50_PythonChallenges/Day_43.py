# Day 43

## Student Marks

'''
Write a function called student_marks that records marks achieved by students in a test. The function should ask the user to input the name of the student and then ask the user to input the marks achieved by the student. 
The information should be stored in a dictionary. The name is the key and the marks are the value. When the user enters done, the function should return a dictionary of names and vales entered. 
'''

def student_marks():
    students_dict = {}
    while True:
        student_name = input("Student Name: ")
        student_surname = ""
        if student_name in students_dict.keys():
            student_surname = input("Student Surname: ")
        student_name += student_surname
        student_marks = []
        while True:
            mark = input("Inser mark -done to stop inserting-: ").rstrip()
            if mark == "done":
                break
            else:
                student_marks.append(mark)
        students_dict[student_name] = student_marks
        to_kepp_inserting = input("Write 'done' to stop inserting : ")
        if to_kepp_inserting == "done":
            break
    return students_dict

print(student_marks())