from Domains.student import Student
from Domains.course import Course

def input_students():
    students = []
    num_students = int(input("Enter number of students: "))
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB (MM/DD/YYYY): ")
        students.append(Student(student_id, name, dob))
    return students

def input_courses():
    courses = []
    num_courses = int(input("Enter number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        credits = int(input("Enter course credits: "))
        courses.append(Course(course_id, name, credits))
    return courses

def input_marks(students, courses):
    course_id = input("Enter course ID to input marks: ")
    course = next((c for c in courses if c.course_id == course_id), None)
    if not course:
        print("Course not found!")
        return
    for student in students:
        mark = float(input(f"Enter marks for {student.name}: "))
        student.add_mark(course_id, mark)
