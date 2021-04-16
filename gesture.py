class Gesture:
    def __init__(self, name):
        self.name = name
        self.beats_list = []

    def add_to_beats_list(self, gesture1, gesture2):
        self.beats_list.append(gesture1)
        self.beats_list.append(gesture2)

