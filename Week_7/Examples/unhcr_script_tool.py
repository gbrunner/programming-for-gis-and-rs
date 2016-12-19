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

#Set Parameters
year = int(arcpy.GetParameterAsText(0))
months = [int(arcpy.GetParameterAsText(1))]
country_fc = arcpy.GetParameterAsText(2) #r'C:\Users\greg6750\Documents\IPython Notebooks\Python_for_GIS_and_RS\Week_5\data\countries.gdb\med'
new_country_fc = arcpy.GetParameterAsText(3)
gdb = os.path.dirname(new_country_fc)
#gdb = arcpy.GetParameterAsText(3) #r"C:\Users\greg6750\Documents\IPython Notebooks\Python_for_GIS_and_RS\Week_5\data\unhcr.gdb"

for month in months:
    tablename = "immigration_stats_" + str(month) + "_" + str(year)
    arcpy.AddMessage("Definint table: " + tablename)
    fields = ('COUNTRY', 'VALUE')
    #new_country_fc = country_fc+'_imm_stats_' + str(month) + '_' + str(year)
    arcpy.AddMessage("Defining output feature class: " + new_country_fc)
    url =  'http://data.unhcr.org/api/stats/mediterranean/monthly_arrivals_by_country.json?year=%s&month=%s' % (year, month)

    #Get data with urllib2
    data = urllib2.urlopen(url)
    imm_data = json.load(data)

    ## Parsing the data into an array
    json_rows = []
    for row in enumerate(imm_data):
        temp = (row[1]['country_en'], row[1]['value'])
        json_rows.append(temp)
        #print(temp)

    #Create table
    arcpy.AddMessage("Creating Table")
    gdb_and_table = os.path.join(gdb, tablename)

    if arcpy.Exists(gdb):
        arcpy.AddMessage(gdb +  " already exists.")
    else:
        arcpy.AddMessage("Creating " + gdb)
        arcpy.CreateFileGDB_management(os.path.split(gdb)[0], os.path.basename(gdb))

    if arcpy.Exists(os.path.join(gdb, tablename)):
        arcpy.AddMessage('Table Exists')
    else:
        arcpy.AddMessage('Creating Table.')
        arcpy.CreateTable_management(gdb, tablename)

        ## Add fields to table
        arcpy.AddField_management(gdb_and_table, fields[0], 'TEXT', "", "", 48)
        arcpy.AddField_management(gdb_and_table, fields[1], "LONG", "", "", "")

    ## Insert data into table
    c = arcpy.da.InsertCursor(gdb_and_table,fields)
    for row in json_rows:
        arcpy.AddMessage(row)
        c.insertRow(row)
    del c

    ## Join Table to Existing feature class
    country_join_field = 'NAME'
    arcpy.AddMessage("Creaging " + new_country_fc)
    arcpy.CopyFeatures_management(country_fc, new_country_fc)
    arcpy.AddMessage("Joining " + gdb_and_table + " to " + new_country_fc)
    arcpy.JoinField_management (new_country_fc, country_join_field, gdb_and_table, fields[0])