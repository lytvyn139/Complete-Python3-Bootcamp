import zipfile, re, os

zip_obj = zipfile.ZipFile('unzip_me_for_instructions.zip', 'r')
zip_obj.extractall('extracted_content')

with open('extracted_content/Instructions.txt') as f:
    content = f.read()
    print(content)

pattern = r'\d{3}-\d{3}-\d{4}'
test_string = "here is a random number 1231231234 , here is phone number formatted 123-123-1234"
re.findall(pattern,test_string)

def search(file,pattern= r'\d{3}-\d{3}-\d{4}'):
    f = open(file,'r')
    text = f.read()
    
    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ''

results = []
for folder , sub_folders , files in os.walk(os.getcwd()+"/extracted_content"):
    for f in files:
        full_path = folder+'/'+f
        print('SEARCHING IN: ', full_path)
        results.append(search(full_path))
        # for r in results:
        #     if r != '':
        #         print(r.group())
    
for r in results:
    if r != '':
        print(r.group())

