try:
    import arcpy
    from arcpy import env
    env.workspace = "C:\EsriPress\Python\Data\Exercise09"
    rasterband = "tm.img\Layer_1"
    desc = arcpy.Describe(rasterband)
    x = desc.meanCellHeight
    y = desc.meanCellWidth
    spatialRef = desc.spatialReference
    units = spatialRef.angularUnitName
    print "The raster resolution of Band 1 is:" + str(x) + " by " + str(y) + " " + units + "."
    
except Exception , e:
    str(e)