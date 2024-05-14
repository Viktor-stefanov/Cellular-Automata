import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from utils.args import parse_args


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conway's Game of Life")
        self.setup_grid()

    def setup_grid(self):
        args = parse_args()

        if args.fullscreen:
            self.showFullScreen()
        if args.width and args.height:
            self.setGeometry(0, 0, args.width, args.height)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        grid_layout = QGridLayout(central_widget)
        grid_layout.setSpacing(10)  # Space between widgets

        # Parameters for the grid
        grid_size = [
            20,
            60,
        ]  # 50x30 grid # TODO: Convert the list to a more appropriate type
        square_size = 15  # Each square has 5x5 pixels

        # Create and add squares to the layout
        for row in range(grid_size[0]):
            for col in range(grid_size[1]):
                square = QWidget()
                square.setFixedSize(square_size, square_size)
                square.setStyleSheet("background-color: #ded5d5;")
                # Set color (randomly chosen here, but can be specific)
                grid_layout.addWidget(square, row, col)

        # Set grid layout to the central widget
        central_widget.setLayout(grid_layout)

        # Resize the window to fit the grid
        self.resize(
            grid_size[0] * (square_size + 10), grid_size[1] * (square_size + 10)
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
