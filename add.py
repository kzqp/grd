"""add problem set and exam scores to gradebook"""
import data
import grd_io

#too low exception
class GradeTooLow(Exception):
    """Raise when entered grade < 0"""

#too high exception
class GradeTooHigh(Exception):
    """Raise when entered grade > 100"""

def add_problem_set(path):
    """add problem set"""
    grd_io.read_file(path)
    print(f'Let\'s add problem set number '
          f'{len(data.gradebook[0].problem_sets) + 1}.')
    i = 0
    while i < len(data.gradebook):
        stri = input(f'({data.gradebook[i].student_ID}) '
                    f'{data.gradebook[i].first_name} '
                    f'{data.gradebook[i].last_name}: ')
        try:
            grade = int(stri)
            if grade < 0:
                raise GradeTooLow
            if grade > 100:
                raise GradeTooHigh
            data.gradebook[i].problem_sets.append(grade)
            i += 1
        except GradeTooLow:
            print('Did they really do that poorly?')
        except GradeTooHigh:
            print('On fire, aren\'t they?')
        except ValueError:
            print('I think you may have made a mistake....')
    print(f'Added {len(data.gradebook)} grades for problem set '
          f'{len(data.gradebook[0].problem_sets)}.')
    grd_io.write_file(path)
    # and backup someday

def add_exam(path):
    """add exam"""
    grd_io.read_file(path)
    print(f'Let\'s add exam number {len(data.gradebook[0].exams) + 1}.')
    i = 0
    while i < len(data.gradebook):
        stri = input(f'({data.gradebook[i].student_ID}) '
                    f'{data.gradebook[i].first_name} '
                    f'{data.gradebook[i].last_name}: ')
        try:
            grade = int(stri)
            if grade < 0:
                raise GradeTooLow
            if grade > 100:
                raise GradeTooHigh
            data.gradebook[i].exams.append(grade)
            i += 1
        except GradeTooLow:
            print('Did they really do that poorly?')
        except GradeTooHigh:
            print('On fire, aren\'t they?')
        except ValueError:
            print('I think you may have made a mistake....')
    print(f'Added {len(data.gradebook)} grades for exam '
          f'{len(data.gradebook[0].exams)}.')
    grd_io.write_file(path)
    # and backup someday

def add_seminar(path):
    """add seminar"""
    grd_io.read_file(path)
    print(f'Let\'s add seminar attendance {len(data.gradebook[0].seminars) + 1}.')
    i = 0
    while i < len(data.gradebook):
        stri = input(f'({data.gradebook[i].student_ID}) '
                    f'{data.gradebook[i].first_name} '
                    f'{data.gradebook[i].last_name}: ')
        try:
            grade = int(stri)
            if grade < 0:
                raise GradeTooLow
            if grade > 1:
                raise GradeTooHigh
            data.gradebook[i].seminars.append(grade)
            i += 1
        except GradeTooLow:
            print('Not in the state?')
        except GradeTooHigh:
            print('Attend more than once? Time travel?')
        except ValueError:
            print('Seminar attendance is binary, 1 or 0.')
    print(f'Added {len(data.gradebook)} attedances for seminar '
          f'{len(data.gradebook[0].seminars)}.')
    grd_io.write_file(path)
    # and backup someday
