import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.init_ui()
    def click_my_btn(self,arg):
        # 将按钮被点击时触发的信号与我们定义的函数(方法)进行绑定
        # 这里的参数正好是信号发出,传递的参数
        print("点击按钮", arg)
    def init_ui(self):
        #更改当前Widge的宽高
        self.resize(500,300)
        #创建一个按钮
        btn = QPushButton("Push me",self)
        #设置窗口位置、宽高
        btn.setGeometry(200,200,100,30)
        # 将按钮被点击时触发的信号与我们定义的函数(方法)进行绑定
        # 注意:这里没有(),即写函数的名字,而不是名字()
        btn.clicked.connect(self.click_my_btn)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()