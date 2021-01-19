import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QListWidget


def list_event():
    global list_widget
    print(list_widget.currentItem().text())
    print(list_widget.currentItem())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    list_widget = QListWidget()
    list_widget.doubleClicked.connect(list_event)

    items = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7']
    list_widget.addItems(items)
    list_widget.show()

    app.exec_()
