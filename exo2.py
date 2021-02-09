import numpy
# import random
from random import randint


def stat():
    stat = sum(tab_note) / len(tab_note)
    return str(stat)


tab_note = []
note = int(input('Note:'))
while 0 <= note <= 20:
    tab_note.append(note)
    note = int(input('Note:'))
    if note == -1:
        print('La moyenne de classe est :' + stat())
print(numpy.average(tab_note))
print(randint(0, 100))
