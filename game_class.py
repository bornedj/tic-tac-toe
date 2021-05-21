#establishing the game class
class Game():
    
    #init
    def __init__(self):     
        self.user_board = """
        0|1|2
        3|4|5
        6|7|8
        """

        self.board = [99] * 9

    #turn method updates the keeps track of winning
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

    #defining the win method
    def win_check(self):
        if self.board[0] + self.board[1] + self.board[2] == 0:
            return 1
        elif self.board[3] + self.board[4] + self.board[5] == 0:
            return 1
        elif self.board[6] + self.board[7] + self.board[8] == 0:
            return 1
        elif self.board[0] + self.board[3] + self.board[6] == 0: return 1
        elif self.board[1] + self.board[4] + self.board[7] == 0: return 1
        elif self.board[2] + self.board[5] + self.board[8] == 0: return 1
        elif self.board[0] + self.board[4] + self.board[8] == 0: return 1
        elif self.board[2] + self.board[4] + self.board[6] == 0: return 1
        elif self.board[0] + self.board[1] + self.board[2] == 3:
            return 2
        elif self.board[3] + self.board[4] + self.board[5] == 3:
            return 2
        elif self.board[6] + self.board[7] + self.board[8] == 3:
            return 2
        elif self.board[0] + self.board[3] + self.board[6] == 3: return 2
        elif self.board[1] + self.board[4] + self.board[7] == 3: return 2
        elif self.board[2] + self.board[5] + self.board[8] == 3: return 2
        elif self.board[0] + self.board[4] + self.board[8] == 3: return 2
        elif self.board[2] + self.board[4] + self.board[6] == 3: return 2
        else: return 0

        
    
    #function that displays current board to let users know where they can play
    def __repr__(self):
        for square in range(len(self.board)):
            if self.board[square] == 0:
                self.user_board = self.user_board.replace(str(square), 'X')
            elif self.board[square] == 1:
                self.user_board = self.user_board.replace(str(square), 'O')
        return "\n{}".format(self.user_board)

        

    



