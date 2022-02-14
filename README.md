# JSONPython_Instance()

This is a Library for making 2D lists in Python. That can be pushed and pulled between Array form & String form.

<br>
<br>

First:
<br>
-Download the module.
<br>
-Import it to your Python project
<br>
```from JSONPython_Instance import *```
<br>
-Declare a variable with which you will create a new instance of JSONPython

<br><br>
for this *README* I will be using ```myJSON```

=================

<u>The functions of this library are as follows:</u>
<br><br>
```myJSON.add(*data*)```
<br>
Where _data_ is a single Dimensions Python List
<br><br>
```myJSON.printOut()```
<br>
Simple _printout_ function that prints out the current working data
<br><br>

```myJSON.arrayToString(*arrayData*)``` 
<br>
Function for converting _arrayData_ to a StringData form
<br><br>

```myJSON.stringToArray(*stringData*)```
<br>
Function for converting _stringData_ to arrayData
<br><br>

```myJSON.addMoreAtIndex(*index*, *data*, *overwriteBoolean*)```
<br>
Function for adding more data at a specific index
_data_ - is the data (2D list) to be added at that index
_overwriteBoolean_ - If True - it will overwrite all List Data (at that *index*)
If False - it will simply append data (to that *index*)
<br><br>

```myJSON.insertStr(*previousStringData*)```
<br>
Function for pulling previous data (in String Form) and 
converting it, to be accessible to manipulated as data, 
as if it were created by organically
<br><br>

```myJSON.removeAtIndex(*index*)```
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



