"""Gradebook initialization functions"""

from datetime import datetime
import os
import grd_io
import data
import user

def read_settings():
    """read variables from config file"""
    grd_io.read_config_file()

def init():
    """initialize gradebook"""
    #check current gradebook, skip if there for this year
    year = datetime.now().year
    print(f'Let\'s get started for {year}.')
    print('Enter your student list in the form StudentID:Username:'
          'Last Name:First Name.\n'
          'Enter a blank line when finished.')
    string = 'x'
    while string != '':
        string = input('Student: ')
        if string != '':
            try:
                grd_io.parse_student(string)
                print(f'Added '
                      f'{data.gradebook[len(data.gradebook)-1].first_name}'
                      f' {data.gradebook[len(data.gradebook)-1].last_name}'
                      f' ({data.gradebook[len(data.gradebook)-1].student_ID}'
                      f', {data.gradebook[len(data.gradebook)-1].username}).')
            except Exception as e:
                print(e)
                print('I think you may have made a mistake....')
    print(f'Added {len(data.gradebook)} students to the gradebook for {year}.')
    #now to write the file(s)
    print('Writing student data to disk...', end='')
    grd_io.write_file(f'.grd-{year}')
    data.registered_user.current_grade_book = os.getcwd() + '/.grd-' + str(year)
    grd_io.set_current_gradebook()
    print('done!')
    #and the history file, someday

def gather_user_info():
    """collect user info, first run"""
    print('Let\'s collect some basic information to get started.')
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    email = input('email : ')
    data.registered_user = user.User(first_name, last_name, email)
    grd_io.write_config_file()
