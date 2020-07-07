#############################
# Map
# apply splicer fn to every element in my_nums list

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

#appliying sqaure fn to every item in list
for item in map(square, my_nums):
    print(item) #1, 4, 9, 16, 25

print( list(map(square, my_nums)) ) #[1, 4, 9, 16, 25]

def splicer(mystring):
    #if even length of char
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']
print( list(map(splicer, names)) )

############################
# Filter
# it will filter based on fn condition

def check_even(num):
    return num % 2 == 0

mynums = [1,2,3,4,5,6]
list(filter(check_even, mynums))

for n in filter(check_even, mynums):
    print(n)

############################
# lambda
print('turning into lambda')
def square(num):
    result = num ** 2
    return result

print(square(3))

square = lambda num: num ** 2
print(square(5))

# lambda map
mynums = [4,5,10]
print(list(map(lambda num: num**2, mynums)))

# lambda filter
print(list(filter(lambda num: num % 2 == 0, mynums)))



names = ['Andy', 'Eve', 'Sally']
print( list(map(lambda x: x[0],names)))
print( list(map(lambda x: x[::-1],names)))