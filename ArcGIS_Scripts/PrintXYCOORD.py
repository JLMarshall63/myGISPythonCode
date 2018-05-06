try:
    import arcpy
    from arcpy import env
    env.workspace = "C:\EsriPress\Python\Data\Exercise08"
    fc = "dams.shp"
    cursor = arcpy.da.SearchCursor(fc, ["SHAPE@XY"])
    for row in cursor:
        x, y = row[0]
        print("{0}, {1}".format(x, y))

except Exception , e:
    str(e)