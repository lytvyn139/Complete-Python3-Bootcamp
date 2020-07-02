my_list = [1,2,3]
my_list = ['NEWS', 100.40, False]
print(len(my_list)) #3
my_list = ['one', 'two', 'three']
print(my_list[0]) #one
print(my_list[1:]) #'two', 'three'

another_list = ['four','five']
print(another_list) #['four', 'five']

final_list = my_list + another_list
print(final_list) #['one', 'two', 'three', 'four', 'five']

final_list[0] = 'ONE ALL CAPS'
print(final_list) #['ONE ALL CAPS', 'two', 'three', 'four', 'five']

#append to end of the list
final_list.append('six') #['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six']
print(final_list)

#removes last item of the list
popped_item = final_list.pop()
print(popped_item) #six
print(final_list) #['ONE ALL CAPS', 'two', 'three', 'four', 'five']

final_list.pop(0)
print(final_list) #['two', 'three', 'four', 'five']

print('SORT //')
letter_list = ['v', 'x', 'a', 'k']
num_list = [4,33,2,1,0]
letter_list.sort()
num_list.sort()
print(letter_list,num_list)

print('REVERSE //')
num_list = [4,33,2,1,0]
num_list.reverse()
print(num_list) 

print('CREATE //')
print([5]*5)
list2 = [0,0,0]
print(list2)

nested_list = [
    [14,14,14],
    [13,'middle',13],
    [100,100,100]]
print(nested_list[1][1])

l_one = [1,2,[3,4]]
l_two = [1,2,{
                'k1':4
        }]

# True or False?
print(l_one[2][0] >= l_two[2]['k1'])
#false