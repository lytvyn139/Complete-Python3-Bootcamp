# def display(row1, row2, row3):
#     print(row1)
#     print(row2)
#     print(row3)
# row1 = [' ',' ',' ']
# row2 = [' ',' ',' ']
# row3 = [' ',' ',' ']

# display(row1, row2, row3)    
# print('\n')    
# row2[1] = 'X'
# display(row1, row2, row3)

# position_index = int(input('Choose and index position: '))
# print(result, type(position_index))

""" PICK 1-10 logic """
# def user_choice():
#     choice = 'WRONG'
#     acceptable_range = range(0,10)
#     within_range = False

#     while choice.isdigit() == False or within_range == False:
#         choice = input('Please enter value 0-10: ')
#         #digit check
#         if choice.isdigit() == False:
#             print('Sorry it\'s not a digit')
#         #range check
#         #if choice.isdigit() == True:
#         if choice.isdigit():
#             if (int(choice) in acceptable_range):
#                 within_range = True
#             else:
#                 print('Sorry the digit is')
#                 pass
#                 #within_range = False
#     return int(choice)

# print( user_choice() ) 

# game_list = [0,1,2]
# def display_game(game_list):
#     print('here is curent list')
#     print(game_list)

# display_game(game_list)

# def position_choice():
#     choice = 'invalid'
#     acceptable_values = ['0','1','2']
#     while choice not in acceptable_values:
#         choice = input('Pick a position (0,1,2): ')
#         if choice not in acceptable_values:
#             print('Sorry invalid choice')
#     return int(choice)
# position_choice()

# def replacement_choice(game_list, position):
#     user_placement = input('Type a string to place at position: ')
#     game_list[position] = user_placement
#     return game_list
# replacement_choice(game_list, 1)
import random

board = ['#','X','O','X','O','X','O','X','O','X']
def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

#randomly decide which player goes first.
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def player_input():
    """
        OUTPUT = (Player 1 marker, Player 2 marker)
    """
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: pick X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else: 
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker


#returns a boolean indicating whether a space on the board is freely available.
def space_check(board, position):
    return board[position] == ' '

#  fn that checks if the board is full and returns a boolean value. True if full, False otherwis
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    #board is full when return false
    return True

# asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if its a free position. If it is, then return the position for later use.
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        print('\n'*100)
    return position

# fn takes in a board and checks to see if someone has won.
def win_check(board,mark):
    return (
    (board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark))   # diagonal

#function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

# START
print('Welcome to Tic Tac Toe!')
while True:
    # Reset the board

    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break