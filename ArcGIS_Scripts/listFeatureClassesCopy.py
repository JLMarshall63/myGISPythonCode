import arcpy
from arcpy import env
env.workspace = "C:\EsriPress\Python\Data\Exercise06"
fclist = arcpy.ListFeatureClasses()

print fclist

for fc in fclist:
    arcpy.CopyFeatures_management(fc, "C:\EsriPress\Python\Data\Exercise06\Results\copy" + fc)
    


