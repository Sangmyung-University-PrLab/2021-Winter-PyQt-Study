from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
import sys


def event():
    global label

    text = label.text()
    text += "!!!"
    label.setText(text)

    print(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    label = QLabel('Text')
    label.show()

    label.setStyleSheet('color: white; background-color:#0000ff')

    button = QPushButton('Button')
    button.clicked.connect(event)
    button.show()

    app.exec_()
