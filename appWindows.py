#from app_class import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import *

class Window2(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Playing window")
        self.setGeometry(0, 0, 800, 550)

        self.label = QLabel(self);
        self.label.setPixmap(QPixmap('images/map.png'))
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

class Window3(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Score window")
        self.setGeometry(0, 0, 800, 550)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('images/score.png'))
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

class Window4(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Final window")
        self.setGeometry(0, 0, 800, 550)

        self.label = QLabel(self);
        self.label.setPixmap(QPixmap('images/final.jpg'))
        self.label.setGeometry(0, 0, 800, 550)

        self.labelWinner = QLabel(self);
        self.labelWinner.setText("WINNER IS SIMBA")
        self.labelWinner.setGeometry(130, 50, 570, 100)
        self.labelWinner.setFont(QtGui.QFont("Jokerman", 44, QtGui.QFont.Black));
        self.labelWinner.setStyleSheet("color: rgba(255, 255, 255, 255);")

        pbtn = QPushButton("Main menu",self)
        pbtn.clicked.connect(self.mainWindow)
        pbtn.setFont(QtGui.QFont("Jokerman", 24, QtGui.QFont.Black))
        pbtn.setGeometry(295, 440, 185, 50)
        pbtn.setStyleSheet('QPushButton {background-color: rgba(255, 255, 255, 0); color: white;}')
        pbtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def mainWindow(self):  # <===
            self.w = MainWindow()
            self.w.show()
            self.hide()

class MainWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(0, 0, 800, 550)
        self.setWindowTitle("Start window")

        self.label = QLabel(self);
        self.label.setPixmap(QPixmap('images/background.png'))
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
        #self.w = Window2()
        #self.w.show()
        #self.hide()
        self.gc = GameController()
'''
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(self.close)
        qbtn.move(350, 350)
        self.setGeometry(300, 300, 250, 150)
        self.show()
'''
