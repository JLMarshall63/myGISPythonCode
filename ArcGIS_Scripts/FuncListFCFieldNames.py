import arcpy

def listfieldnames(table):
    fields = arcpy.ListFields(table)
    namelist = []
    for field in fields:
        namelist.append(field.name)
    print namelist
    return namelist

fn = listfieldnames(r"C:\EsriPress\Python\Data\Exercise07\roads.shp")

##fields = arcpy.ListFields("C:\\EsriPress\\Python\\Data\\Exercise07\\roads.shp")
##namelist = []
##for field in fields:
##    namelist.append(field.name)
##print namelist
    