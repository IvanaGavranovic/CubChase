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
        self.scoreWindowScene = ScoreWindow(self.startMethod, self.continueMethod, self.simba_points, self.simba_lives, self.nala_points, self.nala_lives)
        self.finalWindowScene = FinalWindow(self.backToMainMenuMethod, self.simba_points, self.nala_points)
        self.show()

    def quitMethod(self):
        sys.exit(self.app.exec_())

    def startMethod(self):
        self.board = Board()
        self.changeViewMethod(self.board)
        self.lock_object = threading.RLock()
        self.gc = GameController(self.board, self.lock_object)

        self.thread1 = threading.Thread(target=self.gc.timon_movement)
        self.thread1.daemon = True
        self.thread1.start()
        self.thread2 = threading.Thread(target=self.gc.pumba_movement)
        self.thread2.daemon = True
        self.thread2.start()

        self.thread3 = threading.Thread(target=self.gc.enemy_avatar_collision)
        self.thread3.daemon = True
        self.thread3.start()

        self.thread4 = threading.Thread(target=self.gc.simba_movement)
        self.thread4.daemon = True
        self.thread4.start()

        self.thread5 = threading.Thread(target=self.gc.nala_movement)
        self.thread5.daemon = True
        self.thread5.start()

        self.thread6 = threading.Thread(target=self.gc.trap1_active)
        self.thread6.daemon = True
        self.thread6.start()

        self.thread7 = threading.Thread(target=self.gc.trap2_active)
        self.thread7.daemon = True
        self.thread7.start()

        self.thread8 = threading.Thread(target=self.gc.activate_trap)
        self.thread8.daemon = True
        self.thread8.start()

        self.thread9 = threading.Thread(target=self.gc.enemy_in_trap)
        self.thread9.daemon = True
        self.thread9.start()

        #self.thread10 = threading.Thread(target=self.fieldAndLivesCounting)
        #self.thread10.daemon = True
        #self.thread10.start()

        #Deo kako bi imao prikaz ScoreWindow-a i FinalWindow-a
        #view = QGraphicsView(self.scoreWindowScene)
        #self.changeViewMethod(view)

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

    def fieldAndLivesCounting(self):
        work = True
        while work:
            self.lock_object.acquire()
            if self.board.numberOfMarkedFields == 147 or (self.gc.simba.LifeNum == 0 and self.gc.nala.LifeNum == 0):
               self.simba_points += self.gc.simba.Points
               self.simba_lives += self.gc.simba.LifeNum
               self.nala_points += self.gc.nala.Points
               self.nala_lives += self.gc.nala.LifeNum
               work = False
            self.lock_object.release()
            time.sleep(3)

        view = QGraphicsView(self.scoreWindowScene)
        self.changeViewMethod(view)