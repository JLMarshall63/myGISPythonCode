# Directions: You should already have gone through the instructions to make your data driven pages
# and you should have your Title and Overview pages ready as well.

# Write Python script to export selected map pages of your map to a PDF file and
# create a new PDF that includes the Title, Overview, and your exported pages.

# import arcpy and set up your workspace and environments


# create an arcpy.mapping.MapDocument using your mxd


# Export your Data Driven Pages to a PDF file
# provide the path and file name of the PDF so thath all pages will be exported
# If you want to just export certain pages, you must specify page number or page
# number range(s) if only selected pages will be exported


# create a fresh pdf document that will hold all of your pages

#use PDFDocumentCreate function's updateDocProperties method to update the mapbook title and authorship

#this is IMPORTANT - the changes made to the mapbook won't be saved if the script is closed before executing saveAndClose()

import arcpy
pdfpath = "C:\Workspace\Data\NorthSeattle\North_Seattle_MapBook.pdf"

# use PDFDocumentCreate(pdf_path) function
pdfdoc = arcpy.mapping.PDFDocumentCreate(pdfpath)

# append the title page, the index pages, and the map pages to the PDF map book in that order
# assume the title page and index page are already created as PDF documents
# use PDFDocumentCreate function's appendPages method 3 times, one for title, one for overview, one for your exported pages

pdfdoc.appendPages("C:\Workspace\Data\NorthSeattle\TOC.pdf")
pdfdoc.appendPages("C:\Workspace\Data\NorthSeattle\IndexMap.pdf")
pdfdoc.appendPages("C:\Workspace\Data\NorthSeattle\MarshallJ_Assignment4_MapBook.pdf")

#save and close the mapbook
pdfdoc.saveAndClose()

#delete reference to mapBookPDF
del pdfdoc





