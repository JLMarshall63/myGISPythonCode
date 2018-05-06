import arcpy
from arcpy import env
env.workspace = "C:\EsriPress\Python\Data\Exercise08"
fc = "Hawaii.shp"
cursor = arcpy.da.SearchCursor(fc, ["OID@", "SHAPE@"])
for row in cursor:
    if row[1].isMultipart:
        print("Feature {0} is multi-part and has {1} parts.".format(row[0], str(row[1].partCount)))
    else:
        print("Feature {0} is single-part.".format(row[0]))