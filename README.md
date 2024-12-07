# 简单的AI
## 介绍
这是一个简单静态的AI。

## 功能概览
- 登录注册
  - 密码加密：使用PBKDF2_SHA256加密
- Ai聊天
  - 模糊匹配问题

## 学习
Python
- PyQt5控件QWebEngineView:[https://blog.csdn.net/qq_59636442/article/details/144061937](https://blog.csdn.net/qq_59636442/article/details/144061937)
- pyinstaller的打包Python(包含静态文件）:[https://blog.csdn.net/qq_59636442/article/details/144071283](https://blog.csdn.net/qq_59636442/article/details/144071283)
前端
- Vue3实现打字机效果：[https://blog.csdn.net/qq_59636442/article/details/130504479](https://blog.csdn.net/qq_59636442/article/details/130504479)
- 

## 目录结构
- QuickBat(git脚本，与程序无关)
- Test(学习过程的测试代码，与程序无关)
- template(html,css,js)
- Initialize(初始化程序，生成数据文件)
- settings.py(项目设置文件)
- main.py(主程序)

## 项目技术栈
### 主框架
Python3

### 视图层
- PyQt5
- PyQtWebEngine
- Vue 3.5.13


## 常用命令
```shell
# 生成requirements.txt
pip freeze > requirements_test.txt
# 打包
#“-F”效果是打包成一个文件，“-w”则可以使打包后的程序运行时不弹出黑窗口
pyinstaller -F -w Login.py
# 按照 spec文件打包
pyinstaller  Login.spec
```


## 项目依赖
- PyQt5(构建界面)
- PyQtWebEngine(通过WebView构建界面)
- FuzzyWuzzy(字符串的模糊匹配)
- python-levenshtein(Levenshtein距离的计算,FuzzyWuzzy需要)
- pyinstaller(将Python代码打包成exe文件)

## 使用方法
### 下载依赖
```shell
pip install --index-url=https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
```
or
```shell
pip install --index-url=https://mirrors.aliyun.com/pypi/simple/ PyQt5
pip install --index-url=https://mirrors.aliyun.com/pypi/simple/ PyQtWebEngine
pip install --index-url=https://mirrors.aliyun.com/pypi/simple/ pyinstaller
pip install --index-url=https://mirrors.aliyun.com/pypi/simple/ FuzzyWuzzy
pip install --index-url=https://mirrors.aliyun.com/pypi/simple/ python-levenshtein
```

### 运行
```shell
python3 main.py
# or
python main.py
```

## 作者信息
* Name: CY
* QQ: 1871263099
* 邮箱：1871263099@qq.com
* CSDN博客：[https://blog.csdn.net/qq_59636442?type=blog](https://blog.csdn.net/qq_59636442?type=blog)
* Gitee:[https://gitee.com/REMOTE_CY](https://gitee.com/REMOTE_CY)
* Github:[https://github.com/NianY2](https://github.com/NianY2)
* GitCode[https://gitcode.com/qq_59636442](https://gitcode.com/qq_59636442)

## 引用
- 登入界面模板:[https://codepen.io/fghty/pen/PojKNEG](https://codepen.io/fghty/pen/PojKNEG)