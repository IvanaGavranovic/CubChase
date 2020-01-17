from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import *
from appWindow import *

class Window4(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Final window")
        self.setGeometry(0, 0, 800, 550)

        self.label = QLabel(self);
        self.label.setPixmap(QPixmap('Images/final.jpg'))
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
