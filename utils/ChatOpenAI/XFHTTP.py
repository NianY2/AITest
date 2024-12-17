"""
pip install openai
使用讯飞大模型
使用HTTP调用
"""
from openai import OpenAI,InternalServerError

ERROR_CODE = {
    "0": "成功",
    "10007": "用户流量受限：服务正在处理用户当前的问题，需等待处理完成后再发送新的请求。（必须要等大模型完全回复之后，才能发送下一个问题）",
    "10013": "输入内容审核不通过，涉嫌违规，请重新调整输入内容",
    "10014": "输出内容涉及敏感信息，审核不通过，后续结果无法展示给用户",
    # "10019": "表示本次会话内容有涉及违规信息的倾向；建议开发者收到此错误码后给用户一个输入涉及违规的提示",
    "10019": "输入内容审核不通过，涉嫌违规，请重新调整输入内容",
    "10907": "token数量超过上限。对话历史+问题的字数太多，需要精简输入",
    "11200": "授权错误：该appId没有相关功能的授权或者业务量超过限制",
    "11201": "日流控超限。超过当日最大访问量的限制",
    "11202": "秒级流控超限。秒级并发超过授权路数限制",
    "11203": "并发流控超限。并发路数超过授权路数限制"
}

client = OpenAI(
		# 控制台获取key和secret拼接，假使控制台获取的APIPassword是123456
        api_key="vmoiXentJZJiMnGBkBTs:OqsZQpWYFZODBojeimhd",
         base_url = 'https://spark-api-open.xf-yun.com/v1' # 指向讯飞星火的请求地址
)

def get_chat_response(msg=None, history=[]):
    try:
        completion = client.chat.completions.create(
            model='lite',  # 指定请求的版本
            messages=[
                *history,
                {
                    "role": "user",
                    "content": msg
                },
            ]
        )
        return  completion.choices[0].message.content
    except InternalServerError as e:
        print("\033[31m", end="")
        print("讯飞大模型异常：")
        print(e)
        print(ERROR_CODE[str(e.response.json()["error"]["code"])])
        print("\033[0m")
        return  ERROR_CODE[str(e.response.json()["error"]["code"])]

if __name__ == '__main__':
    history = []
    while True:
        msg = input("请输入问题：")
        res = get_chat_response(msg,history)
        print("=========================")
        print(res)
        print("=========================")
        history.append({"role": "user", "content": msg})
        history.append({"role": "system", "content": res})