import data
import grd_io

def BrightspaceOutput(path):
    grd_io.readFile(path)
    psc = len(data.gradebook[0].ps)
    exc = len(data.gradebook[0].ex)

    if psc == 0 and exc == 0:
        return

    #headline = 'OrdDefinedId, Username, '
    headline = 'OrgDefinedId, '
    i = 0
    while i < psc:
        headline += 'Problem Set ' + str(i + 1) + ' Text Grade'
        i += 1
        if i < psc:
            headline += ', '
    i = 0
    while i < exc:
        if i == 0:
            headline += ', '
        headline += 'Exam ' + str(i + 1) + ' Text Grade'
        i += 1
        if i < exc:
            headline += ', '
    headline += ', End-of-Line Indicator'
    print(headline)
    for s in data.gradebook:
        line = ''
        line += s.id
        line += ', '
        #line += s.fn + '.' + s.ln + ', '
        i = 0
        for ps in s.ps:
            line += str(ps)
            i += 1
            if i < psc:
                line += ', '
        for ex in s.ex:
            line += ', '
            line += str(ex)
        line += ', #'
        print(line)
