"""Brightspace cvs format writer"""
import data
import grd_io

def brightspace_output(path):
    """Produces CSV output suitable for Brightspace input."""
    grd_io.read_file(path)
    psc = len(data.gradebook[0].problem_sets)
    exc = len(data.gradebook[0].exams)
    sec = len(data.gradebook[0].seminars)

    if psc == 0 and exc == 0 and sec == 0:
        return

    headline = 'OrgDefinedId, Username, '
    #headline = 'OrgDefinedId, '
    headline += 'Seminar Requirement, '
    i = 0
    while i < psc:
        headline += 'Problem Set ' + str(i + 1) + ' Text Grade'
        i += 1
        if i < psc:
            headline += ', '
    i = 0
    while i < exc:
        if i == 0:
            headline += ', '
        headline += 'Exam ' + str(i + 1) + ' Text Grade'
        i += 1
        if i < exc:
            headline += ', '
    headline += ', End-of-Line Indicator'
    print(headline)
    for student in data.gradebook:
        line = ''
        line += student.student_ID
        line += ', '
        line += student.username + ', '
        #line += student.fn + '.' + student.ln + ', '
        if sec == 0:
            line += '(0/0), '
        else:
            sem = 0
            total_sem = 0
            for seminar in student.seminars:
                sem += seminar
                total_sem += 1
            if sem >= 2:
                line += f'Met ({sem}/{total_sem}), '
            else:
                line += f'Unmet ({sem}/{total_sem}), '
        i = 0
        for problem_set in student.problem_sets:
            line += str(problem_set)
            i += 1
            if i < psc:
                line += ', '
        for exam in student.exams:
            line += ', '
            line += str(exam)
        line += ', #'
        print(line)
