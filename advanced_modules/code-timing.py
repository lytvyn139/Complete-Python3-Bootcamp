import time, timeit

def func_one(n):
    return [str(num) for num in range(n)]
def func_two(n):
    return list(map(str, range(n)))

start_time = time.time()
result = func_one(1000000)
end_time = time.time()
elapsed_time = end_time - start_time
print('func one: ',elapsed_time)


start_time = time.time()
result = func_two(1000000)
end_time = time.time()
elapsed_time = end_time - start_time
print('func two: ',elapsed_time)

""" Timeit Module """

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''
#Now let try running func_two 10,000 times and compare the length of time it took.
stmt = 'func_one(100)'
stmt2 = 'func_two(100)'
print('running tests 100k times FOR vs MAP')
print(timeit.timeit(stmt2,setup2,number=100000))
print(timeit.timeit(stmt,setup,number=100000))
