"""
属性方法装饰器@property
"""
class Test():
    @property
    def is_login(self):
        return  False

if __name__ == '__main__':
    print(Test().is_login)