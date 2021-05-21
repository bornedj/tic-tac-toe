""" Here I will create the classes for a player"""

class Player():
    won = False
    turn = False
    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f"Player is {self.name}."
    
        