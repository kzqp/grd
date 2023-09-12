class student:

    def addProblemSet(self, score):
        self.ps.append(score)

    def addExam(self, score):
        self.ex.append(score)

    def __init__(self, student_ID, first_name, last_name, username):
        self.student_ID = student_ID
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.ps = []
        self.ex = []
