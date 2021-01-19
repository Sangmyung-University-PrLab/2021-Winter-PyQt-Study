from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QButtonGroup
import sys


def radio1_event():
    global group1
    print('Button ID : ', group1.checkedId(), 'Button Text: ', group1.checkedButton().text())


def radio2_event():
    global group2
    print('Button ID : ', group2.checkedId(), 'Button Text: ', group2.checkedButton().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    radio_1 = QRadioButton('Radio_1')
    radio_2 = QRadioButton('Radio_2')
    radio_3 = QRadioButton('Radio_3')
    radio_4 = QRadioButton('Radio_4')

    group1 = QButtonGroup()
    group2 = QButtonGroup()

    group1.addButton(radio_1, 1)
    group1.addButton(radio_2, 2)

    group2.addButton(radio_3, 1)
    group2.addButton(radio_4, 2)

    radio_1.setGeometry(200, 200, 50, 50)
    radio_2.setGeometry(400, 200, 50, 50)
    radio_3.setGeometry(600, 200, 50, 50)
    radio_4.setGeometry(800, 200, 50, 50)

    group1.buttonClicked.connect(radio1_event)
    group2.buttonClicked.connect(radio2_event)

    radio_1.show()
    radio_2.show()
    radio_3.show()
    radio_4.show()

    app.exec_()
