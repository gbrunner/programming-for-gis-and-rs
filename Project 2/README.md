# Spring 2019
 Please Complete Both Problems

## Problem 1 (**60 Points**)
There is a tool in ArcGIS Pro and ArcMap called [Points to Line](https://pro.arcgis.com/en/pro-app/tool-reference/data-management/points-to-line.htm). This tool creates line features from points. **For this problem, do not use that tool!**. What I want you to do is essentially create that tool using cursors.

What I would like you to do is create a line feature from the point features in **zoo_featues_wgs84.shp** by using a search cursor to retrieve the x,y locations of the points and an insert cursor to insert thost features into a new feature class.

Grading this problem breaks down as follows:
  - Read geometries from **zoo_features_wgs84.shp** (10 points)
  - Create a new *'Polyline'* features class (10 points)
  - Convert points to a line (10 points)
  - Insert points into *'Polyline'* feature class (10 points)
  - Create Python Script Tool to turn points into a polyline
    - User interface (10 points)
    - Connecting the script to the tool with right parameters (10 points)

If you a re looking for a starting point, I recoment looking at Zandbergen's Chapter 8 Challenge Problems and Solutions. 

## Problem 2 (**40 points**)
Write a Python script that uses *Raster* objects (see Zandbergen Chapter 9) and Spatial Analyst to create an average (mean) raster from p114r075_7t20000501_z50_nn10.tif, p114r075_7t20000501_z50_nn20.tif, p114r075_7t20000501_z50_nn30.tif, and p114r075_7t20000501_z50_nn40.tif found here (). Use mathematical operations similar to achieve this. If you need help, look to the exercises from Chapter 9 of Zandbergen.

# Fall 2020
## Problem 1 (out of 50 points)
Here is a list of Landsat Scenes over Oregon:

    https://landsat-pds.s3.amazonaws.com/c1/L8/046/028/LC08_L1TP_046028_20200908_20200918_01_T1/LC08_L1TP_046028_20200908_20200918_01_T1_B1.TIF
    https://landsat-pds.s3.amazonaws.com/c1/L8/046/028/LC08_L1TP_046028_20200908_20200918_01_T1/LC08_L1TP_046028_20200908_20200918_01_T1_B2.TIF
    https://landsat-pds.s3.amazonaws.com/c1/L8/046/028/LC08_L1TP_046028_20200908_20200918_01_T1/LC08_L1TP_046028_20200908_20200918_01_T1_B3.TIF
    https://landsat-pds.s3.amazonaws.com/c1/L8/046/028/LC08_L1TP_046028_20200908_20200918_01_T1/LC08_L1TP_046028_20200908_20200918_01_T1_B4.TIF
    https://landsat-pds.s3.amazonaws.com/c1/L8/046/028/LC08_L1TP_046028_20200908_20200918_01_T1/LC08_L1TP_046028_20200908_20200918_01_T1_B5.TIF
    https://landsat-pds.s3.amazonaws.com/c1/L8/046/028/LC08_L1TP_046028_20200908_20200918_01_T1/LC08_L1TP_046028_20200908_20200918_01_T1_B6.TIF
    https://landsat-pds.s3.amazonaws.com/c1/L8/046/028/LC08_L1TP_046028_20200908_20200918_01_T1/LC08_L1TP_046028_20200908_20200918_01_T1_B7.TIF
    https://landsat-pds.s3.amazonaws.com/c1/L8/046/028/LC08_L1TP_046028_20200908_20200918_01_T1/LC08_L1TP_046028_20200908_20200918_01_T1_B8.TIF
    https://landsat-pds.s3.amazonaws.com/c1/L8/046/028/LC08_L1TP_046028_20200908_20200918_01_T1/LC08_L1TP_046028_20200908_20200918_01_T1_B9.TIF
    https://landsat-pds.s3.amazonaws.com/c1/L8/046/028/LC08_L1TP_046028_20200908_20200918_01_T1/LC08_L1TP_046028_20200908_20200918_01_T1_B10.TIF
    https://landsat-pds.s3.amazonaws.com/c1/L8/046/028/LC08_L1TP_046028_20200908_20200918_01_T1/LC08_L1TP_046028_20200908_20200918_01_T1_B11.TIF

You can also access them through: https://landsat-pds.s3.amazonaws.com/c1/L8/046/028/LC08_L1TP_046028_20200908_20200918_01_T1/index.html

Using Python, create the following raster products:

1. [Calculate the NDVI of the scene (10 points)](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-normalized-difference-vegetation-index?qt-science_support_page_related_con=0#qt-science_support_page_related_con)
2. [Calculate the SAVI of the scene (10 points)](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-soil-adjusted-vegetation-index#:~:text=This%20image%20displays%20a%20(left,Adjusted%20Vegetation%20Index%20(SAVI).&text=SAVI%20is%20used%20to%20correct,where%20vegetative%20cover%20is%20low.)
3. Using [Composite Bands](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/composite-bands.htm), create a 3 band R-G-B image from [bands 2, 3, and 4 (10 points)](https://gisgeography.com/landsat-8-bands-combinations/)
4. Using [Composite Bands](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/composite-bands.htm), create a false color infrared image from [bands 3, 4, 5 (10 points)](https://gisgeography.com/landsat-8-bands-combinations/)

Be sure to save the resulting rasters to disk as TIF files. 
Please create a clear, well-documented script or notebook. 
The readability will be graded out of 10 points.

You can use ```arcpy``` or ```numpy```. Just solve the problem.

## Problem 2 - Out of 50 Points

Turn script2.py into an ArcGIS Python GP Tool. 
Please submit the modified python script and the ArcGIS geoprocessing toolbox. 
You can test the script with the August2020.CSV file that is attached.

I am being very open ended here. 
I just want to see you complete the tasks. 
Don't over think it.
