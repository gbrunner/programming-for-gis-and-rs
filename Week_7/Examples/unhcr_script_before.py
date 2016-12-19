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

year = 2016
months = [1,2,3,4,5]
country_fc = r'C:\Users\greg6750\Documents\IPython Notebooks\Python_for_GIS_and_RS\Week_5\data\countries.gdb\med'
gdb = r"C:\Users\greg6750\Documents\IPython Notebooks\Python_for_GIS_and_RS\Week_5\data\unhcr.gdb"

for month in months:
    tablename = "immigration_stats_" + str(month) + "_" + str(year)
    fields = ('COUNTRY', 'VALUE')
    new_country_fc = country_fc+'_imm_stats_' + str(month) + '_' + str(year)
    url =  'http://data.unhcr.org/api/stats/mediterranean/monthly_arrivals_by_country.json?year=%s&month=%s' % (year, month)

    #Get data with urllib2
    data = urllib2.urlopen(url)
    imm_data = json.load(data)

    ## Parsing the data into an array
    json_rows = []
    for row in enumerate(imm_data):
        temp = (row[1]['country_en'], row[1]['value'])
        json_rows.append(temp)
        print(temp)

    #Create table
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
        arcpy.AddField_management(gdb_and_table, fields[0], 'TEXT', "", "", 48)
        arcpy.AddField_management(gdb_and_table, fields[1], "LONG", "", "", "")

    ## Insert data into table
    c = arcpy.da.InsertCursor(gdb_and_table,fields)
    for row in json_rows:
        print(row)
        c.insertRow(row)
    del c

    ## Join Table to Existing feature class
    country_join_field = 'NAME'
    arcpy.CopyFeatures_management(country_fc, new_country_fc)
    arcpy.JoinField_management (new_country_fc, country_join_field, gdb_and_table, fields[0])