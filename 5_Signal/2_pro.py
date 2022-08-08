"""
    自行定义信号，在合适的时机，自行发射信号
"""
import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    # 声明一个信号 只能放在函数的外面
    my_signal = pyqtSignal(str)
    def __init__(self):
        super(MyWindow, self).__init__()
        self.init_ui()
        self.msg_history = list()
    def init_ui(self):
        self.resize(500,200)
        container = QVBoxLayout()
        self.msg = QLabel("")
        self.msg.resize(440,15)
        # 自动换行
        self.msg.setWordWrap(True)
        self.msg.setAlignment(Qt.AlignTop)
        # 创建一个滚动对象
        scroll = QScrollArea()
        scroll.setWidget(self.msg)
        # 创建垂直布局器,用来添加自动滚动条
        v_layout = QVBoxLayout()
        v_layout.addWidget(scroll) # 自动滚动条
        # 创建水平布局器
        h_layout = QHBoxLayout()
        btn = QPushButton("开始检测",self)
        # 绑定按钮的点击,点击按钮则开始检测
        btn.clicked.connect(self.check)
        h_layout.addStretch(1) #伸缩器
        h_layout.addWidget(btn)
        h_layout.addStretch(1)
        # 操作将要显示的控件以及子布局器添加到container
        container.addLayout(v_layout)
        container.addLayout(h_layout)
        #设置布局器
        self.setLayout(container)
        #绑定信号和槽
        self.my_signal.connect(self.my_slot)
    def my_slot(self,msg):
        print(msg)
        self.msg_history.append(msg)
        self.msg.setText("<br>".join(self.msg_history))
        self.msg.resize(400,self.msg.frameSize().height() + 15)
    def check(self):
        for i,ip in enumerate(["192.168.1.%d"% x for x in range(1,255)]):
            msg = "模拟,正在检查 %s 上的漏洞...." % ip
            # 打印所有信号
            # print(msg)
            # 打印带漏洞的信号
            if i % 5 == 3:
                # 表示发射信号 对象.信号.发射(参数)
                self.my_signal.emit(msg + "[发现漏洞]") #相当于调用了 my_slot 函数
            time.sleep(0.01)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()
