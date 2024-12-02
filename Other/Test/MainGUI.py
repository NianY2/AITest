"""
包含图形用户界面
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from  HtmlInteraction import  HtmlInteraction

def main():
    app = QApplication(sys.argv)
    web_view = QWebEngineView()
    web_view.setWindowTitle('登录界面')
    web_view.setGeometry(5,30,1355,730)
    channel = QWebChannel()
    html_interaction = HtmlInteraction()
    channel.registerObject("obj", html_interaction)
    web_view.page().setWebChannel(channel)
    web_view.load(QUrl('file:///./template/AIChat.html'))
    web_view.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    # 创建一个QApplication对象，sys.argv参数确保了命令行参数能够传递给应用程序
    main()
    # 进入应用程序的主事件循环，直到应用程序退出。app.exec_()是一个阻塞调用，直到退出事件循环
    print("程序退出")

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle('登录界面')
#         self.setGeometry(5, 30, 1355, 730)
#
#         web_view = QWebEngineView()
#         channel = QWebChannel()
#         html_interaction = HtmlInteraction()
#         channel.registerObject("obj", html_interaction)
#         web_view.page().setWebChannel(channel)
#         web_view.load(QUrl('file:///./template/AIChat.html'))
#
#         # 启用开发者工具
#         web_page = web_view.page()
#         web_inspector = QWebEngineView()
#         web_inspector.setPage(web_page)
#         web_inspector.setVisible(False)
#
#         layout = QVBoxLayout()
#         layout.addWidget(web_view)
#         layout.addWidget(web_inspector)
#
#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)
#
#         # 绑定快捷键 F12 切换开发者工具
#         web_page.action(QWebEnginePage.InspectElement).setShortcut('F12')
#         web_page.action(QWebEnginePage.InspectElement).triggered.connect(self.toggle_inspector)
#
#     def toggle_inspector(self):
#         self.findChild(QWebEngineView, "inspector").setVisible(
#             not self.findChild(QWebEngineView, "inspector").isVisible()
#         )
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())