# Directions: Complete the function below. 

# Geog 565 2016 Assignment 6 Part 2
# Name: John Marshall
# Date: 7/25/2017
# This script creates and tests the listpolygons function

import arcpy
import os

# the listpolygons function takes in a workspace path and returns a list of
# all the polygons in that workspace
# for example, using your exercise 2 folder as the input workspace should print
#this to the console: [u'parks.shp', u'zip.shp']
list = []
def listpolygons(workspace):
    # set the workspace to the input workspace
    arcpy.env.workspace = workspace
    # your code here
    featureclasses = arcpy.ListFeatureClasses()
    for fc in featureclasses:
        list.append(fc)
        print list
##        if fc == "Polygon":          
    return list
    
##    for file in os.listdir(workspace):
####        if file.geometry == "Polygon"
##        print file
    
# Tests - Feel free to add more workspaces to test your function. Modify the workspace paths
#if necessary to point to your own exercise folders.

# this test should print out a list of all the polygons in your exercise 2 folder
listpolygons(r'C:\EsriPress\Python\Data\Exercise02')

# this test should print out a list of all the polygons in your exercise 5 folder
listpolygons(r'C:\EsriPress\Python\Data\Exercise05')