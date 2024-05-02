import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget

# 1. Create the toroidal shape of the 2D plane
# 2. Impement the conway protocol (rule set)

# Maybe make it web based frontend written in modern react (maybe even next.js)
# Two backends Backend in 1. Django & 2. Spring Boot 

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600
SQUARES_VERTICALLY = SCREEN_HEIGHT // 5
SQUARES_HORIZONTALLY = SCREEN_WIDTH // 5

class Cell:
    def __init__(self, state: bool):
        self.state = state

    def change_state(self) -> None:
        self.state = not self.state

class Grid(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Conway's game of life")
        self.setGeometry(100, 100, 800, 600)

        self.setup_grid()

    def setup_grid(self):
        grid = QGridLayout()
        self.setLayout(grid)

        buttons = []
        for i in range(3):
            for j in range(3):
                button = QPushButton(f"Button {i}, {j}", )
                buttons.append(button)
                grid.addWidget(button, i, j)
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Grid()
    window.show()
    sys.exit(app.exec())
