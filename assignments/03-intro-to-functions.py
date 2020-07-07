#https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

#LESSER OF TWO EVENS: Write a function 
#that returns the
#- lesser of two given numbers 
#- if both numbers are even, 
#- but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a,b):
    #both are even
    if a % 2 == 0 and b % 2 == 0:
        return min (a,b)
    else:
    #one or both number are odd!
        return max (a,b)

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(7,5))


#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    words = text.lower().split()
    return words[0][0] == words[1][0]

    
print (animal_crackers('Levelheaded Llama')) #true
print (animal_crackers('Crazy Kangaroo'))              #false

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(num1,num2):
    return (num1 + num2) == 20 or num1 == 20 or num2 == 20

print(makes_twenty(20,10))# --> True
print(makes_twenty(12,8)) #--> True
print(makes_twenty(2,3)) #--> False

# LEVEL 1 PROBLEMS

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    first_half = name[:3]
    rest = name[3:]
    return first_half.capitalize()+rest.capitalize()

print(old_macdonald('macdonald'))

#MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    words = text.split()
    reversed_word_list = words[::-1]
    return ' '.join(reversed_word_list)
print(master_yoda('My name is Juda'))

#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)
print('almost there')
print(almost_there(90)) #--> True
print(almost_there(104)) #--> True
print(almost_there(150)) #--> False
print(almost_there(209)) #--> True

#LEVEL 2 PROBLEMS
# Find 33
#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.


def has_33(nums):
    for three in range(0, len(nums)-1):
        if nums[three] == 3 and nums[three+1] == 3:
        #if nums[i:i+2] == [3,3]
            return True
    return False
print('find 33')
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(input):
    result = ''
    for char in input:
        result += char*3
    return result


print( paper_doll('Hello') ) #--> 'HHHeeellllllooo'
print( paper_doll('Mississippi') ) #--> 'MMMiiissssssiiippppppiii'

#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
        return sum([a,b,c])-10
    else: 
        return 'bust'

print('blackjack')    
print( blackjack(5,6,7) ) # --> 18
print( blackjack(9,9,9) ) #--> 'BUST'
print( blackjack(9,9,11) )#  --> 19

#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num!= 6:
                total +=num
                break
            else:
                add = False
        while not add:
            if num !=9:
                break
            else:
                add = True
                break
    return total
print('summer of 69')
print( summer_69([1, 3, 5])) # --> 9
print( summer_69([4, 5, 6, 7, 8, 9])) #--> 9
print( summer_69([2, 1, 6, 9, 11])) # --> 14
# CHALLENGING PROBLEMS

#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game (code_list):
    sequence = [0,0,7, 'x']
    for num in code_list:
        if num == sequence[0]:
            sequence.pop(0)
    return len(sequence) == 1
print('print 007')
print( spy_game([1,2,4,0,0,7,5]) ) # --> True
print( spy_game([1,0,2,4,0,5,7]) ) # --> True
print( spy_game([1,7,2,0,4,5,0]) ) # --> False

#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
#By convention, 0 and 1 are not prime.
#https://cdn-skill.splashmath.com/panel-uploads/GlossaryTerm/62571c61b87c497caac1aa3228efd5a0/1545882174_List-of-prime-numbers-chart-1-to-100.png

def count_primes(num):
    #base case
    if num < 2:
        return 0
    primes = [2]
    x = 3

    #x is going thru every number un to 
    while x <= num:
        #check if x is prime
        for y in primes
        #for y in range(3,x,2):
            if x%y == 0: #no primes there
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return(len(primes))

print( count_primes(100) ) #25




#PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
# out:   *  
#       * *
#      *****
#      *   *
#      *   *
#HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
#For purposes of this exercise, it's ok if your dictionary stops at "E".
def print_big(letter):
    patterns = {1:'  *  ',
                2:' * * ',
                3:'*   *',
                4:'*****',
                5:'**** ',
                6:'   * ',
                7:' *   ',
                8:'*   * ',
                9:'*    '}
    alphabet = {'A':[1,2,4,3,3],
                'B':[5,3,5,3,5],
                'C':[4,9,9,9,4],
                'D':[5,3,3,3,5],
                'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
print_big('c')
print_big('d')