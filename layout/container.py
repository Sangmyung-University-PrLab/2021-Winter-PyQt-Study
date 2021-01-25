import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QGroupBox, QVBoxLayout, QPushButton, QScrollArea, \
    QLabel, QTabWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(400, 400)
    window.show()

    main_layout = QHBoxLayout()
    window.setLayout(main_layout)

    group_box = QGroupBox('그룹')
    group_layout = QVBoxLayout(group_box)
    group_layout.addWidget(QPushButton('Group Box Button'))
    main_layout.addWidget(group_box)

    scroll_area = QScrollArea()
    label = QLabel('a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\n\y\nz')
    scroll_area.setWidget(label)
    main_layout.addWidget(scroll_area)

    tab_widget = QTabWidget()
    tab1 = QPushButton('Tab1 Button')
    tab_widget.addTab(tab1, 'Tab 1')

    tab2 = QWidget()
    tab_layout = QVBoxLayout(tab2)
    tab_layout.addWidget(QLabel('Tab2 Label'))
    tab_layout.addWidget(QPushButton('Tab2 Button'))
    tab_widget.addTab(tab2, 'Tab 2')

    main_layout.addWidget(tab_widget)

    app.exec_()
