def say():
    print ('Hello!')

greet = say
greet()
say()
del say
greet() #still running
########################
def hello(name='user'):
    print ('hello() executed')
    def greet():
        return '\t This is the greet() inside hello()'
    
    def welcome():
        return '\t This is welcome() inside hello()'

    if name == 'CPU':
        return greet
    else:
        return welcome
hello()

def cool():
    def super_cool():
        return 'Im very cool!'
    return super_cool
z = cool()
print(z)
###############################
def hello():
    return 'hi jose'

def other(some_def_func):
    print('other code runs here')
    print(some_def_func())
other(hello)
#############
print('!!! decorator !!!')
def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()
func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()

@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")
func_needs_decorator()