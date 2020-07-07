#one.py
def func():
    print('func() in one.py')

print('1. top level in one.py')

if __name__ == "__main__":    #build in
    print('2. one.py is being run directly!')
else:
    print('3. one.py has beem imported!')

