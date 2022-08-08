import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    #只要Qt制作的app,必须有且只有1个QApplication对象
    #sys.argv当作参数的目的是将运行时的命令参数传递给QApplication对象
    app = QApplication(sys.argv)

    #创建QWidget对象
    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle("第一个PyQt")

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()