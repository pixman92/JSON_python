# JSONPython_Instance()

This is a Library for makinge 2D lists in Python. That be pushed and pulled between Array form & String form.

First:
-Download the module.
-Import it to your Python project
```from JSONPython_Instance import *```

-Declare a variable with which you will create a new instance of JSONPython

for this README I will be using ```myJSON```

=================

The functions of this library are as follows:

```myJSON.add(_data_)```

Where _data_ is a single Deminsion Python List

```myJSON.printOut()```

Simple _printout_ function that prints out the current working data

```myJSON.arrayToString(_arrayData_)```

Function for converting _arrayData_ to a StringData form

```myJSON.stringToArray(_stringData_)```

Function for converting _stringData_ to arrayData

```myJSON.addMoreAtIndex(_index_, _data_, _overwriteBoolean_)```

Function for adding more data at a specific index
_data_ - is the data (2D list) to be added at that index
_overwriteBoolean_ - If True - it will overwrite all List Data (at that _index_)
If False - it will simply append data (to that _index_)

```myJSON.insertStr(_previousStringData_)```

Function for pulling previous data (in String Form) and 
converting it, to be accessible to manipulated as data, 
as if it were created by organically

```myJSON.removeAtIndex(_index_)```

Function for removing data from array, at 
_index_ point






