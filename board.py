from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class Board(QGraphicsView):

    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(0,0,320,240)
        self.scene.setBackgroundBrush(Qt.white)
        self.setScene(self.scene)
        self.setWindowTitle("Cub Chase 1.0")
        f = open("map.txt","r")
        height = 6
        width = 8
        size = 40
        brownColor = QColor()
        brownColor.setRgb(89,60,31)
        self.map = [['w' for x in range(width)] for y in range(height)]
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

        self.fields = [[QGraphicsRectItem(0,0,size,size) for x in range(width)] for y in range(height)]
        for x in range(height):
            for y in range(width):
                self.fields[x][y].setPos(0+y*size,0+x*size)
                self.scene.addItem(self.fields[x][y])
                if(self.map[x][y] == 'z'):
                    self.fields[x][y].setBrush(brownColor)
                elif(self.map[x][y] == 't'):
                    self.fields[x][y].setBrush(Qt.green)
                else:
                    self.fields[x][y].setBrush(Qt.yellow)
            y = 0
        #self.fields[1][1].setBrush(QBrush(QPixmap("simba.png")));
        self.show()


app = QApplication([])
b = Board()
sys.exit(app.exec_())