import sys
from board import Board
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QFrame, QDesktopWidget, QApplication, QWidget, QHBoxLayout, QLabel, QFileDialog


if __name__ == '__main__':
    app = QApplication([])
    b = Board()
    sys.exit(app.exec_())