import arcpy
import os
def countstringfields(table):
    fields = arcpy.ListFields(table)
    i = 0
    for field in fields:
        if field.type == "String":
            i += 1

    return i
