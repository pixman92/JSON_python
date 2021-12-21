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
    return toPrint

renewedArray=[]
def pushToNew(one, two, three, four, index):
    global renewedArray
    first = pullFromTwoIndexes(one, two)            # pulls the whole string of variables (strungVariables)
    second = pullFromTwoIndexes(three, four)        # pulls the whole string of variables (strungVariables)

    tmpArray = [first, second]
    if(index!=-1):
        renewedArray[index] = tmpArray
    else:
        renewedArray.append(tmpArray)
    tmpArray = []
    print (renewedArray)
        

# =============================
def parseThrough():
    parseQt()
    index = 0
    # for index in range(0, len(indexesOfSingleQuotes)):
    while (index < (len(indexesOfSingleQuotes)/4)):
        print ('???, ', index, indexesOfSingleQuotes[index])
        print (index, '...', indexesOfSingleQuotes[index], indexesOfSingleQuotes[index+1], indexesOfSingleQuotes[index+2], indexesOfSingleQuotes[index+3] )
        pushToNew(indexesOfSingleQuotes[index], indexesOfSingleQuotes[index+1], indexesOfSingleQuotes[index+2], indexesOfSingleQuotes[index+3], -1)
        # if(index+4<=len(indexesOfSingleQuotes)):
        #     index = index + 4
        # else:
        #     print("Out of bounds!")
        index = index+4
        pushToNew(indexesOfSingleQuotes[index], indexesOfSingleQuotes[index+1], indexesOfSingleQuotes[index+2], indexesOfSingleQuotes[index+3], -1)
        # index = index+5

    print('renewedArray ', renewedArray)

# TODO - function that takes parsed data and puts it back into an accepable array
# TODO - going back and forth



# =================
def run():
    data('name?', 'loverBoy')
    data('place?', 'home!')
    data('age?', 23)
    # parseQt()

run()

# =================
# y = [['name?', 'loverBoy'], ['place?', 'home!']]


# x = '{ "name":"John", "age":30, "city":"New York"}'

# =================
# TODO - take an object from Python
# TODO - make it into a string

# TODO - put the strinbg back into object data