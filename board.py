from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication,QGridLayout,QVBoxLayout,QWidget
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
import sys


class CubChase(QMainWindow):

    def __init__(self):
        super().__init__()
        self.height = 240
        self.width = 320
        self.initUI()

    def initUI(self):
        self.board = Board(self)
        self.setCentralWidget(self.board)
        self.setGeometry(270,60,self.width,self.height)
        self.setWindowTitle('CubChase')
        self.show()


class Board(QFrame):

    def __init__(self,window):
        super().__init__(window)
        self.init()

    def init(self):
        self.timer = QBasicTimer()
        self.setFocusPolicy(Qt.StrongFocus)
        self.loadMap()

    def loadMap(self):
        self.map = [['w' for x in range(8)] for y in range(6)]
        f = open("map.txt","r")
        x = 0
        y = 0
        for line in f:
            for letter in line:
                if(letter == '\n'):
                    continue
                self.map[x][y] = letter
                y = y + 1
            y = 0
            x = x + 1
        f.close()
        self.buildBoard()

    def buildBoard(self):
        self.drawField()

    def drawField(self):
        self.w = QWidget()
        self.vb = QVBoxLayout()
        self.grid = QGridLayout()
        self.grid.setSpacing(1)
        self.vb.addLayout(self.grid)
        self.w.setLayout(self.vb)
        self.setCentralWidget(self.w)


app = QApplication([])
cc = CubChase()
sys.exit(app.exec_())
