import sys
import math
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QGridLayout, QHBoxLayout, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor


SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600
VERTICAL_SQUARES = math.gcd(SCREEN_HEIGHT, SCREEN_WIDTH)
HORIZONTAL_SQUARES = math.gcd(VERTICAL_SQUARES, 2)

# 1. Create the toroidal shape of the 2D plane
# 2. Impement the conway protocol (rule set)

# Maybe make it web based frontend written in modern react (maybe even next.js)
# Two backends Backend in 1. Django & 2. Spring Boot 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minimalist QLabel Example")
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout()
        
        # LCD 200 = 2
        # 200 * 2 = 400
        for i in range(VERTICAL_SQUARES):
            row_layout = QHBoxLayout()
            for j in range(HORIZONTAL_SQUARES):
                label = QLabel()
                label.setFixedSize(5, 5)
                if (i + j) % 2 == 0:
                    label.setStyleSheet("background-color: white")         
                else:
                    label.setStyleSheet("background-color: black")         
                row_layout.addWidget(label)
            layout.addLayout(row_layout)
        self.central_widget.setLayout(layout)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
