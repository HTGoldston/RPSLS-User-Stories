class Player:
    def __init__(self):
        self.user_name = input("What is your name: ")
        self.score = 0


        self.list_gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.list_gestures[0] = 1
        self.list_gestures[1] = 2
        self.list_gestures[2] = 3
        self.list_gestures[3] = 4
        self.list_gestures[4] = 5

        print(self.user_name, "score", self.score, "Please Select your gestures.")
        self.chosen_gesture = self.list_gestures








