#this will import classes and will be where the game is played
import random
from player import Player
tic_tac_toe_board = """_|_|_
_|_|_
 | |
 """

#function that will run for every new game
def game():
    print(tic_tac_toe_board, "\nWelcome to tic tac toe. Please enter player names and then we will decide who goes first.")
    player_one = Player(input("Please enter player one's name: "))
    player_two = Player(input("Please enter player two's name: "))

    player_one.guess = int(input(f'Alright {player_one} please guess a number between 1 and 50 inclusive: '))
    player_two.guess = int(input(f'Alright {player_two} please guess a number between 1 and 50 inclusive: '))

    rand_num = random.randint(1, 50)

    differences = [abs(rand_num - player_one.guess), abs(rand_num - player_two.guess)]
    if differences[0] < differences[1]:
        print('player 1')
    else: print('player 2')

        


'''
player_one.row = input(f'{player_one.name} please select the row (top, middle, bottom).').lower()
player_one.col = input(f'{player_one.name} please select the column (left, middle, right).').lower()
player_one.two = input(f'{player_one.name} please select the row (top, middle, bottom).').lower()
player_one.col = input(f'{player_one.name} please select the column (left, middle, right).').lower()
'''

game()
# print(tic_tac_toe_board)