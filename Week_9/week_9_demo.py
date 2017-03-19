import arcpy

arcpy.env.workspace = r"C:\Student\DEM"

ras_list = arcpy.ListRasters()
print(ras_list)

#Using Wildcards
a_ras_list = arcpy.ListRasters("a*")
print(a_ras_list)

###Describing Rasters
##single_raster = r"C:\Student\DEM\na_dem.tif"
##raster_info = arcpy.Describe(single_raster)
##print(raster_info.format)
##print(raster_info.spatialReference.name)

###Slope with Raster Objects
##import datetime
##arcpy.env.overwriteOutput = True
##master_times = datetime.datetime.now()
##arcpy.env.overwriteOutput = True
##arcpy.CheckOutExtension("Spatial")
##from arcpy.sa import *
##out_ras = Slope(single_raster)
##out_ras.save(r"C:\Student\DEM\na_slope.tif")
##print("Total Time %s" % (datetime.datetime.now() - master_times))
##print("Done.")

###Slope with Numpy
###Run this is 64-bit Python
##import numpy as np
##import time
##import datetime
##master_times = datetime.datetime.now()
##arcpy.env.overwriteOutput = True
##arcpy.env.outputCoordinateSystem = single_raster
##
##def calc_slope(dem, cellsize):
##    #Modified from calculation found here:
##    #http://geoexamples.blogspot.com/2014/03/shaded-relief-images-using-gdal-python.html
##    x, y = np.gradient(dem, cellsize, cellsize)
##    #slope = np.pi/2.0 - np.arctan(np.sqrt(x*x + y*y))
##    slope = np.arctan(np.sqrt(x*x + y*y))
##    return slope
##
##myRaster = arcpy.RasterToNumPyArray(single_raster)
##myRasterInfo = arcpy.Raster(single_raster)
##mx = myRasterInfo.extent.XMin + myRasterInfo.meanCellWidth
##my = myRasterInfo.extent.YMin + myRasterInfo.meanCellHeight
##print("Cell Size = " + str(myRasterInfo.meanCellWidth))
##slope_ras = calc_slope(myRaster, myRasterInfo.meanCellWidth)
##output_slope_ras = arcpy.NumPyArrayToRaster(slope_ras,arcpy.Point(mx, my),
##                                                 myRasterInfo.meanCellWidth,
##                                                 myRasterInfo.meanCellHeight)
##output_slope_ras.save(r"C:\Student\DEM\na_slope_numpy.tif")
##print("Total Time %s" % (datetime.datetime.now() - master_times))