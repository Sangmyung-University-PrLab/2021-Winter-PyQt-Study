from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QPushButton
import sys


def event():
    global checkbox
    state = checkbox.isChecked()

    if state:
        print('눌렸다')
    else:
        print('안눌렸다')


def checkbox_event():
    global checkbox

    state = checkbox.isChecked()
    text = checkbox.text()

    print(state, text)
    checkbox.setText(text + '!!!')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    checkbox = QCheckBox('Check box')
    checkbox.show()

    button = QPushButton('button')
    button.clicked.connect(event)
    button.show()

    checkbox.clicked.connect(checkbox_event)

    app.exec_()
