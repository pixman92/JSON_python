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


# =================
indexesOfSingleQuotes = []
def parseQt():
    # pulls out an Array of Single Quotes!
    global indexesOfSingleQuotes
    indexesOfSingleQuotes=[]
    for i in range(0, len(strungVariables)):
        if(strungVariables[i]=="\'"):
            indexesOfSingleQuotes.append(i)
    print('quotes? ', indexesOfSingleQuotes)


def pullFromTwoIndexes(one, two):
    # pulls the data between two indexes
    toPrint = strungVariables[one+1:two]
    print(toPrint)
    return toPrint

renewedArray=[]
def pushToNew(one, two, three, four, index):
    # pulling 2 terms, one dictionary | another (key) definition
    global renewedArray

    first = pullFromTwoIndexes(one, two)            # pulls the whole string of variables (strungVariables)
    second = pullFromTwoIndexes(three, four)        # pulls the whole string of variables (strungVariables)

    # import pdb; pdb.set_trace()   #debugger

    tmpArray = [first, second]
    if(index!=-1):
        renewedArray[index] = tmpArray
    else:
        renewedArray.append(tmpArray)

    # import pdb; pdb.set_trace()   #debugger
    
    tmpArray = []
    print (renewedArray)
        

# =============================
arrayPlacementIndex = 0
def parseThrough():
    # pull all 'variables' from whole Quotes Array
    parseQt()
    index = 0
    global arrayPlacementIndex
    # for index in range(0, len(indexesOfSingleQuotes)):
    # while (index < (len(indexesOfSingleQuotes)/4)):
    while(index < len(indexesOfSingleQuotes)):
        print ('???, ', index, indexesOfSingleQuotes[index])
        print (index, '...', indexesOfSingleQuotes[index], indexesOfSingleQuotes[index+1], indexesOfSingleQuotes[index+2], indexesOfSingleQuotes[index+3] )
        pushToNew(indexesOfSingleQuotes[index], indexesOfSingleQuotes[index+1], indexesOfSingleQuotes[index+2], indexesOfSingleQuotes[index+3], -1)

        index = index+4  # increment to the next Set of 4!
        arrayPlacementIndex+=1
    print('renewedArray ', renewedArray)

finalArray=[]
def makingArray():
    parseThrough()
    global finalArray
    for x in range(0, arrayPlacementIndex):
        finalArray.insert(x, renewedArray[x])

    print ('finalArray, ', finalArray)



# TODO - function that takes parsed data and puts it back into an accepable array
# TODO - going back and forth




# =================
# y = [['name?', 'loverBoy'], ['place?', 'home!'], ['age?', '23'], ['attendes?', 'people']]
# quotes?  [2, 8, 11, 20, 25, 32, 35, 41, 46, 51, 54, 57, 62, 72, 75, 82]

def run():
    data('name?', 'loverBoy')
    data('place?', 'home!')
    data('age?', 23)
    data('attendes?', 'people')
    data('favorite Number?', 345383)
    # parseQt()

run()

# =================
# y = [['name?', 'loverBoy'], ['place?', 'home!']]


# x = '{ "name":"John", "age":30, "city":"New York"}'

# =================
# TODO - take an object from Python
# TODO - make it into a string

# TODO - put the strinbg back into object data


