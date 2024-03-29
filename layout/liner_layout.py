import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(500, 500)

    layout = QHBoxLayout(window)  # Horizental
    window.setLayout(layout)

    label1 = QLabel('label1')
    label2 = QLabel('label2')
    label3 = QLabel('label3')

    label1.setStyleSheet('background-color:red')
    label2.setStyleSheet('background-color:yellow')
    label3.setStyleSheet('background-color:green')

    layout.addWidget(label1)
    layout.addWidget(label2)
    layout.addWidget(label3)

    window.show()

    app.exec_()
