#########################


def say_name(name="Stranger"):
    print('Hello '+name)
say_name()
say_name('IURII')

#####################################
#return allows us to assing output to new fn
num1 = 10
num2 = 20
def add_fn (num1,num2):
    return num1+num2
print( add_fn(num1,num2) )

""" Find if the word dog in str """

#ROOKIE CODE
s = 'The dogo run away'
def dog_check(s):
    if 'dog' in s.lower():
        return True
    else:
        return False
print( dog_check(s) )

# PRO CODE
def dog_check(s):
    #dog is t   rue boolean
    return 'dog' in s.lower()
print( dog_check(s) )

# PIG LATIN
# if word starts with a vovel, add 'ay' to end
# if starts with nouns 'a,e,i,u", put first letter at the ednd, and add 'ay

def pig_latin(word):
    first_letter = word[0]
    # check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        #word fron index 1 to end
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word
print( pig_latin('word') )
print( pig_latin('apple') )

def even_check(number):
    return number % 2 == 0
print( even_check(20) )

#return true of any number is even
def list_check_even(num_list):
    for num in num_list:
        if num % 2 == 0:
            print(num)
            return True
        else:
            #return False = WRONG
            pass
    return False #correct !
print( list_check_even([1,3,7,4,66,3,2,13]) )



def return_all_even(num_list):
    #placeholder
    even_numbers = [] 

    for num in num_list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            pass
    return even_numbers 
print( return_all_even([1,3,7,4,66,3,2,13]) )