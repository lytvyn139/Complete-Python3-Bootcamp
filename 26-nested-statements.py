x = 25 
def printer():
    x = 50
    return x
print(x) #25

print(printer()) #50

""" 
LEGB Rule:

L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.
E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.
B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...
"""

# x is local here:
f = lambda x:x**2
#################
name = 'This is a global name'
def greet():
    name = 'Sammy'
    def hello():
        print('Hello '+name)

    hello()
greet() #hello Sammy
#################
name = 'This is a global name'
def greet():
    #name = 'Sammy'
    def hello():
        print('Hello '+name)

    hello()
greet() #hello This is a global string
#################
name = 'This is a global name'
def greet():
    name = 'Sammy'
    def hello():
        name = 'LOCAL'
        print('Hello '+name)
    hello()
greet() #hello LOCAL


x = 50

def func(x):
    #global x #only if you know what you're doint
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is: ', x)
func(10)
print('Value of x (outside of func()) is: ', x)