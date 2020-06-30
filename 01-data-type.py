####################################################
#            Primitive data types 
""" Integers """ #int   
integer_num = 3
integer_num = 200
integer_num = 300

""" Floating point """ #float
floating_num = 2.3
floating_num = 4.6
floating_num = 100.3

""" String """ #str
just_a_string = "Hello"
just_a_string = "Joe Blue"
just_a_string = "2000"

""" Lists """ #list 
#ordered sequence of objects
my_list = [10, "hello", 23.3]

""" Dictionaris """ #dict
#Unordered key: value pairs 
my_dict = {
    "mykey": "value",
    "name": "frankie"
}

""" Tuples """ #tup
#ordered immutable sequence of objects 
#Tuples, are like const arrays, you can't change them
my_tuple = (10,"hello", 200.3)
dog = ('Bruce', 'cocker spaniel', 19, False)
#print(dog[0])		# output: Bruce
#dog[1] = 'dachshund' #error

""" Sets """ #set
#unordered collection of unique objects 
#{"a", "b"}

"""  Boolean """ #bool
is_hungry = True
has_freckles = False
####################################################
#                Composite types 



#lists, arrays than can be changed
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
ninjas[0] = 'Sam'
#print(ninjas)

#dictionaries = objects
new_person = {
    'name': 'John', 
    'age': 38, 
    'weight': 160.2, 
    'has_glasses': False
}
print(new_person)	
print(f"You, {new_person['name']} is boring, you need some new hobbies")	
new_person['hobbies'] = ['climbing', 'coding']	# adds a key-value pair if the key doesn't exist
new_person['name'] = 'Jack'	# updates if the key exists
print(f"Wait what??? You not John anymore ! you are {new_person['name']} ")	
print(new_person)	

w = new_person.pop('has_glasses')	# removes the specified key and returns the value
print(w)		# output: 160.2

new_person['weight'] = 260
print(new_person)	
print(f"You, {new_person['name']} gained some weight, but you not using glasses anymore")	


# Touching dictionaries
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 
    'last_name' : 'Jordan'},
    {'first_name' : 'John', 
    'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ 
    {'x': 10, 
    'y': 20} 
]

x[1][0] = 15
print(x)

students[0]['last_name'] = "Bryant"
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z[0]['y'] = 30
print(z)

####################################################
#                    Common Functions 
print(type('sdsdd'))		# output: <class 'str'>
print(type(is_hungry))	    # output: <class 'boolean'>
print(type(2.63))		    # output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>
print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))	# output: 11

####################################################
#               Type Casting or Explicit Type Conversion
#print("Hello" + 42)		    # output: TypeError
print("Hello" + str(42))		# output: Hello 42
total = 35
user_val = "26"
#total = total + user_val		# output: TypeError
total = total + int(user_val)	# total will be 61

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30



