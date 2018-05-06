# Name: John Marshall
# Date: 6/29/2017

# This script looks at all of the feature classes in a workspace and copies all of the point and line feature classes
# into a new database that the script creates.
# import modules
# import modules
# set workspace
# allow overwriting
# create new geodatabase
# Execute CreateFileGDB
# print out that the geodatabase was successfully created (this is very nice for the user,
#but not necessary for the script's purpose
# set a variable equal to a list of the feature classes in the workspace (use an arcpy
#function to do this)
# loop through each feature class in the list of feature classes
# use arcpy.Describe to set variables to the feature class name and shapeType
# if the shapeType is Point or Polyline, add it to the new geodatabase
# otherwise, if the shapeType is Polygon, do nothing

import arcpy
import os
from arcpy import env
arcpy.env.overwriteOutput = True

arcpy.env.workspace = "C:\TestGDB\Exercise06"
out_folder_path = "C:\TestGDB\Exercise06\Results\Resultsb"
out_name = "NM.gdb"
outWorkspace = "C:\TestGDB\Exercise06\Results\Resultsb\NM.gdb"

try:   
    fclist = arcpy.ListFeatureClasses()
    
    arcpy.CreateFileGDB_management(out_folder_path, out_name)  
    print "Geodatabase was created!"

    for fc in fclist:
        desc = arcpy.Describe(fc)
        type = desc.shapeType
        
        if (type == "Point" or type == "Polyline"):
            outFeatureClass = os.path.join(outWorkspace, fc.strip(".shp"))
            arcpy.CopyFeatures_management(fc, outFeatureClass)
            print "Feature class of type: " + type + " is imported."
        else:
            print "Feature class of type: " + type + " is not imported."
        
except Exception, e:
    print str(e)