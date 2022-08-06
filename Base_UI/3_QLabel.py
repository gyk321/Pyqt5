import sys

from PyQt5.QtWidgets import QApplication,QWidget,QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("天马喂狗")
    #创建一个Label(纯文本),在创建的时候指定了父对象
    label = QLabel("账号:",w)
    label.setGeometry(60,50,200,50)
    w.show()
    app.exec()