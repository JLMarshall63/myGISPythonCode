# Directions: Using the lakes.shp file from the Exercise 2 folder, create a script that
# adds a new field called AreaClass (type Text), and then uses the AREA_ column to classify
# each lake as "Small", "Medium", or "Large" in this field.
# Hint: we already did this in the Field Calculator, but now we're doing it in a stand-alone script!

# Small - Area less than 35000
# Medium - Area greater than or equal to 35000 and less than 120000 feet
# Large - Area greater than or equal to 120000 feet

# Geog 565 2016 Assignment 2 Part 2
# Name: John Marshall
# Date: 6/29/2017

# This script adds a new field to a shapefile, then populates it with the size classification.
# import modules
# set workspace
# define a variable for our shapefile
# add a new field to hold our area class

# We need to make changes to the attribute table, and to do that we need to create an update cursor
# Use the AREA_ field and the new SizeClass field in the cursor
# populate SizeClass based on the value in AREA_ specified in the Directions
    # loop though the cursor
        # if area is small, define SizeClass as Small
        # if area is medium, define SizeClass as Medium
        # if area is large, define SizeClass as Large
        # update the row with the appropriate value - Don't forget this step!
# delete your row variable
# delete your cursor variable

try:
    #set workspace
    import arcpy
    arcpy.env.workspace = "C:\EsriPress\Python\Data\Exercise2b"

    #declare variable    
    lakes = "lakes.shp"
  
    # update cursor
    #add a new field to hold AreaClass value
    
    arcpy.AddField_management(lakes, "AreaClass", "TEXT", field_length = 15)
    
    #apply update cursor          
    with arcpy.da.UpdateCursor(lakes, ["AREA_","AreaClass"]) as cursor:
        for row in cursor:
            if row[0] < 35000:
                row[1] = "Small"
            if  row[0] >= 35000 and row[0] <120000:
                row[1] = "Medium"
            if row[0] >= 120000:
                row[1] = "Large"
    
            cursor.updateRow(row)

    del cursor, row
except Exception, e:
    print str(e)
