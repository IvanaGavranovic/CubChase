from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import *
from appWindow import *
from PyQt5.QtCore import pyqtSlot

class FinalWindow(QGraphicsScene):                           # <===
    def __init__(self, backToMainMenuMethodFinalWindow, parent=None):
        super(FinalWindow, self).__init__(parent)

        screenWidth =  800
        screenHeigth = 550

        self.setSceneRect(0, 0, screenWidth, screenHeigth)

        self.label = QLabel()
        self.label.setPixmap(QPixmap('Images/final.jpg'))
        self.label.setGeometry(0, 0, 800, 550)
        self.addWidget(self.label)

        self.labelWinner = QLabel()
        self.labelWinner.setText("WINNER IS SIMBA")
        self.labelWinner.setGeometry(130, 50, 570, 100)
        self.labelWinner.setFont(QtGui.QFont("Jokerman", 44, QtGui.QFont.Black))
        self.labelWinner.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.addWidget(self.labelWinner)

        self.labelWinner = QLabel()
        self.labelWinner.setText("Score: ")
        self.labelWinner.setGeometry(250, 120, 570, 100)
        self.labelWinner.setFont(QtGui.QFont("Jokerman", 34, QtGui.QFont.Black))
        self.labelWinner.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.addWidget(self.labelWinner)

        self.labelWinner = QLabel()
        self.labelWinner.setText("4000")
        self.labelWinner.setGeometry(400, 120, 570, 100)
        self.labelWinner.setFont(QtGui.QFont("Jokerman", 34, QtGui.QFont.Black))
        self.labelWinner.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.addWidget(self.labelWinner)

        pbtn = QPushButton("Main menu")
        pbtn.clicked.connect(backToMainMenuMethodFinalWindow)
        pbtn.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black))
        pbtn.setGeometry(295, 440, 185, 50)
        pbtn.setStyleSheet('QPushButton {background-color: rgba(255, 255, 255, 0); color: white; background-color: rgba(0,0,0,0%)}')
        pbtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.addWidget(pbtn)