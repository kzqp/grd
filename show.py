import data
import grd_io

def show(path):
    grd_io.readFile(path)
    d = []
    i = 0
    while i < len(data.gradebook):
        idn = data.gradebook[i].id
        name = data.gradebook[i].fn + ' ' + data.gradebook[i].ln
        ps = ''
        j = 0
        while j < len(data.gradebook[i].ps):
          if len(str(data.gradebook[i].ps[j])) < 3:
            z = len(str(data.gradebook[i].ps[j]))
            while z < 3:
              ps += ' '
              z += 1
          ps += str(data.gradebook[i].ps[j])
          ps += ' '
          j += 1
        ex = ''
        k = 0
        while k < len(data.gradebook[i].ex):
          if len(str(data.gradebook[i].ex[k])) < 3:
            z = len(str(data.gradebook[i].ex[k]))
            while z < 3:
              ps += ' '
              z += 1
          ex += str(data.gradebook[i].ex[k])
          ex += ' '
          k += 1
        d.append((idn, name, ps.rstrip(), ex.rstrip()))
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
        print(line)
    else:
      print('No grades to show. Sorry.')

