#Write a function that computes the volume of a sphere given its radius.
def vol(rad):
    return (4/3*3.14)*(rad**3)
print( vol(2) )

# Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    # my one liner
    #return num > low and num < high
    if num in range(low, high+1):
        print ('in range')
    else:
        print('not in range')
print(ran_check(4,20,60))

#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
#Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#Expected Output : 
#No. of Upper case characters : 4
#No. of Lower case Characters : 33
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
def up_low(s):
    result = {
        'upper': 0,
        'lower': 0
    }
    for char in s:
        if char.isupper():
            result['upper'] += 1
        elif char.islower():
            result['lower'] += 1
        else:
            pass
    return result
print(up_low(s))


#Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]
def unique_list(lst):
    seen_numbers = []
    for number in lst:
        if number not in seen_numbers:
            seen_numbers.append(number)
    print(seen_numbers)
    print('uniq oneliner supper efficient')
    return list(set(lst)) 

print( unique_list([1,1,1,1,2,2,3,3,3,3,4,5]) ) #[1, 2, 3, 4, 5]


#Write a Python function to multiply all the numbers in a list.
list = [1, 2, 3, -4] #-24
def multiply(numbers):  
    total = 1 #if add start from 0
    for num in numbers:
        total = total * num
    return total

print(multiply(list))

#Write a Python function that checks whether a word or phrase is palindrome or not.
#madam,kayak,racecar, or a phrase "nurses run".
def palindrome(s):
    # remove spaces
    s = s.replace(' ','')
    # check if string is == reversed 
    return s == s[::-1]
print( palindrome('nu rs e s r   un') ) 


#Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog"
#Hint: You may want to use .replace() method to get rid of spaces.
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    #create set of alphabet
    alphaset = set(alphabet)

    #remove spaces
    str1 = str1.replace(' ','')

    #conver input into lowercase
    str1 = str1.lower()

    #grab all uniq letters from the string
    str1 = set(str1)

    #comprare alphabet set == string set input
    srt1 = set(str1)
    return str1 == alphaset
print('is paragram ???')
print( ispangram("The quick brown fox jumps over the lazy dog") )
