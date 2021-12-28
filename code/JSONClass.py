
# test

class JSONPython_Instance():

    def __init__(self) -> None:
        self.meData = []
        self.strungVariables = ""
        self.seindexesOfSingleQuotes=[]
        self.indexesOfSingleQuotes = []

        self.renewedArray = []
        self.finalArray = []

        self.arrayPlacementIndex = 0
        self.index = 0

        self.pulledArray = []

        self.tmpArray = []
        self.tmp2Array = []
        self.tmp3Array = []


    def data(self, toAdd1, toAdd2):
        # adds data to array
        self.meData.append([str(toAdd1), str(toAdd2)])


    def makeIntoString(self):
        # makes data into string
        self.strungVariables = str(self.meData)
        print (self.strungVariables)
        return self.strungVariables

    # =================
    def addToIndex(self, indexToReplace, toAdd1, toAdd2):
        # adds data to a specific Index
        self.meData.insert(indexToReplace
        , [str(toAdd1), str(toAdd2)])
        print(self.meData)

    # =================
    def printOut(self):
        # prints out the data
        print(self.meData)

    # =================
    def parseQt(self):
        # pulls out an Array of Single Quotes!
        # global indexesOfSingleQuotes
        self.makeIntoString()
        for i in range(0, len(self.strungVariables)):
            if(self.strungVariables[i]=="\'"):
                self.indexesOfSingleQuotes.append(i)
        print('quotes? ', self.indexesOfSingleQuotes)

    # =================
    def pullFromTwoIndexes(self, one, two):
        # pulls the data between two indexes
        # used by pushToNew()
        toPrint = self.strungVariables[one+1:two]
        print(toPrint)
        return toPrint

    # =================
    def pushToNew(self, one, two, three, four, index):
        # pulling 2 terms, one dictionary | another (key) definition
        first = self.pullFromTwoIndexes(one, two)            # pulls the whole string of variables (strungVariables)
        second = self.pullFromTwoIndexes(three, four)        # pulls the whole string of variables (strungVariables)

        # import pdb; pdb.set_trace()   #debugger

        tmpArray = [first, second]
        if(index!=-1):
            self.renewedArray[index] = tmpArray
        else:
            self.renewedArray.append(tmpArray)

        # import pdb; pdb.set_trace()   #debugger
        
        tmpArray = []
        print (self.renewedArray)
    # =================
    def parseThrough(self):
        # pull all 'variables' from whole Quotes Array

        self.parseQt()
        
        while(self.index < len(self.indexesOfSingleQuotes)):
            print ('???, ', self.index, self.indexesOfSingleQuotes[self.index])
            print (self.index, '...', self.indexesOfSingleQuotes[self.index], self.indexesOfSingleQuotes[self.index+1], self.indexesOfSingleQuotes[self.index+2], self.indexesOfSingleQuotes[self.index+3] )
            self.pushToNew(self.indexesOfSingleQuotes[self.index], self.indexesOfSingleQuotes[self.index+1], self.indexesOfSingleQuotes[self.index+2], self.indexesOfSingleQuotes[self.index+3], -1)

            self.index = self.index+4  # increment to the next Set of 4!
            self.arrayPlacementIndex+=1
        print('renewedArray ', self.renewedArray)
        return self.renewedArray
    # =================

    def makingArray(self):
        # parseThrough() - run first
        # makes into an array
        self.parseThrough()
        for x in range(0, self.arrayPlacementIndex):
            self.finalArray.insert(x, self.renewedArray[x])

        print ('finalArray, ', self.finalArray)
        return self.finalArray

    # =================

    # TODO - add a file stream to a file
    # TODO - pull text from file

    # =================
    # foolish trying
    # def makingList(self, pullListIndex):
    #     self.pulledArray = self.meData[pullListIndex] 
    #     print (self.pulledArray)

    # =================
    def add2(self, toAdd1, toAdd2):
        tmpArr = [str(toAdd1), str(toAdd2)]
        pos = 2
        for i in range(len(tmpArr)): 
            self.meData.insert(i+pos, tmpArr[i])

    def pullIndex(self, index):
        self.pulledArray = [self.meData[index]]
        print (self.pulledArray)

    def addToFront(self, toAdd1, toAdd2, index):
        # self.makingList(index)
        # tmp.addToFront("time1", "somewhere", 0)
        self.pullIndex(index)

        
        self.tmpArray = [str(toAdd1), str(toAdd2)]
        self.pulledArray.append([[0, self.tmpArray]])
        # print(self.pulledArray)

        del self.meData[index]

        self.meData.insert(index, self.pulledArray)
        print("medata", self.meData)


        # self.tmp2Array = [self.pulledArray[0], self.pulledArray[1]]
        # self.tmp2Array[0] = self.pulledArray[0]
        # self.tmp2Array[1] = self.pulledArray[1]


        # self.tmp3Array = [[self.tmp2Array]+[self.tmpArray]]

        # self.tmp3Array = self.tmp2Array.append(self.tmpArray)
        
        # # import pdb; pdb.set_trace()



# ==================================
tmp = ""
def run():
    global tmp
    tmp = JSONPython_Instance()
    tmp.data('name?', 'sam')
    tmp.data('people', 'are awesome')
    tmp.data('age', 12)
    tmp.makeIntoString()
    # tmp.parseQt()
    # tmp.parseThrough()

    # tmp.parseThrough
    # tmp.makingArray
    

run()




