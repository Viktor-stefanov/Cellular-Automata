# steps
# 1. Create the toroidal shape of the 2D plane
# 2. Impement the conway protocol (rule set)

class Cell:
    state = False
    
    def __init__(self, state):
        self.state = state

    def change_state(self):
        self.state = not self.state


class Grid:
    pass


if __name__ == "__main__":
    print("ok")
