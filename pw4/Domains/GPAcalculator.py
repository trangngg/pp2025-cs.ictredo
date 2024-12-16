import math

class GPACalculator:
    @staticmethod
    def calculate_gpa(student, courses):
        total_credits = 0
        weighted_sum = 0
        for course_id, mark in student.marks.items():
            course = next((c for c in courses if c.course_id == course_id), None)
            if course:
                total_credits += course.credits
                weighted_sum += mark * course.credits
        if total_credits == 0:
            return 0.0
        return math.floor((weighted_sum / total_credits) * 10) / 10  # Round to 1 decimal
