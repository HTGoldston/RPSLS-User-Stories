import random
from player import Player

class AI (Player):

    def choosing_gesture(self):
        AI.score= 0
        self.chosen_gesture = random.choice(self.list_gestures)

