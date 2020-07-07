from collections import Counter
mylist = [1,2,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3]
print(Counter(mylist))
mylist = ['a','a','a', 10, 10, 10, 10, 10]
print(Counter(mylist))

# WORDS
print(Counter('aaaaaabbbbbddddd'))
sentence = 'How many times does each word showed up in sentence'
print(Counter(sentence.lower().split()))

# MOST COMMON 
letters = 'aaaaaaabbbbbbccccccdddaaaddd'
c = Counter(letters)
print(c.most_common)

#Common patterns when using the Counter() object
print(list(c))                     # list unique elements

# sum(c.values())                 # total of all counts
# c.clear()                       # reset all counts
# set(c)                          # convert to a set
# dict(c)                         # convert to a regular dictionary
# c.items()                       # convert to a list of (elem, cnt) pairs
# Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
# c.most_common()[:-n-1:-1]       # n least common elements
# c += Counter()                  # remove zero and negative counts

""" defaultdict """
from collections import defaultdict
d = {'a':10}
print(f'd: {d["a"]}')
#print(f'd: {d["WRONG"]}') #key error

d = defaultdict(lambda: 0)
d['correct'] = 100
print(d['correct'])     #100
print(d['WRONG'])       #0 will return default value

""" namedtuple """
from collections import namedtuple

mytuple = (10,20,30)
t[0] #10

Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sammy = Dog(age=5, breed='Husky', name='Sam')
print(sammy)



