import  os
BATH_PATH =  os.getcwd()
PROGRAM_DATA_PATH = os.path.join(BATH_PATH,"ProgramData")
# 用户数据存放位置
USER_LIST_DATA_PATH  = os.path.join(PROGRAM_DATA_PATH, 'UserList.json')
# 聊天机器人对话数据存放位置
CHATAI_DATA_PATH = os.path.join(PROGRAM_DATA_PATH, 'ChatAi.json')
# 登录数据存放位置
LOGIN_DATA_PATH = os.path.join(PROGRAM_DATA_PATH, 'Login.json')
# 当前用户数据存放目录
USER_DATA_PATH = os.path.join(PROGRAM_DATA_PATH, 'User')

# AI 模糊匹配最小值
MIN_AI_MATCH_VALUE = 80
# 默认回复
DEFAULT_REPLY = "我暂时听不懂这个问题耶，换个问题问我吧。"
# 启动回复
START_REPLY = "欢迎使用CYChatAi,我现在可以回答研学、旅游、美食、健康方面的问题。"
# DEFAULT_REPLY = "我暂时听不懂这个问题耶，可以主动添加这个问题的回答哦。"

# 默认用户
DEFAULT_USER = {
    "admin":{"password": "admin","school": "广州商学院","uid":"admin"},
    "202212390606":{"password": "202212390606","school": "广州商学院","uid":"202212390606"}
}

# 默认聊天机器人对话数据

DEFAULT_CHATAI = {
    "你是谁": "我是一个聊天机器人",
    "哈哈哈":"哈哈哈",
    "你叫什么名字": "我叫CYChatAi",
    "你今年多大": "我今年18岁",
    "你喜欢做什么": "我喜欢睡觉",
    "你喜欢吃什么": "我喜欢吃辣条",
    "世界上最好的编程语言是什么": "Python",
    "编程语言推荐": "人生苦短，我学Python",
    "换行测试":"换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试",
    "你好": "你好",
}