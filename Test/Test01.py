class AI:
    isLosgin = False
    user = {"202212390606":'123'}
    lt_map = {
        "1":"111",
        "12": "1112",
        "13": "1113334",
    }
    def __init__(self):
        ans = 0
        while  ans < 3:
            if self.login():
                self.lt()
                return
            ans += 1
            print("密码错误,还剩"+str(3-ans)+"次")
        print("你完了")

    def login(self):
        zh = input("zh:")
        mm = input("mm:")
        if zh in self.user:
            return  self.user[zh] == mm
        self.isLosgin = True

    def lt(self):
        msg = input("请输入你的问题：")
        if msg not in self.lt_map:
            print("我不知道你说什么")
        else:
            print(self.lt_map[msg])
        self.lt()

if __name__ == '__main__':
    AI()
