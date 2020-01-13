from enemy import *


class Timon(Enemy):
    def __init__(self, x, y, picture, board, lock_object):
        super().__init__(x, y, picture, board, lock_object)
