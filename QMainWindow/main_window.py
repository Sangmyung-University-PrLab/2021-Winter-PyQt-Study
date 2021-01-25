import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QWidget, QVBoxLayout, QPushButton, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)

        self.action_load = QAction(QIcon(), 'Load File', self)
        self.action_load.setShortcut('Ctrl+L')
        self.action_load.triggered.connect(self.load_event)

        self.action_exit = QAction(QIcon(), 'Exit', self)
        self.action_exit.setShortcut('ESC')
        self.action_exit.triggered.connect(self.close)

        self.status_bar = self.statusBar()

        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu('File')
        self.option_menu = self.menu_bar.addMenu('Options')

        self.file_menu.addAction(self.action_load)
        self.file_menu.addAction(self.action_exit)

        self.tool_bar = self.addToolBar('Tool Bar')
        self.tool_bar.addAction(self.action_load)
        self.tool_bar.addAction(self.action_exit)

        window_widget = QWidget()
        window_layout = QVBoxLayout(window_widget)
        window_layout.addWidget(QPushButton('Button'))
        self.setCentralWidget(window_widget)

    def load_event(self):
        self.status_bar.showMessage('Load File...')
        path = QFileDialog.getOpenFileName(self)
        print(path)
        self.status_bar.clearMessage()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
