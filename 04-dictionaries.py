""" When use list and when dict
Dictionaries are unordered and can't be sorted(good for prices in the store)
Dictionaries are mappings and do not retain order! 
If you do want the capabilities of a dictionary but you would like ordering as well, 
check out the ordereddict object lecture later on in the course!
List can be indexed and sliced 

"""
#https://www.w3schools.com/python/python_ref_dictionary.asp

my_dict =  {'key1': 15,
            'key2': True,
            'key3': ['read me', 'please']}

print(my_dict['key1'])    # value
print(my_dict['key2'])    # True

print(my_dict['key3'][1].upper()) #PLEASE
print(my_dict.keys())   #dict_keys(['key1', 'key2', 'key3'])
print(my_dict.values()) #dict_values([15, True, ['read me', 'please']])
print(my_dict.items())  #dict_items([('key1', 15), ('key2', True), ('key3', ['read me', 'please'])])

# won't print
#print(f'key: {['key1'][5]}') # 1

print('********** PRICES ***********')
prices_lookup = {'apple': 2.99,
                'oranges': 1.99,
                'milk': 0.99}
print(f"apple price ${prices_lookup['apple'] }")
print(f"orange price ${prices_lookup['oranges'] }")
print(f"milk price ${prices_lookup['milk'] }")

                        print('********** TOUCHING DICT ***********')
#warmup
d = {
    'k1': ['a','b','c'],
    'k2': [0,1,666],
    'k3': {
        'inside_key': 100
        }
    }
print(d['k2']) #[0,1,666]
print(d['k2'][2]) # key from d dict k2 index 2 = 666
print(d['k3']) #'inside_key': 100
print(d['k3']['inside_key']) #100

#EASY
d = {'simple_key' : 'hello'}
print(d['simple_key'])

#MEDIUM
d = {'k1':{
            'k2':'hello'}
        }
print(d['k1']['k2'])

#MEDIUM.task2
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

#HARD
d = {'k1': [{ 'nest_key':
                        ['this is deep', 
                            ['hello'] 
                        ]}
            ]}
print(d['k1'][0]['nest_key'][1][0])

#NIGHTMARE
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

#IMPOSIBLE
# does some one know how get to the 🍿 😬 ???
get_the_present = {'a1cb1':[1,2,{'a2bc1':['this but not that',{'::-1[({% self %})]':['append('')',False,['🍿']]}]}]}
print(get_the_present['a1cb1'][2]['a2bc1'][1]['::-1[({% self %})]'][2][0])

