from board import *
from timon import *
from pumba import *
from trap import *
from simba import *
from nala import *


class GameController:

    def __init__(self, board, lock_object=None):
        self.lock_object = lock_object
        self.board = board
        self.timon = Timon(1, 2, TIMON_GREEN, TIMON_YELLOW, self.board, lock_object)
        self.pumba = Pumba(17, 14, PUMBA_GREEN, PUMBA_YELLOW, self.board, lock_object)
        self.simba = Simba(9, 10, SIMBA_GREEN, SIMBA_YELLOW, SIMBA_FOOTPRINT, self.board, lock_object)
        self.nala = Nala(11, 10, NALA_GREEN, NALA_YELLOW, NALA_FOOTPRINT, self.board, lock_object)
        self.trap1 = Trap(2, 4, self.board, 1, True, lock_object)
        self.trap2 = Trap(17, 10, self.board, 2, True, lock_object)

    def simba_movement(self):
        self.simba.changePositionSimba()

    def nala_movement(self):
        self.nala.changePositionNala()

    def timon_movement(self):
        self.timon.changePosition()

    def pumba_movement(self):
        self.pumba.changePosition()

    def trap1_active(self):
        self.trap1.controlTrap()

    def trap2_active(self):
        self.trap2.controlTrap()

    def activate_trap(self):
        trap1_active = False
        trap2_active = False
        while not trap1_active or not trap2_active:
            self.lock_object.acquire()
            print("uzeo activate trap")
            if not trap1_active:
                if (self.check_coords(self.simba.X,self.simba.Y,self.trap1.X,self.trap1.Y) or
                self.check_coords(self.nala.X,self.nala.Y,self.trap1.X,self.trap1.Y)):
                    self.trap1.isActive = trap1_active = True
                else:
                    self.trap1.isActive = trap1_active = False
            if not trap2_active:
                if (self.check_coords(self.simba.X,self.simba.Y,self.trap2.X,self.trap2.Y) or
                self.check_coords(self.nala.X,self.nala.Y,self.trap2.X,self.trap2.Y)):
                    self.trap2.isActive = trap2_active = True
                else:
                    self.trap2.isActive = trap2_active = False
            print("pustio activate trap")
            self.lock_object.release()
            time.sleep(0.2)

    def enemy_in_trap(self):
        trap1_exists = True
        trap2_exists = True
        while trap1_exists or trap2_exists:
            self.lock_object.acquire()
            print("uzeo enemy in trap")
            if self.trap1.Trap and self.trap1.isActive:
                if self.check_coords(self.timon.X,self.timon.Y,self.trap1.X,self.trap1.Y):
                    trap_field = self.board.get_field(self.trap1.Y,self.trap1.X)
                    clr = trap_field.get_color_name()
                    if clr == YELLOW:
                        self.board.set_field(self.trap1.Y,self.trap1.X,TIMON_Y_IN_TRAP)
                        self.trap1.timon_in_trap_y(True)
                    else:
                        self.board.set_field(self.trap1.Y, self.trap1.X, TIMON_G_IN_TRAP)
                        self.trap1.timon_in_trap_g(True)
                    self.board.update_board()
                    trap1_exists = False
                if self.check_coords(self.pumba.X,self.pumba.Y,self.trap1.X,self.trap1.Y):
                    trap_field = self.board.get_field(self.trap1.Y,self.trap1.X)
                    clr = trap_field.get_color_name()
                    if clr == YELLOW:
                        self.board.set_field(self.trap1.Y,self.trap1.X,PUMBA_Y_IN_TRAP)
                        self.trap1.pumba_in_trap_y(True)
                    else:
                        self.board.set_field(self.trap1.Y, self.trap1.X, PUMBA_G_IN_TRAP)
                        self.trap1.pumba_in_trap_g(True)
                    self.board.update_board()
                    trap1_exists = False
            if self.trap2.Trap and self.trap2.isActive:
                if self.check_coords(self.timon.X,self.timon.Y,self.trap2.X,self.trap2.Y):
                    trap_field = self.board.get_field(self.trap2.Y,self.trap2.X)
                    clr = trap_field.get_color_name()
                    if clr == YELLOW:
                        self.board.set_field(self.trap2.Y,self.trap2.X,TIMON_Y_IN_TRAP)
                        self.trap2.timon_in_trap_y(True)
                    else:
                        self.board.set_field(self.trap2.Y, self.trap2.X, TIMON_G_IN_TRAP)
                        self.trap2.timon_in_trap_g(True)
                    self.board.update_board()
                    trap2_exists = False
                if self.check_coords(self.pumba.X,self.pumba.Y,self.trap2.X,self.trap2.Y):
                    trap_field = self.board.get_field(self.trap2.Y,self.trap2.X)
                    clr = trap_field.get_color_name()
                    if clr == YELLOW:
                        self.board.set_field(self.trap2.Y,self.trap2.X,PUMBA_Y_IN_TRAP)
                        self.trap2.pumba_in_trap_y(True)
                    else:
                        self.board.set_field(self.trap2.Y, self.trap2.X, PUMBA_G_IN_TRAP)
                        self.trap2.pumba_in_trap_g(True)
                    self.board.update_board()
                    trap2_exists = False
            trap1_exists = self.trap1.Trap
            trap2_exists = self.trap2.Trap
            print("pustio enemy in trap")
            self.lock_object.release()
            time.sleep(0.2)

    def check_coords(self,x_e: int, y_e: int, x_t:int, y_t: int) -> bool:
        if x_e == x_t and y_e == y_t:
            return True
        return False

    def enemy_avatar_collision(self):
        simba = True
        nala = True
        while simba or nala:
            self.lock_object.acquire()
            simba = self.simba.Alive
            nala = self.nala.Alive
            if simba:
                if (self.check_coords(self.simba.X,self.simba.Y,self.timon.X,self.timon.Y) or
                        self.check_coords(self.simba.X,self.simba.Y,self.pumba.X,self.pumba.Y)):
                    self.simba.remove_self_from_field()
                    self.simba.update_coords(self.simba.Xbase,self.simba.Ybase)
                    self.simba.dec_lives_and_restart()
            if nala:
                if (self.check_coords(self.nala.X,self.nala.Y,self.timon.X,self.timon.Y) or
                        self.check_coords(self.nala.X, self.nala.Y, self.pumba.X, self.pumba.Y)):
                    self.simba.remove_self_from_field()
                    self.nala.update_coords(self.nala.Xbase,self.nala.Ybase)
                    self.nala.dec_lives_and_restart()
            self.lock_object.release()
            time.sleep(0.2)