# JSONPython_Instance()

This is a Library for makinge 2D lists in Python. That be pushed and pulled between Array form & String form.

First:
-Download the module.
-Import it to your Python project
```from JSONPython_Instance import *```

-Declare a variable with which you will create a new instance of JSONPython

for this README I will be using ```myJSON```

=================

<u>The functions of this library are as follows:</u>
<br><br>
```myJSON.add(_data_)```
<br>
Where _data_ is a single Deminsion Python List
<br><br>
```myJSON.printOut()```
<br>
Simple _printout_ function that prints out the current working data
<br><br>

```myJSON.arrayToString(_arrayData_)``` 
<br>
Function for converting _arrayData_ to a StringData form
<br><br>

```myJSON.stringToArray(_stringData_)```
<br>
Function for converting _stringData_ to arrayData
<br><br>

```myJSON.addMoreAtIndex(_index_, _data_, _overwriteBoolean_)```
<br>
Function for adding more data at a specific index
_data_ - is the data (2D list) to be added at that index
_overwriteBoolean_ - If True - it will overwrite all List Data (at that _index_)
If False - it will simply append data (to that _index_)
<br><br>

```myJSON.insertStr(_previousStringData_)```
<br>
Function for pulling previous data (in String Form) and 
converting it, to be accessible to manipulated as data, 
as if it were created by organically
<br><br>

```myJSON.removeAtIndex(_index_)```
<br>
Function for removing data from array, at 
_index_ point

<br><br>
=================
<br>
To access the inner Data
```myJSON.JSONArray```
<br>
For the _Array_ data
<br><br>
```myJSON.JSONString```
<br>
For the _String_ data

<br><br><br>



