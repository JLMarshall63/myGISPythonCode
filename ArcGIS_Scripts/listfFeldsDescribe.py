try:
    import arcpy
    from arcpy import env
    env.workspace = "C:\EsriPress\Python\Data\Exercise06"
    fieldList = arcpy.ListFields("railroads.shp")
    for field in fieldList:
        print "{0} is a type of {1} with a length of {2}.".format(field.name,
        field.type, field.length)

except Exception, e:
    print str(e)