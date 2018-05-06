arcpy.env.workspace = "C:\EsriPress\Python\Data\Exercise06"
fclist = arcpy.ListFeatureClasses()
print fclist
fclist[0]
fclist[3]
fclist[-1]
fclist[1:3]
fclist[2:]

cities = ["Alameda","Brazos","Chimayo","Duice"]
len(cities)
del cities[2]
print cities
cities.sort(reverse = True)

print cities
cities.sort()

print cities
"Zuni" in cities
cities.append("Zuni")
"Zuni" in cities
print cities
cities.insert(0,"Espanola")
print cities

