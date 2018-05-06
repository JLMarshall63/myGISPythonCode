import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Calculate Geometry"
        self.alias = "geometry"

        # List of tool classes associated with this toolbox
        self.tools = [CalculateGeometry]


class CalculateGeometry(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Calculate Geometry"
        self.description = ""
        self.canRunInBackground = True

    def getParameterInfo(self):
       # First parameter
        in_features = arcpy.Parameter(
        displayName="Input Features",
        name="in_features",
        datatype="Feature Layer",
        parameterType="Required",
        direction="Input")
        in_features.filter.list = ["Point", "Line", "Polygon"]
        
        # Second parameter
        in_features = arcpy.Parameter(
        displayName="Field Name",
        name="field_name",
        datatype="Field",
        parameterType="Required",
        direction="Input")

         field.parameterDependencies = [in_features.name]
         field.filter.list = ["Short","Long","Double","Float","Text"]

         # Third parameter
          geomProperty = arcpy.Parameter(
        displayName="Property",
        name="geomProperty",
        dataType="String",
        parameterType="Required",
        direction="Input")

         # Fourth parameter
         units = arcpy.Parameter(
        displayName="Units",
        name="units",
        datatype="String",
        parameterType="Optional",
        direction="Input"
        enabled=False)

          # Fifth parameter
        out_features = arcpy.Parameter(
        displayName="Output Feature",
        name="out_features",
        datatype="Feature Layer",
        parameterType="Derived",
        direction="output")	

           out_features.parameterDependencies = [in_features.name]
           out_features.schema.clone = True

        params = [in_features, field, geomProperty, units, out_features]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        return