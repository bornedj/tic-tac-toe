""" Here I will create the classes for a player"""

class Player():
    wins = 0    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f"Player is {self.name}."
        
    def update_wins(self):
        self.wins += 1

    def update_name(self, new_name):
        self.name = new_name

    def display_wins(self):
        return "{} has won {} time(s).".format(self.name, self.wins)
    
        