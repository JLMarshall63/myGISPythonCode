try:
    import arcpy
    from arcpy import env
    env.workspace = "C:\EsriPress\Python\Data\Exercise06"

    #prints railroads fields as objects    
    fieldList = arcpy.ListFields("railroads.shp")
    print fieldList

    #prints railroads fields names    
    fieldList = arcpy.ListFields("railroads.shp")
    for field in fieldList:
        print field.name

    #selects railroads fields by integer data type
    fieldList = arcpy.ListFields("railroads.shp", "", "Integer")
    for field in fieldList:
        print field.name

    #selects railroads fields by string data type and prints length
    fieldList = arcpy.ListFields("railroads.shp", "", "String")
    for field in fieldList:
        print field.name + " " + str(field.length)        
    #string length ineger is converted to string in print method
except Exception, e:
    print  str(e)