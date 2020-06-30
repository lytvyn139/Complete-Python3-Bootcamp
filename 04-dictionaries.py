""" When use list and when dict
Dictionaries are unordered and can't be sorted(good for prices in the store)
Dictionaries are mappings and do not retain order! 
If you do want the capabilities of a dictionary but you would like ordering as well, 
check out the ordereddict object lecture later on in the course!
List can be indexed and sliced 

"""

my_dict =  {'key1': 'value1',
            'key2': 'value2' }

print(my_dict['key1'])    # value
print(my_dict['key1'][5]) # 1


prices_lookup = {'apple': 2.99,
                'oranges': 1.99,
                'milk': 0.99}
print(f"milk price: {prices_lookup['milk'] }")

d = {'k1': ['a','b','c'],
    'k2': [0,1,666],
    'k3': {
        'inside_key': 100
        }
    }
print(d['k2'])
print(d['k2'][2]) # key from d dict k2 index 2 = 666
print(d['k3'])
print(d['k3']['inside_key'])

""" DICT TREE """
#EASY
d = {'simple_key' : 'hello'}
print(d['simple_key'])

#MEDIUM
d = {'k1':{
            'k2':'hello'}
        }
print(d['k1']['k2'])

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

#NIGHTMARE

# does some one know how get to the 🍿 😬 ???
get_the_present = {'a1cb1':[1,2,{'a2bc1':['this but not that',{'::-1[({% self %})]':['append('')',False,['🍿']]}]}]}
print(get_the_present['a1cb1'][2]['a2bc1'][1]['::-1[({% self %})]'][2][0])
#print( ??? )

#################
d = {'key1': ['a','b','c']}
mylist = d['key1']
letter = mylist[2]
print(letter.upper()) #C

print(d['key1'][2].upper()) #C one liner

fav_num = {
        'num1': 8,
        'num2': 31337,
}
fav_num['num3'] = 69
print(fav_num)
fav_num['num2'] = 'eeee'
print(fav_num)

# COOL
print(d.keys())
print(d.values())
print(d.items())
