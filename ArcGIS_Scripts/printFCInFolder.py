try:
    import arcpy
    from arcpy import env
    env.workspace = "C:\EsriPress\Python\Data\Exercise06"
    fclist = arcpy.ListFeatureClasses()
    print fclist

#first argument/param of method takes wildcard * to
#select fc staring with "r*"
    fclist = arcpy.ListFeatureClasses("r*")
    print fclist

#second argument/param of method takes featureType to
#select fc staring with "point"
    fclist = arcpy.ListFeatureClasses("","point")
    print fclist    

except Exception, e:
    print(e)