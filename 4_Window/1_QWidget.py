import sys
from PyQt5.QtWidgets import QWidget,QLabel,QApplication

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()
    def initUI(self):
        label = QLabel("这是文字")
        label.setStyleSheet("font-size:30px;color:red")
        label.setParent(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.setWindowTitle('QWidget')
    w.show()
    app.exec()