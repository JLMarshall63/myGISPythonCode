import arcpy
mapdoc = arcpy.mapping.MapDocument(r"C:\EsriPress\Python\Data\Exercise02\Flooding2.mxd")
df = arcpy.mapping.ListDataFrames(mapdoc)[0]
layr1 = arcpy.mapping.Layer(r"C:\EsriPress\Python\Data\Exercise02\Results\rivers.lyr")
layr2 = arcpy.mapping.Layer(r"C:\EsriPress\Python\Data\Exercise02\Results\floodZn_clp.lyr")
legend = arcpy.mapping.ListLayoutElements(mapdoc, "LEGEND_ELEMENT")[0]
legend.autoAdd = True
arcpy.mapping.AddLayer(df, layr1, "BOTTOM")
legend.autoAdd = True
arcpy.mapping.AddLayer(df, layr2, "BOTTOM")
mapdoc.save()
del mapdoc