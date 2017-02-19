import arcpy
import os


output_gdb = r"C:\Users\greg6750\Documents\IPython Notebooks\Python_for_GIS_and_RS\Week_6\Superbowl.gdb"
output_feature_class = "football_field"

if arcpy.Exists(output_gdb):
    print("GDB exists")
else:
    arcpy.CreateFileGDB_management(os.path.split(output_gdb)[0],
                                os.path.split(output_gdb)[1])

print('Creating football field.')

footbal_field_fields = ('SHAPE@', 'TEAM')

fc = os.path.join(output_gdb, output_feature_class)
if not arcpy.Exists(os.path.join(output_gdb, output_feature_class)):
    arcpy.CreateFeatureclass_management(
        output_gdb, output_feature_class, "POLYGON", "#", "DISABLED",
        "DISABLED", arcpy.SpatialReference(3857))
    arcpy.AddField_management(fc, footbal_field_fields[1], "TEXT",
                              field_length=20)

cursor = arcpy.da.InsertCursor(fc, footbal_field_fields)

field = [(0, 533.3),
         (1000, 533.3),
         (1000, 0),
         (0, 0)]
cursor.insertRow([field, ""])

home_endzone = [(-100, 533.3),
                (0, 533.3),
                (0, 0),
                (-100, 0)]
cursor.insertRow([home_endzone, "ATLANTA"])

away_endzone = [(1000, 533.3),
                (1100, 533.3),
                (1100, 0),
                (1000, 0)]
cursor.insertRow([away_endzone, "NEW ENGLAND"])

del cursor

##------------------------------------------------------------------------------


output_feature_class = "football_yard_markers"

print('Creating yard markers.')

footbal_line_fields = ('SHAPE@', 'MARKER')

fc = os.path.join(output_gdb, output_feature_class)

if not arcpy.Exists(os.path.join(output_gdb, output_feature_class)):
    arcpy.CreateFeatureclass_management(
        output_gdb, output_feature_class, "POLYLINE", "#", "DISABLED",
        "DISABLED", arcpy.SpatialReference(3857))
    arcpy.AddField_management(fc, footbal_line_fields[1], "TEXT",
                              field_length=10)

line_cursor = arcpy.da.InsertCursor(fc, footbal_line_fields)
markers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
for marker in markers:
    line_1 = [(marker * 10, 533.3 / 2), (marker * 10, 0)]
    line_2 = [(marker * 10, 533.3 / 2), (marker * 10, 533.3)]
    if marker > 50:
        line_cursor.insertRow((line_1, str(100 - marker)))
        line_cursor.insertRow((line_2, str(100 - marker)))
    else:
        line_cursor.insertRow((line_1, str(marker)))
        line_cursor.insertRow((line_2, str(marker)))

del line_cursor