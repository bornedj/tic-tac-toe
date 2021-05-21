#establishing the game class
class Game():
    #user board will be displayed to the players so they can see what choices remain
    user_board = """
    0|1|2
    3|4|5
    6|7|8
    """

    board = [99] * 9
    row_options = ['top', 'middle', 'bottom']
    col_options = ['left, middle', 'right']
    new_game = False

    def __repr__(self):
        return str(self.user_board)

    # def check_winner(self):
    #     if board[0] + board[1] + board[2] == 0:            

    def turn(self, player_turn, pick):
        if player_turn == 0:
            self.board[pick] = 0

        else: 
            self.board[pick] = 1
            
        return self.board

    #function to check game resulted in a tie
    def tie_check(self):
        if 99 not in self.board:
            return True
        else:
            return False
    
    def display_board(self):
        for square in range(len(self.board)):
            if self.board[square] == 0:
                self.user_board = self.user_board.replace(str(square), 'X')
            elif self.board[square] == 1:
                self.user_board = self.user_board.replace(str(square), 'O')
        return "\n{}".format(self.user_board)

        

    



