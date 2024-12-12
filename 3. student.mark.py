import math
import numpy as np  #numerical computing & data manipulation
import curses #TUI


class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}  # {course_id: {'marks': float, 'credits': int}}
        self.gpa = 0.0

    def add_marks(self, course_id, marks, credits):
        rounded_marks = math.floor(marks * 10) / 10  # Round down to 1 decimal
        self.marks[course_id] = {'marks': rounded_marks, 'credits': credits}

    def calculate_gpa(self):
        if not self.marks:
            self.gpa = 0.0
            return
        total_weighted_score = sum(
            v['marks'] * v['credits'] for v in self.marks.values()
        )
        total_credits = sum(v['credits'] for v in self.marks.values())
        self.gpa = round(total_weighted_score / total_credits, 2)

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}, GPA: {self.gpa}"


class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}, Credits: {self.credits}"


class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student DoB (MM/DD/YYYY): ")
            self.students.append(Student(student_id, name, dob))

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            credits = int(input("Enter course credits: "))
            self.courses.append(Course(course_id, name, credits))

    def input_marks(self):
        course_id = input("Enter course ID to input marks: ")
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if not course:
            print(f"Course ID {course_id} not found.")
            return
        for student in self.students:
            try:
                marks = float(input(f"Enter marks for {student.name}: "))
                student.add_marks(course_id, marks, course.credits)
            except ValueError:
                print("Invalid marks entered. Skipping.")

    def calculate_gpas(self):
        for student in self.students:
            student.calculate_gpa()

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda s: s.gpa, reverse=True)

    def list_students(self):
        print("\nList of Students:")
        for student in self.students:
            print(student)

    def list_courses(self):
        print("\nList of Courses:")
        for course in self.courses:
            print(course)

    def decorate_ui(self, screen):
        self.calculate_gpas()
        self.sort_students_by_gpa()

        screen.clear()
        screen.addstr("Student List Sorted by GPA:\n")
        for student in self.students:
            screen.addstr(str(student) + "\n")
        screen.addstr("\nPress any key to exit.")
        screen.refresh()
        screen.getch()

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Input students")
            print("2. Input courses")
            print("3. Input marks")
            print("4. Calculate GPAs")
            print("5. Sort students by GPA")
            print("6. List students")
            print("7. List courses")
            print("8. Decorate UI")
            print("9. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.input_students()
            elif choice == '2':
                self.input_courses()
            elif choice == '3':
                self.input_marks()
            elif choice == '4':
                self.calculate_gpas()
            elif choice == '5':
                self.sort_students_by_gpa()
                print("Students sorted by GPA.")
            elif choice == '6':
                self.list_students()
            elif choice == '7':
                self.list_courses()
            elif choice == '8':
                curses.wrapper(self.decorate_ui)
            elif choice == '9':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    smm = StudentMarkManagement()
    smm.menu()
