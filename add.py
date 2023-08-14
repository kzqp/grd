import init
import data
import grd_io

def add_problem_set(path):
    grd_io.readFile(path)
    print(f'Let\'s add problem set number {len(data.gradebook[1].ps) + 1}.')
    i = 0
    while i < len(data.gradebook):
        str = input(f'({data.gradebook[i].id}) {data.gradebook[i].fn} {data.gradebook[i].ln}: ')
        try:
          grade = int(str)
          data.gradebook[i].ps.append(grade)
          i += 1
        except:
          print('I think you may have made a mistake....')
    print(f'Added {len(data.gradebook)} grades for problem set {len(data.gradebook[1].ps)}.')
    grd_io.writeFile(path)
    # and backup someday
def add_exam(path):
    grd_io.readFile(path)
    print(f'Let\'s add exam number {len(data.gradebook[1].ex) + 1}.')
    i = 0
    while i < len(data.gradebook):
        str = input(f'({data.gradebook[i].id}) {data.gradebook[i].fn} {data.gradebook[i].ln}: ')
        try:
            grade = int(str)
            data.gradebook[i].ex.append(grade)
            i += 1
        except:
            print('I think you may have made a mistake....')
    print(f'Added {len(data.gradebook)} grades for exam {len(data.gradebook[1].ps)}.')
    grd_io.writeFile(path)
    # and backup someday
