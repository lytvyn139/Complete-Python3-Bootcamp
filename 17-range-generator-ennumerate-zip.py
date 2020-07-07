###########################
""" RANGE GENERATOR """
for num in range(0,20,2):
    print(num)

print(list(range(0,20,2)))

###########################
""" ENNUMERATE """

index_count = 0
for letter in 'abcde':
    print(f'at index {index_count} the letter is {letter}')
    index_count += 1

index_count = 0
word = 'abcd'
for letter in word:
    print(word[index_count])
    index_count += 1

word = 'abcd'
for item in enumerate(word):
    print(item) #return tuples

for index,letter in enumerate(word):
    print(index) #return tuples
    print(letter) #return tuples
    print('\n')

######################
""" ZIP """

mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c']
mylist3 = ['a','b','c','d']
zip(mylist1, mylist2)
for item in zip(mylist1, mylist2, mylist3):
    print(f"will return the shortest concat{item}")

######################
""" IN """
'x' in [1,2,3,4] #false
'x' in ['x','y','z'] #false

'mykey' in {'mykey': 345} #true


d = {'mykey': 345} 
345 in d.values() #true

