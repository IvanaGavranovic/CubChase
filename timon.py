from PyQt5.QtCore import pyqtSignal, QBasicTimer
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QLabel, QGraphicsScene

class Timon(QLabel):

    def __init__(self, h, w, iconWidth):
        super().__init__()
        self.setPixmap(QPixmap("player.png")) # slika timona
        self.step = 10
        self.win_h = h
        self.win_w = w
        self.setStyleSheet("background:white;color:white;")
        self.iconWidth = iconWidth
        self.timer = QBasicTimer()
        self.timer.start(30, self)
        self.direction = 'up'

    def initialize(self):
        self.move(self.win_w/2, self.win_h-2*self.iconWidth)

    def move_up(self):
        y = self.geometry().y()
        self.direction = 'up'
        if y - self.step > -self.iconWidth:
            self.move(self.geometry().x(), self.geometry().y() - self.step)
            trans = QTransform()
            trans.rotate(0)
            self.setPixmap(QPixmap("player.png").transformed(trans))
            self.update()

    def move_down(self):
        y = self.geometry().y()
        self.direction = 'down'
        if y + self.step < self.win_h - 2*self.iconWidth:
            self.move(self.geometry().x(), self.geometry().y() + self.step)
            trans = QTransform()
            trans.rotate(-180)
            self.setPixmap(QPixmap("player.png").transformed(trans))
            self.update()

    def move_left(self):
        x = self.geometry().x()
        self.direction = 'left'
        if x - self.step > 0 - self.iconWidth:
            self.move(self.geometry().x() - self.step, self.geometry().y())
            trans = QTransform()
            trans.rotate(-90)
            self.setPixmap(QPixmap("player.png").transformed(trans))
            self.update()

    def move_right(self):
        x = self.geometry().x()
        self.direction = 'right'
        if x + self.step < self.win_w - 2*self.iconWidth:
            self.move(self.geometry().x() + self.step, self.geometry().y())
            trans = QTransform()
            trans.rotate(90)
            self.setPixmap(QPixmap("player.png").transformed(trans))
            self.update()

 #   def timerEvent(self, a0: 'QTimerEvent'):
 # logika