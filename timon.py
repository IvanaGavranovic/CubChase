from enemy import *


class Timon(Enemy):
    def __init__(self, x, y, picture_g,picture_y, board, lock_object):
        super().__init__(x, y, picture_g,picture_y, board, lock_object)
