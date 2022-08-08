import sys
from PyQt5.QtWidgets import QDialog,QPushButton,QApplication
# 通过点击操作弹出，起到提示作用
class MyDialog(QDialog):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.init_ui()
    def init_ui(self):
        ok_btn = QPushButton("确定",self)
        ok_btn.setGeometry(50,50,100,30)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyDialog()
    w.setWindowTitle("对话框")
    w.show()
    app.exec()