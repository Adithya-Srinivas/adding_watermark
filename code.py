import PyPDF2

template = PyPDF2.PdfFileReader(open('given_file.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('water_mark.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(watermark.getPage(0))   # This is a method that can merge the pages 
  output.addPage(page)

  with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)       # Writing to the PDF 
