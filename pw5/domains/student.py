# domains/student.py
class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def set_mark(self, course, mark):
        self.marks[course] = mark

    def get_gpa(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)
