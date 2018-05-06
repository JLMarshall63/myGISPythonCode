import arcpy
arcpy.env.workspace = r'C:\EsriPress\Python\Data\Exercise05\Facilities.gdb'
arcpy.ListFeatureClasses()
fcs = arcpy.ListFeatureClasses()
fcs[0]
fcs[0:3]
fcs.reverse()
fcs
fcs.remove("zip")
fcs
for fc in fcs:
    arcpy.Clip_analysis(fc, "zip", fc + "_clip")
    

