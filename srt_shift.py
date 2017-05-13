from itertools import groupby
from collections import namedtuple
from datetime import datetime
import datetime as dt

def mathMicroSecs(tm, msecs, operation):
    fulldate = dt.datetime(100, 1, 1, tm.hour, tm.minute, tm.second, tm.microsecond)
    if operation == 'forward':
        fulldate = fulldate + dt.timedelta(microseconds=msecs)
    elif operation == 'backward':
        fulldate = fulldate - dt.timedelta(microseconds=msecs)
    return fulldate.time()


def shiftSrt(namefile, orientation, delta):
    with open(namefile, 'r') as f:
        res = [list(g) for b, g in groupby(f, lambda x: bool(x.strip())) if b]

    Subtitle = namedtuple('Subtitle', 'number start end content')

    subs = []
    new_text = ''

    for sub in res:
        if len(sub) >= 3: # not strictly necessary, but better safe than sorry
            sub = [x.strip() for x in sub]
            number, start_end, *content = sub # py3 syntax
            start, end = start_end.split(' --> ')
            subs.append(Subtitle(number, start, end, content))

    for value in subs:
        v_start = mathMicroSecs(datetime.strptime(value.start, '%H:%M:%S,%f').time(), delta*1000000, orientation)
        v_end = mathMicroSecs(datetime.strptime(value.end, '%H:%M:%S,%f').time(), delta*1000000, orientation)

        if(v_start.strftime('%H:%M:%S,%f')[:2] != '23'):
            new_text += value.number + "\n"
            new_text += v_start.strftime('%H:%M:%S,%f')[:-3] + " --> " + v_end.strftime('%H:%M:%S,%f')[:-3] + "\n"
            new_text += ''.join(str(e + "\n") for e in value.content)
            new_text += "\n"

    try:
        f1 = open(namefile, 'w')
        print(new_text, file=f1)
        result  = f1
    except AttributeError:
        print("problems in overwriting file! Another one is going to be created\n")
        f1 = open('NEW_' + namefile, 'w')
        print(new_text, file=f1)
        result = f1

    return result

