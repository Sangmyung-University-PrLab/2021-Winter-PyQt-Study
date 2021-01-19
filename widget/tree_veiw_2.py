import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QLabel
from PyQt5.QtWidgets import QTreeView

def tree_event(index):
    global model,label

    if model.isDir(index):
        print('Diecctory')
    else:
        path= model.filePath(index)
        label.setPixmap(QPixmap(path))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    tree = QTreeView()
    model = QFileSystemModel()
    tree.setModel(model)
    tree.show()

    root_path = '../'
    model.setRootPath(root_path)
    tree.setRootIndex(model.index(root_path))
    tree.setColumnWidth(0,400)
    tree.resize(700,500)

    tree.setColumnHidden(1,True)
    tree.setColumnHidden(2, True)
    tree.setColumnHidden(3, True)

    tree.doubleClicked.connect(tree_event)

    label = QLabel('label')
    label.resize(600,400)
    label.show()

    app.exec_()
