arcpy.env.workspace = r'D:\University of Washington GIS\UOFWWinter2018\Geog564\PythonTests\myPythonTests12.gdb'
path = arcpy.env.workspace
arcpy.CreateTable_management(path,"myTable1")
arcpy.AddField_management("myTable1","ID","SHORT")
arcpy.AddField_management("myTable1","DateTime","DATE")
arcpy.AddField_management("myTable1","Value","DOUBLE")
arcpy.CreateTable_management(path,"myTable2","myTable1")
editrows = arcpy.da.InsertCursor("myTable2",["ID"])
row = [100]
editrows.fields
editrows.insertRow(row)
for tblID in range(101,121):
    row = [tblID]
    editrows.insertRow(row)
    
del editrows
editrows = arcpy.da.InsertCursor("myTable1","*")
editrows.fields
OID = 1
for i in range(1,21):
    OID = i
    ID = i + 100
    Value = i + 3.33
    str_date = '3/18/2018' + str(int(Value)) + ':00:00 PM'
    row = [OID,ID,str_date,Value]
    print row
    
OID = 1
for i in range(1,21):
    OID = i
    ID = i + 100
    Value = i + 3.33
    str_date = '3/18/2018' + str(int(Value)) + ':00:00 PM'
    row = [OID,ID,str_date,Value]
    editrows.insertRow(row)
    
OID = 1
for i in range(1,21):
    OID = i
    ID = i + 100
    Value = i + 3.33
    str_date = '3/18/2018' + str(datetime(Value)) + ':00:00 PM'
    row = [OID,ID,str_date,Value]
    editrows.insertRow(row)
    
OID = 1
for i in range(1,21):
    OID = i
    ID = i + 100
    Value = i + 3.33
    str_date = '3/18/2018' + datetime(int(Value)) + ':00:00 PM'
    row = [OID,ID,str_date,Value]
    editrows.insertRow(row)
    
OID = 1
for i in range(1,21):
    OID = i
    ID = i + 100
    Value = i + 3.33
    str_date = '3/18/2018' + str_date(int(Value)) + ':00:00 PM'
    row = [OID,ID,str_date,Value]
    editrows.insertRow(row)
    
OID = 1
for i in range(1,21):
    OID = i
    ID = i + 100
    Value = i + 3.33
    str_date = '3/18/2018' + str(int(Value)) + ':00:00 PM'
    row = [OID,ID,str_date,Value]
    editrows.insertRow(row)
    
OID = 1
for i in range(1,21):
    OID = i
    ID = i + 100
    Value = i + 3.33
    str_date = '3/18/2018' + str_date(int(Value)) + ':00:00 PM'
    row = [OID,ID,str_date,Value]
    editrows.insertRow(row)
    
del editrows

