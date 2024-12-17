import  os
"""
测试模式
1. 会提示登入错误次数
"""
DEBUG = True
BATH_PATH =  os.getcwd()
# 静态资源文件
# files_settings
FILES_PATH = {
    "page":{
        "login":"file:///./template/login.html",
        "AIChat":"file:///./template/AIChat.html"
    }
}
PROGRAM_DATA_PATH = os.path.join(BATH_PATH,"ProgramData")
# 用户数据存放位置
USER_LIST_DATA_PATH  = os.path.join(PROGRAM_DATA_PATH, 'UserList.json')
# 聊天机器人对话数据存放位置
CHATAI_DATA_PATH = os.path.join(PROGRAM_DATA_PATH, 'ChatAi.json')
# 登录数据存放位置
LOGIN_DATA_PATH = os.path.join(PROGRAM_DATA_PATH, 'Login.json')
# 当前用户数据存放目录
USER_DATA_PATH = os.path.join(PROGRAM_DATA_PATH, 'User')


# 最大登录尝试次数
LOGIN_TRY_NUM = 3
"""
登录尝试间隔时间(单位：秒) 
计算规则：
在该时间内，登录尝试次数到达最大次数时，不允许登录
"""
LOGIN_TRY_INTERVAL = 60*10

# 默认用户
DEFAULT_USER = {
    "admin":{"password": "admin","name":"admin","school": "广州商学院","uid":"admin"},
    "202212390606":{"password": "202212390606","name":"陈煜","school": "广州商学院","uid":"202212390606"}
}

# AI 模糊匹配最小值
MIN_AI_MATCH_VALUE = 80
# 默认回复
DEFAULT_REPLY = "我暂时听不懂这个问题耶，换个问题问我吧。"
# DEFAULT_REPLY = "我暂时听不懂这个问题耶，可以主动添加这个问题的回答哦。"
# 启动回复
START_REPLY = """欢迎使用CYChatAi,当前为本地对话,我现在可以回答研学、旅游、美食、健康方面的问题。
输入<strong class="text-question" onclick="sendMessage('代码模式')">代码模式</strong>可以让我进入代码模式。
输入<strong class="text-question" onclick="sendMessage('讯飞大模型Lite版')">讯飞大模型Lite版</strong>可以让我进入联网模式(讯飞大模型Lite)。
"""

# 讯飞大模型启动回复
XF_LITE_OPENAI_REPLY = """进入联网模式(讯飞大模型Lite版)成功。
在联网模式下，输入<strong class="text-question" onclick="sendMessage('exit')">exit</strong>或<strong class="text-question" onclick="sendMessage('退出')">退出</strong>可以退出联网模式。
<strong>注意：</strong>在联网模式下，可能会有一定的时间思考，请耐心等待。
"""

# 讯飞大模型退出回复
XF_LITE_OPENAI_EXIT_REPLY = """退出联网模式成功。现在可以本地对话。"""

# 代码模式启动回复
CODE_REPLY = """进入代码模式成功，我目前支持执行<i>Python</i>代码。
在代码模式下，输入<strong class="text-question" onclick="sendMessage('exit')">exit</strong>或<strong class="text-question" onclick="sendMessage('退出')">退出</strong>可以退出代码模式。
<strong>注意：</strong>在代码模式下，所有输入都会尝试在真实环境中执行，需要确保你的代码是安全的。否则可能对你的计算机造成<strong>不可逆的损害。</strong>
"""

# 代码模式退出回复
CODE_EXIT_REPLY = """退出代码模式成功。现在可以正常对话。"""

# 代码模式默认回复
CODE_DEFAULT_REPLY = "输入的内容可能不是有效的代码，无法执行。"

# 默认聊天机器人对话数据
import DEFAULT_CHATAI as DEFAULT_CHATAI_DATA
DEFAULT_CHATAI  = DEFAULT_CHATAI_DATA.DEFAULT_CHATAI