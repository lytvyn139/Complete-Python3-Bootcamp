my_itrabale = [1,2,3]
for item_name in my_itrabale:
    print(item_name)

my_list = [1,2,3,4,5,6,7,8,9,10]
for num in my_list:
    #even print
    if num % 2 == 0:
        print(f"even {num} ")
    else:
        print(f"odd {num}")

list_sum = 0
for num in my_list:
    list_sum = list_sum + num
    print(f'adding: {list_sum} + {num}')
print(f'sum: {list_sum}')

mystring = "hello world"
for letter in mystring:
    print(letter)

#will print 6 times    
for _ in "ololol":
    print('count the letters')

""" tuple """
tup = (1,2,3,4)
for item in tup:
    print(item)

my_tup_list = [
    (1,2),
    (3,4),
    (5,6),
    (7,8)
]
len(my_tup_list)
for item in my_tup_list:
    print(item)

""" tuple unpacking """
for a,b in my_tup_list:
    print(a)
    #print(b)


my_tup_list = [
    (1,2,3),
    (4,5,6),
    (7,8,9)
]
for a,b,c in my_tup_list:
    print(b)

#dictionary are unordered
d = {
    'key1': 1,
    'key2': 2,
    'key3': 3,
}
for item in d:
    print(item) #will print keys

for item in d.items():
    print(item) #will print keys

for key,value in d.items():
    print(value) #will print keys

