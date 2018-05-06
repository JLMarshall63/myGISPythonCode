import arcpy
import os
from arcpy import env
env.workspace = GetParameterAsText(0)
path = env.workspace
outgdb = GetParameterAsText(1)
fclist = arcpy.ListFeatureClasses(path)
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    arcpy.CopyFeatures_management(fc, os.path.join(outgdb, fcdesc.basename))
   