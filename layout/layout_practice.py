import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)
        # main_layout.addWidget(QPushButton('Button'))
        layout = QHBoxLayout()

        label1 = QLabel('label1')
        label2 = QLabel('label2')
        label3 = QLabel('label3')

        label1.setStyleSheet('background-color:red')
        label2.setStyleSheet('background-color:yellow')
        label3.setStyleSheet('background-color:green')

        main_layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        main_layout.addLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # window = QWidget()
    window = MainWindow()
    window.resize(500, 500)
    window.show()

    app.exec_()
