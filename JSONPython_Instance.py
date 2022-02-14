# JSONPython_Instance - to make a txt file with JSON string
import ast

class JSONPython_Instance():

    def __init__(self):
        self.JSONArray = []
        self.JSONString = ""
        # self.arrayHold = []
        # self.stringHold = ""

    def add(self, data):
        if(isinstance(data, list)==True):
            self.JSONArray.append([[[0], [data]]])
            self.arrayToString(self.JSONArray)
            self.stringToArray(self.JSONString)
        else:
            print ('Data MUST be list')
            

    def addAtIndex(self, indexToReplace, dataToOverwrite):
        self.JSONArray.insert(indexToReplace, dataToOverwrite)
        print (self.JSONArray)
    
    def printOut(self):
        # self.stringToArray()
        print('Array form', self.JSONArray)
        print('===========')
        # self.arrayToString()
        print('String form', self.JSONString)    

    def arrayToString(self, array):
        # self.stringHold = str(self.JSONArray)
        self.JSONString = str(array)

        # print (self.JSONString)
        return self.JSONString
    
    def stringToArray(self, str):
        # self.arrayToString(self)
        # self.arrayHold = ast.literal_eval(self.stringHold)
        self.JSONArray = ast.literal_eval(str)

        # print (self.JSONArray)
        return self.JSONArray

    # =================
    def addMoreAtIndex(self, index, data, override):
        # data = just one set of brackets!
        if(override==True):
            self.JSONArray[index][0][1] = data
        else:
            self.JSONArray[index][0][1].append(data)
        # self.arrayHold = self.JSONArray
        self.arrayToString(self.JSONArray)    
        self.stringToArray(self.JSONString)

    # =================
    def insertStr(self, str):
        
        self.JSONString = str
        # self.stringHold = str
        self.stringToArray(self.JSONString)
        self.arrayToString(self.JSONArray)
        self.printOut()
        import pdb; pdb.set_trace() #debugger

    # =================
    def removeAtIndex(self, index):
        self.JSONArray.pop(index)
        # self.arrayHold = self.JSONArray

