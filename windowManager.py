import sys
import threading

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from board import *
from gameController import *
from appWindow import *
from board import *

class WindowManager(QMainWindow):
    def __init__(self, app):
        #This initializes the main window or form
        super(WindowManager, self).__init__()
        self.setGeometry(0,0,845,645)#0,0,850,685
        self.setWindowTitle("Cub Chase")

        #polja koja ce se promeniti unutar startMethod-e tako sto ce se na neki nacin izvuci potrebni podaci
        self.simba_points = 0
        self.simba_lives = 0
        self.nala_points = 0
        self.nala_lives = 0

        #create the view
        self.app = app
        self.mainWindowScene = MainWindow(self.startMethod, self.quitMethod)
        self.changeViewMethod(QGraphicsView(self.mainWindowScene))
        #self.boardWindowScene = BoardWindow(self.nextMethod)
        self.scoreWindowScene = ScoreWindow(self.startMethod, self.continueMethod, self.simba_points, self.simba_lives, self.nala_points, self.nala_lives)
        self.finalWindowScene = FinalWindow(self.backToMainMenuMethod, self.simba_points, self.nala_points)
        self.show()

    def quitMethod(self):
        sys.exit(self.app.exec_())

    def startMethod(self):
        board = Board()
        self.changeViewMethod(board)
        lock_object = threading.RLock()
        gc = GameController(board, lock_object)

        thread1 = threading.Thread(target=gc.timon_movement)
        thread1.daemon = True
        thread1.start()

        thread2 = threading.Thread(target=gc.pumba_movement)
        thread2.daemon = True
        thread2.start()

        thread4 = threading.Thread(target=gc.simba_movement)
        thread4.daemon = True
        thread4.start()

        thread5 = threading.Thread(target=gc.nala_movement)
        thread5.daemon = True
        thread5.start()

        thread6 = threading.Thread(target=gc.trap1_active)
        thread6.daemon = True
        thread6.start()

        thread7 = threading.Thread(target=gc.trap2_active)
        thread7.daemon = True
        thread7.start()

        thread8 = threading.Thread(target=gc.activate_trap)
        thread8.daemon = True
        thread8.start()

        thread9 = threading.Thread(target=gc.enemy_in_trap)
        thread9.daemon = True
        thread9.start()

        # if popunjenaSvaPolja ili lives==0:
        #     thread1.stop
        #     thread2.stop
        #     thread4.stop
        #     thread5.stop
        #     thread6.stop
        #     ...
        #     self.simba_points = self.simba_points + gc.simba.points
        #     self.simba_lives = self.simba_lives + gc.simba.lives
        #     self.nala_points = self.nala_points + gc.nala.points
        #     self.nala_lives = self.nala_lives + gc.nala.lives
        #
        #     view = QGraphicsView(self.scoreWindowScene)
        #     self.changeViewMethod(view)

        #Deo kako bi imao prikaz ScoreWindow-a i FinalWindow-a
        view = QGraphicsView(self.scoreWindowScene)
        self.changeViewMethod(view)

    def nextMethod(self):
        view = QGraphicsView(self.scoreWindowScene)
        self.changeViewMethod(view)

    def continueMethod(self):
        view = QGraphicsView(self.finalWindowScene)
        self.changeViewMethod(view)

    def backToMainMenuMethod(self):
        view = QGraphicsView(self.mainWindowScene)
        self.changeViewMethod(view)

    def changeViewMethod(self, view):
        self.setCentralWidget(view)
