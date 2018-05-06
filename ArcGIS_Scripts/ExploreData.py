import arcpy
myshape = arcpy.Describe("cities")
myshape.dataType
myshape = arcpy.Describe("C:\EsriPress\Python\Data\Exercise06cities.shp")
myshape = arcpy.Describe("C:\EsriPress\Python\Data\Exercise06\cities.shp")
myshape.dataType
mylayer = arcpy.Describe("cities")
mylayer.dataType
mylayer.datasetType
mylayer.catalogPath
mylayer.basename
mylayer.isVersioned
mylayer.shpType
mylayer.shapeType
mylayer.spatialReference
mylayer.spatialReference.name
mylayer.spatialReference.type
mylayer.spatialReference.domain

