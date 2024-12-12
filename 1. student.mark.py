def input_student_info():
    num_students = int(input("Enter number of students: "))
    if num_students == 0:
        print("No students to input.")
        return []
    students = []
    for i in range(num_students):
        student_id = input(f"Enter ID for student {i + 1}: ")
        name = input(f"Enter name for student {i + 1}: ")
        dob = input(f"Enter DoB for student {i + 1} (MM/DD/YYYY): ")
        students.append({'id': student_id, 'name': name, 'dob': dob, 'courses': {}})
    return students

def input_course_info():
    num_courses = int(input("Enter number of courses: "))
    if num_courses == 0:
        print("No courses to input.")
        return []
    courses = []
    for i in range(num_courses):
        course_id = input(f"Enter ID for course {i + 1}: ")
        name = input(f"Enter name for course {i + 1}: ")
        courses.append({'id': course_id, 'name': name})
    return courses

def input_marks(students, courses):
    if not students or not courses:
        print("Students or courses data is missing.")
        return
    course_id = input("Enter course ID to input marks: ")
    course = next((c for c in courses if c['id'] == course_id), None)
    if not course:
        print(f"Course ID {course_id} not found.")
        return
    for student in students:
        try:
            marks = float(input(f"Enter marks for {student['name']} in {course['name']}: "))
            student['courses'][course_id] = marks
        except ValueError:
            print("Invalid marks entered. Skipping.")

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

def get_student_grade(students, student_id, course_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        print(f"Student with ID {student_id} not found.")
        return
    marks = student['courses'].get(course_id)
    if marks is None:
        print(f"No marks found for {student['name']} in course {course_id}.")
        return
    grade = calculate_grade(marks)
    print(f"Grade for {student['name']} in course {course_id} is {grade}.")

def main():
    students = input_student_info()
    courses = input_course_info()
    input_marks(students, courses)
    
    while True:
        print("\n Menu:")
        print("1. Check student grade")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            student_id = input("Enter student ID to check grade: ")
            course_id = input("Enter course ID to check grade: ")
            get_student_grade(students, student_id, course_id)
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
