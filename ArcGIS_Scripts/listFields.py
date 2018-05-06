try:
    import arcpy
    from arcpy import env
    env.overwriteOutput = True
    env.workspace = "C:\EsriPress\Python\Data\Exercise06"
    fieldlist = arcpy.ListFields("cities.shp")
    for field in fieldlist:
        print field.name + " " + field.type

except Exception, e:
    print str(e)
    