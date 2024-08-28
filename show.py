"""write grades to terminal"""

import data
import grd_io

def show(path):
    """show grades on terminal, all pretty-like.
       Pass None to this function if the gradebook is already loaded
       in memory"""
    if path is not None:
        grd_io.read_file(path)
    d = []
    i = 0
    while i < len(data.gradebook):
        idn = data.gradebook[i].student_ID
        name = data.gradebook[i].first_name + ' ' \
               + data.gradebook[i].last_name
        ps = ''
        j = 0
        while j < len(data.gradebook[i].problem_sets):
          if len(str(data.gradebook[i].problem_sets[j])) < 3:
            z = len(str(data.gradebook[i].problem_sets[j]))
            while z < 3:
              ps += ' '
              z += 1
          ps += str(data.gradebook[i].problem_sets[j])
          ps += ' '
          j += 1
        ex = ''
        j = 0
        while j < len(data.gradebook[i].exams):
          if len(str(data.gradebook[i].exams[j])) < 3:
            z = len(str(data.gradebook[i].exams[j]))
            while z < 3:
              ps += ' '
              z += 1
          ex += str(data.gradebook[i].exams[j])
          ex += ' '
          j += 1

        #seminars
        se = ''
        j = 0
        while j < len(data.gradebook[i].seminars):
            if len(str(data.gradebook[i].seminars[j])) < 2:
                z = len(str(data.gradebook[i].seminars[j]))
                while z < 2:
                    se += ' '
                    z += 1
            se += str(data.gradebook[i].seminars[j])
            j += 1
        d.append((idn, name, ps.rstrip(), ex.rstrip(), se.rstrip()))
        i += 1
        
    if (len(d) > 0):
      longest_name = 0
      ps_length = 0
      for l in d:
        x = len(l[1])
        if x > longest_name:
          longest_name = x
      titleline = '  ID   Student'
      i = 0
      while i < longest_name - 7:
        titleline += ' '
        i += 1
      titleline += ' Problem Sets'

      for l in d:
        x = len(l[2])
        if x > ps_length:
          ps_length = x
      if ps_length > 12:
        i = 0
        while i < ps_length - 12:
          titleline += ' '
          i += 1
      titleline += ' Exams'
      titleline += ' Seminars'
      print(titleline)
      for l in d:
        line = str(l[0]) + ' ' + str(l[1])
        i = len(l[1]) - 1
        while i < longest_name:
          line += ' '
          i += 1
        line += str(l[2])
        i = len(l[2])
        if ps_length > 12:
          while i < ps_length + 1:
            line += ' '
            i += 1
        else:
          while i < 13:
            line += ' '
            i += 1
        
        line += str(l[3])
        i = len(l[3])
        while i < 5:
            line += ' '
            i += 1
        line += str(l[4])
        print(line)
    else:
      print('No grades to show. Sorry.')
      
