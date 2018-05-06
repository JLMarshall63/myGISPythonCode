import arcpy
from arcpy import env
env.workspace = "C:\EsriPress\Python\Data\Exercise06"
fclist = arcpy.ListFeatureClasses()

print fclist

for fc in fclist:
    fcdescribe = arcpy.Describe(fc)
    print "Name: " + fcdescribe.name
    print "Data type: " + fcdescribe.dataType
    


