import requests
import time

LOCAL_URL = "http://127.0.0.1:8000/chat"

def chat_with_retry(messages, model="glm-4-flash", max_retries=3):
    """带重试的聊天函数"""
    
    for attempt in range(1, max_retries + 1):
        try:
            print(f"  第 {attempt} 次尝试...")
            
            data = {
                "model": model,
                "messages": messages
            }
            
            response = requests.post(
                LOCAL_URL,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                return result["choices"][0]["message"]["content"]
            
            elif response.status_code == 429:
                print("  被限流了，等5秒...")
                time.sleep(5)
                continue
            
            elif response.status_code == 500:
                print("  服务器错误，重试...")
                time.sleep(3)
                continue
            
            else:
                print(f"  错误 {response.status_code}：{response.text}")
                return f"错误：{response.status_code}"
                
        except requests.exceptions.Timeout:
            print("  超时了，重试...")
            time.sleep(3)
            continue
            
        except requests.exceptions.ConnectionError:
            print("  连不上本地服务，确认 uvicorn 在运行吗？")
            return "错误：本地服务未启动"
            
        except Exception as e:
            return f"未知错误：{str(e)}"
    
    return "错误：重试3次都失败了"


# ===== 测试 =====

print("===== 正常请求 =====")
result = chat_with_retry([
    {"role": "user", "content": "1+1等于几？"}
])
print("回复：" + result)

print("\n===== 测试超时（故意设很短）=====")
# 这个测试本地服务是否正常
result = chat_with_retry([
    {"role": "user", "content": "你好"}
], max_retries=2)
print("回复：" + result)