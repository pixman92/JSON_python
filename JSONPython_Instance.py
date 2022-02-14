# JSONPython_Instance - to make a txt file with JSON string
import ast

class JSONPython_Instance():

    def __init__(self):
        self.JSONArray = []
        self.JSONString = ""
        self.arrayHold = []
        self.stringHold = ""

    def add(self, data):
        if(isinstance(data, list)==True):
            self.JSONArray.append([[[0], [data]]])
            self.arrayToString()
            self.stringToArray()
        else:
            print ('Data MUST be list')
            

    def addAtIndex(self, indexToReplace, dataToOverwrite):
        self.JSONArray.insert(indexToReplace, dataToOverwrite)
        print (self.JSONArray)
    
    def printOut(self):
        self.stringToArray()
        print('Array form', self.arrayHold)
        print('===========')
        self.arrayToString()
        print('String form', self.stringHold)    

    def arrayToString(self):
        self.stringHold = str(self.JSONArray)
        # print (self.stringHold)
        return self.stringHold
    
    def stringToArray(self):
        # self.arrayToString(self)
        self.arrayHold = ast.literal_eval(self.stringHold)
        # print (self.arrayHold)
        return self.arrayHold

    # =================
    def addMoreAtIndex(self, index, data, override):
        if(override==True):
            self.JSONArray[index][0][1][0] = data
        else:
            self.JSONArray[index][0][1][0].append(data)
        self.arrayHold = self.JSONArray
        self.arrayToString()    
        self.stringToArray()


# me = JSONPython_Instance()
def run():
    me = JSONPython_Instance()
    me.add([['age', '16']])
    me.printOut()
    me.add([['time', 'lunch'], ['time?', 'bedtime']])
    import pdb; pdb.set_trace() #debugger