import arcpy
import os

gdb = r"C:\Users\greg6750\Documents\IPython Notebooks\Python_for_GIS_and_RS\Week_5\Crime.gdb"
feature_class = "December2017_Crime"

fc = os.path.join(gdb, feature_class)

fields = ['OID@', 'ILEADSStreet', 'LocationComment']

#update cursor
with arcpy.da.UpdateCursor(fc, fields) as cursor:
    for row in cursor:
        if row[2] == None:
            row[2] = "No Comment"
            print "Row " + str(row[0]) + " Updated with No Comment"
            cursor.updateRow(row)



print('Done')