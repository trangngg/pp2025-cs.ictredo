# output.py
import curses

def display_students(stdscr, students):
    stdscr.clear()
    stdscr.addstr("Student List:\n")
    for student in students:
        stdscr.addstr(f"{student.student_id} - {student.name} - {student.dob}\n")
    stdscr.refresh()
    stdscr.getch()

def display_courses(stdscr, courses):
    stdscr.clear()
    stdscr.addstr("Course List:\n")
    for course in courses:
        stdscr.addstr(f"{course['id']} - {course['name']}\n")
    stdscr.refresh()
    stdscr.getch()
