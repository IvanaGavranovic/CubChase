from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal, QEventLoop, QTimer
from pictures import *


class Trap(QLabel):

    Trap = 1
    isActive = False
    activeTrap = pyqtSignal()

    def __init__(self, x, y, picture, board, id, t):
        super().__init__()
        self.board = board
        self.initTrap(x, y, picture, id, t)

    def initTrap(self, x, y, picture, id, t):
        self.X = x
        self.Y = y
        self.Picture = picture
        self.ID = id
        self.Trap = t
        self.activeTrap.connect(self.active)

    def trap(self, enemy):
        print("")

    def active(self):
        self.isActive= True
        self.Picture = TRAP_ACTIVE
        loop = QEventLoop()
        QTimer.singleShot(10000, loop.quit)
        loop.exec_()
        self.Picture = TRAP_PASSIVE
        self.isActive = False
