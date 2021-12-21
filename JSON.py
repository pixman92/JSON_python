# TODO - take an object from Python
# TODO - make it into a string

# TODO - put the strinbg back into object data
# =================



# take an array (list?) - make into string
# put all the variable data -> to a file
# make that file into string, and then bring it bac

meString = ""
meData = []
strungVariables = ""

def resetIt():
    global meString; global meData
    meString=""
    meData=[]

def makeString(str):
    global meString; global meData
    meString += str + ' '
    print (meString)

def data(toAdd1, toAdd2):
    global meString; global meData
    meData.append([str(toAdd1), str(toAdd2)])
    # print (meData)

    global strungVariables
    strungVariables = str(meData)
    print (strungVariables)


# y = [['name?', 'loverBoy'], ['place?', 'home!']] 
# =================
indexesOfSingleQuotes = []
def parseQt():
    global indexesOfSingleQuotes
    for i in range(0, len(strungVariables)):
        if(strungVariables[i]=="\'"):
            indexesOfSingleQuotes.append(i)
    print('quotes? ', indexesOfSingleQuotes)


def pullFromTwoIndexes(one, two):
    toPrint = strungVariables[one+1:two]
    print(toPrint)


# =================
def run():
    data('name?', 'loverBoy')
    data('place?', 'home!')
    data('age?', 23)
    parseQt()

run()

# =================
# y = [['name?', 'loverBoy'], ['place?', 'home!']]


# x = '{ "name":"John", "age":30, "city":"New York"}'

# =================
# TODO - take an object from Python
# TODO - make it into a string

# TODO - put the strinbg back into object data