import arcpy
import os
import string
from arcpy import env
env.workspace = "C:\University of Washington GIS\UOWSummer2017\GEOG565\PythonScripts\ArcGIS_Scripts"
ws = env.workspace

pythonFiles = []

for x in os.listdir(ws):
    pythonFiles.append(x)   

for (num, fn) in enumerate(pythonFiles):
    print num + 1, fn

                                                    
