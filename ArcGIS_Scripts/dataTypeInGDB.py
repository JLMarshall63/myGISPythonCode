try:
    import arcpy
    arcpy.env.workspace = "C:\EsriPress\Python\Data\Exercise06\Results\NM.gdb"
    dataItem = "railroad"
    desc = arcpy.Describe(dataItem)
    print "Dataset type: " + desc.datasetType
    print "File path: " + desc.path
    print "Catalog path: " + desc.catalogPath
    print "File name: " + desc.file
    print "Base name: " + desc.baseName
    print "Name: " + desc.name

except Exception, e:
    print str(e)