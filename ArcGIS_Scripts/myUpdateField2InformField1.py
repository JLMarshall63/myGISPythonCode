try:
    #set workspace
    import arcpy
    arcpy.env.workspace = "C:\EsriPress\Python\Data\Exercise05"

    #declare variables    
    prks = "parks.shp"
    newField = "ACRES"
    # update cursor

    #add a new field to hold our acres values

    arcpy.AddField_management(prks, newField,"FLOAT")

    #apply update cursor    
        
    with arcpy.da.UpdateCursor(prks, ["ACRES","SHAPE_AREA"]) as cursor:
        for row in cursor:
            row[0] = row[1]/43560
            cursor.updateRow(row)

    del cursor, row

except Exception, e:
    print str(e)