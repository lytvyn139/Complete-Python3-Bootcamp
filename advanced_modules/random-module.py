import random

#generate 0 to 100
#print(random.randint(0, 100))

# random.seed(101) #starts the same series of random integers
# print(random.randint(0, 100)) #74
# print(random.randint(0, 100)) #24
# print(random.randint(0, 100)) #69
# print(random.randint(0, 100)) #45

mylist = list(range(0,20))
print(random.choice(mylist))

#grab 5 random from the list

# sample with replacement
print(random.choices(population=mylist, k=10))

# sample without replacement, not gonna pick twice
print(random.choices(population=mylist, k=10))

#will permanetly shuffle a list
random.shuffle(mylist)
print(mylist)
print(mylist)
random.shuffle(mylist)
print(mylist)

print(random.uniform(a=0,b=100))

print(random.gauss(mu=0,sigma=1))