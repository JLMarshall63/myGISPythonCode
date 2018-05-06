
#Clip Oregon City Limits to Willamette Valley Ecoregion
#imprt arcpy libraries
import arcpy

#establish workspace
arcpy.env.workspace = r"C:\Data\Models\TModel1.gdb\Boundaries"

#declare variables
infc = "Oregon_CityLimits"
clipfc = "WV_Ecoregion"
outfc = "WV_Cities"

#execute clip method with 4 arguments
arcpy.Clip_analysis(infc, clipfc, outfc, .001)

#notify copletion of procedure
print "Clip is completed."
