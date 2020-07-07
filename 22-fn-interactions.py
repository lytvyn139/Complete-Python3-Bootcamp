from random import shuffle
mylist = [' ', 'O', ' ']


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input ('pick numbe from the box: | 0 | 1 | 2 | \n')
    return int(guess)

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print('you won')
    else:
        print('nope')
        print(mylist)

mixed_list = shuffle_list(mylist)
guess = player_guess()
check_guess(mixed_list, guess)
