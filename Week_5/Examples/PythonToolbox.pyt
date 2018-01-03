import urllib2
import json
import os
import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "UNHCR Python Toolbox"
        self.alias = "UNHCR"

        # List of tool classes associated with this toolbox
        self.tools = [unhcr]


class unhcr(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "UNHCR Immigration Analysis"
        self.description = "Brings in the UNHCR data and joins it to a feature class."
        self.canRunInBackground = True

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName = "Year (i.e. 2015)",
            name = "Year",
            datatype = "GPString",
            parameterType="Required",
            direction="Input")

        param1 = arcpy.Parameter(
            displayName = "Month (i.e. 1 for January)",
            name = "Month",
            datatype = "GPString",
            parameterType="Required",
            direction="Input")

        param2 = arcpy.Parameter(
            displayName = "Country Feature Class",
            name = "Country Feature Class",
            datatype = "DEFeatureClass",
            parameterType="Required",
            direction="Input")

        param3 = arcpy.Parameter(
            displayName = "Output Feature Class",
            name = "Output Feature Class",
            datatype = "DEFeatureClass",
            parameterType="Required",
            direction="Output")

        params = [param0, param1, param2, param3]

        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        #Set Parameters
        year = int(parameters[0].valueAsText)
        months = [int(parameters[1].valueAsText)]
        country_fc = parameters[2].valueAsText #r'C:\Users\greg6750\Documents\IPython Notebooks\Python_for_GIS_and_RS\Week_5\data\countries.gdb\med'
        new_country_fc = parameters[3].valueAsText
        gdb = os.path.dirname(new_country_fc)

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

        return
