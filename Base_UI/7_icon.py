import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle("Title")
    #设置图标
    w.setWindowIcon(QIcon('icon.png'))
    w.show()
    app.exec()