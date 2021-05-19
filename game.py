

from ai import AI
from human import Human

class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None


    def Welcome(self):
        print("Welcome ")
        print( "Welcome to rock, paper, scissors.")
        self.player_one = Human()
        self.player_two = AI()
        self.player_one.choosing_gesture()
        self.player_two.choosing_gesture()
        if self.player_one.chosen_gesture =="Rock" and self.player_two.chosen_gesture == "Paper":
            print("Player 2 wins!")
            self.player_two.score += 1
        if self.player_one.chosen_gesture == "Scissors" and self.player_two.chosen_gesture == "Rock":
            print("Player 2 wins!")
            self.player_two.score += 1
        if self.player_one.chosen_gesture ==





