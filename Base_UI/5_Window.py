import sys
from PyQt5.QtWidgets import QApplication,QWidget
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("Title")

    #窗口的大小
    w.resize(500,500)
    w.show()
    app.exec()