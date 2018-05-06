import pandas, os
import sys
import geopy
df1=pandas.read_csv("C:\\Python27\\ArcGIS10.4\\Scripts\\supermarkets.csv")
print(df1)
print (dir(geopy))
from geopy.geocoders import Nominatim
nom=Nominatim()
n=nom.geocode("3995 23rd St, San Francisco, CA 94114")
print(n.latitude)
print(n.longitude)

import pandas
df=pandas.read_csv("C:\\Python27\\ArcGIS10.4\\Scripts\\supermarkets.csv")
print(df)
df["Address"]=df["Address"] + ", " + df["State"] + ", " + df["Country"]
print(df)
df["Coordinates"]=df["Address"].apply(nom.geocode)

print(df.Coordinates[0].latitude)
print(df.Coordinates[0].longitude)

##print(df.Coordinates[1].latitude)
##print(df.Coordinates[1].longitude)

print(df.Coordinates[2].latitude)
print(df.Coordinates[2].longitude)

print(df.Coordinates[3].latitude)
print(df.Coordinates[3].longitude)

print(df.Coordinates[4].latitude)
print(df.Coordinates[4].longitude)

print(df.Coordinates[5].latitude)
print(df.Coordinates[5].longitude)

##print(df.Coordinates[6].latitude)
##print(df.Coordinates[6].longitude)

df["Latitude"]=df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df["Longitude"]=df["Coordinates"].apply(lambda x: x.longitude if x != None else None)
print(df)

