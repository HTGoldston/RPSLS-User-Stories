import random
from player import Player

class AI (Player):
    def chosen_gesture(self):
        self.chosen_gesture = random.choice(self.list_gestures)

