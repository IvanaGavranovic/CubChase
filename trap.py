from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal, QEventLoop, QTimer
from pictures import *


class Trap(QLabel):

    isActive = False
    activeTrap = pyqtSignal()

    def __init__(self, x, y, picture, board, t):
        super().__init__()
        self.board = board
        self.initTrap(x, y, picture, id, t)

    def initTrap(self, x, y, picture, id, t):
        self.X = x
        self.Y = y
        self.ID = id
        self.Picture = picture
        self.activeTrap.connect(self.active)
        self.Trap = t
        self.Label = QLabel()
        self.Label.move(x, y)


    def trap(self, enemy):
        print("")

    def active(self):
        self.isActive= True
        self.picture(TRAP_ACTIVE)
        loop = QEventLoop()
        QTimer.singleShot(10000, loop.quit)
        loop.exec_()
        self.picture(TRAP_PASSIVE)
        self.isActive = False
