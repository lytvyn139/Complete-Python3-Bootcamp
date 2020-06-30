""" SLICE 
[start:stop:step]
start is a index for slice start
stop is the index will go up to (but not include)
step is the size of the jump you take
"""

#my_string = 'i'm going for a run'      #error single quoutes 
#my_string = 'I\'m going for a run'     #will work
my_string = "I'm going for a run"
print(my_string)

my_sting_new_line = "hello \npeople"
print(my_sting_new_line)

my_sting_tab = "hello \tpeople"
print(my_sting_tab)

my_string = "Please get my length"
print(len(my_string))

print(my_string[0])   #P
print(my_string[19])  #h
print(my_string[-3])  #g 

my_string = "ABCDEFGHK"
print(my_string[2:])  #will print everything after [2] CDEFG
print(my_string[:5])  #will print everything before [5] ABCDE

my_string = "ABCDEFGHK"
print(my_string[2:6]) #CDEF

my_string = "112233445566778899"
print(my_string[::3]) #go to the end with the step 3

my_string = "112233445566778899"
print(my_string[2:7:2]) #234

my_string = "112233445566778899"
print(my_string[::-1]) #998877665544332211 REVERSED

"""  Immutability  """
name = "Sam"
#name[0] = "P" #Error
last_letters = name[1::] 
print(last_letters) #am
print('P' + last_letters) #Pam

x = "hello world"
x = x + " its good outside"
print(x) #hello world its good outside

put_me_into_sleep = 'z'
print(put_me_into_sleep * 10) #zzzzzzzzzz

'2' + '3' #23

x = x.upper()       #HELLO WORLD ITS GOOD OUTSIDE
print(x)

x = x.lower()
print(x)            #hello world its good outside

x = "hello world !"
print(x.split())    # ['hello', 'world', '!']
print(x.split('l')) # ['he', '', 'o wor', 'd !']

""" .format() """
print('This is a string {}'.format('INSERTED'))
print('The {2} {1} {0} {0}'.format('fox', 'brown', 'quick'))
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

result = 0.12870000
print("the result was {r:1.3f}".format(r=result)) #0.129

""" f-strings """
print(f'My result is {result}, so {x}')



