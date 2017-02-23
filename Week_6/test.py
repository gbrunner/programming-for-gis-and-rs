fc = r"C:\Users\greg6750\Documents\IPython Notebooks\Python_for_GIS_and_RS\Ch5.gdb\TestPoly"

import arcpy
footbal_field_fields = ('SHAPE@', 'BLOCK')

cursor = arcpy.da.InsertCursor(fc, footbal_field_fields)

field = [(0, 5.3),
         (1, 5.3),
         (1, 0),
         (0, 0)]
cursor.insertRow([field, ""])

print "done"