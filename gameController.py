from pictures import *
from board import *
from timon import *
from pumba import *
from trap import *
from simba import *

class GameController:

    def __init__(self, board, lock_object=None):
        self.board = board
        self.timon = Timon(1, 1, TIMON_GREEN, TIMON_YELLOW, self.board, lock_object)
        self.pumba = Pumba(18, 14, PUMBA_GREEN, PUMBA_YELLOW, self.board, lock_object)
        self.simba = Simba(1, 2, SIMBA_YELLOW, self.board, lock_object)
        self.trap1 = Trap(4, 2, self.board, 1, 1, lock_object)
        self.trap2 = Trap(10, 17, self.board, 2, 1, lock_object)
        self.board.set_field(1, 1, TIMON_YELLOW)
        self.board.set_field(18, 14, PUMBA_YELLOW)
        self.board.set_field(4, 2, TRAP_ACTIVE_Y)
        self.board.set_field(10, 17, TRAP_ACTIVE_Y)


    def timon_movement(self):
        self.timon.changePosition()


    def simba_movement(self):
        self.simba.changePosition()


    def pumba_movement(self):
        self.pumba.changePosition()


    def trap1_active(self):
        self.trap1.controlTrap()


    def trap2_active(self):
        self.trap2.controlTrap()