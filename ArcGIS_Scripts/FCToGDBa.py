import arcpy
import os
from arcpy import env
env.workspace = GetParameterAsText(0)
outgdb = GetParameterAsText(1)
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    arcpy.CopyFeatures_management(fc, os.path.join(outgdb, fcdesc.basename))