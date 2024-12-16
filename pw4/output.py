import curses

def display_students(stdscr, students):
    stdscr.clear()
    stdscr.addstr("Student List:\n", curses.A_BOLD)
    for student in students:
        stdscr.addstr(f"ID: {student.student_id}, Name: {student.name}, DoB: {student.dob}\n")
    stdscr.addstr("\nPress any key to continue...")
    stdscr.refresh()
    stdscr.getch()

def display_courses(stdscr, courses):
    stdscr.clear()
    stdscr.addstr("Course List:\n", curses.A_BOLD)
    for course in courses:
        stdscr.addstr(f"ID: {course.course_id}, Name: {course.name}, Credits: {course.credits}\n")
    stdscr.addstr("\nPress any key to continue...")
    stdscr.refresh()
    stdscr.getch()

def display_gpa(stdscr, student, gpa):
    stdscr.clear()
    stdscr.addstr(f"GPA for {student.name}: {gpa}\n", curses.A_BOLD)
    stdscr.addstr("\nPress any key to continue...")
    stdscr.refresh()
    stdscr.getch()