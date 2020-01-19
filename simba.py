from avatar import *


class Simba(Avatar):
    def __init__(self, x, y, picture_g,picture_y, board, lock_object):
        super().__init__(x, y, picture_g,picture_y, board, lock_object)
        self.board.set_field(y, x, SIMBA_YELLOW)
        self.Xbase = x
        self.Ybase = y
