from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import *
from scoreWindow import *


class MainWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(0, 0, 800, 550)
        self.setWindowTitle("Start window")

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Images/background.png'))
        self.label.setGeometry(0, 0, 800, 550)

        qbtn = QPushButton(self)
        qbtn.clicked.connect(self.close)
        qbtn.setGeometry(330, 170, 120, 50)
        qbtn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        qbtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        pbtn = QPushButton(self)
        pbtn.clicked.connect(self.window2)
        pbtn.setGeometry(330, 100, 133, 50)
        pbtn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        pbtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.show()

    def window2(self):  # <===
        self.w = Window2()
        self.w.show()
        self.hide()


class Window2(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Playing window")
        self.setGeometry(0, 0, 800, 550)

        self.label = QLabel(self);
        #self.label.setPixmap(QPixmap('Images/map.png'))
        self.label.setGeometry(0, 0, 800, 550)

        pbtn = QPushButton("Show score table",self)
        pbtn.clicked.connect(self.window3)
        pbtn.setGeometry(330, 100, 133, 50)
        pbtn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        pbtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def window3(self):  # <===
            self.w = Window3()
            self.w.show()
            self.hide()

