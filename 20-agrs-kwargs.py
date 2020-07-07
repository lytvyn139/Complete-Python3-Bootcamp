
def myfunc(a,b):
    #return 5 of the sum a+b
    return sum((a,b)) * 0.05
print( myfunc(40,60) )
# ERROR takes 2 positional arguments but 3 were given
#print( myfunc(40,60, 100) )

def myfunc(*args):
    print(args)
        print(f'args are:{item}')
    return sum(args) * 0.05
    #return len(args) #^
#how you can pass as many as you can
print( myfunc(40,60, 13, 230, 999, 2.23) )
#print( myfunc(1,4,7,8,3,7) )

#Def a functions that takes arbitrary number of args,
#returns a list containing only those args that are even.

def myfunc(*args):
    result = []
    for item in args:
        if item % 2 == 0:
            result.append(item)
    return result
print(myfunc(4,2,1,5,72,14))



#kwargs - key word arguments, bulds a dictiionary of key value pairs
def myfunc(**kwargs):
    if 'apple' in kwargs:
        print(f'My fav fruit is: {kwargs["fruit"]}')
    else:
        print('No apples were found')
myfunc(fruit='mango', dance='tango', car='mulsane') #no apples

def myfunc(*args, **kwargs):
    print(f"I would like {args[0]} {kwargs['food']}")

myfunc(10,20,30, fruit='orange', food='eggs', animal='god')


def myfunc(a,b):
    return sum(a,b)