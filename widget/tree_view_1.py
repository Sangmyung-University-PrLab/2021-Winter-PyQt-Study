import sys

from PyQt5.Qt import Qt
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import QTreeView

def create_model():
    model = QStandardItemModel(0,3)
    model.setHeaderData(0, Qt.Horizontal,'Name')
    model.setHeaderData(1, Qt.Horizontal, 'Size')
    model.setHeaderData(2, Qt.Horizontal, 'Type')

    return model

def tree_event(index):
    global model

    data1 = model.item(index.row(),0).data(Qt.DisplayRole)
    data2 = model.item(index.row(), 1).data(Qt.DisplayRole)
    data3 = model.item(index.row(), 2).data(Qt.DisplayRole)

    print(data1,data2,data3)

def remove_event():
    global model, tree
    model.removeRow(tree.currentIndex().row())
    
if __name__ == '__main__':
    app = QApplication(sys.argv)

    tree = QTreeView()
    model = create_model()
    tree.setModel(model)
    tree.show()

    tree.clicked.connect(tree_event) #index가 포함된 시그널 발생

    model.insertRow(0)
    model.setData(model.index(0,0), 'test.py')
    model.setData(model.index(0, 1), '100')
    model.setData(model.index(0, 2), 'python script')

    model.insertRow(0)
    model.setData(model.index(0, 0), 'image.jpg')
    model.setData(model.index(0, 1), '264')
    model.setData(model.index(0, 2), 'Image file')

    button = QPushButton('remove')
    button.show()
    button.clicked.connect(remove_event)

    app.exec_()
