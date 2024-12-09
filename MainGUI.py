"""
包含图形用户界面
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from HtmlInteraction import  HtmlInteraction
import settings
from Login import Login

# 定义一个对象，其中包含槽函数，注册到channel可以传递给JS代码
html_interaction = HtmlInteraction()
# 定义一个channel全局对象，用于注册一些对象提供给html页面中的JS代码调用
channel = QWebChannel()
channel.registerObject("obj", html_interaction)
import utils.glo as glo
class MainWindow(QWidget):
    """
    图形用户界面类
    """
    def __init__(self):
        global page
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.setGeometry(5, 30, 1355, 730)
        channel.registerObject("obj", html_interaction)
        self.browser.page().setWebChannel(channel)
        login = Login()
        if login.is_login:
            self.browser.setUrl(QUrl(settings.FILES_PATH['page']['AIChat']))
        else:
            self.browser.setUrl(QUrl(settings.FILES_PATH['page']['login']))
        glo.set_value('update_page',self.update_page)

        # 设置开发者工具
        self.dev_tools = QWebEngineView()
        self.browser.page().setDevToolsPage(self.dev_tools.page())

        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        self.setLayout(layout)
        # 添加窗口标题
        self.setWindowTitle("CYAI")
        # 绑定快捷键 F12 到打开/关闭开发者工具的槽函数
        shortcut = QShortcut(QKeySequence("F12"), self)
        shortcut.activated.connect(self.toggle_dev_tools)
    
    def update_page(self,page_name):
        """更新页面"""
        self.browser.setUrl(QUrl(settings.FILES_PATH['page'][page_name]))

    def toggle_dev_tools(self):
        """切换开发者工具的可见性"""
        if self.dev_tools.isVisible():
            self.dev_tools.hide()
        else:
            self.dev_tools.show()
            self.dev_tools.resize(800, 600)  # 可选：设置初始大小
            self.dev_tools.move(self.geometry().right(), self.geometry().top())  # 可选：设置初始位置

if __name__ == '__main__':
    # 创建一个QApplication对象，sys.argv参数确保了命令行参数能够传递给应用程序
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # 进入应用程序的主事件循环，直到应用程序退出。app.exec_()是一个阻塞调用，直到退出事件循环
    app.exec_()
    print("程序退出")
