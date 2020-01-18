from PyQt5.QtWidgets import QLabel
from random import randint
import sys
import time
from color import *
from movement import *
from picture import *


class Enemy:

    Speed = 0.18
    Lock = None

    def __init__(self, x, y, picture_g, picture_y, board, lock_object):
        self.board = board
        self.initEnemy(x, y, picture_g, picture_y, lock_object)

    def initEnemy(self, x, y, picture_g, picture_y, lock_object):
        self.X = x
        self.Y = y
        self.PictureYellow = picture_y
        self.PictureGreen = picture_g
        self.Lock = lock_object

    def changePosition(self):
        while True:
                p1 = randint(1, 4)
                p2 = randint(1, 14)
                if p1 % 4 == LEFT:
                    self._go(p2, LEFT)
                elif p1 % 4 == RIGHT:
                    self._go(p2, RIGHT)
                elif p1 % 4 == UP:
                    self._go(p2, UP)
                else:
                    self._go(p2, DOWN)

    def _go(self, steps_num: int, direction: int):
        for x in range(steps_num):
            new_coord = self.get_coordinates(direction)
            self.Lock.acquire()
            next_field = self.board.get_field(new_coord[1], new_coord[0])
            nf_color = next_field.get_color_name()
            image = next_field.get_image()
            self.Lock.release()
            if image in {TRAP_ACTIVE_Y, TRAP_ACTIVE_Z}:
                self.Lock.acquire()
                self.board.set_field(self.Y, self.X)
                self.X = new_coord[0]
                self.Y = new_coord[1]
                self.Lock.release()
                time.sleep(5)
                if nf_color == YELLOW:
                    self.Lock.acquire()
                    self.board.set_field(new_coord[1], new_coord[0], self.PictureYellow)
                    self.Lock.release()
                else:
                    self.Lock.acquire()
                    self.board.set_field(new_coord[1], new_coord[0], self.PictureGreen)
                    self.Lock.release()
                continue
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
                self.board.update_board()
                self.Lock.release()
                self.X = new_coord[0]
                self.Y = new_coord[1]
                time.sleep(self.Speed)
            else:
                break

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
