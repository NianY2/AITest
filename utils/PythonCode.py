class NoPythonCodeError(Exception):
    """提供非Python代码时引发的异常"""
    def __init__(self, message="未提供Python代码"):
        self.message = message
        super().__init__(self.message)

def is_python_code(code_str):
    """
    判断字符串是否是python代码
    """
    try:
        compile(code_str, '<string>', 'exec')
        return True
    except SyntaxError:
        return False




import io
import contextlib
def get_python_code_result(code_str):
    """
    获取执行结果（输出类型）
    要捕获Python代码片段中print函数的输出，
    我们可以使用io.StringIO和上下文管理器contextlib.redirect_stdout。
    这将允许我们将print语句的输出重定向到一个字符串缓冲区，而不是默认的标准输出（通常是控制台）。
    然后我们可以从这个缓冲区中获取输出结果。
    """
    print(code_str)
    if not is_python_code(code_str):
        raise NoPythonCodeError("这可能并不是Python代码")
    # 创建一个 StringIO 对象来捕获输出
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        exec(compile(code_str, '<string>', 'exec'))
    # 获取捕获的输出并去除末尾的换行符
    captured_output = output.getvalue().strip()
    # 关闭 StringIO 对象
    output.close()
    return captured_output


if __name__ == '__main__':
#     print(get_python_code_result("print('hello world')"))
#     print(get_python_code_result("""
# print('hello world')
# print('hello world')
# print('hello world')
# print('hello world')
# """))
    
    print(get_python_code_result("""
for i in range(10):
    print(i)
    print(i)
"""))