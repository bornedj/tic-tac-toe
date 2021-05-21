""" Here I will create the classes for a player"""

class Player():
    won = False
    turn = False
    
    #these will check to see if a player has one
    row_top = ['','','']
    row_middle = ['','','']
    row_bottom = ['','','']

    col_left = ['','','']
    col_middle = ['','','']
    col_right = ['','','']

    tl_diag = ['','','']
    tr_diag = ['','','']


    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f"Player is {self.name}."
    
        