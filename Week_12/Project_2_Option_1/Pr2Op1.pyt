import arcpy
import os


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "SLMPD Crime Data CVS Import"
        self.alias = "crime"

        # List of tool classes associated with this toolbox
        self.tools = [CrimeImport]


class CrimeImport(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Crime Import"
        self.description = ""
        self.canRunInBackground = True

    def getParameterInfo(self):
        """Define parameter definitions"""
	#First Parameter
	CSV_files = arcpy.Parameter(
		displayName = "CSV Files",
		name = "CSV_files",
		datatype = "DEFile",
		parameterType = "Required",
		direction = "Input",
		multiValue=True)
	#Second Parameter
	out_features = arcpy.Parameter(
		displayName = "Output Feature Class",
		name = "out_features",
		datatype = "Feature Class",
		parameterType = "Required",
		direction = "Output")
        params = [CSV_files, out_features]
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
        output_features = parameters[1].valueAsText
        arcpy.AddMessage(output_features)

        CSV_files = parameters[0].valueAsText
        CSV_list = CSV_files.split(';')

        for x in CSV_list:
            arcpy.AddMessage(x)

        spRef = arcpy.SpatialReference("NAD 1983 StatePlane Missouri East FIPS 2401 (US Feet)")

        output_gdb = (os.path.dirname(output_features))
        arcpy.AddMessage(output_gdb)

        feature_class = os.path.join(output_gdb, output_features)
        arcpy.AddMessage(feature_class)

        if arcpy.Exists(output_gdb) == False:
            arcpy.AddMessage("Creating GDB...")
            arcpy.CreateFileGDB_management(os.path.split(output_gdb)[0], os.path.split(output_gdb)[1])

        list_fc = []

        arcpy.AddMessage(len(CSV_list))

        for x in range(len(CSV_list)):
        	arcpy.AddMessage("Copying Rows...")
        	temp_table = os.path.join(output_gdb, "temp_crime_table")
        	arcpy.CopyRows_management(CSV_list[x], temp_table)

        	arcpy.AddMessage("Making Point Features...")
        	arcpy.MakeXYEventLayer_management(temp_table, "XCoord", "YCoord", "Temp_Points", spRef, "")
        	arcpy.FeatureClassToFeatureClass_conversion("Temp_Points", output_gdb, "temp_feature_class"+str(x))

		arcpy.AddMessage("Adding Feature Class to List...")
		list_fc.append(os.path.join(output_gdb,"temp_feature_class"+str(x)))

        	arcpy.AddMessage("Deleting Table...")
        	arcpy.Delete_management(temp_table)


        arcpy.Merge_management(list_fc,output_features)

        arcpy.AddMessage("Done.")
        return
