# main.py
from input import input_students, input_courses, input_marks
from output import display_students, display_courses
from saveload import save_data, load_data
import curses

def main(stdscr):
    # Load existing data
    file_path = "students.dat"
    data = load_data(file_path)
    students = data.get("students", [])
    courses = data.get("courses", [])
    marks = data.get("marks", {})

    while True:
        stdscr.clear()
        stdscr.addstr("1. Input students\n")
        stdscr.addstr("2. Input courses\n")
        stdscr.addstr("3. Input marks\n")
        stdscr.addstr("4. Display students\n")
        stdscr.addstr("5. Display courses\n")
        stdscr.addstr("6. Exit\n")
        stdscr.refresh()

        choice = stdscr.getch()
        
        if choice == ord('1'):
            input_students(students)
        elif choice == ord('2'):
            input_courses(courses)
        elif choice == ord('3'):
            input_marks(students, courses, marks)
        elif choice == ord('4'):
            display_students(stdscr, students)
        elif choice == ord('5'):
            display_courses(stdscr, courses)
        elif choice == ord('6'):
            save_data(file_path, {"students": students, "courses": courses, "marks": marks})
            stdscr.addstr("Exiting program. Data saved.\n")
            stdscr.refresh()
            break
        else:
            stdscr.addstr("Invalid choice. Try again.\n")
            stdscr.refresh()
            stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
