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

""" COPY AND CLEAR """
s = {1,2,3}
sc = s.copy() #{1,2,3} 

s.add(4)
print(s)
print(sc)
s.clear() #wiil clear the set,
print(s)

""" Difference """
s.difference(sc) #diffrence between s and sc is {4}

""" Discard """
s = {1,2,3}
s.discard(2)
print(s) #{1,3}

""" intersection and intersection_update """
#Returns the intersection of two or more sets as a new set.(i.e. elements that are common to all of the sets.)
s1 = {1,2,3}
s2 = {1,2,4}
s1.intersection(s2) #{1,2}
s1.intersection_update(s2)

""" isdisjoint """
#This method will return True if two sets have a null intersection.
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}
print(s1.isdisjoint(s2)) #false

""" is subset (set contans set2) """
#This method reports whether another set contains this set.
s1 = {1,2}
s2 = {1,2,4}
s1.issubset(s2)   #true
s2.issuperset(s1) #true

""" symmetric_difference and symmetric_update """
#Return the symmetric difference of two sets as a new set.(i.e. all elements that are in exactly one of the sets.)
s1 = {1, 2}
s2 = {1, 2, 4}
s1.symmetric_difference(s2) #{4}

""" union """
#Returns the union of two sets (i.e. all elements that are in either set.)
s1.union(s2) {1,2,4}

""" update """
#Update a set with the union of itself and others.
s1.update(s2) #{1, 2, 4}

