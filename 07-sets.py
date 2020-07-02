""" Sets are unordered collection of unique elements """
myset = set()
myset.add(1)
print(myset) #{1} it doesn't have key, so it's not dictionary
myset.add(2)
myset.add(2)
print(myset) #doesn't add 2 twice, no errors, but print {1},{2}

""" casting a list so will only get unique values """

mylist = [1,1,1,2,3,3,4,5,6,6,6,6,6,6,7,8,9,10]

set(mylist)
print(set(mylist)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(set('Mississippi')) #{'i', 's', 'p', 'M'}
