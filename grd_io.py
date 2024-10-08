"""File IO functions"""

import os
import data
import init
import student
import user

config_path = os.path.expanduser('~') + '/.grd'

def write_student_line(current_student):
    """generate a student line in the gradebook file"""
    #2.87s for removing
    #3.00s for keeping tracking
    #be sloppy but fast

    line = str(current_student.student_ID)
    line = line + '*'
    line = line + current_student.first_name
    line = line + '*'
    line = line + current_student.last_name
    line = line + '*'
    line = line + current_student.username
    line = line + '*'
    for grade in current_student.problem_sets:
        line = line + str(grade)
        line = line + ':'
    if len(current_student.problem_sets) > 0:
        line = line[:-1]
    if len(current_student.exams) > 0:
         line = line + '$'
    for grade in current_student.exams:
        line = line + str(grade)
        line = line + '$'
    if len(current_student.exams) > 0:
        line = line[:-1]

    if data.registered_user.seminars:
        line = line + '%'
        for attendance in current_student.seminars:
            line = line + str(attendance)
            line = line + '%'
        line = line[:-1]
    return line    

def read_file(path):
     """read student line from gradebook"""

     with open(path, mode='r', buffering=1, encoding='utf-8') as f:
         for line in f:
             id_line = line.split(sep='*')
             s = student.Student(id_line[0], id_line[1], id_line[2],
                                 id_line[3].replace('\n',''))
             if len(id_line) > 4:
                 data_line = id_line[4].rstrip()
                 try:
                     ps = data_line[0:data_line.index('$')]
                 except ValueError:
                     try:
                         ps = data_line[0:data_line.index('%')]
                         if len(ps) == 0:
                             ps = None
                     except ValueError:
                         if len(data_line) == 0:
                             ps = None
                         else:
                             if len(data_line) != 1:
                                 ps = data_line
                             else:
                                 se = data_line

                 try:
                     if '%' in data_line:
                         ex = data_line[data_line.index('$') + 1:data_line.index('%')]
                     else:
                         ex = data_line[data_line.index('$') + 1:len(data_line)]
                 except ValueError:
                     ex = None

                 try:
                     se = data_line[data_line.index('%') + 1:len(data_line)]
                 except ValueError:
                     se = None
                 if ps is not None:
                     problemsets = ps.split(':')
                     for p in problemsets:
                         s.add_problem_set(int(p))
                 if ex is not None:
                     exams = ex.split('$')
                     for e in exams:
                         s.add_exam(int(e))
                 if se is not None:
                     seminars = se.split('%')
                     for ss in seminars:
                         s.add_seminar(int(ss))
             data.gradebook.append(s)
         f.close()


def write_file(path):
    """write gradebook to disk"""
    i = 1
    with open(path, mode='w', buffering=1, encoding='utf-8') as f:
        
        for current_student in data.gradebook:
            f.write(write_student_line(current_student))
            if i < len(data.gradebook):
                f.write('\n')
            i += 1

def parse_student(string):
    """generate student from string, add to gradebook"""
    prts = string.split(':')
    s = student.Student(prts[0], prts[3], prts[2], prts[1])
    data.gradebook.append(s)


def read_config_file():
    """read and parse config file"""
    if os.path.exists(config_path):
        with open(config_path, mode='r', encoding='utf-8') as f:
            first_name = ''
            last_name = ''
            email = ''
            current_grade_book = ''
            seminar = False
            for line in f:
                v = line.split(sep='=')
                if v[0] == 'firstname':
                    first_name = v[1].rstrip()
                if v[0] == 'lastname':
                    last_name = v[1].rstrip()
                if v[0] == 'email':
                    email = v[1].rstrip()
                if v[0] == 'current_grade_book':
                    current_grade_book = v[1].rstrip()
                if v[0] == 'seminar':
                    if v[1].rstrip() == '1':
                        seminar = True
        data.registered_user = user.User(first_name, last_name, email)
        if data.registered_user.current_grade_book is None and \
           os.path.exists(current_grade_book):
            data.registered_user.current_grade_book = current_grade_book
        else:
            pass
            #maybe do nothing?
            #print('run grd init to start a gradebook')
            #init.gather_user_info()
        data.registered_user.seminars = seminar

def write_config_file():
    """write configuration file"""
    with open(config_path, mode='w', encoding='utf-8') as f:
        f.write(f'firstname={data.registered_user.first_name}\n')
        f.write(f'lastname={data.registered_user.last_name}\n')
        f.write(f'email={data.registered_user.email}\n')
        if data.registered_user.current_grade_book is not None:
            f.write(
            f'current_grade_book={data.registered_user.current_grade_book}\n')
        if data.registered_user.seminars is not None:
            if data.registered_user.seminars is True:
                f.write('seminar=1')
            else:
                f.write('seminar=0')

# This one is going away due to the append issue, above function should
# always be used.
def set_current_gradebook():
    """open current gradebook"""
    with open(config_path, mode='a', encoding='utf-8') as f:
        f.write(
          f'current_grade_book={data.registered_user.current_grade_book}\n')
        if data.registered_user.seminars is True:
            f.write('seminar=1')
        else:
            f.write('seminar=0')
            
