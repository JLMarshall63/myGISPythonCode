# Name: CreateFeatureDataset_Example2.py
# Description: Create a feature dataset 

# Import system modules
import arcpy

# Set local variables
out_dataset_path = "C:\\PyGEOGCoastal\\SAMPLE5.gdb" 
out_name = "FDS1"

# Creating a spatial reference object
sr = arcpy.SpatialReference("C:\\PyGEOGCoastal\\DataReferences\\AOI.prj")

# Create a FileGDB for the fds
arcpy.CreateFileGDB_management("C:\\PyGEOGCoastal", "SAMPLE5.gdb")

# Execute CreateFeaturedataset 
arcpy.CreateFeatureDataset_management(out_dataset_path, out_name, sr)


