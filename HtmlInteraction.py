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
    def login(self, msg):
        """登入接口"""
        msg_data = json.loads(msg)
        flag, data = Login().login(msg_data["sid"], msg_data["pwd"])
        if flag:
            return Rseponse.success(data,"登入成功")
        else:
            return Rseponse.fail("账号密码错误")

    @pyqtSlot(str, result=str)
    def chat_ai_cy(self, msg):
        """聊天接口"""
        msg_data = json.loads(msg)
        data = chat_ai.chat_cy(msg_data["key"],msg_data.get("num",0))
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
        """获取聊天记录"""
        return Rseponse.success([
            {"type":"ai","content":"欢迎使用CYChatAi,我现在可以回答研学、旅游、美食、健康方面的问题。"},
            {"type":"user","content":"你好"},
            {"type":"ai","content":"你好"},
            {"type": "user", "content": "你好"},
            {"type": "ai", "content": "你好"},
            {"type": "user", "content": "你好"},
            {"type": "ai", "content": "你好"}
        ])