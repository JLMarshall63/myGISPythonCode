import arcpy
import os
from arcpy import env
env.workspace = arcpy.GetParameterAsText(0)
env.overwriteOutput = True
outgdb = arcpy.GetParameterAsText(1)
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    arcpy.CopyFeatures_management(fc, os.path.join(outgdb, fcdesc.basename))
   