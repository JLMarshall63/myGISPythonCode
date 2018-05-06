# Name: CreateFeatureDataset_Example2.py
# Description: Create a feature dataset 

# Import system modules
import arcpy
import os

# Set local variables
out_dataset_path = "C:\\PyGEOGCoastal\\SAMPLE25.gdb" 
out_name = "FDS1"

# Creating a spatial reference object
sr = arcpy.SpatialReference("C:\\PyGEOGCoastal\\DataReferences\\AOI.prj")

# Create a FileGDB for the fds
arcpy.CreateFileGDB_management("C:\\PyGEOGCoastal", "SAMPLE25.gdb")

# Execute CreateFeaturedataset 
arcpy.CreateFeatureDataset_management(out_dataset_path, out_name, sr)

#Reestablish workspace settings, paths, and Featureclass specs
#arcpy.env.workspace = "C:\\PyGEOGCoastal\\SAMPLE25.gdb"
outpath = "C:\\PyGEOGCoastal\\SAMPLE25.gdb"
outname = "testHab.shp"
##geometry_type = "Polygon"
##template = "C:\\PyGEOGCoastal\\DataReferences\\AOI.shp"
##has_m = "Disabled"
##has_z = "Disabled"

#Get a spatial reference object
sr = arcpy.Describe("C:\\PyGEOGCoastal\\DataReferences\\AOI.shp").spatialReference

#Create Featureclass
arcpy.CreateFeatureclass_management(outpath, outname, "POLYGON", sr)

"geometry_type, template, has_m, has_z, "