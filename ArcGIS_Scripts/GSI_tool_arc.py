import arcpy
import sys
arcpy.env.overwriteOutput = True
from os.path import join

# it is very helpful for students if the fields are in a logical order
# this will yeild a new mapping based on an existing table and a
# list of the fields in order of appearance.
def orderly_table(tablelist, out_table, field_order, add_missing):
    """ 
    Reorders fields in input featureclass/table
    :table:         input table (fc, table, layer, etc)
    :out_table:     output table (fc, table, layer, etc)
    :field_order:   order of fields (objectid, shape not necessary)
    :add_missing:   add missing fields to end if True (leave out if False)
    -> path to output table
    """
    table=tablelist[0]
    existing_fields = arcpy.ListFields(table)
    existing_field_names = [field.name for field in existing_fields]
    existing_mapping = arcpy.FieldMappings()
    existing_mapping.addTable(table)
    new_mapping = arcpy.FieldMappings()
    def add_mapping(field_name):
        mapping_index = existing_mapping.findFieldMapIndex(field_name)
        # required fields (OBJECTID, etc) will not be in existing mappings
        # they are added automatically
        if mapping_index != -1:
            field_map = existing_mapping.fieldMappings[mapping_index]
            new_mapping.addFieldMap(field_map)
    # add user fields from field_order
    for field_name in field_order:
        #if field_name not in existing_field_names:
        #    pass #raise Exception("Field: {0} not in {1}".format(field_name, table))
        #else:
        #    add_mapping(field_name)
        add_mapping(field_name)
    # add missing fields at end
    #if add_missing:
    #    missing_fields = [f for f in existing_field_names if f not in field_order]
    #    for field_name in missing_fields:
    #        add_mapping(field_name)
    # use merge with single input just to use new field_mappings
    arcpy.Merge_management(tablelist, out_table, new_mapping)
    #return out_table

#output geodatabase workspace
workgdb=arcpy.GetParameterAsText(0)
arcpy.env.workspace=workgdb
msg = "Workspace:   " + workgdb
arcpy.AddMessage(msg)
# input AU layer from the TOC - supports selected records
AU_fn=arcpy.GetParameterAsText(1)
# text file with coded filenames to process
lf_fn=arcpy.GetParameterAsText(2)
lf=open(lf_fn,"r")
lines=lf.readlines()
out_str_list = []
for aline in lines:
    out_str_list.append(aline.strip().replace("\n","").replace("\t",""))
lf.close()
arcpy.AddMessage("Scenarios to process: ")
for out_str in out_str_list:
    msg = "  "+out_str
    arcpy.AddMessage(msg)
arcpy.AddMessage(" ")

lyr_fn=arcpy.GetParameterAsText(3)

#loop to process input filenames
merge_inputs = []  #ready a list to remember the summary stats tables for merging at the end

for out_fn in out_str_list:
    merge_scenarios = []
##    with arcpy.da.SearchCurosr(AU_fn, ["wf_acres", "wq_acres"]) as cursor:
##        for row in cursor:
##            if row != (None, None):
##                out_fn = "manual_" + out_fn
##                break
    field_order = ['AU_ID', 'WF_order', 'WQ_order', 'wf_acres', 'wq_acres', 'Sum_riv_ac', 'Sum_wet_ac', 'FD_cs', 'FW_cs', 'QD_cs', 'QW_cs', 'FD_caa', 'FW_caa', 'QD_caa', 'QW_caa', 'wet_F_esv', 'riv_F_esv', 'wet_Q_esv', 'riv_Q_esv', 'AU_ESV', 'FD_esv_net', 'FW_esv_net', 'QD_esv_net', 'QW_esv_net', 'AU_ESV_net', 'GSI_cost', 'AU_TPR', 'AU_cost_balance', 'AU_esv_net_roi']
    #field_order = ["AU_ID","WF_order","WQ_order","wf_acres","wq_acres","Sum_riv_ac","Sum_wet_ac","FD_cs","FW_cs","QD_cs","QW_cs","FD_caa","FW_caa","QD_caa","QW_caa","wet_F_esv","riv_F_esv","wet_Q_esv","riv_Q_esv","AU_esv","AU_TPR","FD_esv_net","FW_esv_net","QD_esv_net","QW_esv_net","AU_esv_net","GSI_cost","AU_esv_net_roi"]
    orderly_table([AU_fn], out_fn, field_order, True)
    fclist = arcpy.ListFeatureClasses()

    #the file name from the text file isn't recognized by arcpy but python sees them as equal strings.  Maybe it's an ascii thing.
    out_fn = fclist[fclist.index(out_fn)]
    msg = "Scenario " + " " * (20 - len("Scenario ")) + out_fn
    arcpy.AddMessage(msg)

    # >>>>>>>>>>>>>>>>  BEGIN CALCULATION OF FIELD VALUES FOR THIS SCENARIO FEATURE CLASS

    #get parameters and calculate intervention area
    ### dryland
    ### to bypass calculation of x_area or y_area do not include the X and/or Y values in the file name
    try:
        F_pct=float("0."+out_fn.split("f")[1].split("q")[0])
        if "manual" in out_fn:
            expression = "(!wf_acres! if !wf_acres! <= !shape.area@acres! else !shape.area@acres!) if !wf_acres! is not None else (!shape.area@acres! * "+str(F_pct)+")"
            F_pct = "manual (or {0})".format(F_pct)
        else:
            expression = "!shape.area@acres! * "+str(F_pct)
        arcpy.CalculateField_management(out_fn, "wf_acres", expression,"PYTHON_9.3")
    except:
        if "manual" in out_fn:
            F_pct = "manual"
            expression = "(!wf_acres! if !wf_acres! <= !shape.area@acres! else !shape.area@acres!) if !wf_acres! is not None else 0.0"
        else:
            F_pct=float("0.0")
            expression = str(F_pct)
        arcpy.CalculateField_management(out_fn, "wf_acres", expression,"PYTHON_9.3")
    ### wetland
    try:
        Q_pct=float("0."+out_fn.split("q")[1])
        # Calculate dryland acres
        if "manual" in out_fn:
            expression = "(!wq_acres! if !wq_acres! <= !shape.area@acres! else !shape.area@acres!) if !wq_acres! is not None else (!shape.area@acres! * "+str(Q_pct)+")"
            Q_pct = "manual (or {0})".format(Q_pct)
        else:
            expression = "!shape.area@acres! * "+str(Q_pct)
        arcpy.CalculateField_management(out_fn, "wq_acres", expression,"PYTHON_9.3")
    except:
        if "manual" in out_fn:
            Q_pct = "manual"
            expression = "(!wq_acres! if !wq_acres! <= !shape.area@acres! else !shape.area@acres!) if !wq_acres! is not None else 0.0"
        else:
            Q_pct=float("0.0")
            expression = str(Q_pct)
        arcpy.CalculateField_management(out_fn, "wq_acres", expression,"PYTHON_9.3")
        
    ##decide which functions and land type combinations the user wants
    FIT_str_list=["FD","FW","QD","QW"]
    FIT_list=[]
    fields=[]  # the fields that will be summed to get GSI_cost
    for FIT_str in FIT_str_list:
        if FIT_str in out_fn:
            FIT_list.append(FIT_str)
    GSI_eq="!"
    for f in FIT_list:
        GSI_eq=GSI_eq + f + "_cs! + !"
    GSI_eq = GSI_eq[:-4]

    for msg in ["wf_acres percent: "+" " * (20 - len("wf_acres percent: "))+str(F_pct), "wq_acres percent: "+" " * (20 - len("wq_acres percent: ")) + str(Q_pct),"FITs evaluated: "+" " * (20 - len("FITs evaluated: ")) + str(FIT_list).replace("[","").replace("]","").replace("'","")]:
        arcpy.AddMessage(msg)

    #zero out the fields that will be calculated so there are no <Null> values when complete
    #for f in ["QD_cs","QW_cs","FD_cs","FW_cs","FD_esv_net","FW_esv_net","QD_esv_net","QW_esv_net","riv_F_esv","wet_F_esv","riv_Q_esv","wet_Q_esv","AU_esv","AU_esv_net","GSI_cost"]:
    #    arcpy.CalculateField_management(out_fn, f, "0","PYTHON_9.3")

    # COST SCHEDULE
    if "FD" in out_fn:
        expression = "!wf_acres! * !FD_caa!"
        arcpy.CalculateField_management(out_fn, "FD_cs", expression,"PYTHON_9.3")    
    if "QD" in out_fn:
        expression = "!wq_acres! * !QD_caa!"
        arcpy.CalculateField_management(out_fn, "QD_cs", expression,"PYTHON_9.3")
    if "FW" in out_fn:
        expression = "!wf_acres! * !FW_caa!"
        arcpy.CalculateField_management(out_fn, "FW_cs", expression,"PYTHON_9.3")
    if "QW" in out_fn:
        expression = "!wq_acres! * !QW_caa!"
        arcpy.CalculateField_management(out_fn, "QW_cs", expression,"PYTHON_9.3")
    #Calculate GSI cost schedule sum
    expression = "!FD_cs! + !FW_cs! + !QD_cs! + !QW_cs!"
    arcpy.CalculateField_management(out_fn, "GSI_cost", expression,"PYTHON_9.3")

    #ECOLOGICAL SERVICES VALUE (esv) FOR RIVERS AND WETLANDS ALREADY ON THE LANDSCAPE
    expression = "!Sum_riv_ac! * (7000.0 + (21000.0 * (!WF_order! - 1.0) / 15.0))"
    arcpy.CalculateField_management(out_fn, "riv_F_esv", expression,"PYTHON_9.3")
    expression = "!Sum_riv_ac! * (7000.0 + (21000.0 * (!WQ_order! - 1.0) / 15.0))"
    arcpy.CalculateField_management(out_fn, "riv_Q_esv", expression,"PYTHON_9.3")
    expression = "!Sum_wet_ac! * (600.0 + (82400.0 *  ((!WF_order! - 1.0) / 15.0)))"
    arcpy.CalculateField_management(out_fn, "wet_F_esv", expression,"PYTHON_9.3")
    expression = "!Sum_wet_ac! * (600.0 + (82400.0 *  ((!WQ_order! - 1.0) / 15.0)))"
    arcpy.CalculateField_management(out_fn, "wet_Q_esv", expression,"PYTHON_9.3")
    #Calculate existing AU_esv
    expression = "!riv_F_esv! + !riv_Q_esv! + !wet_F_esv! + !wet_Q_esv!"
    arcpy.CalculateField_management(out_fn, "AU_esv", expression,"PYTHON_9.3")

    #CALCULATE esv net depending on the user choices for function/type intervention
    codeblock = """def esv_net(FIT,order,acres):
        MAGNITUDE=2
        YEARS=7.0
        if FIT == "FD" or FIT == "QD":
            v1=float(7000)
            v2=float(21000)
            if order + MAGNITUDE > 16:
                magnitude = 16 - order
            else:
                magnitude = MAGNITUDE
            return YEARS * ((acres * ((v1 + (v2 * (order + magnitude - 1) / 15.0)))) - (acres * ((v1 + (v2 * (order - 1) / 15.0)))))
        else:
            v1=float(600)
            v2=float(82400)
            if order + MAGNITUDE > 16:
                magnitude = 16 - order
            else:
                magnitude = MAGNITUDE
            return YEARS * ((acres * ((v1 + (v2 * ((order + magnitude) - 1) / 15.0)))) - (acres * ((v1 + (v2 * (order - 1) / 15.0)))))"""
    if "FD" in out_fn:
        expression = "esv_net('FD',!WF_order!,!wf_acres!)"
        arcpy.CalculateField_management(out_fn, "FD_esv_net", expression,"PYTHON_9.3",codeblock)
    if "QD" in out_fn:
        expression = "esv_net('QD',!WQ_order!,!wq_acres!)"
        arcpy.CalculateField_management(out_fn, "QD_esv_net", expression,"PYTHON_9.3",codeblock)
    if "FW" in out_fn:
        expression = "esv_net('FW',!WF_order!,!wf_acres!)"
        arcpy.CalculateField_management(out_fn, "FW_esv_net", expression,"PYTHON_9.3",codeblock)
    if "QW" in out_fn:
        expression = "esv_net('QW',!WQ_order!,!wq_acres!)"
        arcpy.CalculateField_management(out_fn, "QW_esv_net", expression,"PYTHON_9.3",codeblock)

    # ES Value by analytic and synthetic perspective
    expression = "!FD_esv_net! + !FW_esv_net! + !QD_esv_net! + !QW_esv_net!"
    arcpy.CalculateField_management(out_fn, "AU_esv_net", expression,"PYTHON_9.3")
    expression = "!AU_esv_net! / !GSI_cost!"
    arcpy.CalculateField_management(out_fn, "AU_esv_net_roi", expression,"PYTHON_9.3")
    expression = "!AU_TPR! - !GSI_cost!"
    arcpy.CalculateField_management(out_fn, "AU_cost_balance", expression,"PYTHON_9.3")

    # >>>>>>>>>>>>>  FINISHED FEATURE CLASS SCENARIO CALCULATIONS


    # <<<<<<<<<<< BEGIN CALCULATION OF FIT SUMMARY TABLES
    """    
    try:
        arcpy.Delete_management("temp_table")
    except:
        pass
    # Create list of table statistics to include in summary table
    if "FD" in out_fn:
        statsFields=[["wf_acres", "SUM"],["FD_cs", "SUM"],["FD_esv_net","SUM"]]
        arcpy.Statistics_analysis(out_fn, "temp_table", statsFields,"WF_order")
        arcpy.AddField_management("temp_table", "scenario", "TEXT")
        arcpy.AddField_management("temp_table", "FIT", "TEXT")
        arcpy.AddField_management("temp_table", "GSI_cost", "DOUBLE")
        arcpy.AddField_management("temp_table", "AU_esv_net","DOUBLE")
        arcpy.AddField_management("temp_table", "AU_esv_net_roi","DOUBLE")
        arcpy.CalculateField_management("temp_table", "scenario", '"'+out_fn+'"',"PYTHON_9.3")
        arcpy.CalculateField_management("temp_table", "FIT", '"FD"',"PYTHON_9.3")
        arcpy.CalculateField_management("temp_table", "GSI_cost", '!SUM_FD_cs!',"PYTHON_9.3")
        arcpy.CalculateField_management("temp_table", "AU_esv_net", '!SUM_FD_esv_net!',"PYTHON_9.3")
        arcpy.CalculateField_management("temp_table", "AU_esv_net_roi", '!AU_esv_net! - !GSI_cost!',"PYTHON_9.3")
        for fld in ["SUM_FW_cs","SUM_QW_cs","SUM_QD_cs"]:
            arcpy.AddField_management("temp_table", fld, "DOUBLE")
            arcpy.CalculateField_management("temp_table", fld, "0","PYTHON_9.3")
        for fld in ["SUM_FW_esv_net","SUM_QD_esv_net","SUM_QW_esv_net"]:
            arcpy.AddField_management("temp_table", fld, "DOUBLE")
            arcpy.CalculateField_management("temp_table", fld, "0","PYTHON_9.3")
        # remap fields and write final table
        field_order = ["scenario","function","intervention","WF_order","WQ_order","SUM_wf_acres","SUM_wq_acres","SUM_FD_cs","SUM_FW_cs","SUM_QD_cs","SUM_QW_cs","SUM_FD_esv_net","SUM_FW_esv_net","SUM_QD_esv_net","SUM_QW_esv_net","GSI_cost","AU_esv_net","AU_esv_net_roi"]
        orderly_table(["temp_table"], out_fn+"_FD", field_order, True)
        merge_scenarios.append(out_fn+"_FD")

    if "FW" in out_fn:
        try:
            arcpy.Delete_management("temp_table")
        except:
            pass
        statsFields=[["wf_acres", "SUM"],["FW_cs", "SUM"],["FW_esv_net","SUM"]]
        arcpy.Statistics_analysis(out_fn, "temp_table", statsFields, "WF_order")
        arcpy.AddField_management("temp_table", "scenario", "TEXT")
        arcpy.AddField_management("temp_table", "FIT", "TEXT")
        arcpy.AddField_management("temp_table", "GSI_cost", "DOUBLE")
        arcpy.AddField_management("temp_table", "AU_esv_net","DOUBLE")
        arcpy.AddField_management("temp_table", "AU_esv_net_roi","DOUBLE")
        arcpy.CalculateField_management("temp_table", "scenario", '"'+out_fn+'"',"PYTHON_9.3")
        arcpy.CalculateField_management("temp_table", "FIT", '"FW"',"PYTHON_9.3")
        arcpy.CalculateField_management("temp_table", "GSI_cost", '!SUM_FW_cs!',"PYTHON_9.3")
        arcpy.CalculateField_management("temp_table", "AU_esv_net", '!SUM_FW_esv_net!',"PYTHON_9.3")
        arcpy.CalculateField_management("temp_table", "AU_esv_net_roi", '!AU_esv_net! - !GSI_cost!',"PYTHON_9.3")
        for fld in ["SUM_FD_cs","SUM_QW_cs","SUM_QD_cs"]:
            arcpy.AddField_management("temp_table", fld, "DOUBLE")
        for fld in ["SUM_FD_esv_net","SUM_QD_esv_net","SUM_QW_esv_net"]:
            arcpy.AddField_management("temp_table", fld, "DOUBLE")
            arcpy.CalculateField_management("temp_table", fld, "0","PYTHON_9.3")
        field_order = ["scenario","function","intervention","WF_order","WQ_order","SUM_wf_acres","SUM_wq_acres","SUM_FD_cs","SUM_FW_cs","SUM_QD_cs","SUM_QW_cs","SUM_FD_esv_net","SUM_FW_esv_net","SUM_QD_esv_net","SUM_QW_esv_net","GSI_cost","AU_esv_net","AU_esv_net_roi"]
        orderly_table(["temp_table"], out_fn+"_FW", field_order, True)
        merge_scenarios.append(out_fn+"_FW")
       
    if "QD" in out_fn:
        try:
            arcpy.Delete_management("temp_table")
        except:
            pass
        statsFields=[["wq_acres", "SUM"],["QD_cs", "SUM"],["QD_esv_net","SUM"]]
        arcpy.Statistics_analysis(out_fn, "temp_table", statsFields, "WQ_order")
        arcpy.AddField_management("temp_table", "scenario", "TEXT")
        arcpy.AddField_management("temp_table", "FIT", "TEXT")
        arcpy.AddField_management("temp_table", "GSI_cost", "DOUBLE")
        arcpy.AddField_management("temp_table", "AU_esv_net","DOUBLE")
        arcpy.AddField_management("temp_table", "AU_esv_net_roi","DOUBLE")
        arcpy.CalculateField_management("temp_table", "scenario", '"'+out_fn+'"',"PYTHON_9.3")
        arcpy.CalculateField_management("temp_table", "FIT", '"QD"',"PYTHON_9.3")
        arcpy.CalculateField_management("temp_table", "GSI_cost", '!SUM_QD_cs!',"PYTHON_9.3")
        arcpy.CalculateField_management("temp_table", "AU_esv_net", '!SUM_QD_esv_net!',"PYTHON_9.3")
        arcpy.CalculateField_management("temp_table", "AU_esv_net_roi", '!AU_esv_net! - !GSI_cost!',"PYTHON_9.3")
        for fld in ["SUM_FD_cs","SUM_QW_cs","SUM_FW_cs"]:
            arcpy.AddField_management("temp_table", fld, "DOUBLE")
        for fld in ["SUM_FD_esv_net","SUM_FW_esv_net","SUM_QW_esv_net"]:
            arcpy.AddField_management("temp_table", fld, "DOUBLE")
            arcpy.CalculateField_management("temp_table", fld, "0","PYTHON_9.3")
        field_order = ["scenario","function","intervention","WF_order","WQ_order","SUM_wf_acres","SUM_wq_acres","SUM_FD_cs","SUM_FW_cs","SUM_QD_cs","SUM_QW_cs","SUM_FD_esv_net","SUM_FW_esv_net","SUM_QD_esv_net","SUM_QW_esv_net","GSI_cost","AU_esv_net","AU_esv_net_roi"]
        orderly_table(["temp_table"], out_fn+"_QD", field_order, True)
        merge_scenarios.append(out_fn+"_QD")

    if "QW" in out_fn:
        try:
            arcpy.Delete_management("temp_table")
        except:
            pass
        statsFields=[["wq_acres", "SUM"],["QW_cs", "SUM"],["QW_esv_net","SUM"]]
        arcpy.Statistics_analysis(out_fn, "temp_table", statsFields, "WQ_order")
        arcpy.AddField_management("temp_table", "scenario", "TEXT")
        arcpy.AddField_management("temp_table", "FIT", "TEXT")
        arcpy.AddField_management("temp_table", "GSI_cost", "DOUBLE")
        arcpy.AddField_management("temp_table", "AU_esv_net","DOUBLE")
        arcpy.AddField_management("temp_table", "AU_esv_net_roi","DOUBLE")
        arcpy.CalculateField_management("temp_table", "scenario", '"'+out_fn+'"',"PYTHON_9.3")
        arcpy.CalculateField_management("temp_table", "FIT", '"QW"',"PYTHON_9.3")
        arcpy.CalculateField_management("temp_table", "GSI_cost", '!SUM_QW_cs!',"PYTHON_9.3")
        arcpy.CalculateField_management("temp_table", "AU_esv_net", '!SUM_QW_esv_net!',"PYTHON_9.3")
        arcpy.CalculateField_management("temp_table", "AU_esv_net_roi", '!AU_esv_net! - !GSI_cost!',"PYTHON_9.3")
        for fld in ["SUM_FD_cs","SUM_FW_cs","SUM_QD_cs"]:
            arcpy.AddField_management("temp_table", fld, "DOUBLE")
        for fld in ["SUM_FD_esv_net","SUM_FW_esv_net","SUM_QD_esv_net"]:
            arcpy.AddField_management("temp_table", fld, "DOUBLE")
            arcpy.CalculateField_management("temp_table", fld, "0","PYTHON_9.3")
        field_order = ["scenario","function","intervention","WF_order","WQ_order","SUM_wf_acres","SUM_wq_acres","SUM_FD_cs","SUM_FW_cs","SUM_QD_cs","SUM_QW_cs","SUM_FD_esv_net","SUM_FW_esv_net","SUM_QD_esv_net","SUM_QW_esv_net","GSI_cost","AU_esv_net","AU_esv_net_roi"]
        orderly_table(["temp_table"], out_fn+"_QW", field_order, True)
        merge_scenarios.append(out_fn+"_QW")
        
    try:
        arcpy.Delete_management("temp_table")
    except:
        pass

    #merge the scenarios
    field_order = ["scenario","function","intervention","WF_order","WQ_order","SUM_wf_acres","SUM_wq_acres","SUM_FD_cs","SUM_FW_cs","SUM_QD_cs","SUM_QW_cs","SUM_FD_esv_net","SUM_FW_esv_net","SUM_QD_esv_net","SUM_QW_esv_net","GSI_cost","AU_esv_net","AU_esv_net_roi"]
    orderly_table(merge_scenarios, "temp_table_2", field_order, True)
    orderly_table(["temp_table_2"], out_fn+"_merge", field_order, True)

    """

    #make the statistics table
    statsFields=[["wf_acres","SUM"],["wq_acres","SUM"],["FD_cs","SUM"],["FW_cs","SUM"],["QD_cs","SUM"],["QW_cs","SUM"],["FD_esv_net","SUM"],["FW_esv_net","SUM"],["QD_esv_net","SUM"],["QW_esv_net","SUM"],["AU_esv","SUM"],["AU_esv_net","SUM"],["GSI_cost", "SUM"],["AU_TPR","SUM"],["AU_cost_balance","SUM"],["AU_esv_net_roi","SUM"]]
    arcpy.Statistics_analysis(out_fn, out_fn+"_stats", statsFields)
    arcpy.AddField_management(out_fn+"_stats", "scenario", "TEXT")
    arcpy.CalculateField_management(out_fn+"_stats", "scenario", '"'+out_fn+'"',"PYTHON_9.3")

    #report the results to the tool message dialog
    cursor = arcpy.SearchCursor(out_fn+"_stats")
    for row in cursor:
        for f in arcpy.ListFields(out_fn+"_stats")[2:-1]:
            msg=f.name+" " * (20 - len(f.name)) + str(row.getValue(f.name))
            arcpy.AddMessage(msg)
    arcpy.AddMessage("   ")

    #add to the table of contents
    if lyr_fn:
        arcpy.MakeFeatureLayer_management(out_fn, out_fn)
        MXD = arcpy.mapping.MapDocument("CURRENT")
        DF = arcpy.mapping.ListDataFrames(MXD)[0]
        lyr = arcpy.mapping.Layer(out_fn)
        arcpy.ApplySymbologyFromLayer_management (lyr, lyr_fn)
        lyr.symbology.numClasses = 10
        lyr.symbology.reclassify()
        arcpy.mapping.AddLayer(DF, lyr, "AUTO_ARRANGE")

    # remember the stats table's name
    merge_inputs.append(out_fn+"_stats")
    
#merge the stats tables and delete them
##field_order = ["scenario", "FREQUENCY", "SUM_AU_cost_balance", "SUM_AU_esv_net_roi", "SUM_AU_TPR", "SUM_GSI_cost", "SUM_AU_ESV_net", "SUM_wf_acres", "SUM_wq_acres", "SUM_FD_cs", "SUM_FW_cs", "SUM_QD_cs", "SUM_QW_cs", "SUM_FD_esv_net", "SUM_FW_esv_net", "SUM_QD_esv_net", "SUM_QW_esv_net", "SUM_AU_ESV",]
##orderly_table(merge_inputs, "GSI_cost_summary", field_order, True)
arcpy.Merge_management(merge_inputs, "GSI_cost_summary")
for table in merge_inputs:
    arcpy.Delete_management(table)
