import os
import arcpy
from arcpy import env

input_table = arcpy.GetParameterAsText(0)
output_spatial_ref = arcpy.GetParameter(1)
output_fc = arcpy.GetParameterAsText(2)

gdb_name = os.path.dirname(output_fc)
fc_name = os.path.basename(output_fc)

env.overwriteOutput = True

arcpy.AddMessage("Creating File GDB")
#arcpy.CreateFileGDB_management(os.path.dirname(gdb_name),
#                            os.path.basename(gdb_name))

##Create table from csv file
arcpy.AddMessage(gdb_name)
arcpy.AddMessage("Converting CSV to GDB Table")
arcpy.TableToTable_conversion(input_table, "in_memory", "temp", "", "", "")

##Make XY events layer
events_layer = "crime_points"
arcpy.AddMessage("Make FC Layer")
#arcpy.MakeXYEventLayer_management("in_memory/temp", "xcoord", "ycoord", events_layer, "", "")
arcpy.MakeXYEventLayer_management("in_memory/temp", "xcoord", "ycoord", events_layer, "", "")


##Output events layer to feature class
arcpy.AddMessage("FC to FC")
arcpy.FeatureClassToFeatureClass_conversion(events_layer, gdb_name, fc_name, "", "", "")

##Define projection
arcpy.AddMessage("Defining Projection.")
arcpy.DefineProjection_management(output_fc, output_spatial_ref)

arcpy.AddMessage("Done.")
