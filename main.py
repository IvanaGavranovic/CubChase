import threading
from threading import Thread
from gameController import *
from appWindow import *
from windowManager import *

if __name__ == '__main__':

    app = QApplication([])
    oWindowManager = WindowManager(app)
    sys.exit(app.exec_())