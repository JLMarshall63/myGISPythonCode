import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/data/Exercise05"
env.overwriteOutput = True
arcpy.Clip_analysis("parks.shp", "zip.shp", "Results/parks_Clip.shp")
print arcpy.GetMessages()


