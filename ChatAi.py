import  json
import  settings
from fuzzywuzzy import process
class ChatAi():
    chat_ai_data = {}
    chat_ai_question = []
    def __init__(self):
        self.chat_ai_data = self.get_chat_ai_data_cy()
        self.chat_ai_question = list(self.chat_ai_data.keys())

    def get_chat_ai_data_cy(self):
        with open(settings.CHATAI_DATA_PATH, "r") as f:
            return json.loads(f.read())

    def chat_cy(self,key,num=0):
        """
        :param key: 聊天内容
        :return:
        (是否有匹配结果,回答内容，是否有下一个)
        """
        flag, question, next = self.mathch_question_cy(key,num)
        if flag:
            print(f"匹配成功，问题：{question}，回答为：{self.chat_ai_data[question]}")
            return True,self.chat_ai_data[question],next
        else:
            return False,settings.DEFAULT_REPLY,False

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
            return False,None,False
        next = False
        if len(question)-1 > num and question[num+1][1] > settings.MIN_AI_MATCH_VALUE:
            next = True
        return True,question[num][0],next

if __name__ == '__main__':
    chat =  ChatAi()

    flag = True
    num = 0
    while next:
        flag,question,next = chat.chat_cy("你喜欢吃什么",num)
        print(question)
        num += 1
    print("===============================")
    next = True
    flag = True
    num = 0
    while next:
        flag,question,next = chat.chat_cy("你喜欢吃什么啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊",num)
        print(question)
        num += 1
    print("===============================")
    next = True
    flag = True
    num = 0
    while next:
        flag,question,next = chat.chat_cy("啊啊啊啊啊啊啊啊啊啊你喜欢吃什么啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊",num)
        print(question)
        num += 1
