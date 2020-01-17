from PyQt5.QtWidgets import QLabel
from random import randint
import sys
import time
from colors import *
from movement import *
import keyboard
from key_notifier import KeyNotifier
from pictures import *


class Avatar:

    Speed = 0.18
    Lock = None

    def __init__(self, x, y, picture_g,picture_y, board, lock_object):
        self.board = board
        self.initAvatar(x, y, picture_g, picture_y, lock_object)

    def initAvatar(self, x, y, picture_g,picture_y, lock_object):
        self.set_X(x)
        self.set_Y(y)
        self.PictureGreen = picture_g
        self.PictureYellow = picture_y
        self.Lock = lock_object

    def changePosition(self):
        while True:
                if keyboard.is_pressed('a'):
                    self._go(LEFT)
                elif keyboard.is_pressed('d'):
                    self._go(RIGHT)
                elif keyboard.is_pressed('w'):
                    self._go(UP)
                elif keyboard.is_pressed('s'):
                    self._go(DOWN)

    def _go(self, direction: int):
            new_coord = self.get_coordinates(direction)
            self.Lock.acquire()
            next_field = self.board.get_field(new_coord[1], new_coord[0])
            nf_color = next_field.get_color_name()
            image = next_field.get_image()
            self.Lock.release()
            if image in {TRAP_PASSIVE_Y, TRAP_PASSIVE_Z}:
                self.Lock.acquire()
                self.board.set_field(self.Y, self.X)
                if nf_color == YELLOW:
                    self.board.set_field(new_coord[1], new_coord[0], self.PictureYellow)
                else:
                    self.board.set_field(new_coord[1], new_coord[0], self.PictureGreen)
                self.X = new_coord[0]
                self.Y = new_coord[1]
                self.board.update_board()
                self.Lock.release()
                time.sleep(self.Speed)
                return
            if nf_color == YELLOW or nf_color == GREEN:
                #lock
                self.Lock.acquire()
                #curr_field = self.board.get_field(self.Y, self.X)
                #picture check
                self.board.set_field(self.Y, self.X)
                if nf_color == YELLOW:
                    self.board.set_field(new_coord[1], new_coord[0], self.PictureYellow)
                else:
                    self.board.set_field(new_coord[1], new_coord[0], self.PictureGreen)
                #unlock
                self.set_X(new_coord[0])
                self.set_Y(new_coord[1])
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
        else:
            new_coord = [self.X, self.Y + 1]
        return new_coord

    def set_X(self, value: int):
        self.X = value

    def set_Y(self, value: int):
        self.Y = value