import arcpy

arcpy.env.workspace = arcpy.GetParameterAsText(0)
output_file = arcpy.GetParameterAsText(1)

f = open(output_file, 'w')
#r'C:\Users\greg6750\Documents\IPython Notebooks\intro-prog-for-gis-rs\Projects\tlgdb_2019_a_us_school.gdb'

feature_list = arcpy.ListFeatureClasses()
header = f.write('Feature Class, Feature Count, Projection, Shape \n')

for feature in feature_list:
    feature_count = arcpy.GetCount_management(feature)
    desc = arcpy.Describe(feature)
    projection = desc.SpatialReference.name
    shape_type = desc.shapeType
    seperator = ", "
    arcpy.AddMessage(feature + seperator + str(feature_count) + seperator + projection + seperator + shape_type)
    f.write(feature + seperator + str(feature_count) + seperator + projection + seperator + shape_type + '\n')

f.close()