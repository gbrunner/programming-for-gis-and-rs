import arcpy
from arcpy import env
arcpy.env.overwriteOutput = True

#connect tool to script
inFeatures = arcpy.GetParameterAsText(0)
#default_workspace = arcpy.GetParameterAsText(1)
st_cube = arcpy.GetParameterAsText(1)
out_fc = arcpy.GetParameterAsText(2)

arcpy.AddMessage("Setting Workspace")
#arcpy.env.workspace = default_workspace

#set date variable
arcpy.AddMessage("Adding Time Field and Calculating Time Field")
fieldName1 = 'date'
arcpy.AddField_management(inFeatures, fieldName1, "DATE")
expression = "time.strftime(' !iday! / !imonth! / !iyear! ')"
arcpy.CalculateField_management(inFeatures, fieldName1, expression, "PYTHON")

#create space time cube
arcpy.AddMessage("Creating Space-Time Cube")
arcpy.CreateSpaceTimeCube_stpm(inFeatures, st_cube, fieldName1,"","6 Months","END_TIME", "","","")

arcpy.AddMessage("Running Hot Spot Analysis")
#create emerging hotspot analysis
cube = arcpy.EmergingHotSpotAnalysis_stpm(st_cube, 'COUNT', out_fc, "10 Miles")