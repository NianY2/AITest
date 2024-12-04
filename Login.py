import json,os,datetime
from typing import Optional
import  settings
import  utils.Password as Password

class Login():
    user_list_data = None
    login_data = None
    login_user_data = None
    def __init__(self):
        self.get_user_list_data_cy()
        self.get_login_data_cy()

    def register_cy(self,sid, pwd,school):
        """注册"""
        print("注册",sid, pwd,school)

    def login_cy(self,sid:str, pwd:str)->(bool, Optional[dict]):
        """登录"""
        if sid in self.user_list_data:
            encrypted_pwd = self.user_list_data[sid]["password"]
            if Password.password_verify(pwd, encrypted_pwd):
                self.login_data = {"isLosgin":True,"uid":sid}
                self.save_login_data_cy()
                self.get_login_user_data_cy()
                return  True, self.user_list_data[sid]
        else:
            return False,None

    def get_user_list_data_cy(self):
        """获取用户数据"""
        with open(settings.USER_LIST_DATA_PATH, "r+") as f:
            self.user_list_data = json.loads(f.read())

    def save_user_list_data_cy(self):
        """保存用户数据"""
        with open(settings.USER_LIST_DATA_PATH, "w+") as f:
            f.write(json.dumps(self.user_list_data))

    def get_login_data_cy(self):
        """获取登录数据"""
        with open(settings.LOGIN_DATA_PATH, "r+") as f:
            self.login_data = json.loads(f.read())
        if self.login_data.get('isLosgin'):
            self.get_login_user_data_cy()


    def save_login_data_cy(self):
        """保存登录数据"""
        with open(settings.LOGIN_DATA_PATH, "w+") as f:
            f.write(json.dumps(self.login_data))


    def get_login_user_data_cy(self):
        """验证用户数据文件是否存在，不存在则创建"""
        login_user_data = os.path.join(settings.USER_DATA_PATH,f"{self.login_user['uid']}.json")
        if not os.path.exists(login_user_data):
            print(f"第一次登入,创建用户数据文件,{login_user_data}")
            self.login_user_data = {
                "uid": self.login_user['uid'],
                "chat_data_list": []
            }
            self.save_login_user_data_cy()
        else:
            with open(login_user_data, "r+",encoding="utf8") as f:
                self.login_user_data = json.loads(f.read())

    def save_login_user_data_cy(self):
        """保存登入用户数据"""
        login_user_data = os.path.join(settings.USER_DATA_PATH,f"{self.login_user['uid']}.json")
        with open(login_user_data, "w+",encoding="utf8") as f:
            f.write(json.dumps(self.login_user_data))

    
    def add_chat_data_cy(self,index,type,content):
        """添加聊天记录"""
        if  len(self.login_user_data["chat_data_list"]) == 0 or len(self.login_user_data["chat_data_list"]) == index:
            print(f"添加聊天记录{content}")
            self.login_user_data["chat_data_list"].append({
                "title": content,
                "create_date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "update_date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "data": [{"type": "ai", "content": settings.START_REPLY},{"type": type, "content": content}]
            })
        else:
            self.login_user_data["chat_data_list"][index]["update_date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.login_user_data["chat_data_list"][index]["data"].append({"type": type, "content": content})
        self.save_login_user_data_cy()

    def delete_chat_data_cy(self,index):
        """删除聊天记录"""
        self.login_user_data["chat_data_list"].pop(index)
        self.save_login_user_data_cy()

    @property
    def isLosgin(self):
        return self.login_data.get('isLosgin',False)
    @property
    def login_user(self):
        uid = self.login_data.get('uid')
        return self.user_list_data[uid]

if __name__ == '__main__':
    print(Login().login_cy("admin", "admin"))
    # print(Login().login_cy("202212390606", "202212390606"))
    # print(Login().login_cy("admin2", "admin2222"))