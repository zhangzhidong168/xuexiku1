import requests
import json

LOCAL_URL = "http://127.0.0.1:8000/chat"

messages = [
    {"role": "system", "content": "你是AI助手，回答简洁。"},
    {"role": "user", "content": "用100字介绍一下人工智能"}
]

data = {
    "model": "glm-4-flash",
    "messages": messages,
    "stream": True    # 开启流式输出
}

# 用 stream=True 请求，返回的是逐块数据
response = requests.post(LOCAL_URL, json=data, stream=True)

print("AI：", end="", flush=True)

# 逐块读取
for chunk in response.iter_lines():
    if chunk:
        # 去掉 "data: " 前缀
        line = chunk.decode("utf-8")
        if line.startswith("data: "):
            json_str = line[6:]
            
            # 最后一条是 "[DONE]"
            if json_str == "[DONE]":
                break
            
            try:
                chunk_data = json.loads(json_str)
                # 取出这一小块文字
                delta = chunk_data["choices"][0]["delta"]
                content = delta.get("content", "")
                if content:
                    print(content, end="", flush=True)
            except:
                pass

print("\n\n===== 输出结束 =====")