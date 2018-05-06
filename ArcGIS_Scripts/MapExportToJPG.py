import arcpy
mapdoc = arcpy.mapping.MapDocument(r"C:\EsriPress\Python\Data\Exercise02\Flooding2.mxd")
arcpy.mapping.ExportToJPEG(mapdoc, r"C:\EsriPress\Python\Data\Exercise02\Results\flooding.jpg")
del mapdoc