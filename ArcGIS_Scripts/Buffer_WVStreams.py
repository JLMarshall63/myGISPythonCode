#Buffer the rivers feature for each distance in the distance list

import arcpy
arcpy.env.workspace = r"C:\Data\Models\TModel1.gdb\Hydrology"
fc = "WV_rivers"
distanceList = ["100 meters", "200 meters", "400 meters"]
#Loop through each distance in the distance list
for dist in distanceList:
    outName = fc+"_"+ dist
    arcpy.Buffer_analysis(fc, outName, dist)
    print "Finished Buffering"