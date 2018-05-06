import arcpy
var = arcpy.Exists("C:\EsriPress\Python\Data\Exercise06\Results\cities.shp")

print var
var = arcpy.Exists("C:\EsriPress\Python\Data\Exercise06\cities.shp")
print var
var = arcpy.Describe("C:\EsriPress\Python\Data\Exercise06\cities.shp")
print var
print var.name
print var.shapeType

