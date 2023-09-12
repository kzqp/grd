'''Parse student information from xml derived from
   campus information system.'''

import re
import data
import student

'''Parse student data'''
def parse_student_data(xmlfile):
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
                print(f'({id_number}) {last_name}, {first_name} [{org_id}]')
