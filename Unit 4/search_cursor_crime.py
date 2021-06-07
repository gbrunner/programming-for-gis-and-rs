import arcpy
import os

gdb = r"C:\Users\greg6750\Documents\IPython Notebooks\Python_for_GIS_and_RS\Week_5\Crime.gdb"
feature_class = "December2017_Crime"

fc = os.path.join(gdb, feature_class)

fields = ['SHAPE@XY', 'ILEADSStreet', 'LocationComment']

# For each row print the WELL_ID and WELL_TYPE fields, and the
# the feature's x,y coordinates
with arcpy.da.SearchCursor(fc, fields) as cursor:
    for row in cursor:
        #print row[0]
        if row[2] != None:
            print "Street: " + str(row[1]) + " with comment " + str(row[2])