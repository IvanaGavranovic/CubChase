from timon import *
from pumba import *
from threading import Thread


class GameController:

    def __init__(self):
        self.board = Board()
        self.timon = Timon(1, 1, TIMON_YELLOW,self.board)
        self.pumba = Pumba(18, 14, PUMBA_YELLOW,self.board)
        self.board.set_field(1, 1, TIMON_YELLOW)
        self.board.set_field(18, 14, PUMBA_YELLOW)

    def timon_movement(self):
        self.timon.changePosition()
        #self.timon.changePositionTimon()

    def pumba_movement(self):
        self.pumba.changePosition()
        #self.pumba.changePositionPumba()