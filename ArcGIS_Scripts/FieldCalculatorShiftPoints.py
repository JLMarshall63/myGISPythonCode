Parser - Python
Type: Number

Field: Shape

PreLogic Script Code:

def shiftXCoord(shape):
  point = shape.getPart(0)
  point.X  point.X + 5000
  return point
  
Shape =

shiftXCoord(!Shape!)  