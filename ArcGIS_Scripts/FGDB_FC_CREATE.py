import arcpy

arcpy.env.workspace = "C:\\PyGEOGCoastal"

# Set local variables
fc_out_path = "C:\\PyGEOGCoastal"
fc_out_name = "habitat.shp"
geometry_type = "POLYGON"

template = "C:\\PyGEOGCoastal\\DataReferences\\AOI.shp"
has_m = "DISABLED"
has_z = "DISABLED"

# Use Describe to get a SpatialReference object
spatial_reference = arcpy.Describe("C:\\PyGEOGCoastal\\DataReferences\\AOI.shp").spatialReference


# Execute CreateFeatureclass
arcpy.CreateFeatureclass_management(fc_out_path, fc_out_name, geometry_type, template, has_m, has_z, spatial_reference)

