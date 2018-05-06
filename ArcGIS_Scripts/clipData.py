import arcpy
arcpy.env.workspace = "C:\EsriPress\Python\Data\Exercise06"
infc = "railroads"
clipfc = "new_mexico.shp"
outfc = "railroads_clip.shp"
desc = arcpy.Describe(clipfc)
type = desc.shapeType
if type == "Polygon":
    arcpy.Clip_analysis(infc, clipfc, outfc)
else:
    print "The clip feature is not a polygon."