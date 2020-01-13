from board import Board
from timon import *
from pumba import *
from trap import *
from pictures import *


class GameController:

    def __init__(self, lock_object=None):
        self.board = Board()
        self.timon = Timon(1, 1, TIMON_YELLOW, self.board, lock_object)
        self.pumba = Pumba(18, 14, PUMBA_YELLOW, self.board, lock_object)
        self.trap = Trap(1, 4, TRAP_PASSIV, self.board)
        self.board.set_field(1, 1, TIMON_YELLOW)
        self.board.set_field(18, 14, PUMBA_YELLOW)

    def timon_movement(self):
        self.timon.changePosition()

    def pumba_movement(self):
        self.pumba.changePosition()