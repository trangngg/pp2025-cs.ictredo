# input.py
from domains.student import Student

def input_students(student_list):
    n = int(input("Enter the number of students: "))
    for _ in range(n):
        student_id = input("Student ID: ")
        name = input("Student name: ")
        dob = input("Date of Birth (dd/mm/yyyy): ")
        student_list.append(Student(student_id, name, dob))

def input_courses(course_list):
    n = int(input("Enter the number of courses: "))
    for _ in range(n):
        course_id = input("Course ID: ")
        course_name = input("Course name: ")
        course_list.append({"id": course_id, "name": course_name})

def input_marks(student_list, course_list, marks_dict):
    for course in course_list:
        print(f"Input marks for course: {course['name']}")
        for student in student_list:
            mark = float(input(f"Enter mark for {student.name}: "))
            student.set_mark(course['id'], mark)
            marks_dict[course['id']] = marks_dict.get(course['id'], {})
            marks_dict[course['id']][student.student_id] = mark
