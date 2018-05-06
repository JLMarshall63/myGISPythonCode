arcpy.env.workspace = r'D:\University of Washington GIS\UOFWWinter2018\Geog564\PythonTests\myPythonTests12.gdb'
outpath = arcpy.env.workspace
arcpy.CreateTable_management(outpath, "mytest_table1")
arcpy.AddField_management("mytest_table1", "ID","SHORT")
arcpy.AddField_management("mytest_table1", "DateTime","DATE")
arcpy.AddField_management("mytest_table1", "Value","DOUBLE")
arcpy.CreateTable_management(outpath,"mytest_table2","mytest_table1" )
editrows = arcpy.da.InsertCursor("mytest_table2", ["ID"])
row = [100]
editrows.fields
editrows.insertRow(row)
for table_ID in range(101,120):
    row = [table_ID]
    editrows.insertRow(row)
    
del editrows

