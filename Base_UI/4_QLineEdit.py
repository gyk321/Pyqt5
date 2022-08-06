import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QLineEdit
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("Title")
    #纯文本
    label = QLabel("account:",w)
    label.setGeometry(20,20,20,20)
    #文本框
    edit = QLineEdit(w)
    edit.setPlaceholderText("请输入账号:")
    edit.setGeometry(55,20,200,20)
    #在窗口里面添加控件
    btn = QPushButton("注册",w)
    btn.setGeometry(50,80,70,30)

    w.show()

    app.exec()