from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from color import *
from measure import *
from picture import *
import sys

class Field(QGraphicsRectItem):

    color_name = BROWN
    image_path = None
    footprints = None

    def __init__(self):
        super().__init__(0,0,FIELD_SIZE,FIELD_SIZE)
        self.color = QColor()
        self.color.setNamedColor(self.color_name)
        self.setBrush(self.color)

    def set_color(self, color):
        if color in {WHITE, GREEN, YELLOW, BROWN}:
            self.color_name = color
            self.color.setNamedColor(self.color_name)
            self.setBrush(self.color)
            self.image_path = None

    def get_color(self):
        return self.color

    def set_image(self, image) -> bool:
        footprint = False

        if image in {SIMBA_GREEN, SIMBA_YELLOW, NALA_GREEN, NALA_YELLOW,
                     PUMBA_GREEN, PUMBA_YELLOW, TIMON_GREEN, TIMON_YELLOW,
                     TRAP_PASSIVE_Y, TRAP_ACTIVE_Y, TRAP_PASSIVE_Z, TRAP_ACTIVE_Z,
                     PUMBA_G_IN_TRAP, PUMBA_Y_IN_TRAP, TIMON_G_IN_TRAP, TIMON_Y_IN_TRAP,
                     SIMBA_FOOTPRINT, NALA_FOOTPRINT}:
            if image in {SIMBA_FOOTPRINT, NALA_FOOTPRINT}:
                if self.footprints is None:
                    footprint = True
                    self.image_path = image
                    self.footprints = image
                else:
                    self.image_path = self.footprints
            else:
                self.image_path = image

            q = QBrush()
            q.setTextureImage(QImage(self.image_path))
            self.setBrush(q)
        return footprint

    def get_image(self):
        return self.image_path

    def get_color_name(self):
        return self.color_name

    def _update(self):
        self.update()


class Board(QGraphicsView):

    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 845, 645)
        self.setWindowTitle("Cub Chase 1.0")
        self.temp = self.make_scene()
        self.load_map()
        self.make_fields()

        self.numberOfMarkedFields = 0

        self.labelSimba = QLabel()
        self.labelSimba.setText("Simba:")
        self.labelSimba.setGeometry(20, 0, 200, 30)
        self.labelSimba.setFont(QtGui.QFont("Jokerman", 20, QtGui.QFont.Black))
        self.labelSimba.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.scene.addWidget(self.labelSimba)

        self.labelSimbaPoints = QLabel()
        self.labelSimbaPoints.setText("0")
        self.labelSimbaPoints.setGeometry(120, 0, 200, 30)
        self.labelSimbaPoints.setFont(QtGui.QFont("Jokerman", 20, QtGui.QFont.Black))
        self.labelSimbaPoints.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.scene.addWidget(self.labelSimbaPoints)

        self.labelSimba2 = QLabel()
        self.labelSimba2.setText("Lives:")
        self.labelSimba2.setGeometry(220, 0, 200, 30)
        self.labelSimba2.setFont(QtGui.QFont("Jokerman", 20, QtGui.QFont.Black))
        self.labelSimba2.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.scene.addWidget(self.labelSimba2)

        self.labelSimbaLives = QLabel()
        self.labelSimbaLives.setText("3")
        self.labelSimbaLives.setGeometry(320, 0, 200, 30)
        self.labelSimbaLives.setFont(QtGui.QFont("Jokerman", 20, QtGui.QFont.Black))
        self.labelSimbaLives.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.scene.addWidget(self.labelSimbaLives)

        self.labelNala = QLabel()
        self.labelNala.setText("Nala:")
        self.labelNala.setGeometry(500, 0, 200, 30)
        self.labelNala.setFont(QtGui.QFont("Jokerman", 20, QtGui.QFont.Black))
        self.labelNala.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.scene.addWidget(self.labelNala)

        self.labelNalaPoints = QLabel()
        self.labelNalaPoints.setText("0")
        self.labelNalaPoints.setGeometry(600, 0, 200, 30)
        self.labelNalaPoints.setFont(QtGui.QFont("Jokerman", 20, QtGui.QFont.Black))
        self.labelNalaPoints.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.scene.addWidget(self.labelNalaPoints)

        self.labelNala2 = QLabel()
        self.labelNala2.setText("Lives:")
        self.labelNala2.setGeometry(700, 0, 200, 30)
        self.labelNala2.setFont(QtGui.QFont("Jokerman", 20, QtGui.QFont.Black))
        self.labelNala2.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.scene.addWidget(self.labelNala2)

        self.labelNalaLives = QLabel()
        self.labelNalaLives.setText("3")
        self.labelNalaLives.setGeometry(800, 0, 200, 30)
        self.labelNalaLives.setFont(QtGui.QFont("Jokerman", 20, QtGui.QFont.Black))
        self.labelNalaLives.setStyleSheet("color: rgba(255, 255, 255, 255); background-color: rgba(0,0,0,0%)")
        self.scene.addWidget(self.labelNalaLives)

        self.show()

    def make_scene(self):
        self.scene = QGraphicsScene(0, 0, GRAPHIC_SCENE_WIDTH, GRAPHIC_SCENE_HEIGHT)
        self.scene.setBackgroundBrush(Qt.black)
        self.setScene(self.scene)

    def load_map(self):
        f = open("map.txt", "r")
        self.map = [['w' for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]
        x = 0
        y = 0
        for line in f:
            for letter in line:
                if letter not in {'z', 's', 't'}:
                    continue
                self.map[x][y] = letter
                y = y + 1
            y = 0
            x = x + 1

    def make_fields(self):
        self.fields = [[Field() for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]
        for x in range(BOARD_HEIGHT):
            for y in range(BOARD_WIDTH):
                self.fields[x][y].setPos(0+y*FIELD_SIZE,0+x*FIELD_SIZE)
                self.scene.addItem(self.fields[x][y])
                self.map_to_field(x, y)
            y = 0

    def set_field(self, height: int, width: int, image: str = None) -> int:
        if self.check_board_range(height,width) is False:
            return 0
        if image is not None:
            if self.fields[height][width].set_image(image):
                return 1
            return 0
        else:
            if self.fields[height][width].footprints is not None:
                if self.fields[height][width].set_image(self.fields[height][width].footprints):
                    return 1
                return 0
            else:
                self.map_to_field(height, width)

    def get_field(self, height: int, width: int) -> Field:
        if self.check_board_range(height, width):
            return self.fields[height][width]

    def map_to_field(self, height: int, width: int):
        if self.map[height][width] == 'z':
            self.fields[height][width].set_color(BROWN)
        elif self.map[height][width] == 't':
            self.fields[height][width].set_color(GREEN)
        else:
            self.fields[height][width].set_color(YELLOW)

    def update_board(self):
        for x in range(BOARD_HEIGHT):
            for y in range(BOARD_WIDTH):
                if self.fields[x][y] is None:
                    print(x)
                    print(y)
                self.fields[x][y].update()
        self.scene.update()
        self.update()

    def check_board_range(self, height: int, width: int) -> bool:
        if 0 <= height <= BOARD_HEIGHT and 0 <= width <= BOARD_WIDTH:
            return True
        return False

    def updateSimbaPoints(self, points):#simba menja board tako sto uzme getPoints sabere sa dodatnim poenima i onda pozove ovu metodu
        self.labelSimbaPoints.setText(points)

    def updateSimbaLives(self, lives):
        self.labelSimbaLives.setText(lives)

    def updateNalaPoints(self, points):  # simba menja board tako sto uzme getPoints sabere sa dodatnim poenima i onda pozove ovu metodu
        self.labelNalaPoints.setText(points)

    def updateNalaLives(self, lives):
        self.labelNalaLives.setText(lives)