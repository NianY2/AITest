"""初始化程序"""
import Initialize
Initialize.data_path_cy()
Initialize.user_data_path_cy()
Initialize.user_list_data_cy()
Initialize.chat_ai_data_cy()
Initialize.login_data_cy()

print("======================程序初始化完成======================")

# 模拟登入
from Login import Login
login = Login()
flag,_ = login.login_cy("admin", "admin")
if flag:
    print("======================登录成功======================")

import sys
from MainGUI import MainWindow
from PyQt5.QtWidgets import QApplication

# 创建一个QApplication对象，sys.argv参数确保了命令行参数能够传递给应用程序
app = QApplication(sys.argv)
window = MainWindow()
window.show()
# 进入应用程序的主事件循环，直到应用程序退出。app.exec_()是一个阻塞调用，直到退出事件循环
app.exec_()
print("======================程序退出======================")