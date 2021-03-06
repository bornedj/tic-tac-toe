#this will import classes and will be where the game is played
import random
import sys
from player import Player
from game_class import Game


#function that will run for every new game
def main(player_one = '', player_two =''):
    #create a new instance of a game
    game = Game()

    if player_one == '' or player_two == '':
    #take in inputs to set up the game
        print("Welcome to tic tac toe. Please enter player names and then we will decide who goes first.")
        player_one = Player(input("Please enter player one's name: "))
        player_two = Player(input("Please enter player two's name: "))

    player_one.guess = int(input(f'Alright {player_one} please guess a number between 1 and 50 inclusive: '))
    player_two.guess = int(input(f'Alright {player_two} please guess a number between 1 and 50 inclusive: '))

    rand_num = random.randint(1, 50)

    differences = [abs(rand_num - player_one.guess), abs(rand_num - player_two.guess)]
    if differences[0] < differences[1]:
        game_turns(game, player_one, player_two, 0)
    elif differences[0] > differences[1]:
        game_turns(game, player_one, player_two, 1)

    print(game)
    # print(tic_tac_toe_board)


# defining a function that will use recursion until the game completes to alternate turns  
def game_turns(game, player_one, player_two, player_turn):

    if player_turn == 0: #player ones turn
        print(game)
        pick = int(input(f"{player_one.name} choose your square based on the board above (0-8): "))
        if game.board[pick] == 99:#checks if pick is eligible
            game.turn(0, pick)#assign pick
        else:
            print('\nPlease select a square that hasn\'t been selected')
            game_turns(game, player_one, player_two, 0) #loop through again
        
        #tie check
        if game.tie_check():
            another = input('The game was a tie. If you would like to play again please type "yes" if not type "q": ').lower()
            if another == 'yes':
                main(player_one, player_two)
            else:
                sys.exit()

        #win check
        if game.win_check() == 1:
            print(f"{player_one.name} has one.")
            player_one.update_wins()
            print(player_one.display_wins())
            another = input('If you would like to play again please type "yes" if not type "q": ').lower()
            if another == 'yes':
                main(player_one, player_two)
            else: sys.exit()


        #next players turn after winner/tie check
        game_turns(game, player_one, player_two, 1)

    elif player_turn == 1: #player twos turn
        print(game)
        pick = int(input(f"{player_two.name} choose your square based on the board above (0-8): "))
        if game.board[pick] == 99:#checks if eligible
            game.turn(1, pick)
        else:
            print('\nPlease select a square that hasn\'t been selected')
            game_turns(game, player_one, player_two, 1) # loops through again
        
        #tie check
        if game.tie_check():
            another = input('The game was a tie. If you would like to play again please type "yes" if not type "q": ').lower()
            if another == 'yes':
                main(player_one, player_two)
            else: sys.exit()

        #win check
        if game.win_check() == 2:
            print(f"{player_two.name} has won.")
            player_two.update_wins()
            print(player_two.display_wins())
            another = input('If you would like to play again please type "yes" if not type "q": ').lower()
            if another == 'yes':
                main(player_one, player_two)
            else: sys.exit()

        #next players turn after winner/tie check
        game_turns(game, player_one, player_two, 0)


        

main()
# print(tic_tac_toe_board)