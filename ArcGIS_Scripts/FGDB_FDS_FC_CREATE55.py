# Name: FGDB_FDS_FC_CREATE55
# Description: CreateS a file geodatabase, feature dataset, and a feature class

# Import system modules
import arcpy
import os

# Set local variables
out_dataset_path = "C:\\PyGEOGCoastal\\SAMPLE25.gdb" 
out_name = "FDS1"

# Instantiating a spatial reference object
sr = arcpy.SpatialReference("C:\\PyGEOGCoastal\\DataReferences\\AOI.prj")

# Create a FileGDB
arcpy.CreateFileGDB_management("C:\\PyGEOGCoastal", "SAMPLE25.gdb")

# Execute CreateFeaturedataset 
arcpy.CreateFeatureDataset_management(out_dataset_path, out_name, sr)

#Reestablish workspace settings, paths, and Featureclass specs

outpath = "rC:\\PyGEOGCoastal\\SAMPLE25.gdb\\FDSI"
outname = "testHab.shp"
geometry_type = "Polygon"
template = "C:\\PyGEOGCoastal\\DataReferences\\AOI.shp"
has_m = "Disabled"
has_z = "Disabled"

#Get a spatial reference object
sr = arcpy.Describe("C:\\PyGEOGCoastal\\DataReferences\\AOI.shp").spatialReference

#Create Featureclass
arcpy.CreateFeatureclass_management(outpath, outname, geometry_type, template, has_m, has_z, sr)

