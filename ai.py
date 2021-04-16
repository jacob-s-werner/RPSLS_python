import random

from player import Player


class AI(Player):
    def __init__(self):
        self.name = "ComputerAI"

    def choose_gesture(self):
        self.current_gesture = random.randint(0, len(self.list_of_gestures))
        self.print_gesture_chosen()
