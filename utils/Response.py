import  json
class Rseponse():
    def __init__(self, data=None, err_code=0, msg='操作成功'):
        self.data = data
        self.err_code = err_code
        self.msg = msg

    @staticmethod
    def success(data=None,msg="操作成功"):
        return Rseponse(data=data, msg=msg).to_json()

    @staticmethod
    def fail(msg):
        return Rseponse(msg=msg, err_code=1).to_json()

    def to_json(self):
        return json.dumps(self.__dict__)

if __name__ == '__main__':
    print(Rseponse.success("hello", "world"))