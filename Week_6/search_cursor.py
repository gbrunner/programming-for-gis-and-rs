import arcpy
import os

gdb = r"C:\Users\greg6750\Documents\IPython Notebooks\Python_for_GIS_and_RS\Week_6\Superbowl.gdb"
feature_class = "football_field"

fc = os.path.join(gdb, feature_class)

fields = ['SHAPE@XY', 'TEAM']

# For each row print the WELL_ID and WELL_TYPE fields, and the
# the feature's x,y coordinates
with arcpy.da.SearchCursor(fc, fields) as cursor:
    for row in cursor:
        print row[0]
        print row[1]