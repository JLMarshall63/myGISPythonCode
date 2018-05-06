# Import system modules

import arcpy
import os
from arcpy import env
arcpy.env.overwriteOutput = True

# Set workspace

arcpy.env.workspace = "C:\TestGDB\Exercise06"

# Set local variables

out_folder_path = "C:\TestGDB\Exercise06\Results"
out_name = "NM.gdb"

outWorkspace = "C:\TestGDB\Exercise06\Results\NM.gdb"

try:
    # Use ListFeatureClasses to generate a list of shapefiles in the
    # workspace.

    fclist = arcpy.ListFeatureClasses()
    
    # Execute CreateFileGDB
    arcpy.CreateFileGDB_management(out_folder_path, out_name)

    
    # Execute CopyFeatures for each input shapefile   
    for fc in fclist:
        outFeatureClass = os.path.join(outWorkspace, fc.strip(".shp"))
        arcpy.CopyFeatures_management(fc, outFeatureClass)

except Exception, e:
    print str(e)
        

