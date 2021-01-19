import sys

from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import QLineEdit


def line_event():
    global line

    print(line.text())
    line.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    line = QLineEdit()
    line.show()

    button = QPushButton('Button')
    button.show()
    button.clicked.connect(line_event)

    app.exec_()
