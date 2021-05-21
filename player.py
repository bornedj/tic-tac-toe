""" Here I will create the classes for a player"""

class Player():
    wins = 0    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f"Player is {self.name}."
    
        