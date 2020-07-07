#pip3 install PyPDF2

import PyPDF2
#Reading PDFs
f = open('Working_Business_Proposal.pdf','rb') #rb - read binary
pdf_reader = PyPDF2.PdfFileReader(f)
pdf_reader.numPages
page_one = pdf_reader.getPage(0) #0 based index
page_one_text = page_one.extractText()
print(page_one_text)
f.close()

#Adding to PDFs
f = open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
first_page = pdf_reader.getPage(0)

# create write obj
pdf_writer = PyPDF2.PdfFileWriter()
# add page
pdf_writer.addPage(first_page)
pdf_output = open("Some_New_Doc.pdf","wb")
pdf_writer.write(pdf_output)
f.close()


# Simple Example
f = open('Working_Business_Proposal.pdf','rb')
# List of every page's text.
# The index will correspond to the page number.
pdf_text = []
pdf_reader = PyPDF2.PdfFileReader(f)
for p in range(pdf_reader.numPages):
    page = pdf_reader.getPage(p)
    pdf_text.append(page.extractText())
print(pdf_text[1]) #page 3
print(pdf_text[3]) #page 3