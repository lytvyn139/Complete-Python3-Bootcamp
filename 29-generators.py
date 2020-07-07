def gencubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
        yield x**3
    return result
print(gencubes(5))

for x in gencubes(5):
    print(x)

####################
# not memory efficient 
def fibon(n):
    a = 1
    b = 1
    output = []
    
    for i in range(n):
        output.append(a)
        a,b = b,a+b
    return output
fibon(10)

# yield
def genfibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for num in genfibon(10):
    print(num)

#next() and iter() built-in functions
def simple_gen():
    for x in range(34):
        yield x

for number in simple_gen():
    print(number)
# REMEMBERS THE PREV AND RETURNS THE NEXT VALUE
g = simple_gen()
print(f'REMEMBERS THE PREV AND RETURNS THE NEXT VALUE {next(g)}')
print(f'REMEMBERS THE PREV AND RETURNS THE NEXT VALUE {next(g)}')
print(f'REMEMBERS THE PREV AND RETURNS THE NEXT VALUE {next(g)}')
print(f'REMEMBERS THE PREV AND RETURNS THE NEXT VALUE {next(g)}')

s = 'hello' 
for letter in s:
    print(letter)
#next(s) #TypeError: 'str' object is not an iterator
s_iter = iter(s)
print('*'*80)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
