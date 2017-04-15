import arcpy
from arcpy import env
import os

arcpy.env.overwriteOutput = True

infilename = arcpy.GetParameterAsText(0) #as CSV
infile = arcpy.GetParameter(0)
outfile = arcpy.GetParameterAsText(1) #as GDB
outname = outfile + '\\AllPoints'
csvFile = os.path.basename(infilename)
spRef = arcpy.SpatialReference("NAD 1983 StatePlane Missouri East FIPS 2401 (US Feet)")


if arcpy.Exists(outfile) == False:
     arcpy.AddMessage("Creating GDB...")
     arcpy.CreateFileGDB_management(os.path.dirname(outfile), os.path.basename(outfile))

arcpy.AddMessage("Copying Rows...")
for inputs in infile:
    arcpy.AddMessage(inputs)
    if arcpy.Exists(outname) == False:
        arcpy.CopyRows_management(csvFile, outname)
    else:
        arcpy.Append_management(inputs, outfile + '/AllPoints', 'NO_TEST', '', '')

arcpy.AddMessage("Making Point Features...")
arcpy.MakeXYEventLayer_management(outname, "XCoord", "YCoord", "Temp_Points", spRef, "")
arcpy.FeatureClassToFeatureClass_conversion("Temp_Points", outfile, 'STL_CRIME_POINTS')
arcpy.Delete_management(outname)