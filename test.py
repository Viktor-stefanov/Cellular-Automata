import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel

class ChessBoard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess Board")
        self.setGeometry(100, 100, 800, 600)
        self.setup_grid()

    def setup_grid(self):
        layout = QGridLayout()
        self.setLayout(layout)

        board_size = 50
        square_size = 5 # Adjust this according to your requirements

        for row in range(board_size):
            for col in range(board_size):
                label = QLabel()
                label.setFixedSize(square_size, square_size)
                if (row + col) % 2 == 0:
                    label.setStyleSheet("background-color: white;")
                else:
                    label.setStyleSheet("background-color: black;")
                layout.addWidget(label, row, col)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChessBoard()
    window.show()
    sys.exit(app.exec())
 