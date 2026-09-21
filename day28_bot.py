import requests
import json
import time

LOCAL_URL = "http://127.0.0.1:8000/chat"

def chat_stream(messages, model="glm-4-flash", max_retries=3):
    """流式输出 + 错误重试"""
    
    for attempt in range(1, max_retries + 1):
        try:
            data = {
                "model": model,
                "messages": messages,
                "stream": True
            }
            
            response = requests.post(
                LOCAL_URL, json=data, stream=True, timeout=30
            )
            
            if response.status_code != 200:
                print(f"\n[错误 {response.status_code}，重试...]")
                time.sleep(3)
                continue
            
            full_reply = ""
            
            for chunk in response.iter_lines():
                if chunk:
                    line = chunk.decode("utf-8")
                    if line.startswith("data: "):
                        json_str = line[6:]
                        if json_str == "[DONE]":
                            break
                        try:
                            chunk_data = json.loads(json_str)
                            delta = chunk_data["choices"][0]["delta"]
                            content = delta.get("content", "")
                            if content:
                                print(content, end="", flush=True)
                                full_reply += content
                        except:
                            pass
            
            print()  # 换行
            return full_reply
            
        except requests.exceptions.ConnectionError:
            print("\n[连不上服务，重试...]")
            time.sleep(3)
            continue
        except Exception as e:
            print(f"\n[错误：{e}]")
            return ""
    
    print("\n[3次都失败了]")
    return ""


# ===== 主程序 =====

print("╔══════════════════════════════╗")
print("║   我的 AI 聊天机器人 v1.0    ║")
print("║   输入 quit 退出             ║")
print("║   输入 /new 开新对话          ║")
print("║   输入 /role 切换人设         ")
print("╚══════════════════════════════╝")

# 人设模板
roles = {
    "1": "你是AI助手，友好、简洁、有耐心。",
    "2": "你是一个严格的数学老师，只回答数学问题。回答要简短。",
    "3": "你是一个英语老师，用户说中文时你帮他翻译成英文，并解释语法。",
    "4": "你是一个程序员，用通俗的话解释技术问题。"
}

current_role = roles["1"]
messages = [{"role": "system", "content": current_role}]

print(f"\n当前人设：{current_role}\n")

while True:
    try:
        user_input = input("你：").strip()
    except (KeyboardInterrupt, EOFError):
        print("\n再见！")
        break
    
    if not user_input:
        continue
    
    # 退出
    if user_input == "quit":
        print("再见！")
        break
    
    # 开新对话
    if user_input == "/new":
        messages = [{"role": "system", "content": current_role}]
        print("[已开启新对话]\n")
        continue
    
    # 切换人设
    if user_input == "/role":
        print("\n选择人设：")
        for key, value in roles.items():
            print(f"  {key}. {value}")
        choice = input("选哪个（1-4）：").strip()
        if choice in roles:
            current_role = roles[choice]
            messages = [{"role": "system", "content": current_role}]
            print(f"[已切换人设：{current_role}]\n")
        continue
    
    # 正常对话
    messages.append({"role": "user", "content": user_input})
    print("AI：", end="", flush=True)
    
    ai_reply = chat_stream(messages)
    
    if ai_reply:
        messages.append({"role": "assistant", "content": ai_reply})
    print()