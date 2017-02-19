#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      greg6750
#
# Created:     11/12/2016
# Copyright:   (c) greg6750 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib2
import json
import os
import arcpy

## Get all immigration data
url = 'http://data.unhcr.org/api/stats/mediterranean/monthly_arrivals_by_country.json?'
data = urllib2.urlopen(url)
imm_data = json.load(data)
print(imm_data)


## Get only Greece from 2014
country = 'GRE'
year = 2016
url =  'http://data.unhcr.org/api/stats/mediterranean/monthly_arrivals_by_country.json?year=%s&country=%s' % (year, country)
data = urllib2.urlopen(url)
imm_data = json.load(data)
print(imm_data)

## Get only Greece from 2014
#country = 'GRE'
year = 2016
month = 1
url =  'http://data.unhcr.org/api/stats/mediterranean/monthly_arrivals_by_country.json?year=%s&month=%s' % (year, month)
data = urllib2.urlopen(url)
imm_data = json.load(data)
print(imm_data)


## Parsing the data into an array
json_rows = []
for row in enumerate(imm_data):
    temp = (row[1]['country_en'], row[1]['value'])
    json_rows.append(temp)
    #print(temp)

## Create table
#Let's name it unhcr.gdb
gdb = r"C:\Users\greg6750\Documents\IPython Notebooks\Python_for_GIS_and_RS\Week_5\data\unhcr.gdb"
#arcpy.env.workspace = gdb
tablename = "immigration_stats_" + str(month) + "_" + str(year)
gdb_and_table = os.path.join(gdb, tablename)

if arcpy.Exists(gdb):
    print(gdb +  " already exists.")
else:
    print("Creating " + gdb)
    arcpy.CreateFileGDB_management(os.path.split(gdb)[0], os.path.basename(gdb))

if arcpy.Exists(os.path.join(gdb, tablename)):
    print('Table Exists')
else:
    print('Creating Table.')
    arcpy.CreateTable_management(gdb, tablename)

    ## Add fields to table
    fields = ('COUNTRY', 'VALUE')
    arcpy.AddField_management(gdb_and_table, fields[0], 'TEXT', "", "", 48)
    arcpy.AddField_management(gdb_and_table, fields[1], "LONG", "", "", "")

## Insert data into table
c = arcpy.da.InsertCursor(gdb_and_table,fields)
for row in json_rows:
    print(row)
    c.insertRow(row)
del c

## Join Table to Existing feature class
country_fc = r'C:\Users\greg6750\Documents\IPython Notebooks\Python_for_GIS_and_RS\Week_5\data\countries.gdb\med'
country_join_field = 'NAME'
arcpy.JoinField_management (country_fc, country_join_field, gdb_and_table, fields[0])