import random
from player import Player

class AI (Player):

    def choosing_gesture(self):
        AI.score= 0
        self.chosen_gesture = random.choice(self.list_gestures)

    # choice.random cycle or loops through a set list of 3
   #choice(dict(rock=[0], paper=[1], scissors=[2]))
    #print(random)
    #def super(self):
        #print()


    #def chosing_gesture_random(self): ['r','p', 's'])
    #    self.chosing_gesture_random(
     #       self = [0,1,2]
    #    print(chosing_gesture_random(0))