import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("登录")
        self.setGeometry(5,30,1355,730) # 设置窗口的位置和大小（x, y, width, height）
        self.browser=QWebEngineView()
        # 加载本地的HTML界面
        url=r'file:///./template/Login.html'
        self.browser.load(QUrl(url))
        self.setCentralWidget(self.browser)

if __name__ == '__main__':
    app=QApplication(sys.argv)  # 创建一个QApplication对象，sys.argv参数确保了命令行参数能够传递给应用程序
    win=MainWindow()
    win.show()
    app.exit(app.exec_()) # 进入应用程序的主事件循环，直到应用程序退出。app.exec_()是一个阻塞调用，直到退出事件循环
    print("程序退出")