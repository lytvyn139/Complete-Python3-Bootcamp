print('#Problem 1')
#Create a generator that generates the squares of numbers up to some number N.
def gensquares(N):
    for i in range(N):
        yield i**2
for x in gensquares(10):
    print(x)


print('#Problem 2')
#Create a generator that yields "n" random numbers between a low and high number (that are inputs).
import random
random.randint(1,10)

def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low, high)

for num in rand_num(1,10,12):
    print(num)

#Can you explain what gencomp is in the code below? (Note: We never covered this in lecture!)
# Hint: Google generator comprehension!
print('#Problem 3')
my_list = [1,2,3,4,5]
gencomp = [item for item in my_list if item > 3]
for item in gencomp:
    print(item)
