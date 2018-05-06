>>> arcpy.env.workspace = r'D:\University of Washington GIS\UOFWWinter2018\Geog564\PythonTests\myPythonTests12.gdb'
>>> outpath = arcpy.env.workspace
>>> arcpy.CreateTable_management(outpath, "mytest_table1")
<Result 'D:\\University of Washington GIS\\UOFWWinter2018\\Geog564\\PythonTests\\myPythonTests12.gdb\\mytest_table1'>
>>> arcpy.AddField_management("mytest_table1", "ID","SHORT")
<Result 'mytest_table1'>
>>> arcpy.AddField_management("mytest_table1", "DateTime","DATE")
<Result 'mytest_table1'>
>>> arcpy.AddField_management("mytest_table1", "Value","DOUBLE")
<Result 'mytest_table1'>
>>> arcpy.CreateTable_management(outpath,"mytest_table2","mytest_table1" )
<Result 'D:\\University of Washington GIS\\UOFWWinter2018\\Geog564\\PythonTests\\myPythonTests12.gdb\\mytest_table2'>
>>> editrows = arcpy.da.InsertCursor("mytest_table2", ["ID"])
>>> row = [100]
>>> editrows.fields
(u'ID',)
>>> editrows.insertRow(row)
1L
>>> for table_ID in range(101,120):
...     row = [table_ID]
...     editrows.insertRow(row)
...     
>>> del editrows
>>> editrows = arcpy.da.InsertCursor("mytest_table1", "*")
>>> editrows.fields
(u'OBJECTID', u'ID', u'DateTime', u'Value')
>>> OID = 1
>>> for i in range(1,21):
...     OID = i
...     ID = i + 100
...     Value = i + 3.33
...     str_date = '3/18/2018' + str(int(Value)) + ':00:00 PM'
...     row = [OID,ID,str_date,Value]
...     print row
...     
[1, 101, '3/18/20184:00:00 PM', 4.33]
[2, 102, '3/18/20185:00:00 PM', 5.33]
[3, 103, '3/18/20186:00:00 PM', 6.33]
[4, 104, '3/18/20187:00:00 PM', 7.33]
[5, 105, '3/18/20188:00:00 PM', 8.33]
[6, 106, '3/18/20189:00:00 PM', 9.33]
[7, 107, '3/18/201810:00:00 PM', 10.33]
[8, 108, '3/18/201811:00:00 PM', 11.33]
[9, 109, '3/18/201812:00:00 PM', 12.33]
[10, 110, '3/18/201813:00:00 PM', 13.33]
[11, 111, '3/18/201814:00:00 PM', 14.33]
[12, 112, '3/18/201815:00:00 PM', 15.33]
[13, 113, '3/18/201816:00:00 PM', 16.33]
[14, 114, '3/18/201817:00:00 PM', 17.33]
[15, 115, '3/18/201818:00:00 PM', 18.33]
[16, 116, '3/18/201819:00:00 PM', 19.33]
[17, 117, '3/18/201820:00:00 PM', 20.33]
[18, 118, '3/18/201821:00:00 PM', 21.33]
[19, 119, '3/18/201822:00:00 PM', 22.33]
[20, 120, '3/18/201823:00:00 PM', 23.33]
>>> del editrows
>>> editrows = arcpy.da.InsertCursor("mytest_table1", "*")
>>> editrows.fields
(u'OBJECTID', u'ID', u'DateTime', u'Value')
>>> for i in range(1,21):
...     OID = i
...     ID = i + 100
...     Value = i + 3.33
...     str_date = '3/18/2018' + str(int(Value)) + ':00:00 PM'
...     row = [OID,ID,str_date,Value]
...     editrows.insertRow(row)
...     
Runtime error 
Traceback (most recent call last):
  File "<string>", line 7, in <module>
RuntimeError: The value type is incompatible with the field type. [DateTime]
>>> del editrows
>>> 