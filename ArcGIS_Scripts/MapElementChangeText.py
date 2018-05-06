import arcpy 
mapdoc = arcpy.mapping.MapDocument(r"C:\EsriPress\Python\Data\Exercise10\Georgia.mxd")
title = arcpy.mapping.ListLayoutElements(mapdoc, "TEXT_ELEMENT")[0]
title.text = "Housing Official Vacancy for Georgia Counties (2000)"
mapdoc.save()
del mapdoc