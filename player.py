class Player:
    def __init__(self):
        self.name = "Player 1"
        self.score = 0
        self.current_gesture = None
        self.list_of_gestures = []

    def choose_gesture(self):
        keep_running = True

        while keep_running:
            print(f"{self.name} - enter the number to play from the following gestures")
            i = 1
            for gesture in self.list_of_gestures:
                print(f"{i}: {gesture.name}")
                i += 1

            try:
                chosen_gesture = int(input("Enter Number: "))
                self.current_gesture = self.list_of_gestures[chosen_gesture]
                break
            except ValueError:
                print("Invalid Input " + ValueError)