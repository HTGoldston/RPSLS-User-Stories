class Player:
    def __init__(self):
        self.user_name = input("What is your name: ")
        print(self.user_name), "Please Select your gestures."
        self.list_gestures = ["Rock", "Paper", "Scissors","Lizard", "Spock"]
        self.chosen_gesture = ""
        self.score = 0
