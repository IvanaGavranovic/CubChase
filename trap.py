from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal, QEventLoop, QTimer
from pictures import *
from colors import *
import time


class Trap(QLabel):

    Trap = 1
    isActive = False
    activeTrap = pyqtSignal()

    def __init__(self, x, y, board, id, t, lock_object):
        super().__init__()
        self.board = board
        self.lock = lock_object
        self.initTrap(x, y, id, t)
        self.init_enem_in_trap()

    def initTrap(self, x, y, id, t):
        self.X = x
        self.Y = y
        self.ID = id
        self.Trap = t
        #self.activeTrap.connect(self.active)

    def set_active_trap_green(self,x: int, y: int):
        self.isActive = True
        self.lock.acquire()
        self.board.set_field(x,y,TRAP_ACTIVE_Z)
        self.board.update_board()
        self.lock.release()

    def set_active_trap_yellow(self, x: int, y: int):
        self.isActive = True
        self.lock.acquire()
        self.board.set_field(x, y, TRAP_ACTIVE_Y)
        self.board.update_board()
        self.lock.release()

    def set_inactive_trap_green(self, x: int, y: int):
        self.isActive = False
        self.lock.acquire()
        self.board.set_field(x, y, TRAP_PASSIVE_Z)
        self.board.update_board()
        self.lock.release()

    def set_inactive_trap_yellow(self, x: int, y: int):
        self.isActive = False
        self.lock.acquire()
        self.board.set_field(x, y, TRAP_PASSIVE_Y)
        self.board.update_board()
        self.lock.release()

    def controlTrap(self):
        par = 0
        curr_field = self.board.get_field(self.X, self.Y)
        color_name = curr_field.get_color_name()
        if color_name == YELLOW:
            self.set_active_trap_yellow(self.X, self.Y)
        else:
            self.set_active_trap_green(self.X, self.Y)
        while True:
            self.lock.acquire()
            self.board.pumba_in_g
            self.lock.release()
            time.sleep(10)

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
