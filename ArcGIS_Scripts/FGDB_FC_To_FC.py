 Name: FeatureClassToFeatureClass_Example2.py
# Description: Use FeatureClassToFeatureClass with an expression to create a subset
#  of the original feature class.  
 
# Import system modules
import arcpy
from arcpy import env
 
# Set environment settings
env.workspace = "C:/data/GreenvalleyDB.mdb/Public Buildings"
 
# Set local variables
inFeatures = "buildings_point"
outLocation = "C:/output/output.gdb"
outFeatureClass = "postoffices"
delimitedField = arcpy.AddFieldDelimiters(env.workspace, "NAME")
expression = delimitedField + " = 'Post Office'"
 
# Execute FeatureClassToFeatureClass
arcpy.FeatureClassToFeatureClass_conversion(inFeatures, outLocation, 
                                            outFeatureClass, expression