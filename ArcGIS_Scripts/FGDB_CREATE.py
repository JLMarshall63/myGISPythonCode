# Import system modules

import arcpy
import os
import sys
from arcpy import env
# Set workspace
arcpy.env.workspace = "C:\\PyGEOGCoastal"

# Set local variables
out_folder_path = "C:\\PyGEOGCoastal"
out_name = "SAMPLE2.gdb"

# Execute CreateFileGDB
arcpy.CreateFileGDB_management(out_folder_path, out_name)


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


