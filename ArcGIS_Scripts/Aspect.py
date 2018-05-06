import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:\EsriPress\Python\Data\Exercise09"
outraster2 = arcpy.sa.Aspect("Elevation")
desc = arcpy.Describe(outraster2)
print desc.permanent
outraster2.save("aspect")

