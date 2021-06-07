# Watch this video

[AWS re:Invent 2017: How Esri Optimizes Massive Image Archives for Analytics in the C (ABD402)](https://www.youtube.com/watch?v=U486YxlDoeM)

# This week's reading

Please read Chapter 10 of Python Scripting for ArcGIS Pro.

# This week's slides, notebooks, and demos
These are the slides, notebooks, and demos I will use this week.

Attached Files:

    File Unit_6_Rasters.pptx Click for more options (607.033 KB) 
    File unit_6_lesson_1_working_with_rasters_arcpy.ipynb Click for more options (1.303 MB)
    File unit_6_lesson_2_working_with_rasters_numpy.ipynb Click for more options (413.318 KB)
    File unit_6_lesson_3_working_with_rasters_in_the_cloud.ipynb Click for more options (1.722 MB)
    File working_with_rasters_arcpy.html Click for more options (1.57 MB)
    File working_with_rasters_in_the_cloud.html Click for more options (1.987 MB)
    File working_with_rasters_numpy.html Click for more options (689.53 KB) 
    
# Unit 6 Exercise and Discussion Questions
## In class exercise
Compete exercises for Chapter 10 of Python Scripting for ArcGIS Pro
- Exercise: https://www.arcgis.com/home/item.html?id=1372abc4fb0c4ff0a7c66e8d9c869038
- Data: https://www.arcgis.com/home/item.html?id=862c63f5a50e4a29bb237369a9854838

## Questions
1. What is a "Raster" object, and why do geoprocessing operations and map algebra expressions using rasters often result in temporary outputs?
2. What are the differences between raster datasets and raster bands?
3. What is the difference between raster functions in ArcGIS Pro and their equivalent functions in arcpy.sa or arcpy.ia?

# Unit 6 Assignment
Attached Files:

    File Exercise09.zip Click for more options (21.075 MB) 

## Challenge 1
Create a script that determines what areas meet the following conditions:
- Moderate slope — between 5 and 20 degrees
- Southerly aspect — between 150 and 270 degrees
- Forested — land cover types of 41, 42, or 43
Be sure to use the map algebra expressions of the arcpy.sa module.

## Challenge 2
Write a script that copies all the rasters in a workspace to a new file geo-database. 
You can use the rasters in the Exercise09 folder as an example.

### WARNGING
If you do Challenge 2, you may get an error:

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\Conversion Tools.tbx#RasterToGeodatabase_conversion.InitializeParameters.py in <module>

AttributeError: 'ToolValidator' object has no attribute 'isLicensed'

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\Conversion Tools.tbx#RasterToGeodatabase_conversion.InitializeParameters.py in <module>

AttributeError: 'ToolValidator' object has no attribute 'isLicensed'


If you get this error, check to see whether the tool worked anyway!


