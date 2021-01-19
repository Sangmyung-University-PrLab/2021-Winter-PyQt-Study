from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import QLabel

import sys


def pixmap_event():
    global button
    pixmap = QPixmap('image.jpg')
    label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    label = QLabel('Label')
    button = QPushButton('Button')
    label.show()
    button.show()

    button.clicked.connect(pixmap_event)
    app.exec_()
