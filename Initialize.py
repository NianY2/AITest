import  os
import  json
import  settings
import  utils.Password as Password

def user_data_cy():
    """
    文件 user.json
    """
    # 判断文件是否存在，不存在则创建
    if not os.path.exists(settings.USER_DATA_PATH):
        with open(settings.USER_DATA_PATH, "w+") as f:
            for key in settings.DEFAULT_USER:
                settings.DEFAULT_USER[key]["password"] = Password.password_encrypt(settings.DEFAULT_USER[key]["password"])
            f.write(json.dumps(settings.DEFAULT_USER))
            print("创建默认用户数据成功")
def chat_ai_data_cy():
    """
    文件 ChatAi.json
    """
    # 判断文件是否存在，不存在则创建
    if not os.path.exists(settings.CHATAI_DATA_PATH):
        with open(settings.CHATAI_DATA_PATH, "w+") as f:
            f.write(json.dumps(settings.DEFAULT_CHATAI))
            print("创建默认ChatAi数据成功")


if __name__ == '__main__':
    user_data_cy()
    chat_ai_data_cy()