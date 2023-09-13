"""Student data object + methods"""

class Student:
    """Student data class"""

    def add_problem_set(self, score):
        """add problem set score"""
        self.problem_sets.append(score)

    def add_exam(self, score):
        """add exam score"""
        self.exams.append(score)

    def __init__(self, student_ID, first_name, last_name, username):
        """create a student"""
        self.student_ID = student_ID
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.problem_sets = []
        self.exams = []
