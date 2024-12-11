import  json
import  settings
from PyQt5.QtCore import QObject, pyqtSlot
from utils.Response import  Rseponse
from Login import Login
from ChatAi import ChatAi
import  utils.glo as glo
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
            glo.get_value('update_page')("AIChat")
            return Rseponse.success(data,"登入成功")
        else:
            return Rseponse.fail(data)
            
    @pyqtSlot(str, result=str)
    def register_cy(self, msg):
        """注册接口"""
        login = Login()
        msg_data = json.loads(msg)
        flag, data = login.register_cy(sid=msg_data["sid"], pwd=msg_data["pwd"], school=msg_data["school"],name=msg_data["name"])
        if flag:
            return Rseponse.success(data,"注册成功")
        else:
            return Rseponse.fail(data)
        
    @pyqtSlot(str, result=str)
    def chat_ai_cy(self, msg):
        """聊天接口"""
        msg_data = json.loads(msg)
        data = chat_ai.chat_cy(msg_data["key"],msg_data.get("num",0),msg_data.get("chat_index",0))
        re_data = {
            "flag":data[0],
            "answer":data[1],
            "next":data[2],
            "other_question_list": data[3]
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
        """获取聊天记录标题列表"""
        return Rseponse.success(chat_ai.get_chat_list_title_cy())

    @pyqtSlot(str,result=str)
    def delete_chat_list_cy(self,msg):
        """删除聊天记录"""
        msg_data = json.loads(msg)
        index = msg_data.get("index",0)
        chat_ai.delete_chat_list_cy(index)
        return Rseponse.success()

    @pyqtSlot(str,result=str)
    def keep_chat_data_cy(self,msg):
        """保存聊天记录"""
        msg_data = json.loads(msg)
        index = msg_data.get("index",0)
        if chat_ai.keep_chat_data_cy(index):
            return Rseponse.success()
        else:
            return Rseponse.fail("保存失败")
        
    @pyqtSlot(str,result=str)
    def user_data_cy(self):
        """获取用户数据"""
        login = Login()
        return Rseponse.success(login.login_user)
    
    @pyqtSlot(str,result=str)
    def logout_cy(self):
        """退出登录"""
        login = Login()
        login.logout_cy()
        glo.get_value('update_page')("login")
        return Rseponse.success()