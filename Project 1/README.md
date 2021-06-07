# Spring 2020
## Problem 1 (15 Points)¶

Unzip imagery.zip. Create a Notebook that uses arcpy Answer the following questions:

1. How many rasters are in the folder?
2. What is the projection of the rasters?
3. Do all the rasters have the same projection?
4. How many bands to the rasters have?
5. What is the raster format?

Please use markdown cells to explain your answers. I'm not looking for anything too fancy here, just show me how you can use Python and arcpy to answer these questions.

## Problem 2 (15 Points)

Unzip tlgdb_2019_a_us_school.gdb. Create a Notebook that uses arcpy to create a report about the features in the geodatabase. List out the following:

1. Feature class name
2. Number of features in the feature class
3. Projection of the feature class
4. Shape type of the feature class (point, polyline, polygon, etc.)

Bonus (5 points) Write your results out to a text file or comma separated text file.

## Problem 3 (15 Points)

Unzip usa_cities.gdb.zip. Identify the largest cities in the United States that have a population greater than 1 million people. Using Python, print a table that lists those largest cities and their corresponding population, according to the cities feature class. Use **POPULATION** as the population field.

I recommend using ```arcpy.da.SearchCursor``` to iterate through the cities feature class to create a list of the cities and corresponding populations.

## Problem 4 (15 Points)

Unzip usa_cities.gdb.zip. Create a list of city capitals and their corresponding state.

I recommend Using ```arcpy.da.SearchCursor``` to iterate through the cities feature class to create a list of the cities and corresponding populations.

## Problem 5 (20 Points)

Create a Python script or Notebook that copies all cities with a population over 1 million to a new feature class in the same geodatabase.

I recommend exploring the following GP tools:

- [Make Feature Layer](https://pro.arcgis.com/en/pro-app/tool-reference/data-management/make-feature-layer.htm)
- [Select Layer by Attribute](https://pro.arcgis.com/en/pro-app/tool-reference/data-management/select-layer-by-attribute.htm)
- [Copy Features](https://pro.arcgis.com/en/pro-app/tool-reference/data-management/copy-features.htm)

### Bonus (10 points) Using a for loop, write out the following 4 feature classes:

1. Feature class with a population greater than 1 million.
2. Feature class with a population between 500,000 and 1 million.
3. Feature class with a population between 100,000 and 500,000.
4. Feature class with a population less than 100,000

## Grading

The project is out of a total of 100 points, 80 points for the problems, 20 points for you code documentation. Please use Markdown cells in your notebooks to explain what you are doing or code comments such as ## in your code cells. Any Bonus points can your score above 100 percent.