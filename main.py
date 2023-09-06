import sys
import os
import init
import add
import bs
import data
import grd_io
import grade
import show

def show_unknown(arg, command=None):
  if command == None:
    print(f'The given command ({arg}) is unknown.')
  else:
    print(f'The given option ({arg}) is an unknown option of {command}.')

def show_usage():
  print('This is the usage line. It will be much longer in the future.')

def main():
  if os.path.exists(grd_io.config_path):
    grd_io.read_config_file()
  else:
    init.gather_user_info()
    exit(0)
  if len(sys.argv) == 2:
    if sys.argv[1] == 'init':
      init.init()
    elif sys.argv[1] == 'show':
      show.show(data.RegisteredUser.current_grade_book)
    elif sys.argv[1] == 'bs':
      bs.BrightspaceOutput(data.RegisteredUser.current_grade_book)
    else:
      show_unknown(sys.argv[1])
      show_usage()      
  elif len(sys.argv) == 3:
    if sys.argv[1] == 'add':
      if sys.argv[2] == 'ps':
        add.add_problem_set(data.RegisteredUser.current_grade_book)
      elif sys.argv[2] == 'ex':
        add.add_exam(data.RegisteredUser.current_grade_book)
      else:
        show_unknown(sys.argv[2], command='add')
        show_usage()
    elif sys.argv[1] == 'edit':
      pass
    elif sys.argv[1] == 'grade':
      if sys.argv[2] == 'mt':
        grade.grade(data.RegisteredUser.current_grade_book, period='mt')
      elif sys.argv[2] == 'final':
        grade.grade(data.RegisteredUser.current_grade_book, period='final')
      else:
        show_unknown(sys.argv[2], command='grade')
        show_usage()
    else:
      show_unknown(sys.argv[2])
      show_usage()
    #grd_io.readFile('GradeBook')
  else:
    show_usage()

if __name__ == '__main__':
  main()
