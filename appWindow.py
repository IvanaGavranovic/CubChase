from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import *
from scoreWindow import *
from PyQt5.QtCore import pyqtSlot

class MainWindow(QGraphicsScene):
    def __init__(self, startMethodMainWindow, quitMethodMainWindow, parent=None):
        super(MainWindow, self).__init__(parent)

class MainWindow(QWidget):
        screenWidth = 845
        screenHeigth = 645

        oImage = QPixmap('Images/background.png')
        sImage = oImage.scaled(QSize(screenWidth, screenHeigth))

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Images/background.png'))
        self.label.setGeometry(0, 0, 800, 550)

        self.graphicsPixmapItem = QGraphicsPixmapItem(sImage)
        self.addItem(self.graphicsPixmapItem)
        self.setSceneRect(0, 0, screenWidth, screenHeigth)
        '''
        self.label = QLabel()
        self.label.setPixmap(QPixmap('Images/background.png'))
        self.label.setGeometry(0, 0, screenWidth, screenHeigth)
        self.addWidget(self.label)
        '''
        qbtn = QPushButton()
        qbtn.clicked.connect(quitMethodMainWindow)
        qbtn.setGeometry(330, 170, 120, 50)
        qbtn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        qbtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.addWidget(qbtn)

        pbtn = QPushButton()
        pbtn.clicked.connect(startMethodMainWindow)
        pbtn.setGeometry(330, 100, 133, 50)
        pbtn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        pbtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.addWidget(pbtn)

        #self.show()


class BoardWindow(QGraphicsScene):                           # <===
    def __init__(self, nextMethodBoardWindow, parent=None):
        super(BoardWindow, self).__init__(parent)

        screenWidth = 800
        screenHeigth = 550

class Window2(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Playing window")
        self.setGeometry(0, 0, 800, 550)

        self.setSceneRect(0, 0, screenWidth, screenHeigth)

        self.label = QLabel()
        #self.label.setPixmap(QPixmap('Images/map.png'))
        self.label.setGeometry(0, 0, screenWidth, screenHeigth)
        self.addWidget(self.label)

        pbtn = QPushButton("Show score table")
        pbtn.clicked.connect(nextMethodBoardWindow)
        pbtn.setGeometry(330, 100, 133, 50)
        pbtn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        pbtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.addWidget(pbtn)