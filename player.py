from game import Game
from human import Human
from ai import AI
import random


class Player:
    def __init__(self):
        self.player = Player


    def list_of_gestures():
        user_input = input("Enter a choice (rock 0, paper 1 , scissors 2 ): ")
        if user_input in ["Rock", "rock", "r", "R"]:
            user_input = "r"
        elif user_input in ["Paper", "paper", "p", "P"]:
            user_input = "p"
        elif user_input in ["Scissors","scissors", "s", "S"]:
            user_input = "s"
        else :
            print("I don't understand.")

        self.score = 0
        master_list_of_gestures = ["rock", "paper", "scissors"]











