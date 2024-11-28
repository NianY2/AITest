import json
import  os
from typing import Optional

import  settings
import  utils.Password as Password
class Login():
    isLosgin = False
    user_data = None
    def __init__(self):
        with open(settings.USER_DATA_PATH, "r+") as f:
            self.user_data = json.loads(f.read())

    def register(self,sid, pwd,school):
        """注册"""
        print("注册",sid, pwd,school)

    def login(self,sid:str, pwd:str)->(bool, Optional[dict]):
        """登录"""
        if sid in self.user_data:
            encrypted_pwd = self.user_data[sid]["password"]
            if Password.password_verify(pwd, encrypted_pwd):
                return  True, self.user_data[sid]
        else:
            return False,None

if __name__ == '__main__':
    print(Login().login("admin", "admin"))
    print(Login().login("admin2", "pbkdf2"))