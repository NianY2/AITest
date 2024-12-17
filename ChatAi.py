import  json
from os import mkdir
import os
import tkinter  
from tkinter import filedialog
import  settings
from  Login import  Login
from fuzzywuzzy import process,fuzz
from utils import  PythonCode
class ChatAi:
    chat_ai_data = {}
    chat_ai_question = []
    # 是否为代码模式
    is_code = False
    def __init__(self):
        self.chat_ai_data = self.get_chat_ai_data_cy()
        self.chat_ai_question = list(self.chat_ai_data.keys())
    

    def exit_code_mode(self):
        # 退出代码模式
        self.is_code = False
        print("==============================退出代码模式==============================")

    def get_chat_ai_data_cy(self):
        with open(settings.CHATAI_DATA_PATH, "r",encoding="utf8") as f:
            return json.loads(f.read())

    def chat_cy(self,key,num=0,index=0):
        """
        :param key: 聊天内容
        :return:
        (是否有匹配结果,回答内容，是否有下一个)
        """
        print(key)
        if key == "代码模式":
            print("==============================进入代码模式==============================")
            self.is_code = True
            flag = True
            ans  = settings.CODE_REPLY
            next = False
            other_question_list = [("exit",100),("exit",100),("退出",100)]
            
        elif self.is_code and (key == "退出" or key == "exit"):
            self.exit_code_mode()
            flag = True
            ans  = settings.CODE_EXIT_REPLY
            next = False
            other_question_list = [("代码模式",100),("代码模式",100),("你好",100)]
            
        
        elif self.is_code:
            flag = True
            next = False
            other_question_list = [("exit",100),("exit",100),("退出",100)]
            try:
                ans = f"""
提供的代码片段是一个有效的Python代码片段
输出结果为：
{PythonCode.get_python_code_result(key)}
"""
            except PythonCode.NoPythonCodeError as e:
                ans = settings.CODE_DEFAULT_REPLY
            except Exception as e:
                ans = "这段代码发生了错误，错误信息为："+str(e)
            
        else:
            flag, question, next,other_question_list = self.mathch_question_cy(key,num)
            if flag:
                ans = self.chat_ai_data[question]
            else:
                ans = settings.DEFAULT_REPLY
            print(f"匹配成功，问题：{question}，回答为：{ans}")
        login = Login()
        login.add_chat_data_cy(index,"user",key)
        if flag:
            login.add_chat_data_cy(index,"ai",ans)
            return True,ans,next,other_question_list
        else:
            login.add_chat_data_cy(index,"ai",settings.DEFAULT_REPLY)
            return False,settings.DEFAULT_REPLY,False,other_question_list
        
    def mathch_question_cy(self,key,num=0):
        """
        匹配问题
        :param key: 问题
        :return:
        (是否有匹配结果,匹配结果，是否有下一个)
        """
        question = process.extract(key, self.chat_ai_question)
        print(f"问题：{key},匹配结果：{question}")
        if question[num][1] < settings.MIN_AI_MATCH_VALUE:
            return False,None,False,question
        next = False
        if len(question)-1 > num and question[num+1][1] > settings.MIN_AI_MATCH_VALUE:
            next = True
        return True,question[num][0],next,question

    def get_chat_list_title_cy(self):
        login = Login()
        title_list = [i["title"] for i in login.login_user_data["chat_data_list"]]
        return  title_list
    
    def get_chat_list_data_cy(self,index):
        login = Login()
        return  login.login_user_data["chat_data_list"][index]["data"]
    
    def delete_chat_list_cy(self,index):
        login = Login()
        login.delete_chat_data_cy(index)

    def keep_chat_data_cy(self,index):
        login = Login()
        data = login.login_user_data["chat_data_list"][index]
        date = "".join(data['create_date'].split(":"))
        date = "-".join(date.split(" "))
        try:
            # 选择文件夹
            root = tkinter.Tk()
            root.withdraw() # 隐藏主窗口
            flies_path = filedialog.askdirectory() # 选择文件夹路径
            print(flies_path)
        except Exception as e:
            print("选择文件夹失败")
            print(e)
            return False
        if flies_path == "":
            print("选择文件夹失败")
            return False
        flie_path = os.path.join(flies_path,f"{login.login_user['uid']}-{date}.txt")
        with open(flie_path, "w+",encoding="utf8") as file:
            for i in data["data"]:
                file.write(f"{i['type']:<5}{i['content']}\n")
        os.startfile(flies_path)
        return True



if __name__ == '__main__':
    chat =  ChatAi()
    chat.keep_chat_data_cy(0)
    print([i for i in range(10)])
    # for k,v in enumerate(chat.get_chat_list_title_cy()):
    #     print(k,v)
    #     print(chat.get_chat_list_data_cy(k))
    # flag = True
    # num = 0
    # while next:
    #     flag,question,next = chat.chat_cy("你喜欢吃什么",num)
    #     print(question)
    #     num += 1
    # print("===============================")
    # next = True
    # flag = True
    # num = 0
    # while next:
    #     flag,question,next = chat.chat_cy("你喜欢吃什么啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊",num)
    #     print(question)
    #     num += 1
    # print("===============================")
    # next = True
    # flag = True
    # num = 0
    # while next:
    #     flag,question,next = chat.chat_cy("啊啊啊啊啊啊啊啊啊啊你喜欢吃什么啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊",num)
    #     print(question)
    #     num += 1
