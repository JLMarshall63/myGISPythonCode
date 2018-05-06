import arcpy
mxd = "C:\EsriPress\Python\Data\Exercise10\Georgia.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)
elemlist = arcpy.mapping.ListLayoutElements(mapdoc)
for elem in elemlist:
    print elem.name + " : " + elem.type
del mapdoc