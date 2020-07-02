""" SLICE 
[start:stop:step]
start is a index for slice start
stop is the index will go up to (but not include)
step is the size of the jump you take
"""

my_string = "I\'m going for a run"
print(my_string)

my_sting_new_line = "hello \npeople"
print(my_sting_new_line)

my_sting_tab = "\thello \t\tpeople"
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

"""  String Immutability  """
name = "Sam"
#name[0] = "P" #TypeError: 'str' object does not support item assignment
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
x = x.capitalize()  
print(x)            #Hello world its good outside
x = x.title()
print(x)            #Hello World Its Good Outside

x = "hello world !"
print(x.split())    # ['hello', 'world', '!']
print(x.split('l')) # ['he', '', 'o wor', 'd !']

x = 'hihihihihhhihihihhh'
#['h', 'h', 'h', 'h', 'hhh', 'h', 'h', 'hhh']
print(x.split('i')) 

#('h', 'i', 'hihihihhhihihihhh')
print(x.partition('i')) #first instance of i

""" .format() """
print('This is a string {}'.format('INSERTED'))
print('The {2} {1} {0} {0}'.format('fox', 'brown', 'quick'))
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

result = 0.12870000
print("the result was {r:1.3f}".format(r=result)) #0.129

""" f-strings """
print(f'My result is {result}, so {x}')

s = 'hello world'
z = s.count('o') 
print(z) #2
z = s.find('w') 
print(z) #6

z = s.center(20, 'z')
print(z) #zzzzhello worldzzzzz

print('hello\this'.expandtabs())

a = 'om the string'
print( a.isalnum() ) #false
print( a.isalpha() ) #false
print( a.islower() ) #true
print( a.isupper() ) #true
print( a.isspace() ) #false
print( a.title() )   #Om The String
print( a.endswith('g') ) #true
print( a[-1] == 'o' )    #true




