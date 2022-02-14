from re import M
from JSONPython_Instance import *
# import JSONPython_Instance

me = JSONPython_Instance()

def run():
    global me
    me.add(['place?', 'home'])

    me.printOut()

def addMeToSpecificIndex(index, one, two):
    global me
    tmpArr = [one, two]
    me.addMoreAtIndex(index, tmpArr, False)

def addMoreAtEnd(one, two):
    global me
    tmpArr = [one, two]
    me.add(tmpArr)


# "[[[[0], [['place?', 'home']]]], [[[0], [['name?', 'sam']]]], [[[0], [['name?', 'leo']]]]]"