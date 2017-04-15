#-------------------------------------------------------------------------------
# Set input and import module
import arcpy

mxd = r'C:\Users\greg6750\Documents\IPython Notebooks\Python_for_GIS_and_RS\Week_11\Exercise10\Exercise10\Austin_TX.mxd'
mapdoc = arcpy.mapping.MapDocument(mxd)

DF_list = arcpy.mapping.ListDataFrames(mapdoc)
lyrlist = arcpy.mapping.ListLayers(mapdoc)

# Find the "parks" layer
for lyr in lyrlist:
    if lyr.name == "parks":
        addLayer = lyr
    else:
        print "Not the 'parks' laryer"

# Add the "parks" layer to the Data Frames
for df in DF_list:
    if df.name != "Parks":
        arcpy.mapping.AddLayer(df, addLayer, "BOTTOM")

# Save changes to Map Document
mapdoc.save()

# Delete temporary and intermediate files
del mapdoc
del lyrlist

# Reporet successful message
print "Layer(s) added to data frame."
