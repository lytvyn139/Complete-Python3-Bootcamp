mylist = [1,2,3]
myset = set()
type(mylist) #list
type(myset)  #set
#class name can be without () if it's not inheriting
class Dog():
    # CLASS OBJ ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'

    def __init__(self, breed, name, spots="NO SPOTS"):
        self.my_attribute = breed
        self.name = name
        self.spots = spots

    # methods 
    def bark(self, number):
        print(f'woof woof {self.name}, {number} (C)')

my_dog = Dog('huskie', 'Frankie', False)
print( my_dog.my_attribute, my_dog.name, my_dog.spots, my_dog.species )
my_dog.bark(4)

class Circle():
    pi = 3.14
    def __init__(self, radius = 1):
        self.radius = radius
        self.area = radius*radius*Circle.pi
    
    def get_circumference(self):
        return self.radius * Circle.pi * 2

my_circle = Circle(30) #

print( my_circle.get_circumference() )
print( my_circle.area )
##############################################################
# INHERITANCE

class Animal():
    def __init__(self):
        print('Animal created')
    
    def who_am_i(self):
        print('Im am an animal')

    def eat(self):
        print('Im eating')

class Dog(Animal):
    #create the inctance of animal class
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')

    def who_am_i(self):
        print('im dog')

    def bark(self):
        print('BARK BARK')

    def eat(self):
        print('Im eating meat')


my_animal = Animal()
mydog = Dog()
mydog.who_am_i()
mydog.eat()

#########################################
# Polymorphism
class Dog():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + " BARK BARK"

class Cat():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + " MEOW MEOW"

niko = Dog('niko')
felix = Cat('felix')
print( niko.speak())
print( felix.speak())

class Animal():
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotIplementerError('sub class must implement this abstract method')

#my_animal = Animal('fred')        
#my_animal.speak()
#    raise NotIplementerError('sub class must implement this abstract method')
#NameError: name 'NotIplementerError' is not defined
class Dog(Animal):
    def speak(self):
        return self.name + " say woof"

class Cat(Animal):
    def speak(self):
        return self.name + " say meow"
fido = Dog('Fido')
iris = Cat('Iris')
print(fido.speak())
print(iris.speak())


######################################
# DUNDER
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    #dunder method
    #is there's fn that as for string representaions of 
    # your class, it will return whatever this returns 
    def __str__(self):
        return f'{self.title} by {self.author}'
    def __len__(self):
        return self.pages
    def __del__(self):
        print('Obj has been deleted')
    

b = Book('Python rocks', 'IURII', 221)
print(b)
print(len (b))
del(b)

