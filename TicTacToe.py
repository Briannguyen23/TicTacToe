import random
import time


# Tic tac toe game

def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])
    return board


def player_input():

    # Get user input choosing between x or o
    player = input('Which one would you like to choose? X or O: ').upper()
    # One second delay
    time.sleep(1)

    # Assigns X and O to the players. It will return a tuple
    if player == 'X':
        player2 = 'O'
        return (player, player2)
    else:
        player2 = 'X'
        return (player, player2)


def place_maker(board, marker, position):

    # Takes the user input and replace the position on the board
    board[position] = marker


def win_check(board, mark):
    # Check rows, columns and diagonals, if there's three in a row
    return ((board[1] == board[2] == board[3] == mark) or  # checks the first row if there's three in a row
            (board[4] == board[5] == board[6] == mark) or  # checks the second row if there's three in a row
            (board[7] == board[8] == board[9] == mark) or  # checks the third row if there's three in a row
            (board[1] == board[4] == board[7] == mark) or  # check column one left side, if there's three in a row
            (board[2] == board[5] == board[8] == mark) or  # check column two in the middle, if there's three in a row
            (board[3] == board[6] == board[9] == mark) or  # check last column, if there's three in a row
            (board[1] == board[5] == board[9] == mark) or  # checks bottom left to top right if there's three in a row
            (board[7] == board[5] == board[3] == mark))  # checks top left to bottom right if there's three in a row


def space_check(board, position):

    # Check if the position is empty or not
    return board[position] == ' '


def full_board_check(board):

    # Check between 1-9 if the spaces are full or not.
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def choose_first():

    # Randomly pick between 0 and 1 to see who goes first
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def player_choice(board):
    positions = 0
    while positions is not [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, positions):
        positions = int(input('please enter a number between (1-9): '))
        return positions


def replay():
    play_again = input('Would you like to continue? Y or N: ').upper()
    return play_again == 'Y'


print('Hello welcome to the tik tac toe game!')

while True:

    board_test = [' '] * 10
    player1, player2 = player_input()

    # Check who goes first
    turn = choose_first()
    print(turn + ' will go first')

    # Get user input to see if they are ready to play
    play_game = input('Are you ready to play? Y or N: ').upper()
    # One second delay
    time.sleep(1)

    if play_game == 'Y':
        play_on = True
    else:
        play_on = False

    while play_game:
        if turn == 'Player 1':
            # Show the board
            display_board(board_test)
            # Choose a position
            position = player_choice(board_test)
            # Place the marker on the position
            place_maker(board_test, player1, position)

            # Check if they won
            if win_check(board_test, player1):
                display_board(board_test)
                print('Player 1 has won')
                time.sleep(1)
                game_on = False
                break
            else:
                # Check if there's a tie
                if full_board_check(board_test):
                    display_board(board_test)
                    print('The game is a tie')
                    time.sleep(1)
                    game_on = False
                    break
                else:
                    turn = 'Player 2'
        else:
            if turn == 'Player 2':
                # Show the board
                display_board(board_test)
                # Choose a position
                position = player_choice(board_test)
                # Place the marker on the position
                place_maker(board_test, player2, position)

                # Check if they won
                if win_check(board_test, player2):
                    display_board(board_test)
                    print('Player 2 has won')
                    time.sleep(1)
                    game_on = False
                    break
                else:
                    # Check if there's a tie
                    if full_board_check(board_test):
                        display_board(board_test)
                        print('The game is a tie')
                        time.sleep(1)
                        game_on = False
                        break
                    else:
                        turn = 'Player 1'

    # If they do not want to continue, end game.
    if not replay():
        break