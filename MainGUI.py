"""
包含图形用户界面
"""
import json
import sys
from Login import Login
from utils.Response import  Rseponse
from PyQt5.QtCore import *
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class HtmlInteraction(QMainWindow):
    @pyqtSlot(str, result=str)
    def print_message(self, message):
        print(message)
        return "Test"
    @pyqtSlot(str, result=str)
    def login(self, msg):
        """登入接口"""
        msg_data = json.loads(msg)
        flag, data = Login().login(msg_data["sid"], msg_data["pwd"])
        if flag:
            return Rseponse.success(data,"登入成功")
        else:
            return Rseponse.fail("账号密码错误")





def main():
    app = QApplication(sys.argv)
    web_view = QWebEngineView()
    web_view.setWindowTitle('登录界面')
    web_view.setGeometry(5,30,1355,730)
    channel = QWebChannel()
    html_interaction = HtmlInteraction()
    channel.registerObject("obj", html_interaction)
    web_view.page().setWebChannel(channel)
    web_view.load(QUrl('file:///./template/Login.html'))
    web_view.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    # 创建一个QApplication对象，sys.argv参数确保了命令行参数能够传递给应用程序
    main()
    # 进入应用程序的主事件循环，直到应用程序退出。app.exec_()是一个阻塞调用，直到退出事件循环
    print("程序退出")