#pip3 install ipywidgets
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
def func(x):
    return x

interact(func, x=10)
interact(func, x=True);
interact(func, x='Hi there!')

# Using a decorator!
@interact(x=True, y=1.0)
def g(x, y):
    return (x, y)

# Can call the IntSlider to get more specific
interact(func, x=widgets.IntSlider(min=-10,max=30,step=1,value=10))

# Min,Max slider with Tuples
interact(func, x=(-10,10,1))

# (min, max, step)
@interact(x=(-10,10,1))
def h(x=5.0):
    return x, y

# dropdown
interact(func,x=['hello', 'option', 'other'])
interact(func, x={'one': 10, 'two': 20});

from IPython.display import display
def f(a, b):
    display(a + b)
    return a+b
w = interactive(f, a=10, b=20)
w.children
type(w)
display(w)
