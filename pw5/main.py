import sys
from input import get_student_data, get_course_data, get_mark_data
from output import display_students, display_courses, display_marks
from domains.student import student
from domains.course import course
from domains.mark import mark

def main():
    students = []
    courses = []
    marks = []

    print("Input student data:")
    student_data = []
    get_student_data(student_data)
    for data in student_data:
        id, name, dob = data
        students.append(student(id, name, dob))

    print("\nInput course data:")
    course_data = []
    get_course_data(course_data)
    for data in course_data:
        id, name, credits = data
        courses.append(course(id, name, credits))

    print("\nInput marks:")
    mark_data = []
    get_mark_data(mark_data)
    for data in mark_data:
        course_id, student_id, mark = data
        marks.append(mark(course_id, student_id, mark))

    print("\nDisplaying all data:")
    display_students(students)
    display_courses(courses)
    display_marks(marks)

if __name__ == "__main__":
    main()
