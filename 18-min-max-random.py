from random import shuffle
from random import randint

######################

""" MIN MAX """
mylist = [10,200,3323,410000,5.4,6]
print(min(mylist))
print(max(mylist))

######################
""" RANDOM """
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print(mylist)
shuffle(mylist)
print(mylist)

print(randint(0,100))

z = input('enter a num: ')
print(randint(0,int(z)))