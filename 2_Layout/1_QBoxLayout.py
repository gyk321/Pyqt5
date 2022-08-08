import sys
from PyQt5.QtWidgets import QApplication,QVBoxLayout,QWidget,QPushButton
class MyWindow(QWidget):
    def __init__(self):
        #一定要调用父类的__Init__
        super().__init__()
        #设置大小
        self.resize(300,300)
        #设置标题
        self.setWindowTitle("垂直布局")
        #垂直布局
        layout = QVBoxLayout()
        # 作用是在布局器中增加一个伸缩量,里面的参数表示QSpacerItem中的个数,默认值为零
        # 会将你放在layout中的空间压缩为默认大小
        # 下面的伸缩量为 1:1:1:2
        #按钮1  按钮加入布局器不用设置父对象
        layout.addStretch(1)
        #按钮1
        btn1 = QPushButton("按钮1")
        #添加到布局器中
        layout.addWidget(btn1)
        layout.addStretch(1)
        #按钮2
        btn2 = QPushButton("按钮2")
        layout.addWidget(btn2)
        layout.addStretch(1)
        #按钮3
        btn3 = QPushButton("按钮3")
        layout.addWidget(btn3)
        layout.addStretch(2)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #创建一个QWidget子类
    w = MyWindow()
    w.show()
    app.exec()


