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

        screenWidth = 843#848
        screenHeigth = 643#645

        oImage = QPixmap('Images/background.png')
        sImage = oImage.scaled(QSize(screenWidth, screenHeigth))#850, 685

        self.graphicsPixmapItem = QGraphicsPixmapItem(sImage)
        self.addItem(self.graphicsPixmapItem)
        self.setSceneRect(0, 0, screenWidth, screenHeigth)#848,683

        qbtn = QPushButton()
        qbtn.clicked.connect(quitMethodMainWindow)
        qbtn.setGeometry(350, 200, 120, 50)
        qbtn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        qbtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.addWidget(qbtn)

        pbtn = QPushButton()
        pbtn.clicked.connect(startMethodMainWindow)
        pbtn.setGeometry(350, 120, 133, 50)
        pbtn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        pbtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.addWidget(pbtn)

        #self.show()
