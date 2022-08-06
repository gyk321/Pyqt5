import sys

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    w.setWindowTitle("天马喂狗")
    #窗口添加控件
    btn = QPushButton("按钮")
    #设置按钮的父亲是当前窗口,等于是添加到窗口中显示
    btn.setParent(w)
    #显示窗口
    w.show()

    app.exec()