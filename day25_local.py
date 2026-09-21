import requests
import json

# 调用本地 API，不需要 API Key！
LOCAL_URL = "http://127.0.0.1:8000/chat"

messages = [
    {"role": "system", "content": "你是一个严格的数学老师，只回答数学问题。"},
    {"role": "user", "content": "3×7等于几？"}
]

data = {
    "model": "glm-4-flash",
    "messages": messages
}

response = requests.post(LOCAL_URL, json=data)
result = response.json()

print("AI回复：" + result["choices"][0]["message"]["content"])