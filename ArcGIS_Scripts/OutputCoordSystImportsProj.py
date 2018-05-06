import arcpy
arcpy.env.workspace = "C:\EsriPress\Python\Data\Exercise05"
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = spatial_ref
prjFile = "C:/EsriPress/Python/Data/Exercise05/facilities.prj"
spatial_ref = arcpy.SpatialReference(prjFile)
arcpy.DefineProjection_management("hospitals",spatial_ref)
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = spatial_ref

