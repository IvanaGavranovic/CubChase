import sys
from gameController import *
from board import Board
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QFrame, QDesktopWidget, QApplication, QWidget, QHBoxLayout, QLabel, QFileDialog


if __name__ == '__main__':
    app = QApplication([])
    gc = GameController()

    thread1 = Thread(target=gc.timon_movement)
    thread1.daemon = True
    thread1.start()

    thread2 = Thread(target=gc.pumba_movement)
    thread2.daemon = True
    thread2.start()

    sys.exit(app.exec_())


