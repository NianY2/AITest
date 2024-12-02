import  json
import  settings
from PyQt5.QtCore import QObject, pyqtSlot
from utils.Response import  Rseponse
from Login import Login
from ChatAi import ChatAi

chat_ai = ChatAi()
class HtmlInteraction(QObject):
    """
    与HTML交互的类
    """
    @pyqtSlot(str, result=str)
    def print_message(self, message):
        print(message)
        return "Test"
    @pyqtSlot(str, result=str)
    def login_cy(self, msg):
        """登入接口"""
        login = Login()
        msg_data = json.loads(msg)
        flag, data = login.login_cy(msg_data["sid"], msg_data["pwd"])
        if flag:
            return Rseponse.success(data,"登入成功")
        else:
            return Rseponse.fail("账号密码错误")

    @pyqtSlot(str, result=str)
    def chat_ai_cy(self, msg):
        """聊天接口"""
        msg_data = json.loads(msg)
        data = chat_ai.chat_cy(msg_data["key"],msg_data.get("num",0),msg_data.get("chat_index",0))
        re_data = {
            "flag":data[0],
            "answer":data[1],
            "next":data[2]
        }
        return Rseponse.success(re_data)

    @pyqtSlot(str,result=str)
    def start_reply_cy(self):
        """启动回复"""
        re_data = {
            "flag":True,
            "answer":settings.START_REPLY,
            "next":False
        }
        return Rseponse.success(re_data)


    @pyqtSlot(str,result=str)
    def get_chat_data_cy(self,msg):
        """获取某份聊天记录"""
        msg_data = json.loads(msg)
        index = msg_data.get("index",0)
        print(chat_ai.get_chat_list_data_cy(index))
        return Rseponse.success(chat_ai.get_chat_list_data_cy(index))
    
    @pyqtSlot(str,result=str)
    def get_chat_list_title_cy(self):
        return Rseponse.success(chat_ai.get_chat_list_title_cy())

    @pyqtSlot(str,result=str)
    def delete_chat_list_cy(self,msg):
        msg_data = json.loads(msg)
        index = msg_data.get("index",0)
        chat_ai.delete_chat_list_cy(index)
        return Rseponse.success()