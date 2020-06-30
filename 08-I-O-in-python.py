#the path
#myfile = open('/coding/myfile.txt')
#print(myfile2) 
#FileNotFoundError: [Errno 2] No such file or directory: 'myfile2.txt'

# myfile = open('myfile.txt')
#myfile = open('myfile2.txt')

# print(myfile)
# print(myfile.read())
# print(myfile.read()) # will output nothing
# myfile.seek(0) #seek cursor back to sero
# print(myfile.read()) # will output nothing
# myfile.seek(40) #seek cursor back to sero
# print(myfile.read()) # will output nothing
# myfile.seek(0) #seek cursor back to zero

# print(myfile.readlines()) # will output nothing
# myfile.close()
# with open('myfile.txt') as my_new_file:
#     contents = my_new_file.read()
# #no need to close the file
# contents

"""  context managers to close the files automatically """
#r = read only
#w = write only will OVER WRITE!
#a = append to end of the life
#r+ reading and writing
#w+ writing and reading

with open ('teller.txt', mode='r') as lorem_file:
    content = lorem_file.read()
    print(content)

with open ('teller.txt', mode='w') as lorem_file:
    lorem_file.write('\n ***OVERWRITING ALL***')

with open ('teller.txt', mode='a') as lorem_file:
    for i in range (0,10,1):
        lorem_file.write(f' \n APPENDING ALL FROM PYTHON {i} ')

with open ('teller.txt', mode='r') as lorem_file:
    content = lorem_file.read()
    print(content)


"""  CREATE NEW FILE """
with open ('just_married.txt', mode='w') as f:
    f.write('congrats you are married')