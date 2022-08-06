import sys
from PyQt5.QtWidgets import QApplication,QWidget,QDesktopWidget
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("Title")
    #窗口的大小
    w.resize(500,500)
    # w.move(0,0)
    #调整窗口在屏幕中央显示
    #屏幕可用区域的中央位置
    center_pointer = QDesktopWidget().availableGeometry().center()
    #中央位置的x,y轴
    x = center_pointer.x()
    y = center_pointer.y()
    print(w.frameGeometry())
    print(w.frameGeometry().getRect())
    #获取窗口实际的x,y,width,height
    old_x,old_y,width,height = w.frameGeometry().getRect()
    #将窗口中心移动到屏幕中心
    w.move(x - width/2,y - height/2)
    w.show()
    app.exec()