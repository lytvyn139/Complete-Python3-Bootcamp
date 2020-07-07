import math  

hundered_sumtin = 44+ 59/2 +29.5-2.75
print(hundered_sumtin)
print(4 * (6+5))
print(4 * 6 + 5)
print(4 + 6 * 5)
print(type(3 + 1.5 + 4))


print(math.sqrt(0))  
print(math.sqrt(4))  
print(math.sqrt(3.5)) 

s = 'hello'
print(s[1])
print(s[::-1]) 
print(s[-1]) 
print(s[4]) 

list = [0,0,0]
list2 = [0,0,0]
list2

list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'

list4 = [5,3,4,6,1]
list4.sort()
print(list4)

d = {'simple_key' : 'hello'}
print(d['simple_key'])

d = {'k1':{
            'k2':'hello'}
        }
print(d['k1']['k2'])

d = {'k1': [{ 'nest_key':
                        ['this is deep', ['hello'] ]}
    ]}
print(d['k1'][0]['nest_key'][1][0])
