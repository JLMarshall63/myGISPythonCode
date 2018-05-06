# Geog 565 2016 Assignment 3 Part 3
# Name: John Marshall
# Date: 7/3/2017

# Directions: Using the q1222.dem file in the NSeattleDEM folder included in the starter zip,
# create a contour file that uses an interval that the user specifies. You must use arcpy.GetParameterAsText for this.
# Be sure to test your script using different intervals.


# import arcpy
import arcpy

# import arcpy.sa
from arcpy.sa import *

# set your environment variables

arcpy.env.workspace = "C:\EsriPress\Assignment3\NSeattleDEM"
arcpy.env.overwriteOutput = True

# get your interval from the user using arcpy.GetParameterAsText
inRaster = arcpy.GetParameterAsText(0) #q1222.dem
outContours = arcpy.GetParameterAsText(1)#elev_cont.shp"
ci_str = int(arcpy.GetParameterAsText(2))#100
contInterval = int(ci_str)
bc_str = int(arcpy.GetParameterAsText(3))# 0
baseContour = int(bc_str)

# check out the Spatial Analyst extention if its available
if arcpy.CheckExtension("Spatial") == "Available":
    arcpy.CheckOutExtension("Spatial")

# do the contouring
    Contour(inRaster, outContours, contInterval, baseContour)

# check in the Spatial Analyst extention
arcpy.CheckInExtension("Spatial")