Fields:

SizeClass

Pre-Logic Script Code:

def Reclass(x):
  if x <= 20000: 
    return 1
  elif x > 20000 and  x <= 40000:
    return 2
  elif x > 40000 and  x <= 80000:
    return 3
  elif x > 80000 and  x <= 100000:
    return 4
  else:
     return 5
	 SizeClass =
	 Reclass(!AreaAcres!)