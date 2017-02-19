import arcpy
import os

gdb = r"C:\Users\greg6750\Documents\IPython Notebooks\Python_for_GIS_and_RS\Week_6\Superbowl.gdb"
feature_class = "football_yard_markers"

fc = os.path.join(gdb, feature_class)

#new fields
fields = ['MARKER', 'MARKER_STRING']

#Add new field
arcpy.AddField_management(fc, fields[1], "TEXT", field_length=20)

#update cursor
with arcpy.da.UpdateCursor(fc, fields) as cursor:
    for row in cursor:
        row[1] = str(row[0]) + ' Yard Line'
        cursor.updateRow(row)

print('Done')