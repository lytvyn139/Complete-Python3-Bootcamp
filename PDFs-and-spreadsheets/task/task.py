#Task One: Use Python to extract the Google Drive link from the .csv file. (Hint: Its along the diagonal from top left to bottom right).
import csv, PyPDF2, re
data = open('find_the_link.csv',encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)
print(data_lines)

link_str = ''
for row_num,data in enumerate(data_lines):
    link_str+=data[row_num]

print(link_str)

#Task Two: Download the PDF from the Google Drive link and find the phone number that is in the document
f = open('Find_the_Phone_Number.pdf','rb')
pdf = PyPDF2.PdfFileReader(f)
pdf.numPages #17

#Phone Number Matching
#pattern to search for 3 digits in the row
pattern = r'\d{3}'
all_text = ''

for n in range(pdf.numPages):
    page = pdf.getPage(n)
    page_text = page.extractText()
    all_text = all_text+' '+page_text
    #print(all_text)
    """ start looking into patter with all text """
    #re.search(pattern,all_text) #will only show 1st instance
    print(re.findall(pattern, all_text))

for match in re.finditer(pattern,all_text):
    print(match)


# #Once you know the correct pattern:
pattern = r'\d{3}.\d{3}.\d{4}'
for n in range(pdf.numPages):
    page  = pdf.getPage(n)
    page_text = page.extractText()
    match = re.search(pattern,page_text)
    if match:
        print(match.group())