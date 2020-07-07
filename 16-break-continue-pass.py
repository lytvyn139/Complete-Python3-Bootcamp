""" 
break: breaks aout of the current closest enclosing loop.
continue: goes to the top of the closest  enclosing loop.
pass: will do nothing at all.
"""
x = [1,2,3,4]
for item in x:
    pass #do nothing at all, use that as placeholder
print('end of my script')


mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        continue #will skip a
    print(letter)

mystring = 'Sammy'
for letter in mystring:
    if letter == 'm':
        break #will out loop break on m
    print(letter)

x = 0;
while x < 15:
    if x == 10:
        break
    print(x)
    x += 1
