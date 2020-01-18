import threading
from threading import Thread
from gameController import *
from appWindow import *
from windowManager import *

if __name__ == '__main__':

    app = QApplication([])          # ??
    lock_object = threading.RLock()
    gc = GameController(lock_object)

    thread1 = Thread(target=gc.timon_movement)
    thread1.daemon = True
    thread1.start()

    thread2 = Thread(target=gc.pumba_movement)
    thread2.daemon = True
    thread2.start()

    thread4 = Thread(target=gc.simba_movement)
    thread4.daemon = True
    thread4.start()

    thread5 = Thread(target=gc.nala_movement)
    thread5.daemon = True
    thread5.start()

    thread6 = Thread(target=gc.trap1_active)
    thread6.daemon = True
    thread6.start()

    thread7 = Thread(target=gc.trap2_active)
    thread7.daemon = True
    thread7.start()

    thread8 = Thread(target=gc.activate_trap)
    thread8.daemon = True
    thread8.start()

    thread9 = Thread(target=gc.enemy_in_trap)
    thread9.daemon = True
    thread9.start()

    sys.exit(app.exec_())

    '''
    #Za prikaz prozora
    app = QApplication([])
    oWindowManager = WindowManager(app)
    sys.exit(app.exec_())
    '''