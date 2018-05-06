# Name: CreateFeatureDataset and populate w/fclass
# Description: Create a feature dataset 

# Import system modules
import arcpy

# Set local variables
out_dataset_path = "C:\\PyGEOGCoastal\\SAMPLE4.gdb" 
out_name = "FDS1"

# Creating a spatial reference object
sr = arcpy.SpatialReference("C:\\PyGEOGCoastal\\DataReferences\\AOI.prj")

# Create a FileGDB for the fds
arcpy.CreateFileGDB_management("C:\\PyGEOGCoastal", "SAMPLE4.gdb")

# Execute CreateFeaturedataset 
arcpy.CreateFeatureDataset_management(out_dataset_path, out_name, sr)

# Set local variables
fc_out_path = "C:\\PyGEOGCoastal\\SAMPLE4.gdb\\FDS1"
fc_out_name = "habitat.shp"
geometry_type = "POLYGON"

template = "C:\\PyGEOGCoastal\\DataReferences\\AOI.shp"
has_m = "DISABLED"
has_z = "DISABLED"

# Use Describe to get a SpatialReference object
spatial_reference = arcpy.Describe("C:\\PyGEOGCoastal\\DataReferences\\AOI.shp").spatialReference

# Execute CreateFeatureclass
arcpy.CreateFeatureclass_management(fc_out_path, fc_out_name, geometry_type, template, has_m, has_z, spatial_reference)
