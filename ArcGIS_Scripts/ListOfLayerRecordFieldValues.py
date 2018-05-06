# Directions: Fix the syntax errors in this script. When you find them, make a comment above the
# line describing the problem and how you fixed it.

# Geog 565 2016 Assignment 5 Part 1
# Name: John Marshall
# Date: 7/17/2017
# This script prints the name of each park in the parks.shp file

import arcpy
from arcpy import env
#Reinforced env to inherit from arcpy and copied workspace path directly from my directory
arcpy.env.workspace = "C:/EsriPress/Python/Data/Exercise11"
#Changed variable to match commonly used lower case convention and to match
#method arguments variable is passed to below
fc = "parks.shp"
#Changed 'rows' variable to 'cursor' to better represent variables' role in application.
# & added a bracketed "PARK_NAME" field into the argument to inform search cursor method of focal field
#of interest.  Inserted data access (da) module to employ its functionality, especially suitable
#to access geometries and their attributes.
cursor = arcpy.da.SearchCursor(fc, ["PARK_NAME"])

# commented out unnecessary statement: fields = arcpy.ListFields(fc)
# commented out unnecessary and erroneously expressed forloop 
#for field in fields
    #commented out unnecessary and erroneously expressed if statement
    #if field.name = "PARK_NAME":
#put forloop in proper position (no indentation) and changed iterable to cursor
for row in cursor:
    #Rewrote a more efficient print statement by identifying row index and eliminating
    #unnecessary method to get field values and the associated field name argument
    #that has already been passed to the search cursor method.
    print "Park Name = {0}".format(row[0])
