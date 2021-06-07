# This week's reading

This week, we will cover try-except statments, functions and classes. If you 
have Advanced Python Scripting for ArcGIS Pro, please read Chapter 2 on functions and classes.

# This week's notebooks, data, and demos
Attached Files:

    File requests.ipynb Click for more options (246.125 KB)
    File try_except.ipynb Click for more options (10.719 KB)
    File functions_example.ipynb Click for more options (3.544 KB) 
    File requests.html Click for more options (479.409 KB)
    File try_except.html Click for more options (286.755 KB)
    File functions_example.html Click for more options (274.772 KB) 
    File February2020.CSV Click for more options (509.99 KB) 
    
# Unit 8 Exercise and Discussion Questions
Please complete the following tutorial: https://www.maps.arcgis.com/home/item.html?id=03e58089563646b4a742a6f2cabffa03You can find the data at: https://www.arcgis.com/home/item.html?id=27de226a996946cf9885cd53b96ad53e

## Complete the following problems
### Problem 1
Create a custom function called ```countstringfields``` that determines the number of fields of type 
string in an input feature class. Create this function in a 
separate script ( for example, mycount.py) that you call from 
another script ( for example, callingscript.py). 
You can use the streets.shp feature class in the Exercise12 folder.

### Problem 2
You are given a feature class called parcels.shp 
located in the Exercise12 folder that contains the 
following fields: FID, Shape, Landuse, and Value. 
Modify the parceltax.py script so that it determines the property tax for 
each parcel and stores these values in a list. You should use the class 
created in the parcelclass.py script — the class can remain unchanged. 
Print the values of the final list as follows: **FID: <property tax>**
