"""
控制台运行
"""
if __name__ == '__main__':
    import os
    import sys

    # 检查sys模块是否包含frozen属性，判断是否为pyinstaller打包
    if getattr(sys, 'frozen', False):
        print("正在使用pyinstaller打包")
        """
            sys._MEIPASS是PyInstaller在打包应用时设置的一个特殊变量，
            它指向应用运行时解压缩资源文件的临时目录。
            因此，在这个目录中，你可以找到打包时包含的所有资源文件。
        """
        base_path = sys._MEIPASS
    else:
        print("正在使用python解释器运行")
        base_path = os.path.abspath("..")
    # 改变当前工作目录
    os.chdir(os.path.join(base_path, ''))