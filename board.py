from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from colors import *
from measures import *
from pictures import *
import sys


class Field(QGraphicsRectItem):

    color_name = BROWN
    image_path = None

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

    def set_image(self, image):
        if image in {SIMBA_GREEN, SIMBA_YELLOW, NALA_GREEN, NALA_YELLOW,
                     PUMBA_GREEN, PUMBA_YELLOW, TIMON_GREEN, TIMON_YELLOW,
                     TRAP_PASSIVE_Y, TRAP_ACTIVE_Y, TRAP_PASSIVE_Z, TRAP_ACTIVE_Z,
                     PUMBA_G_IN_TRAP, PUMBA_Y_IN_TRAP, TIMON_G_IN_TRAP, TIMON_Y_IN_TRAP}:
            self.image_path = image
            q = QBrush()
            q.setTextureImage(QImage(self.image_path))
            self.setBrush(q)

    def get_image(self):
        return self.image_path

    def get_color_name(self):
        return self.color_name

    def _update(self):
        self.update()


class Board(QGraphicsView):

    def __init__(self):
        super().__init__()
        self.setGeometry(250, 80, 845, 645)
        self.setWindowTitle("Cub Chase 1.0")
        self.make_scene()
        self.load_map()
        self.make_fields()
        self.show()

    def make_scene(self):
        self.scene = QGraphicsScene(0, 0, GRAPHIC_SCENE_WIDTH, GRAPHIC_SCENE_HEIGHT)
        self.scene.setBackgroundBrush(Qt.white)
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

    def set_field(self, height: int, width: int, image: str = None):
        if self.check_board_range(height,width) is False:
            return
        if image is not None:
            self.fields[height][width].set_image(image)
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
