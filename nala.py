from avatar import *


class Nala(Avatar):
    def __init__(self, x, y, picture_g,picture_y, picture_f, board, lock_object):
        super().__init__(x, y, picture_g,picture_y, picture_f, board, lock_object)
        self.board.set_field(y, x, NALA_YELLOW)
        self.Xbase = x
        self.Ybase = y
