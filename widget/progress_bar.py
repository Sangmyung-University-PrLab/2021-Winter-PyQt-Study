from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import QProgressBar

import sys


def progress_event():
    global progress
    val = progress.value()
    progress.setValue(val + 10)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    progress = QProgressBar()
    progress.setRange(1, 100)
    progress.reset()

    # 실행 중인 것만 보여주고 싶을 때
    # progress.setRange(0,0)

    progress.show()

    button = QPushButton('Button')
    button.show()
    button.clicked.connect(progress_event)

    app.exec_()
