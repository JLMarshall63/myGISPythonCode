import arcpy
mxd = "C:\EsriPress\Python\Data\Exercise10\Georgia.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)
elemlist = arcpy.mapping.ListLayoutElements(mapdoc, "PICTURE_ELEMENT")
for elem in elemlist:
    if elem.name == "Agape":
        elem.sourceImage = "C:\Image\smiley.jpg"
mapdoc.save()
del mapdoc
