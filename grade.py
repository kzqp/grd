"""grading functions"""
import data
import grd_io
import show

numerical_to_letter = { 100: 'A+',
                         99: 'A+',
                         98: 'A',
                         97: 'A',
                         96: 'A',
                         95: 'A',
                         94: 'A',
                         93: 'A',
                         92: 'A',
                         91: 'A-',
                         90: 'A-',
                         89: 'B+',
                         88: 'B+',
                         87: 'B+',
                         86: 'B+',
                         85: 'B',
                         84: 'B',
                         83: 'B',
                         82: 'B',
                         81: 'B-',
                         80: 'B-',
                         79: 'C+',
                         78: 'C+',
                         77: 'C+',
                         76: 'C+',
                         75: 'C',
                         74: 'C',
                         73: 'C',
                         72: 'C',
                         71: 'C-',
                         70: 'C-',
                         69: 'D+',
                         68: 'D+',
                         67: 'D+',
                         66: 'D+',
                         65: 'D',
                         64: 'D',
                         63: 'D',
                         62: 'D',
                         61: 'D-',
                         60: 'D-' }
  
# recreate mt? how many ps were in the mt, store that somewhere

def grade(path, period):
    """display mt or final (period = mt or final) grade"""
    grd_io.read_file(path)
    d = []
    i = 0
    while i < len(data.gradebook):
        j = 0
        pstotal = 0
        psmean = 0
        extotal = 0
        exmean = 0
        sematt = 0
        
        while j < len(data.gradebook[i].problem_sets):
            pstotal += data.gradebook[i].problem_sets[j]
            j += 1
        if j < 1:
            print('Hmm ... it doesn\'t look like you\'ve scored '
                  'any problem sets, I can\'t assign a\ngrade '
                  'without a couple problem sets.\n')
            show.show(None)
            exit(0)
        else:
            psmean = pstotal / j
        if period == 'mt':
            try:
                exmean = data.gradebook[i].exams[0]
            except:
                print('Hmm ... it doesn\'t look like you\'ve given an exam, '
                'I can\'t assign a midterm grade without an exam.\n')
                show.show(None)
                exit(0)
        else:
            j = 0
            while j < len(data.gradebook[i].exams):
                extotal += data.gradebook[i].exams[j]
                j += 1
            if j < 2:
                print('Hmm ...  I can\'t find two exam scores. '
                'I can\'t assign a final grade without two exams.\n')
                show.show(None)
                exit(0) 
            else:
                exmean = extotal / j
        j = 0
        while j < len(data.gradebook[i].seminars):
            sematt += data.gradebook[i].seminars[j]
            j += 1
            
        if data.registered_user.seminars:
            if sematt >= 2:
                g = psmean * 0.65 + exmean * 0.30 + 5
            else:
                g = psmean * 0.65 + exmean * 0.30 + sematt * 50 * 0.05
        else:
            g = psmean * 0.70 + exmean * 0.30
            
        d.append([data.gradebook[i].student_ID, data.gradebook[i].first_name \
              + ' ' +  data.gradebook[i].last_name, round(g)])
        i += 1

    longest_name = 0
    for l in d:
        x = len(l[1])
        if x > longest_name:
            longest_name = x
    for l in d:
        try:
            letter_grade = numerical_to_letter[l[2]]
        except KeyError:
            letter_grade = 'F'
        print('(' + str(l[0]) + ') ' + l[1].ljust(longest_name) +
              ' ' + str(l[2]) + ' ' + letter_grade)
