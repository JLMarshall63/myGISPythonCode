prjFile = "C:/EsriPress/Python/Data/Exercise05/facilities.prj"
spatial_ref = arcpy.SpatialReference(prjFile)
arcpy.DefineProjection_management("hospitals",spatial_ref)
print spatial_ref.name
print spatial_ref.linearUnitName
print spatial_ref.XYResolution

