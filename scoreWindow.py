from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import *

class Window3(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Score window")
        self.setGeometry(0, 0, 800, 550)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Images/score.png'))
        self.label.setGeometry(0, 0, 800, 550)

        # if(lives < 0)
        # Final Window
        # else
        # Playing Window

        self.labelPlayers = QLabel(self)
        self.labelPlayers.setText("Players")
        self.labelPlayers.setGeometry(230, 120, 133, 50)
        self.labelPlayers.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black));
        self.labelPlayers.setStyleSheet("color: rgba(255, 255, 255, 255);")

        self.labelPlayers = QLabel(self)
        self.labelPlayers.setText("Simba")
        self.labelPlayers.setGeometry(250, 200, 133, 50)
        self.labelPlayers.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black));
        self.labelPlayers.setStyleSheet("color: rgba(255, 255, 255, 255);")

        self.labelPlayers = QLabel(self)
        self.labelPlayers.setText("Nala")
        self.labelPlayers.setGeometry(250, 270, 133, 50)
        self.labelPlayers.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black));
        self.labelPlayers.setStyleSheet("color: rgba(255, 255, 255, 255);")

        self.labelPlayers = QLabel(self)
        self.labelPlayers.setText("Points")
        self.labelPlayers.setGeometry(375, 120, 133, 50)
        self.labelPlayers.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black));
        self.labelPlayers.setStyleSheet("color: rgba(255, 255, 255, 255);")

        self.labelPlayers = QLabel(self)
        self.labelPlayers.setText("2000")
        self.labelPlayers.setGeometry(385, 200, 133, 50)
        self.labelPlayers.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black));
        self.labelPlayers.setStyleSheet("color: rgba(255, 255, 255, 255);")

        self.labelPlayers = QLabel(self)
        self.labelPlayers.setText("3700")
        self.labelPlayers.setGeometry(385, 270, 133, 50)
        self.labelPlayers.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black));
        self.labelPlayers.setStyleSheet("color: rgba(255, 255, 255, 255);")

        self.labelPlayers = QLabel(self)
        self.labelPlayers.setText("Lives")
        self.labelPlayers.setGeometry(495, 120, 133, 50)
        self.labelPlayers.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black));
        self.labelPlayers.setStyleSheet("color: rgba(255, 255, 255, 255);")

        self.labelPlayers = QLabel(self)
        self.labelPlayers.setText("3")
        self.labelPlayers.setGeometry(520, 200, 133, 50)
        self.labelPlayers.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black));
        self.labelPlayers.setStyleSheet("color: rgba(255, 255, 255, 255);")

        self.labelPlayers = QLabel(self)
        self.labelPlayers.setText("1")
        self.labelPlayers.setGeometry(520, 270, 133, 50)
        self.labelPlayers.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black));
        self.labelPlayers.setStyleSheet("color: rgba(255, 255, 255, 255);")
        self.labelPlayers = QLabel(self)

        self.labelPlayers.setText("Continue")
        self.labelPlayers.setGeometry(355, 355, 150, 50)
        self.labelPlayers.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black));
        self.labelPlayers.setStyleSheet("color: rgba(255, 255, 255, 255);")
        cbtn = QPushButton(self)
        cbtn.clicked.connect(self.window4)
        cbtn.setGeometry(355, 355, 150, 50)
        cbtn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        cbtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def window4(self):  # <===
            self.w = Window4()
            self.w.show()
            self.hide()

