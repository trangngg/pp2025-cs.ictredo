import curses
from input import input_students, input_courses, input_marks
from output import display_students, display_courses, display_gpa
from Domains.GPAcalculator import GPACalculator

def main(stdscr):
    # Input Data
    students = input_students()
    courses = input_courses()
    input_marks(students, courses)

    # Display Data
    display_students(stdscr, students)
    display_courses(stdscr, courses)

    # Calculate and Display GPA for a Selected Student
    student_id = input("Enter student ID to calculate GPA: ")
    student = next((s for s in students if s.student_id == student_id), None)
    if student:
        gpa = GPACalculator.calculate_gpa(student, courses)
        display_gpa(stdscr, student, gpa)
    else:
        print("Student not found!")

if __name__ == "__main__":
    curses.wrapper(main)
