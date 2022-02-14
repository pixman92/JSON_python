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

```myJSON.add(<data>)```
Where <data> is a single Deminsion Python List

```myJSON.printOut()```
Simple printout function that lays out the current working data

```myJSON.arrayToString(<arrayData>)```
Function for converting <arrayData> to a <StringData> form

```myJSON.stringToArray(<stringData>)```
Function for converting <stringData> to <arrayData>

```myJSON.addMoreAtIndex(<index>, <data>, <overwriteBoolean>)```
Function for adding more data at a specific <index>
<data> - is the data (2D list) to be added at that <index>
<overwriteBoolean> - If True - it will overwrite all List Data (at that index)
If False - it will simply append data (to that index)

```myJSON.insertStr(<previousStringData>)```
Function for pulling previous data (in String Form) and 
converting it, to be accessible to manipulated as data, 
as if it were created by organically

```myJSON.removeAtIndex(<index>)```
Function for removing data from array, at <index> point






