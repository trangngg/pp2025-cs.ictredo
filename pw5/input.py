def get_student_data(students):
    n = int(input("Enter the number of students: "))
    for _ in range(n):
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        students.append((id, name, dob))

def get_course_data(courses):
    n = int(input("Enter the number of courses: "))
    for _ in range(n):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        credits = int(input("Enter course credits: "))
        courses.append((id, name, credits))

def get_mark_data(marks):
    n = int(input("Enter the number of marks: "))
    for _ in range(n):
        course_id = input("Enter course ID: ")
        student_id = input("Enter student ID: ")
        mark = float(input("Enter mark: "))
        marks.append((course_id, student_id, mark))
