import PyPDF2
def mergePDF(filenames,outputFileName):
    openedFiles = []
    for name in filenames:
        try:
            open_file = open(name,"rb")
            openedFiles.append(open_file)
        except:
            return False
    filereaders = []

    for file in openedFiles:
        reader = PyPDF2.PdfFileReader(file)
        filereaders.append(reader)

    writer = PyPDF2.PdfFileWriter()

    for r in filereaders:
        for pageNum in range(r.numPages):
            pageObj = r.getPage(pageNum)
            writer.addPage(pageObj)

    outfile = open(outputFileName,'wb')
    writer.write(outfile)
    outfile.close()

    for file in openedFiles:
        file.close()
    return True

#TO DO