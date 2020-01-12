import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

from key_notifier import KeyNotifier


class SimMoveDemo(QWidget):

    def __init__(self):
        super().__init__()

        self.avatar1 = QPixmap('avatar.png')
        self.label1 = QLabel(self)

        self.setWindowState(Qt.WindowMinimized)
        self.__init_ui__()

        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.__update_position__)
        self.key_notifier.start()

    def __init_ui__(self):

        self.label1.setPixmap(self.avatar1)
        self.setGeometry(30, 30, 800, 600)  # podesava gde ce prozor biti otvoren setGeometry(x,y,widht,height)

        self.setWindowTitle('Cab Chase')
        self.show()

    def keyPressEvent(self, event):
        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        self.key_notifier.rem_key(event.key())

    def draw(self):
        self.autoFillBackground()

    def __update_position__(self, key):
        rec1 = self.label1.geometry()

        if key == Qt.Key_Right:
            self.label1.setGeometry(rec1.x() + 40, rec1.y(), rec1.width(), rec1.height())
        elif key == Qt.Key_Down:
            self.label1.setGeometry(rec1.x(), rec1.y() + 40, rec1.width(), rec1.height())
        elif key == Qt.Key_Up:
            self.label1.setGeometry(rec1.x(), rec1.y() - 40, rec1.width(), rec1.height())
        elif key == Qt.Key_Left:
            self.label1.setGeometry(rec1.x() - 40, rec1.y(), rec1.width(), rec1.height())

    def closeEvent(self, event):
        self.key_notifier.die()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimMoveDemo()
    sys.exit(app.exec_())
