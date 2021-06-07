# Watch this video
## Teaching with ArcGIS Notebooks
[Check out Convert ArcGIS Notebooks to slides. Recognize the voice?](https://s3-us-west-2.amazonaws.com/lp.esri.com/localgovt/LEARN/Videos/Notebooks2.mp4) 
In case that link doesn't work: https://learn.arcgis.com/en/paths/teach-with-arcgis-notebooks/

# More Imagery - GDAL and Python
Attached Files:

    File unit_7_boto_and_azure.ipynb Click for more options (1.564 MB)
    File unit_7_gdal.ipynb Click for more options (2.015 MB) 

# This week's slides

This week we will learn how to create Python geoprocessing tools for ArcGIS Pro.
Attached Files:

    File Python_GP_Tools.ppt Click for more options (8.155 MB) 

# This week's demo scripts
Attached Files:

    File problem1_script.py Click for more options (657 B)
    File problem2_script.py Click for more options (827 B) 
    

# Unit 7 Exercise and Discussion Questions
This goes with Chapter 3 of Advanced Scripting for ArcGIS Pro. Please complete 
this tutorial on creating script tools: https://www.arcgis.com/home/item.html?id=cdb970479d5f4439ac5d2eb155bdd6f6

Here is the data: https://www.arcgis.com/home/item.html?id=fbb1335ef10944259899a3af6206e10e

Please complete the following question. Submit screen shots of the 
results for 1 and 2. Submit the Python script for 3:

1. Create a cloud storage connection to Landsat 8 in Amazon S3 if you 
haven’t already. [Download the Landsat Descending Path Row shapefile.](https://prd-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/atoms/files/WRS2_descending_0.zip) 
Unzip it and view the shapefile in ArcGIS Pro. Identify a path row that 
covers Northern California. Use that path row to find the imagery over 
California in the Landsat 8 cloud storage connection. If you are interested 
in a challenge, find a path row over Northern California from the early 
September 2020 time frame and try to identify the locations of wildfires 
in the Landsat 8 imagery.
2. [SpaceNet](https://registry.opendata.aws/spacenet/) is an open geospatial dataset consisting of freely available imagery. 
That dataset is used as a test bed for computer vision, machine learning, 
deep learning, and GeoAI research. Create a new ArcGIS Pro project. 
In that project, create a cloud storage connection to the SpaceNet dataset. 
You do not need to specify the region when creating the cloud storage connection.
Search through the SpaceNet S3 bucket. Add a few images from the SpaceNet S3 
bucket to the map. What cities does SpaceNet have imagery for?
3. Make a copy of the random_sample.py script and call it random_percent.py. Modify 
the script so that the third parameter is a percentage of the number of input 
records as an integer between 1 and 100. Modify the script tool settings so 
that the input for this parameter is validated on the tool dialog box
