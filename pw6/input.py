from domains.student import student
from domains.course import course
import pickle
import zipfile
import os
import zlib

def student_input(students):
    student_num = int(input("Enter the number of students: "))
    for i in range(student_num):
        student_id = input("Enter the student id: ")
        student_name = input("Enter the student name: ")
        dob = input("Enter day of birth:")
        students[student_id] = student(student_id, student_name, dob)
    with open("students.pickle", 'wb') as f:  
        pickle.dump(students, f)
    
def course_input(courses):
    course_num = int(input("Enter the number of courses: "))
    for i in range(course_num):
        course_id = input("Enter the course id: ")
        if course_id in courses.keys():
            print("Course already exists. Skipping...")
            continue
        course_name = input("Enter the course name: ")
        course_credit = int(input("Enter the course credit: "))
        courses[course_id] = course(course_id, course_name, course_credit)

    with open("courses.pickle", 'wb') as f:  
        pickle.dump(courses, f)
    

def mark_input(students, courses):
    while True:
        courseID = input("Enter the course ID you want to input marks: ")
        if courseID not in courses.keys():
            print("Invalid Course Id! Please enter a valid one.")
        else:      
            for studentID, student in students.items():
                new_mark = float(input(f"Enter mark for {student.get_name()}: "))
                student.get_marks()[courseID] = new_mark
            break
   

def save(data, filelist):
    for i in range(len(filelist)):
        with open(filelist[i], 'wb') as file:
            pickle.dump(data[i], file)

def load(file):
    with open(file, 'rb') as f:
        loaded_data= pickle.load(f)
    for key, value in loaded_data.items():
        print(value.get_id(),"\t", value.get_name(), "\t", "\t")
        

    
def compress(files, output_file):
    try:
        with open(output_file, 'wb') as f:
            for file in files:
                with open(file, 'rb') as input_file:
                    data = input_file.read()
                    compressed_data = zlib.compress(data)
                    f.write(compressed_data)
    except Exception as e:
        print(str(e))

def check_file(file):
    if os.path.exists(file):
        try:
            with zipfile.ZipFile(file,'r') as unz:
                unz.extractall()
        except Exception as e:
            print(str(e))
        print("File does exist")  
    else: 
        print("Does not exist")





    

        