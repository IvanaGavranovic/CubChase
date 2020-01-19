from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal, QEventLoop, QTimer
from picture import *
from color import *
import time
from datetime import datetime


class Trap(QLabel):

    isActive = False
    activeTrap = pyqtSignal()

    def __init__(self, x, y, board, id, t : bool, lock_object):
        super().__init__()
        self.board = board
        self.lock = lock_object
        self.initTrap(x, y, id, t)
        self.init_enem_in_trap()

    def initTrap(self, x, y, id, t : bool):
        self.X = x
        self.Y = y
        self.ID = id
        self.Trap = t
        #self.activeTrap.connect(self.active)

    def set_active_trap_green(self,x: int, y: int):
        self.isActive = True
        self.board.set_field(y,x,TRAP_ACTIVE_Z)
        self.board.update_board()

    def set_active_trap_yellow(self, x: int, y: int):
        self.isActive = True
        self.board.set_field(y, x, TRAP_ACTIVE_Y)
        self.board.update_board()

    def set_inactive_trap_green(self, x: int, y: int):
        self.isActive = False
        self.board.set_field(y, x, TRAP_PASSIVE_Z)
        self.board.update_board()

    def set_inactive_trap_yellow(self, x: int, y: int):
        self.isActive = False
        self.board.set_field(y, x, TRAP_PASSIVE_Y)
        self.board.update_board()

    def controlTrap(self):              # ?
        par = 0
        curr_field = self.board.get_field(self.Y, self.X)
        color_name = curr_field.get_color_name()
        begin = 0
        d1 = None
        while self.Trap:
            self.lock.acquire()
            print("uzela zamka")
            if self.timon_in_g or self.timon_in_y or self.pumba_in_g or self.pumba_in_y:
                self.Trap = False
                print("pustila zamka")
                self.lock.release()
                continue
            if self.isActive:
                if color_name == YELLOW:
                    self.set_active_trap_yellow(self.X, self.Y)
                else:
                    self.set_active_trap_green(self.X, self.Y)
                if begin == 0:
                    d1 = datetime.now()
                    begin = 1
            else:
                if color_name == YELLOW:
                    self.set_inactive_trap_yellow(self.X, self.Y)
                else:
                    self.set_inactive_trap_green(self.X, self.Y)
            d2 = datetime.now()
            if d1 is not None and abs((d2 - d1).seconds) > 10:
                self.Trap = False
                self.board.set_field(self.Y,self.X)
                self.board.update_board()
            print("pustila zamka")
            self.lock.release()
            time.sleep(0.2)

    def init_enem_in_trap(self):
        self.timon_in_trap_g(False)
        self.timon_in_trap_y(False)
        self.pumba_in_trap_g(False)
        self.pumba_in_trap_y(False)

    def timon_in_trap_g(self, state: bool):
        self.timon_in_g = state

    def timon_in_trap_y(self, state: bool):
        self.timon_in_y = state

    def pumba_in_trap_g(self, state: bool):
        self.pumba_in_g = state

    def pumba_in_trap_y(self, state: bool):
        self.pumba_in_y = state
