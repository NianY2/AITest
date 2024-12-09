import  os
import  json
import  settings
import  utils.Password as Password

def data_path_cy():
    """
    判断保存程序数据的文件夹是否存在，不存在则创建
    """
    if not os.path.exists(settings.PROGRAM_DATA_PATH):
        os.mkdir(settings.PROGRAM_DATA_PATH)
        print("创建程序数据文件夹成功")

def user_data_path_cy():
    """
    判断保存用户数据文件夹是否存在，不存在则创建
    """
    if not os.path.exists(settings.USER_DATA_PATH):
        os.mkdir(settings.USER_DATA_PATH)
        print("创建用户数据文件夹成功")

def user_list_data_cy():
    """
    文件 user.json
    """
    # 判断文件是否存在，不存在则创建
    if not os.path.exists(settings.USER_LIST_DATA_PATH):
        with open(settings.USER_LIST_DATA_PATH, "w+",encoding="utf8") as f:
            for key in settings.DEFAULT_USER:
                settings.DEFAULT_USER[key]["password"] = Password.password_encrypt(settings.DEFAULT_USER[key]["password"])
            f.write(json.dumps(settings.DEFAULT_USER))
            print("创建默认用户数据成功")

def login_data_cy():
    """
    文件 login.json
    """
    # 判断文件是否存在，不存在则创建
    if not os.path.exists(settings.LOGIN_DATA_PATH):
        with open(settings.LOGIN_DATA_PATH, "w+",encoding="utf8") as f:
            test_data = {
                "is_login": False,
                "uid": None,
            }
            data = test_data
            f.write(json.dumps(data))
            print("创建默认登录数据成功")

def chat_ai_data_cy():
    """
    文件 ChatAi.json
    """
    # 判断文件是否存在，不存在则创建
    if not os.path.exists(settings.CHATAI_DATA_PATH):
        with open(settings.CHATAI_DATA_PATH, "w+",encoding="utf8") as f:
            f.write(json.dumps(settings.DEFAULT_CHATAI))
            print("创建默认ChatAi数据成功")


if __name__ == '__main__':
    data_path_cy()
    user_data_path_cy()
    user_list_data_cy()
    chat_ai_data_cy()
    login_data_cy()