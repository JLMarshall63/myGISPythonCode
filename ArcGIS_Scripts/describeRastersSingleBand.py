try:
    import arcpy
    from arcpy import env
    env.workspace = "C:\EsriPress\Python\Data\Exercise09"
    raster = "landcover.tif"
    desc = arcpy.Describe(raster)
    x = desc.meanCellHeight
    y = desc.meanCellWidth
    spatialRef = desc.spatialReference
    units = spatialRef.linearUnitName
    print "The raster resolution is:" + str(x) + " by " + str(y) + " " + units + "."
    
except Exception , e:
    str(e)