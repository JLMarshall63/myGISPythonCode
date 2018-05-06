try:
     # set workspace
    import arcpy
    arcpy.env.workspace = "C:\EsriPress\Python\Data\Exercise05"

    fchosp = "hospitals.shp"

    # insert cursor
    cursor = arcpy.da.InsertCursor(fchosp, ['NAME'])
    cursor.insertRow(['Waverly Valley'])
    del cursor

    # insert cursor 2
    cursor = arcpy.da.InsertCursor(fchosp, ['NAME'])

    x = 1
    while x <= 5:
        cursor.insertRow(['My Angles of Trinity'])
        x += 1

    del cursor        
    
except Exception, e:
    print str(e)