import data
import init
import os
import student
import user

config_path = os.path.expanduser('~') + '/.grd'

def writeStudentLine(student):
  #2.87s for removing
  #3.00s for keeping tracking
  #be sloppy but fast

  line = str(student.id)
  line = line + '*'
  line = line + student.fn
  line = line + '*'
  line = line + student.ln
  line = line + '*'
  for grade in student.ps:
    line = line + str(grade)
    line = line + ':'
  line = line[:-1]
  line = line + '$'
  for grade in student.ex:
    line = line + str(grade)
    line = line + '$'
  return line[:-1]

def readFile(path):
  f = open(path, mode='r', buffering=1, encoding='utf-8')
  for line in f:
    id = line.split(sep='*')
    s = student.student(id[0], id[1], id[2].replace('\n',''))
    if len(id) > 3:
      ps = id[3].split(':')
      for p in ps:
        if ( '$' in p ):
          ex = p.split('$')
          s.addProblemSet(int(ex[0]))
          ex.pop(0)
          for e in ex:
            s.addExam(int(e))
        else:
          s.addProblemSet(int(p))
    data.gradebook.append(s)
  f.close()

def writeFile(path):
  i = 1
  with open(path, mode='w', buffering=1, encoding='utf-8') as f:
    for student in data.gradebook:
      f.write(writeStudentLine(student))
      if i < len(data.gradebook):
        f.write('\n')
      i += 1

def parse_student(str):
  prts = str.split(':')
  s = student.student(prts[0], prts[2], prts[1])
  data.gradebook.append(s)

def read_config_file():
  if os.path.exists(config_path):
    with open(config_path, mode='r', encoding='utf-8') as f:
      fn = ''
      ln = ''
      email = ''
      current_grade_book = ''
      for line in f:
        v = line.split(sep='=')
        if v[0] == 'firstname':
          fn = v[1]
        if v[0] == 'lastname':
          ln = v[1]
        if v[0] == 'email':
          email = v[1]
        if v[0] == 'current_grade_book':
          current_grade_book = v[1]
    data.RegisteredUser = user.user(fn, ln, email)
    if data.RegisteredUser.current_grade_book == None and os.path.exists(current_grade_book):
      data.RegisteredUser.current_grade_book = current_grade_book
  else:
    init.gather_user_info()

def write_config_file():
  with open(config_path, mode='w', encoding='utf-8') as f:
    f.write(f'firstname={data.RegisteredUser.fn}\n')
    f.write(f'lastname={data.RegisteredUser.ln}\n')
    f.write(f'email={data.RegisteredUser.email}\n')
    if data.RegisteredUser.current_grade_book != None:
      f.write(f'current_grade_book={data.RegisteredUser.current_grade_book}\n')

def set_current_gradebook():
  with open(config_path, mode='a', encoding='utf-8') as f:
    f.write(f'current_grade_book={data.RegisteredUser.current_grade_book}')
