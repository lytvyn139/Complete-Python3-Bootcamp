""" tuples are immutable """
""" but same methods as string and lists """
t = (1,2,3)
my_list = [1,2,3]
print(type(t))
print(type(my_list))

t = ('one', 2)

""" count """
t = ('a', 'a', 'b')
print(t.count('a')) #count 'a' times
print(t.index('a')) #appears fisrt appearance

my_list[0] = "NEW"
print(my_list)

t[0] = "NEW" #error
print(t)

