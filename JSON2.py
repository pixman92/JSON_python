import re
import ast

myJSONpy = []

def addData(data):
    global myJSONpy
    myJSONpy.append([data])
    # myJSONpy.append([data])
    # import pdb; pdb.set_trace() #debugger

# =================

def printJSON():
    print(myJSONpy)

strVersion = ""
def makeStr():
    global strVersion
    strVersion = str(myJSONpy)


# =================

def run():
    global strVersion
    addData([['places', 'GVCC'],['places', 'Goleta'],['places', 'home']])
    addData([['age', '10'],['age', '12'], ['age', '14']])
    makeStr()
    print(strVersion)


def matchingBrackets():
    reg = r"\[\[(.*?)\]\]"

    # if re.match(reg, strVersion):
    #     print(strVersion)
    x = re.split(reg, strVersion)
    import pdb; pdb.set_trace() #debugger

def evaluate():
    newList = res = ast.literal_eval(strVersion)
    print (newList)
    import pdb; pdb.set_trace() #debugger
