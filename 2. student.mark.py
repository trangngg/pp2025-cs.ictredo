class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}  # Stores marks for courses in the format {course_id: marks}

    def add_marks(self, course_id, marks):
        self.marks[course_id] = marks

    def get_marks(self, course_id):
        return self.marks.get(course_id, None)

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}"


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}"


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
            self.courses.append(Course(course_id, name))

    def input_marks(self):
        course_id = input("Enter course ID to input marks: ")
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if not course:
            print(f"Course ID {course_id} not found.")
            return
        for student in self.students:
            try:
                marks = float(input(f"Enter marks for {student.name}: "))
                student.add_marks(course_id, marks)
            except ValueError:
                print("Invalid marks entered. Skipping.")

    def list_students(self):
        print("\nList of Students:")
        for student in self.students:
            print(student)

    def list_courses(self):
        print("\nList of Courses:")
        for course in self.courses:
            print(course)

    def get_student_grade(self):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        student = next((s for s in self.students if s.student_id == student_id), None)
        if not student:
            print(f"Student with ID {student_id} not found.")
            return
        marks = student.get_marks(course_id)
        if marks is None:
            print(f"No marks found for course ID {course_id}.")
        else:
            grade = self.calculate_grade(marks)
            print(f"Grade for {student.name} in course {course_id} is {grade}.")

    @staticmethod
    def calculate_grade(average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Input students")
            print("2. Input courses")
            print("3. Input marks")
            print("4. List students")
            print("5. List courses")
            print("6. Check student grade")
            print("7. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.input_students()
            elif choice == '2':
                self.input_courses()
            elif choice == '3':
                self.input_marks()
            elif choice == '4':
                self.list_students()
            elif choice == '5':
                self.list_courses()
            elif choice == '6':
                self.get_student_grade()
            elif choice == '7':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    smm = StudentMarkManagement()
    smm.menu()
