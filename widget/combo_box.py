from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QComboBox
import sys


def combo_event():
    global combo

    index = combo.currentIndex()
    text = combo.currentText()

    print(index, text)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    combo = QComboBox()
    combo_items = ['item1', 'item2', 'item3', 'item4', 'item5']
    for item in combo_items:
        combo.addItem(item)
    combo.show()

    combo.currentIndexChanged.connect(combo_event)

    app.exec_()
