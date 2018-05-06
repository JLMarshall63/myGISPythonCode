try:
    import arcpy
    arcpy.env.workspace = "C:\EsriPress\Python\Data\Exercise06\Results\NM.gdb"
    fc = "railroad"
    cursor = arcpy.da.SearchCursor(fc, ["RROWNER1"])
    for record in cursor:
        print "Railroad owner:   {0}".format(record[0])

except Exception, e:
    print str(e)