###########################################################
#                           FOR LOOP

# for (let i=0; x< 10; i++) {}
# for i in range(0, 10, 1):
#     print(i)

# # increment of +1 is simplied
# for y in range(0, 10):	
#     print(y)

# # increment of +1 and start at 0 is implied
# for z in range(10):	
#     print(z)

#note that if you need to specify an increment other than +1, 
# all three arguments are required.
# for a in range(0, 10, 2):
#     print(a)
# # output: 0, 2, 4, 6, 8

#loop backward
# for b in range(10, 1, -3):
#     print(b)
# # output: 10, 7, 2

###########################################################
#                     FOR LOOPS THROUGH LISTS
my_list = [0, False, 'Cake', 3, 4, 5]
print(type(my_list[1]))
for i in range(0, len(my_list)):
    print(f"index#{i} = {my_list[i]}")
    
# OR 
    
# for v in my_list:
#     print(v)
# output: abc, 123, xyz
###########################################################
#                     WHILE LOOPS THROUGH LISTS
for count in range(0,5):
    print("looping - ", count)

count = 0
while count < 5:
    print("looping - ", count)
    count += 1

y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final")
#3,2,1, final
#                   BREAK
for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

#                   Continue
for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
    print("Final else statement")
# output: 3, 2, 1

###########################################################
#                     FOR LOOPS THROUGH DICTIONARIES
# my_dict = { 
#     "name": "Noelle", 
#     "language": "Python",
#     "type": "Weak"
#     }
# for k in my_dict:
#     # print(k)
#     # print(my_dict[k])
#     print(k,"is",my_dict[k])

# capitals = {
#     "Washington":"Olympia",
#     "California":"Sacramento",
#     "Idaho":"Boise",
#     "Illinois":"Springfield",
#     "Texas":"Austin",
#     "Oklahoma":"Oklahoma City",
#     "Virginia":"Richmond"}
# # another way to iterate through the keys
# for key in capitals.keys():
#     print(key)
# # output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia

# #to iterate through the values
# for val in capitals.values():
#     print(val)
# # output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
# #to iterate through both keys and values
# for key, val in capitals.items():
#     print(key, " = ", val)
# # output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

#1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

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
#print(x)

students[0]['last_name'] = "Bryant"
#print(students)

sports_directory['soccer'][0] = 'Andres'
#print(sports_directory)

z[0]['y'] = 30
#print(z)
##################################################################################################################################
#2. Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.
#  For example, given the following list:
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for i in range(1, len(students)):
        print(f"Student #{i} first name: {students[i]['first_name']}, last name is - {students[i]['last_name']} ")
#iterateDictionary(students) 
# Student #1 first name: John, last name is - Rosales 
# Student #2 first name: Mark, last name is - Guillen 
# Student #3 first name: KB, last name is - Tonel 
##################################################################################################################################
#3. Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, 
# given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. 
# For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB
# And iterateDictionary2('last_name', students) should output:

# Jordan
# Rosales
# Guillen
# Tonel

no_namers = [
        {'name':  'user1', 'last' : 'last1'},
        {'name' : 'user2', 'last' : 'last2'},
        {'name' : 'user3', 'last' : 'last3'},
    ]

def iterateDictionary2(key_name, no_namers):
    for i in range(len(no_namers)):
        print(no_namers[i][key_name])
#iterateDictionary2('name',no_namers)
#iterateDictionary2('last',no_namers)
# user1
# user2
# user3
# last1
# last2
# last3
##################################################################################################################################
#4. Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, 
# and then prints the associted values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dictionary):
    for key, value in some_dictionary.items():
        print(f"{len(some_dictionary[key])} {key.upper():}")
        for item in some_dictionary[key]:
            print(item)
printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devona
