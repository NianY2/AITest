import  os
BATH_PATH =  os.getcwd()
PROGRAM_DATA_PATH = os.path.join(BATH_PATH,"ProgramData")
# 用户数据存放位置
USER_DATA_PATH  = os.path.join(BATH_PATH, 'user.json')
# 聊天机器人对话数据存放位置
CHATAI_DATA_PATH = os.path.join(BATH_PATH, 'ChatAi.json')

# AI 模糊匹配最小值
MIN_AI_MATCH_VALUE = 80
# 默认回复
DEFAULT_REPLY = "我暂时听不懂这个问题耶，换个问题问我吧。"
# DEFAULT_REPLY = "我暂时听不懂这个问题耶，可以主动添加这个问题的回答哦。"

# 默认用户
DEFAULT_USER = {
    "admin":{"password": "admin","school": "广州商学院","student_id":"admin"},
    "202212390606":{"password": "202212390606","school": "广州商学院","student_id":"202212390606"}
}

# 默认聊天机器人对话数据

DEFAULT_CHATAI = {
    "你好": "你好",
    "你叫什么名字": "我叫CYChatAi",
    "你今年多大": "我今年18岁",
    "你喜欢做什么": "我喜欢睡觉",
    "你喜欢吃什么": "我喜欢吃辣条",
    "世界上最好的编程语言是什么": "人生苦短，我学Python"
}