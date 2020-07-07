#two.py
import one
print('4. top level in two.py')
one.func()
if __name__ == "__main__":    #build in
    print('5. two.py is being run directly')
else:
    print('6. one.py has been imported')


