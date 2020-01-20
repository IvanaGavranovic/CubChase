from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import *
from finalWindow import *
from PyQt5.QtCore import pyqtSlot, QSize


class ScoreWindow(QGraphicsScene):                           # <===
    def __init__(self, startMethodScoreWindow, continueMethodScoreWindow, simbaPoints, simbaLives, nalaPoints, nalaLives, parent=None):
        super(ScoreWindow, self).__init__(parent)

        screenWidth = 843
        screenHeigth = 643

        # self.label = QLabel()
        # self.label.setPixmap(QPixmap('Images/score.png'))
        # self.label.setGeometry(0, 0, screenWidth, screenHeigth)
        # self.addWidget(self.label)

        oImage = QPixmap('Images/score.png')
        sImage = oImage.scaled(QSize(screenWidth, screenHeigth))  # 850,685

        self.graphicsPixmapItem = QGraphicsPixmapItem(sImage)
        self.addItem(self.graphicsPixmapItem)
        self.setSceneRect(0, 0, screenWidth, screenHeigth)  # 848,683

        # if(lives < 0)
        # Final Window
        # else
        # Playing Window

        self.labelPlayers1 = QLabel()
        self.labelPlayers1.setText("Players")
        self.labelPlayers1.setGeometry(230, 150, 133, 50)
        self.labelPlayers1.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black))
        self.labelPlayers1.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.addWidget(self.labelPlayers1)

        self.labelPlayers2 = QLabel()
        self.labelPlayers2.setText("Simba")
        self.labelPlayers2.setGeometry(250, 230, 133, 50)
        self.labelPlayers2.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black))
        self.labelPlayers2.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.addWidget(self.labelPlayers2)

        self.labelPlayers3 = QLabel()
        self.labelPlayers3.setText("Nala")
        self.labelPlayers3.setGeometry(250, 300, 133, 50)
        self.labelPlayers3.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black))
        self.labelPlayers3.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.addWidget(self.labelPlayers3)

        self.labelPoints1 = QLabel()
        self.labelPoints1.setText("Points")
        self.labelPoints1.setGeometry(395, 150, 133, 50)
        self.labelPoints1.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black))
        self.labelPoints1.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.addWidget(self.labelPoints1)

        self.labelPoints2 = QLabel()
        self.labelPoints2.setText(str(simbaPoints))
        self.labelPoints2.setGeometry(395, 230, 133, 50)
        self.labelPoints2.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black))
        self.labelPoints2.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.addWidget(self.labelPoints2)

        self.labelPoints3 = QLabel()
        self.labelPoints3.setText(str(nalaPoints))
        self.labelPoints3.setGeometry(395, 300, 133, 50)
        self.labelPoints3.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black))
        self.labelPoints3.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.addWidget(self.labelPoints3)

        self.labelLives1 = QLabel()
        self.labelLives1.setText("Lives")
        self.labelLives1.setGeometry(525, 150, 133, 50)
        self.labelLives1.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black))
        self.labelLives1.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.addWidget(self.labelLives1)

        self.labelLives2 = QLabel()
        self.labelLives2.setText(str(simbaLives))
        self.labelLives2.setGeometry(530, 230, 133, 50)
        self.labelLives2.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black))
        self.labelLives2.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.addWidget(self.labelLives2)

        self.labelLives3 = QLabel()
        self.labelLives3.setText(str(nalaLives))
        self.labelLives3.setGeometry(530, 300, 133, 50)
        self.labelLives3.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black))
        self.labelLives3.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.addWidget(self.labelLives3)

        self.labelContinue = QLabel()
        self.labelContinue.setText("Continue")
        self.labelContinue.setGeometry(375, 420, 150, 50)
        self.labelContinue.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black))
        self.labelContinue.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.addWidget(self.labelContinue)

        if simbaLives == 0 and nalaLives == 0:
            cbtn = QPushButton()
            cbtn.clicked.connect(continueMethodScoreWindow)
            cbtn.setGeometry(335, 415, 230, 60)
            cbtn.setStyleSheet("background-color: rgba(255, 255, 255, 0); background-color: rgba(0,0,0,0%)")
            cbtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            self.addWidget(cbtn)
        else:
            cbtn = QPushButton()
            cbtn.clicked.connect(startMethodScoreWindow)
            cbtn.setGeometry(335, 415, 230, 60)
            cbtn.setStyleSheet("background-color: rgba(255, 255, 255, 0); background-color: rgba(0,0,0,0%)")
            cbtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            self.addWidget(cbtn)