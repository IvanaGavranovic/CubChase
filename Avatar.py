from PyQt5.QtWidgets import QLabel
from random import randint
import sys
import time
from colors import *
from movement import *


class Avatar:

    Speed = 0.18
    Lock = None

    def __init__(self, x, y, picture, board, lock_object):
        self.board = board
        self.initEnemy(x, y, picture, lock_object)

        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.__update_position__)
        self.key_notifier.start()

    def initAvatar(self, x, y, picture, lock_object):
        self.X = x
        self.Y = y
        self.Picture = picture
        self.Lock = lock_object

    def changePosition(self):
        while True:
                if keyboard.is_pressed('a'):
                    self._go(LEFT)
                elif keyboard.is_pressed('d'):
                    self._go(RIGHT)
                elif keyboard.is_pressed('w'):
                    self._go(UP)
                else:
                    self._go(DOWN)

    def _go(self, direction: int):
            new_coord = self.get_coordinates(direction)
            self.Lock.acquire()
            next_field = self.board.get_field(new_coord[1], new_coord[0])
            nf_color = next_field.get_color_name()
            self.Lock.release()
            if nf_color == YELLOW or nf_color == GREEN:
                #lock
                self.Lock.acquire()
                #curr_field = self.board.get_field(self.Y, self.X)
                #picture check
                self.board.set_field(self.Y, self.X)
                self.board.set_field(new_coord[1], new_coord[0], self.Picture)
                #unlock
                self.board.update_board()
                self.Lock.release()
                self.X = new_coord[0]
                self.Y = new_coord[1]
                time.sleep(self.Speed)

    def get_coordinates(self, direction: int):
        new_coord = []
        if direction == LEFT:
            new_coord = [self.X - 1, self.Y]
        elif direction == RIGHT:
            new_coord = [self.X + 1, self.Y]
        elif direction == UP:
            new_coord = [self.X, self.Y - 1]
        else:
            new_coord = [self.X, self.Y + 1]
        return new_coord
