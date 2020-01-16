from enemy import *


class Pumba(Enemy):
    def __init__(self, x, y, picture, game_board, lock_object):
        super().__init__(x, y, picture, game_board, lock_object)
