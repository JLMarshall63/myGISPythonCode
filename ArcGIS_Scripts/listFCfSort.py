try:
    import arcpy
    from arcpy import env
    env.workspace = "C:\EsriPress\Python\Data\Exercise06\Results\NM.gdb"
    fcs = arcpy.ListFeatureClasses()
    #prints the number of feature classes in the gdb
    print len(fcs)

    #creates list and sorts and reverse sorts the list of feature classes in gdb

    fcs.sort()
    print fcs
    
    fcs.sort(reverse = True)
    print fcs

except Exception, e:
    print str(e)