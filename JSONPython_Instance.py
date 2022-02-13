# JSONPython_Instance - to make a txt file with JSON string
import ast
from xml.etree.ElementTree import tostring


class JSONPython_Instance():

    def __init__(self) -> None:
        self.JSONArray = []
        self.JSONString = ""


    def add(self, data):
        self.JSONArray.append(str(data))


    def addAtIndex(self, indexToReplace, dataToOverwrite):
        self.JSONArray.insert(indexToReplace, dataToOverwrite)
        print (self.JSONArray)
    
    def printOut(self):
        print('Array form\n', self.JSONArray)
        print('===========')
        print('String form', self.JSONString)    

    def arrayToString(self):
        self.JSONString = str(self.JSONArray)
        print (self.JSONString)
        return self.JSONString
    
    def stringToArray(self):
        arrayToString(self)
        self.JSONArray = ast.literal_eval(self.JSONString)
        print (self.JSONArray)