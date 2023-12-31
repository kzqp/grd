"""add problem set and exam scores to gradebook"""
import init
import data
import grd_io

#too low exception
class GradeTooLow(Exception):
    """Raise when entered grade < 0"""
    pass

#too high exception
class GradeTooHigh(Exception):
    """Raise when entered grade > 100"""
    pass

def add_problem_set(path):
    """add problem set"""
    grd_io.read_file(path)
    print(f'Let\'s add problem set number '
          f'{len(data.gradebook[1].problem_sets) + 1}.')
    i = 0
    while i < len(data.gradebook):
        str = input(f'({data.gradebook[i].student_ID}) '
                    f'{data.gradebook[i].first_name} '
                    f'{data.gradebook[i].last_name}: ')
        try:
            grade = int(str)
            if grade < 0:
                raise GradeTooLow
            elif grade > 100:
                raise GradeTooHigh
            else:
                data.gradebook[i].problem_sets.append(grade)
                i += 1
        except GradeTooLow:
            print('Did they really do that poorly?')
        except GradeTooHigh:
            print('On fire, aren\'t they?')
        except NameError:
            print('I think you may have made a mistake....')
    print(f'Added {len(data.gradebook)} grades for problem set '
          f'{len(data.gradebook[1].problem_sets)}.')
    grd_io.write_file(path)
    # and backup someday
    
def add_exam(path):
    """add exam"""
    grd_io.read_file(path)
    print(f'Let\'s add exam number {len(data.gradebook[1].exams) + 1}.')
    i = 0
    while i < len(data.gradebook):
        str = input(f'({data.gradebook[i].student_ID}) '
                    f'{data.gradebook[i].first_name} '
                    f'{data.gradebook[i].last_name}: ')
        try:
            grade = int(str)
            if grade < 0:
                raise GradeTooLow
            elif grade > 100:
                raise GradeTooHigh
            else:
                data.gradebook[i].exams.append(grade)
                i += 1
        except GradeTooLow:
            print('Did they really do that poorly?')
        except GradeTooHigh:
            print('On fire, aren\'t they?')
        except:
            print('I think you may have made a mistake....')
    print(f'Added {len(data.gradebook)} grades for exam '
          f'{len(data.gradebook[1].exams)}.')
    grd_io.write_file(path)
    # and backup someday
