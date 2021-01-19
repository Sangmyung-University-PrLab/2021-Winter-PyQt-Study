from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import QTextEdit

import sys


def text_event():
    global text_edit

    print(text_edit.toPlainText())
    text_edit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    text_edit = QTextEdit()
    text_edit.show()

    button = QPushButton('Button')
    button.show()
    button.clicked.connect(text_event)

    app.exec_()
