from PyQt5.QtCore import pyqtSignal, QBasicTimer
from PyQt5.QtGui import QPixmap, QBrush
from PyQt5.QtWidgets import QLabel
from random import randint
import time

import board


class Timon(QLabel):
    Width = 40
    Height = 40
    X = 0
    Y = 0
    CanMove = True
    Picture = ""
    Speed = 0.5
    Move = pyqtSignal()

    def __init__(self, parent, x, y, picture):
        super().__init__(parent)

        self.initTimon( parent, x, y, picture)

    def initTimon(self, parent, x, y, picture):
        self.resize(40,40)
        self.X = x
        self.Y = y
        self.Picture = picture
        self.Move.connect(self.moveTimon)
        PixmapTimon = QPixmap(picture)
        PixmapResizeTimon = PixmapTimon.scaled(self.Width, self.Height)
        self.setPixmap(PixmapResizeTimon)
        self.timer = QBasicTimer()
        self.timer.start(20, self)
        self.move(x,y)
        board.Board.fields[1][2].setBrush(QBrush(QPixmap("imgTimon.png")))

        print(picture)

    def updatePosition(self, x, y):
        self.X = x
        self.Y = y
        self.move(x, y)

    def changePosition(self):
        while True:
            p1 = randint(1,4)
            p2 = randint(1,15)

            if p1 % 4 == 0:
                for x in range(p2):
                    #if (self.X - 40, self.Y) not in board.Board.
                        self.X = self.X-40
                        time.sleep(self.Speed)
            if p1 % 4 == 1:
                for x in range(p2):
                    # if (self.X - 40, self.Y) not in board.Board.
                    self.X = self.X + 40
                    time.sleep(self.Speed)
            if p1 % 4 == 2:
                for x in range(p2):
                    # if (self.X - 40, self.Y) not in board.Board.
                    self.Y = self.Y - 40
                    time.sleep(self.Speed)
            if p1 % 4 == 3:
                for x in range(p2):
                    # if (self.X - 40, self.Y) not in board.Board.
                    self.Y = self.Y + 40
                    time.sleep(self.Speed)

    def moveTimon(self):
        self.move(self.X, self.Y)

    def timerEvent(self, event):
        self.Move.emit()




