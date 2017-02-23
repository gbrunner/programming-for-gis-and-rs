import arcpy

p1 = arcpy.Point(4,5)
p2 = arcpy.Point(4,5)
p3 = arcpy.Point(5,5)

print(p1.contains(p2))
print(p1.contains(p3))
print(p1.crosses(p2))
print(p1.crosses(p3))
#crosses is not made for point fearures

Point = arcpy.Point(4,5)
point1 = arcpy.Point(7,9)
pList = [Point, point1]
array = arcpy.Array()
array.extend(pList)
pLine = arcpy.Polyline(array)
print(pLine)
print(pLine.firstPoint)
print(pLine.lastPoint)
print(pLine.length)

p1 = arcpy.Point(12,16)
p2 = arcpy.Point(14,18)
p3 = arcpy.Point(11,20)
Array=arcpy.Array()
Points=[p1,p2,p3]
Array.extend(Points)
Polygon = arcpy.Polygon(Array)
arcpy.CopyFeatures_management(Polygon, r"C:\Users\greg6750\Documents\IPython Notebooks\Python_for_GIS_and_RS\Week_7\Polygon.shp" )
print('Done')