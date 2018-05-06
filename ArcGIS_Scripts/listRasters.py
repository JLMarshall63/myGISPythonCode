try:
    import arcpy
    from arcpy import env
    env.workspace = "C:\EsriPress\Python\Data\Exercise09"
    rasterList = arcpy.ListRasters()
    for raster in rasterList:
        print raster

except Exception , e:
    str(e)