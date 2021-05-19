from player import Player

class Human(Player):

    def choosing_gesture(self):
        user_input = int(input("Enter a choice (rock 0, paper 1 , scissors 2 ): "))
        self.chosen_gesture = self.list_gestures[user_input]