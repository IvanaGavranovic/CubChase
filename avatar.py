import time
from color import *
from movement import *
import keyboard
from picture import *


class Avatar:

    Speed = 0.18
    Lock = None

    def __init__(self, x, y, picture_g, picture_y, picture_f, board, lock_object):
        self.board = board
        self.initAvatar(x, y, picture_g, picture_y, picture_f, lock_object)

    def initAvatar(self, x, y, picture_g, picture_y, picture_f, lock_object):
        self.set_X(x)
        self.set_Y(y)
        self.PictureGreen = picture_g
        self.PictureYellow = picture_y
        self.PictureFootprint = picture_f
        self.Lock = lock_object
        self.LifeNum = 3
        self.Points = 0
        self.Alive = True
        self.Xbase = None
        self.Ybase = None

    def changePositionSimba(self):
        while self.Alive:
                if keyboard.is_pressed('a'):
                    self._go(LEFT)
                elif keyboard.is_pressed('d'):
                    self._go(RIGHT)
                elif keyboard.is_pressed('w'):
                    self._go(UP)
                elif keyboard.is_pressed('s'):
                    self._go(DOWN)
                else:
                    self._go(STAY)

    def changePositionNala(self):
        while self.Alive:
                if keyboard.is_pressed('LEFT'):
                    self._go(LEFT)
                elif keyboard.is_pressed('RIGHT'):
                    self._go(RIGHT)
                elif keyboard.is_pressed('UP'):
                    self._go(UP)
                elif keyboard.is_pressed('DOWN'):
                    self._go(DOWN)
                else:
                    self._go(STAY)

    def _go(self, direction: int):
            self.Lock.acquire()
            new_coord = self.get_coordinates(direction)
            self.remove_self_from_field()
            if self.check_enemy(new_coord[0],new_coord[1]):
                self.update_coords(self.Xbase,self.Ybase)
                self.dec_lives_and_restart()
            elif self.check_next_field(new_coord[0],new_coord[1]):
                self.update_coords(new_coord[0],new_coord[1])
            if self.Alive:
                self.set_avatar_on_field()
            self.board.update_board()
            self.Lock.release()
            time.sleep(self.Speed)

    def get_coordinates(self, direction: int):
        new_coord = []
        if direction == LEFT:
            new_coord = [self.X - 1, self.Y]
        elif direction == RIGHT:
            new_coord = [self.X + 1, self.Y]
        elif direction == UP:
            new_coord = [self.X, self.Y - 1]
        elif direction == DOWN:
            new_coord = [self.X, self.Y + 1]
        else:
            new_coord = [self.X,self.Y]
        return new_coord

    def dec_lives_and_restart(self):
        self.Points -= 100
        self.LifeNum -= 1
        if self.LifeNum == 0:
            self.Alive = False

    def set_avatar_on_field(self):
        field = self.board.get_field(self.Y,self.X)
        color_name = field.get_color_name()
        if color_name == YELLOW:
            self.board.set_field(self.Y, self.X,self.PictureYellow)
        else:
            self.board.set_field(self.Y,self.X,self.PictureGreen)

    def check_next_field(self,x:int,y:int) -> bool:
        next_field = self.board.get_field(y,x)
        color_name = next_field.get_color_name()
        image = next_field.get_image()
        if color_name == BROWN or image in {PUMBA_G_IN_TRAP,PUMBA_Y_IN_TRAP,TIMON_Y_IN_TRAP,TIMON_G_IN_TRAP}:
            return False
        return True

    def check_enemy(self,x:int,y:int) -> bool:
        next_field = self.board.get_field(y, x)
        image = next_field.get_image()
        if image in {TIMON_GREEN,TIMON_YELLOW,PUMBA_GREEN,PUMBA_YELLOW}:
            return True
        return False

    def remove_self_from_field(self):
        if self.board.get_field(self.Y, self.X).get_color_name() == YELLOW:
            self.board.set_field(self.Y, self.X, self.PictureFootprint)
        else:
            self.board.set_field(self.Y, self.X)

    def update_coords(self,x,y):
        self.X = x
        self.Y = y

    def set_X(self, value: int):
        self.X = value

    def set_Y(self, value: int):
        self.Y = value