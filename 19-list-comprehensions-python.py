mystring = 'hello'
mylist = []

#bad practice
for letter in mystring:
    mylist.append(letter)
print(mylist)

mylist = [letter for letter in mystring]
print(mylist)

mylist = [num for num in range(0,11)]
print(mylist)

mylist = [num**2 for num in range(0,11)]
print(mylist)

mylist = [x for x in range (0,11) if x%2 == 0]
print(mylist)

mylist = [x**x for x in range (0,11) if x%2 == 0]
print(mylist)

celcius = [0,20,10,34.5]
fah = [ ((9/5)*temp + 32) for temp in celcius]
print(fah)

#same as above
fah = []
for temp in celcius:
    fah.append(( (9/5)*temp + 32))
print(fah)

#ugly one liner don't do it
result = [x if x % 2 == 0 else 'ODD' for x in range(0,11)]
print(result)

#nested loop
mylist = []
for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)
print(mylist)
#nested loop list comprehensive UGLY DONT
mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist)

