import arcpy
import os

gdb = r"C:\Users\greg6750\Documents\IPython Notebooks\Python_for_GIS_and_RS\Week_5\Crime.gdb"
feature_class = "December2017_Crime"

fc = os.path.join(gdb, feature_class)

fields = ['SHAPE@XY', 'ILEADSStreet', 'LocationComment']

crime_cursor = arcpy.da.InsertCursor(fc, fields)
crime_1 = ((895401,1020601), 'Des Peres 204', 'This class is a crime')
crime_2 = ((895409,1020610), 'Des Peres 204', None)
crime_cursor.insertRow(crime_1)
crime_cursor.insertRow(crime_2)

del crime_cursor

print("Done.")