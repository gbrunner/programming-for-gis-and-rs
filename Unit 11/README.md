# This week's lectures
This week's lecture notebooks can be found in 
ArcGIS Online at [GIS 4090\5090 Unit 11 Notebooks](https://slustl.maps.arcgis.com/home/group.html?id=b3d8431a10c64970b43e4ff59dd083d6#overview)

# Data for this week
Here are a few datasets that we will use this week:

    File Thunder_Departures_gjb.csv Click for more options (1.215 KB)
    File Thunder_Acquisitions_gjb.csv Click for more options (1.304 KB)
    File STL_Crime_gjb.gdb.zip Click for more options (640.133 KB)
    File STL_Crime_1.gdb.zip Click for more options (640.133 KB)
    File nbrhds_wards_demo1.zip Click for more options (179.985 KB)
    File national_rainfall_data_demogjb.zip Click for more options (992.424 KB) 
    
# Supplemental materials
If you are new to hex codes and colors, you can learn more on [the colorwheel](https://www.colorspire.com/rgb-color-wheel/).

# Unit 11 Exercise and Discussion Questions
Please complete the following for homework:
1. For context, [read this tutorial on Adding Spreadsheet data to ArcGIS Online.](https://www.esri.com/arcgis-blog/products/arcgis-online/data-management/add-spreadsheet-data-to-arcgis-online/)
2. Optionally, [watch the videos in Symbolize Data and Publish Maps.](https://learn.arcgis.com/en/paths/symbolize-data-and-publish-maps/)
3. Download the attached CSVs. Rename them to "Thunder_Departed_" followed by 
your initials and ".csv" and "Thunder_Acquisitions_" followed by your initials 
and ".csv". Create a notebook that geocodes those CSVs of addresses and adds 
each to the same map object with a different symbology 
(see [this tutorial](https://developers.arcgis.com/python/sample-notebooks/publishing-sd-shapefiles-and-csv/#Publish-a-CSV-file-and-move-it-into-a-folder) 
if you need help). Save this as a webmap following from [this 
example](https://developers.arcgis.com/python/guide/working-with-web-maps-and-web-scenes/#Saving-or-Updating-a-web-map). 
Be sure to go to ArcGIS online and check that the Webmap is there!

**Hint:** You can change the symbology by changing the renderer. 
For example, if you change the color values in this renderer, the points will 
change color accordingly.
    
    simple_renderer = {
      "renderer": {
        "type": "simple",
        "symbol": {
          "color": [
            0,
            0,
            128,
            128
          ],
          "size": 15,
          "angle": 0,
          "xoffset": 0,
          "yoffset": 0,
          "type": "esriSMS",
          "style": "esriSMSCircle",
          "outline": {
            "color": [
              0,
              0,
              128,
              255
            ],
            "width": 0.99975,
            "type": "esriSLS",
            "style": "esriSLSSolid"
          }
        }
      }
    }
    
    map1.add_layer(acled, simple_renderer)