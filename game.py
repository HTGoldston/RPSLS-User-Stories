from ai import AI
from human import Human

class Game:
    def __init__(self):
        self.player_one = None

        self.player_two =None


    def Welcome(self):
        print("Rock-Paper-Scissors")
        print("Welcome")
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
        self.player_two_options = int(input("enter a choice for Opponent (Computer 1, Human 2):"))
        self.player_two_ai = AI()
        self.player_two_human = Human()

        if self.player_two_options == 1:
            print("Human vs Computer")
        elif self.player_two_ai == 2:
            print("Human vs Human")


        self.player_one.choosing_gesture()
        #self.player_two.chosen_gesture() == self.player_one.chosen_gesture

        self.msg_player_1_win = "Player 1 wins!"
        self.msg_player_2_win = "Player 2 wins!"

        if self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == "Paper":
            print("Paper covers Rock")
            print(self.msg_player_2_win)
        self.player_two.score += 1
        if self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == "Scissors":
            print("Rock crushes Scissors")
            print(self.msg_player_1_win)
        self.player_one.score += 1
        if self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == "Lizard":
            print("Rock crushes Lizard")
            print(self.msg_player_2_win)
        self.player_two.score += 1
        if self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == "Spock":
            print("Spock vaporizes Rock")
            print(self.msg_player_2_win)
        self.player_two.score += 1
        if self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == "Rock":
            print("Game is was a tie")
        self.player_one.score += 0
        self.player_two.score += 0
        if self.player_one.chosen_gesture == "Paper" and self.player_two.chosen_gesture == "Scissors":
            print("Scissors cuts Paper")
            print(self.msg_player_2_win)
        self.player_two.score += 1
        if self.player_one.chosen_gesture == "Paper" and self.player_two.chosen_gesture == "Rock":
            print("Paper covers Rock")
            print(self.msg_player_1_win)
        self.player_one.score += 1
        if self.player_one.chosen_gesture == "Paper" and self.player_two.chosen_gesture == "Lizard":
            print("Lizard eats Paper")
            print(self.msg_player_2_win)
        self.player_two.score += 1
        if self.player_one.chosen_gesture == "Paper" and self.player_two.chosen_gesture == "Spock":
            print("Paper disproves Spock")
            print(self.msg_player_1_win)
        self.player_one.score += 1
        if self.player_one.chosen_gesture == "Paper" and self.player_two.chosen_gesture == "Paper":
            print("Game is was a tie")
        self.player_one.score += 0
        self.player_two.score += 0
        if self.player_one.chosen_gesture == "Scissors" and self.player_two.chosen_gesture == "Rock":
            print(self.msg_player_2_win)
        self.player_two.score += 1
        if self.player_one.chosen_gesture == "Scissors" and self.player_two.chosen_gesture == "Paper":
            print(self.msg_player_1_win)
        self.player_one.score += 1
        if self.player_one.chosen_gesture == "Scissors" and self.player_two.chosen_gesture == "Lizard":
            print("Scissors decapitates Lizard")
            print(self.msg_player_1_win)
        self.player_one.score += 1
        if self.player_one.chosen_gesture == "Scissors" and self.player_two.chosen_gesture == "Spock":
            print(self.msg_player_2_win)
        self.player_two.score += 1
        if self.player_one.chosen_gesture == "Scissors" and self.player_two.chosen_gesture == "Scissors":
            print("Game is was a tie")
        self.player_one.score += 1
        self.player_two.score += 1
        if self.player_one.chosen_gesture == "Lizard" and self.player_two.chosen_gesture == "Scissors":
            print("Scissors decapitates Lizard")
            print(self.msg_player_2_win)
        self.player_two.score += 1
        if self.player_one.chosen_gesture == "Lizard" and self.player_two.chosen_gesture == "Paper":
            print("Lizard eats Paper")
            print(self.msg_player_1_win)
        self.player_one.score += 1
        if self.player_one.chosen_gesture == "Lizard" and self.player_two.chosen_gesture == "Rock":
            print("Rock crushes Lizard")
            print(self.msg_player_2_win)
        self.player_two.score += 1
        if self.player_one.chosen_gesture == "Lizard" and self.player_two.chosen_gesture == "Spock":
            print("Lizard poisons Spock")
            print(self.msg_player_2_win)
        self.player_two.score += 1
        if self.player_one.chosen_gesture == "Lizard" and self.player_two.chosen_gesture == "Lizard":
            print("Game is was a tie")
        self.player_one.score += 0
        self.player_two.score += 0
        if self.player_one.chosen_gesture == "Spock" and self.player_two.chosen_gesture == "Paper":
            print("Paper disproves Spock")
            print(self.msg_player_2_win)
        self.player_two.score += 1
        if self.player_one.chosen_gesture == "Spock" and self.player_two.chosen_gesture == "Scissors":
            print("Spock smashes Scissors")
            print(self.msg_player_1_win)
        self.player_one.score += 1
        if self.player_one.chosen_gesture == "Spock" and self.player_two.chosen_gesture == "Rock":
            print("Spock vaporizes Rock")
            print(self.msg_player_1_win)
        self.player_two.score += 1
        if self.player_one.chosen_gesture == "Spock" and self.player_two.chosen_gesture == "Lizard":
            print("Lizard poisons Spock")
            print(self.msg_player_2_win)
        self.player_two.score += 1
        if self.player_one.chosen_gesture == "Spock" and self.player_two.chosen_gesture == "Spock":
            print("Game is was a tie")
        self.player_one.score += 0
        self.player_two.score += 0

