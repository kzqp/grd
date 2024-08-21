'''Parse student information from xml derived from
   campus information system.'''

from datetime import datetime
import os
import re
import data
import grd_io
import student

def parse_student_data(xmlfile):
    '''Parse student data'''
    year = datetime.now().year
    print(f'Let\'s get started for {year}.')
    string = input('Will there be a seminar series? [Y|n]: ')
    if string.lower() == 'y' or string.lower() == '':
        user.seminars = True
    else:
        user.seminars = False
    re_student_id = re.compile('[0-9]{6}')
    with open(xmlfile, 'r') as xml_file:
        while True:
            line = xml_file.readline()
            if len(line) == 0:
                break
            id = re_student_id.search(line)
            if not id == None:
                id_number = id.group(0)
                re_student_name = re.compile('([a-zA-Z]*), ([a-zA-Z]*)')
                re_student_org_id = re.compile('([a-zA-Z0-9]*)@')
                name = re_student_name.search(line)
                last_name = name.group(1)
                first_name = name.group(2)
                org_id_match = re_student_org_id.search(line)
                org_id = org_id_match.group(1)
                new_student = student.Student(id_number, last_name,
                                              first_name, org_id)
                data.gradebook.append(new_student)
    print(f'Added {len(data.gradebook)} students to the gradebook for {year}.')
    #now to write the file(s)
    print('Writing student data to disk...', end='')
    grd_io.write_file(f'.grd-{year}')
    data.registered_user.current_grade_book = os.getcwd() + \
                                              '/.grd-' + str(year)
    grd_io.set_current_gradebook()
    print('done!')
#                print(f'({id_number}) {last_name}, {first_name} [{org_id}]')
