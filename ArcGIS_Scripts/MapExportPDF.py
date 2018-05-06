import arcpy
mapdoc = arcpy.mapping.MapDocument(r"C:\EsriPress\Python\Data\Exercise02\Flooding2.mxd")
arcpy.mapping.ExportToPDF(mapdoc, r"C:\EsriPress\Python\Data\Exercise02\Results\Flooding.pdf")
del mapdoc