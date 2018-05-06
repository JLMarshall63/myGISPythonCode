try:
    import arcpy
    from arcpy import env
    env.workspace = "C:\EsriPress\Python\Data\Exercise09"
    raster = "tm.img"
    desc = arcpy.Describe(raster)
    print "Raster baseName is: " + desc.basename
    print "Raster dataType is: {0}".format(desc.dataType)
    print "Raster fileExtension is: {0}".format(desc.extension)
    print "Raster spatial reference is: {0}".format(desc.spatialReference.name)
    print "Raster format is: {0}".format(desc.format)
    print "Raster compression type is {0}".format(desc.compressionType)
    print "Raster number of bands is: " + str(desc.bandCount)

except Exception , e:
    str(e)