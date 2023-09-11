class student:

    def addProblemSet(self, Score):
        self.ps.append(Score)

    def addExam(self, Score):
        self.ex.append(Score)

    def __init__(self, StudentID, FirstName, LastName):
        self.id = StudentID
        self.fn = FirstName
        self.ln = LastName
        self.ps = []
        self.ex = []
