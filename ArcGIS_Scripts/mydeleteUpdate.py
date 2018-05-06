try:
     # set workspace
    import arcpy
    arcpy.env.workspace = "C:\EsriPress\Python\Data\Exercise05"

    fchosp = "hospitals.shp"

    # update cursor
    cursor = arcpy.da.UpdateCursor(fchosp, ['NAME'])
    for row in cursor:
        if row[0] == "Recovery" or row[0] == "Prudence":
            cursor.deleteRow()
    
except Exception, e:
    print str(e)