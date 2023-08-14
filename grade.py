import data
import grd_io


def midtermgrade(path):
  grd_io.readFile(path)
  d = []
  i = 0
  while i < len(data.gradebook):
    j = 0
    psmean = 0
    while j < len(data.gradebook[i].ps):
      psmean += data.gradebook[i].ps[j]
      j += 1
    mtg = psmean / j * 0.70 + data.gradebook[i].ex[0] * 0.30
    d.append([data.gradebook[i].id, data.gradebook[i].fn + ' ' +  data.gradebook[i].ln, round(mtg)])

    i += 1

  long_name = 0
  for l in d:
    x = len(l[1])
    if x > long_name:
      long_name = x
  for l in d:
    print('(' + str(l[0]) + ') ' + l[1].ljust(long_name) + ' ' + str(l[2]))  
  
# recreate mt? how many ps were in the mt, store that somewhere

def grade(path, period):
  grd_io.readFile(path)
  d = []
  i = 0
  while i < len(data.gradebook):
    j = 0
    pstotal = 0
    psmean = 0
    extotal = 0
    exmean = 0
    while j < len(data.gradebook[i].ps):
      pstotal += data.gradebook[i].ps[j]
      j += 1
    psmean = pstotal / j
    if period == 'mt':
      exmean = data.gradebook[i].ex[0]
    else:
      j = 0
      while j < len(data.gradebook[i].ex):
        extotal += data.gradebook[i].ex[j]
        j += 1
      exmean = extotal / j
    g = psmean * 0.70 + exmean * 0.30
    d.append([data.gradebook[i].id, data.gradebook[i].fn + ' ' +  data.gradebook[i].ln, round(g)])
    i += 1

  longest_name = 0
  for l in d:
    x = len(l[1])
    if x > longest_name:
      longest_name = x
  for l in d:
    print('(' + str(l[0]) + ') ' + l[1].ljust(longest_name) + ' ' + str(l[2])) 
