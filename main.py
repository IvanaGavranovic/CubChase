import threading
from threading import Thread
from gameController import *
from PyQt5.QtWidgets import QApplication
from appWindow import *
from windowManager import *

if __name__ == '__main__':
    #Za prikaz prozora
    app = QApplication([])
    oWindowManager = WindowManager(app)
    sys.exit(app.exec_())
