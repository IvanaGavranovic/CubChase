from PyQt5.QtCore import pyqtSignal, QBasicTimer
from PyQt5.QtGui import QPixmap, QBrush
from PyQt5.QtWidgets import QLabel
from random import randint
import time
from pictures import *
from  colors import *
import board


class Timon(QLabel):
    X = 0
    Y = 0
    Picture = ""
    Speed = 0.3

    def __init__(self, x, y, picture, board):
        super().__init__()
        self.board = board
        self.initTimon(x, y, picture)

    def initTimon(self, x, y, picture):
        self.X = x
        self.Y = y
        self.Picture = picture
        #self.timer = QBasicTimer()
        #self.timer.start(20, self)

    def changePositionTimon(self):
        while True:
            p1 = randint(1,4)
            p2 = randint(1,14)

            if p1 % 4 == 0:
                for x in range(p2):
                    if self.X - 1 < 0:
                        break
                    next_field = self.board.get_field(self.Y, self.X - 1)
                    if next_field.get_color() != BROWN:
                        curr_field = self.board.get_field(self.Y, self.X)
                        self.board.set_field(self.Y, self.X)
                        self.board.set_field(self.Y, self.X - 1, self.Picture)
                        self.X = self.X - 1
                        time.sleep(self.Speed)
                    else:
                        break
            if p1 % 4 == 1:
                for x in range(p2):
                    if self.X + 1 > 20:
                        break
                    next_field = self.board.get_field(self.Y, self.X + 1)
                    if next_field.get_color() != BROWN:
                        curr_field = self.board.get_field(self.Y, self.X)
                        self.board.set_field(self.Y, self.X)
                        self.board.set_field(self.Y, self.X + 1, self.Picture)
                        self.X = self.X + 1
                        time.sleep(self.Speed)
                    else:
                        break
            if p1 % 4 == 2:
                for x in range(p2):
                    if self.Y - 1 < 0:
                        break
                    next_field = self.board.get_field(self.Y - 1, self.X)
                    if next_field.get_color() != BROWN:
                        curr_field = self.board.get_field(self.Y, self.X)
                        self.board.set_field(self.Y, self.X)
                        self.board.set_field(self.Y - 1, self.X, self.Picture)
                        self.Y = self.Y - 1
                        time.sleep(self.Speed)
                    else:
                        break
            if p1 % 4 == 3:
                for x in range(p2):
                    if self.Y + 1 > 15:
                        break
                    next_field = self.board.get_field(self.Y + 1, self.X)
                    if next_field.get_color() != BROWN:
                        curr_field = self.board.get_field(self.Y, self.X)
                        self.board.set_field(self.Y, self.X)
                        self.board.set_field(self.Y + 1, self.X, self.Picture)
                        self.Y = self.Y + 1
                        time.sleep(self.Speed)
                    else:
                        break





