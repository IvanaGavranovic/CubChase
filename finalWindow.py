from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import *
from appWindow import *
from PyQt5.QtCore import pyqtSlot

class FinalWindow(QGraphicsScene):                           # <===
    def __init__(self, backToMainMenuMethodFinalWindow, simbaPoints, nalaPoints, parent=None):
        super(FinalWindow, self).__init__(parent)

        screenWidth =  843
        screenHeigth = 643

        self.winner = ""
        self.points = 0

        # self.label = QLabel()
        # self.label.setPixmap(QPixmap('Images/final.jpg'))
        # self.label.setGeometry(0, 0, screenWidth, screenHeigth)
        # self.addWidget(self.label)

        oImage = QPixmap('Images/final.jpg')
        sImage = oImage.scaled(QSize(screenWidth, screenHeigth))  # 850, 685

        self.graphicsPixmapItem = QGraphicsPixmapItem(sImage)
        self.addItem(self.graphicsPixmapItem)
        self.setSceneRect(0, 0, screenWidth, screenHeigth)  # 848,683

        self.labelWinnerIs = QLabel()
        self.labelWinnerIs.setText("WINNER IS")
        self.labelWinnerIs.setGeometry(140, 50, 570, 100)
        self.labelWinnerIs.setFont(QtGui.QFont("Jokerman", 44, QtGui.QFont.Black))
        self.labelWinnerIs.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.addWidget(self.labelWinnerIs)

        if simbaPoints > nalaPoints:
            self.winner = "SIMBA"
            self.points = simbaPoints
        else:
            self.winner = "NALA"
            self.points = nalaPoints

        self.labelWinner = QLabel()
        self.labelWinner.setText(self.winner)
        self.labelWinner.setGeometry(500, 50, 570, 100)
        self.labelWinner.setFont(QtGui.QFont("Jokerman", 44, QtGui.QFont.Black))
        self.labelWinner.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.addWidget(self.labelWinner)

        self.labelScoreIs = QLabel()
        self.labelScoreIs.setText("Score: ")
        self.labelScoreIs.setGeometry(270, 120, 570, 100)
        self.labelScoreIs.setFont(QtGui.QFont("Jokerman", 34, QtGui.QFont.Black))
        self.labelScoreIs.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.addWidget(self.labelScoreIs)

        self.labelScore = QLabel()
        self.labelScore.setText(str(self.points))
        self.labelScore.setGeometry(420, 120, 570, 100)
        self.labelScore.setFont(QtGui.QFont("Jokerman", 34, QtGui.QFont.Black))
        self.labelScore.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.addWidget(self.labelScore)

        pbtn = QPushButton("Main menu")
        pbtn.clicked.connect(backToMainMenuMethodFinalWindow)
        pbtn.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black))
        pbtn.setGeometry(315, 520, 185, 50)
        pbtn.setStyleSheet('QPushButton {background-color: rgba(255, 255, 255, 0); color: white; background-color: rgba(0,0,0,0%)}')
        pbtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.addWidget(pbtn)