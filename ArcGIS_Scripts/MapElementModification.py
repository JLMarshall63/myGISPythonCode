try:
    import arcpy
    mxd = "C:\EsriPress\Python\Data\Exercise10\Georgia.mxd"
    mapdoc = arcpy.mapping.MapDocument(mxd)
    elemlist = arcpy.mapping.ListLayoutElements(mapdoc)
    title = elemlist[0]
    title.text = "Housing Vacancy for Georgia Counties (2000)"
    mapdoc.save()
    del mapdoc

except Exception , e:
    str(e)