import arcpy
import random
from arcpy import env

env.overwriteoutput = True

inputfc = arcpy.GetParameterAsText(0)
outputfc = arcpy.GetParameterAsText(1)
percent = int(arcpy.GetParameterAsText(2))

outcount = int(percent * 0.01 * int(arcpy.GetCount_management(inputfc)[0]))
arcpy.AddMessage ("Total records: " + str(arcpy.GetCount_management(inputfc)))

arcpy.AddMessage ("Outcount: " + str(outcount))

desc = arcpy.Describe(inputfc)
inlist = []
randomlist = []
fldname = desc.OIDFieldName
rows = arcpy.SearchCursor(inputfc)
row = rows.next()
while row:
    id = row.getValue(fldname)
    inlist.append(id)
    row = rows.next()
while len(randomlist) < outcount:
    selitem = random.choice(inlist)
    randomlist.append(selitem)
    inlist.remove(selitem)
length = len(str(randomlist))
sqlexp = '"' + fldname + '"' + " in " + "(" + str(randomlist)[1:length - 1] + ")"
arcpy.MakeFeatureLayer_management(inputfc, "selection", sqlexp)
arcpy.CopyFeatures_management("selection", outputfc)