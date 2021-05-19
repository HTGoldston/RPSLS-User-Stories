from ai import AI
from human import Human

class Game:
    def __init__(self):
        self.player_one = None

        self.player_two =None


    def Welcome(self):
        print("Rock-Paper-Scissors")
        print( "Welcome")
        print()
        print("Instructions for Rock-Paper-Scissors : ")
        print()
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")
        print()

        self.player_one = Human()
        self.player_two = int(input("Enter a choice (Human 1, Computer 2):"))
        if self.player_two == 1:
            print("Human vs Human")
        if self.player_two == 2:
            print("Human vs Computer")


             #("Human vs Human")

        self.player_one.choosing_gesture()
        self.player_two.chosen_gesture()


        if self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == "Paper":
            print("Player 2 wins!")
        self.player_two.score += 1
        if self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == "Scissors":
            print("Player 1 wins!")
        self.player_one.score += 1
        if self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == "Rock":
            print("Game is was a tie")
        self.player_one.score += 1
        self.player_two.score += 1
        if self.player_one.chosen_gesture == "Paper" and self.player_two.chosen_gesture == "Scissors":
            print("Player 2 wins!")
        self.player_two.score += 1
        if self.player_one.chosen_gesture == "Paper" and self.player_two.chosen_gesture == "Rock":
            print("Player 1 wins!")
        self.player_one.score += 1
        if self.player_one.chosen_gesture == "Paper" and self.player_two.chosen_gesture == "Paper":
            print("Game is was a tie")
        self.player_one.score += 1
        self.player_two.score += 1
        if self.player_one.chosen_gesture == "Scissors" and self.player_two.chosen_gesture == "Rock":
            print("Player 2 wins!")
        self.player_two.score += 1
        if self.player_one.chosen_gesture == "Scissors" and self.player_two.chosen_gesture == "Paper":
            print("Player 1 wins!")
        self.player_one.score += 1
        if self.player_one.chosen_gesture == "Scissors" and self.player_two.chosen_gesture == "Scissors":
            print("Game is was a tie")
        self.player_one.score += 1
        self.player_two.score += 1



