#!/usr/bin/python3

from PyQt5.QtWidgets import (QApplication, QWidget, 
              QToolTip, QPushButton, QMainWindow)
from PyQt5.QtGui import QFont, QPalette, QBrush, QPixmap
import sys

class TestGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("../test.jpg")))
        self.setPalette(palette)
        new = QPushButton('New Game', self)
        new.resize(new.sizeHint())
        new.move(50,40)
        join = QPushButton('Join Game', self)
        join.resize(join.sizeHint())
        join.move(50,65)
        exit = QPushButton('Exit', self)
        exit.resize(exit.sizeHint())
        exit.move(50,90)
        self.setGeometry(300,300,342,342)
        self.show()

if __name__ == "__main__":
    print("testing compatibilty\n")
    app = QApplication(sys.argv)
    test = TestGUI()
    sys.exit(app.exec_())
