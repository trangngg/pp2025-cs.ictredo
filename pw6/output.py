def list_students(students):
    for id, student in students.items():
        print("\n ID:", id)
        print("\tName : ", student.get_name())
        print("\tDate Of Birth : ", student.get_dob())


def list_courses(courses):
    for id_key, course in courses.items():
        print("CourseID:", id_key, "Course name:", course.get_name())


def show_marks(students, courses):
    course_id = input("Enter course id to show mark: ")
    if course_id not in courses:
        print("The course is not available")
        return
    else:
        for student_id_key, student_object in students.items():
            if course_id in student_object.get_marks():
                print(f"{student_object.get_name()}: {student_object.get_marks()[course_id]}")
            else:
                print(student_id_key, ": not available")


def calcGPA_sortdescend(students, courses):
    course_ids = list(courses.keys())
    course_credits = [credit.get_credit() for credit in courses.values()]
    credit_sum = sum(course_credits)
    student_gpas = []

    for id, student_object in students.items():
        student_marks = [student_object.get_marks().get(course_id, 0) for course_id in course_ids]
        gpa = sum(student_marks[i] * course_credits[i] for i in range(len(course_ids))) / credit_sum
        student_gpas.append((id, student_object.get_name(), gpa))

    # Sort students by GPA in descending order
    sorted_students = sorted(student_gpas, key=lambda x: x[2], reverse=True)
    
 
    print("\nSorted Students by GPA (Descending Order):")
    for student_info in sorted_students:
        print(f"ID: {student_info[0]}, Name: {student_info[1]}, GPA: {student_info[2]}")
