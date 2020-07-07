import csv
data = open('examples.csv',encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

print(data_lines[:3])

for line in data_lines[:5]:
    print(line)

#get all the emails
print(data_lines[10])
all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])
print('')
print(f"\033[1;34;40m, {all_emails} ")

#get full names
full_names = []
for line in data_lines[1:15]:
    full_names.append(line[1]+' '+line[2])
print(f'\033[1;31;40m ☠ {full_names} ☠')

#Writing to CSV Files
#This will also overwrite any exisiting file with the same name, so be careful with this

# newline controls how universal newlines works (it only applies to text
# mode). It can be None, '', '\n', '\r', and '\r\n'. 
file_to_output = open('to_save_file.csv','w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',') #delimiter = column separator
csv_writer.writerow(['a','b','c'])
csv_writer.writerows([
                    ['1','2','3'],
                    ['4','5','6']])
file_to_output.close()

f = open('to_save_file.csv','a',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['new','new','new'])
f.close()

