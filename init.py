from datetime import datetime
import os
import student
import grd_io
import data
import user

def read_settings():
  grd_io.read_config_file()

def init():
  year = datetime.now().year
  print(f'Let\'s get started for {year}.')
  print('Enter your student list in the form StudentID:Last Name:First Name.\n'
        'Enter a blank line when finished.')
  string = 'x'
  while string != '':
    string = input('Student: ')
    if string != '':
      try:
        grd_io.parse_student(string)
        print(f'Added {data.gradebook[len(data.gradebook)-1].fn}'
              f' {data.gradebook[len(data.gradebook)-1].ln}'
              f' ({data.gradebook[len(data.gradebook)-1].id}).')
      except Exception as e:
        print(e)
        print('I think you may have made a mistake....')
  print(f'Added {len(data.gradebook)} students to the gradebook for {year}.')
  #now to write the file(s)
  print('Writing student data to disk...', end='')
  grd_io.writeFile(f'.grd-{year}')
  data.RegisteredUser.current_grade_book = os.getcwd() + '/.grd-' + str(year)
  grd_io.set_current_gradebook()
  print('done!')
  #and the history file, someday

def gather_user_info():
  print('Let\'s collect some basic information to get started.')
  fn = input('First Name: ')
  ln = input('Last Name: ')
  em = input('email : ')
  data.RegisteredUser = user.user(fn, ln, em)
  grd_io.write_config_file()
