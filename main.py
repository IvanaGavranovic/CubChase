import threading
from threading import Thread
from gameController import *
from PyQt5.QtWidgets import QApplication
from appWindow import *

if __name__ == '__main__':

    app = QApplication([])
    lock_object = threading.RLock()
    gc = GameController(lock_object)

    thread1 = Thread(target=gc.timon_movement)
    thread1.daemon = True
    thread1.start()

    thread2 = Thread(target=gc.pumba_movement)
    thread2.daemon = True
    thread2.start()

    thread3 = Thread(target=gc.trap.active)
    thread3.daemon = True
    thread3.start()

    thread4 = Thread(target=gc.simba_movement)
    thread4.daemon = True
    thread4.start()

    sys.exit(app.exec_())

    '''
    #Za prikaz prozora
    app = QApplication([])
    oMainwindow = MainWindow()
    sys.exit(app.exec_())
    '''