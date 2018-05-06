import arcpy
pdfpath = "F:\MarshallJ_EPA_SEEPosition\SEE_PugetSound\USACOAssist\HelpforKristina\HelpforKristina\CorpsRGP6\Maps\PS_MapBook.pdf"
pdfdoc = arcpy.mapping.PDFDocumentCreate(pdfpath)
pdfdoc.appendPages("F:\MarshallJ_EPA_SEEPosition\SEE_PugetSound\USACOAssist\HelpforKristina\HelpforKristina\CorpsRGP6\Maps\Deschutes.pdf")
pdfdoc.appendPages("F:\MarshallJ_EPA_SEEPosition\SEE_PugetSound\USACOAssist\HelpforKristina\HelpforKristina\CorpsRGP6\Maps\Duwamish.pdf")
pdfdoc.appendPages("F:\MarshallJ_EPA_SEEPosition\SEE_PugetSound\USACOAssist\HelpforKristina\HelpforKristina\CorpsRGP6\Maps\ElwhaChimacum.pdf")
pdfdoc.appendPages("F:\MarshallJ_EPA_SEEPosition\SEE_PugetSound\USACOAssist\HelpforKristina\HelpforKristina\CorpsRGP6\Maps\NisquallyChambers.pdf")
pdfdoc.appendPages("F:\MarshallJ_EPA_SEEPosition\SEE_PugetSound\USACOAssist\HelpforKristina\HelpforKristina\CorpsRGP6\Maps\Nooksack.pdf")
pdfdoc.appendPages("F:\MarshallJ_EPA_SEEPosition\SEE_PugetSound\USACOAssist\HelpforKristina\HelpforKristina\CorpsRGP6\Maps\NorthHoodCanal.pdf")
pdfdoc.appendPages("F:\MarshallJ_EPA_SEEPosition\SEE_PugetSound\USACOAssist\HelpforKristina\HelpforKristina\CorpsRGP6\Maps\SouthHoodCanal2.pdf")
pdfdoc.appendPages("F:\MarshallJ_EPA_SEEPosition\SEE_PugetSound\USACOAssist\HelpforKristina\HelpforKristina\CorpsRGP6\Maps\Puyallup.pdf")
pdfdoc.appendPages("F:\MarshallJ_EPA_SEEPosition\SEE_PugetSound\USACOAssist\HelpforKristina\HelpforKristina\CorpsRGP6\Maps\SalmonDuwamish.pdf")
pdfdoc.appendPages("F:\MarshallJ_EPA_SEEPosition\SEE_PugetSound\USACOAssist\HelpforKristina\HelpforKristina\CorpsRGP6\Maps\Skagit.pdf")
pdfdoc.appendPages("F:\MarshallJ_EPA_SEEPosition\SEE_PugetSound\USACOAssist\HelpforKristina\HelpforKristina\CorpsRGP6\Maps\Snohomish.pdf")
pdfdoc.saveAndClose()
del pdfdoc

