import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:\EsriPress\Python\Data\Exercise09"
elevRaster = arcpy.Raster("Elevation")

outraster3 = elevRaster * 3.281
outraster3.save("elev_ft")

