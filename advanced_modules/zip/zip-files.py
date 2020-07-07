import zipfile

f = open('fileone.txt', 'w+')
f.write('one file info')
f.close()

f = open('filetwo.txt', 'w+')
f.write('two file info')
f.close()

comp_file = zipfile.ZipFile('myzip.zip', 'w')
comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

#unzip, open file with read method
zip_obj = zipfile.ZipFile('myzip.zip', 'r')
zip_obj.extractall('extracted_content')