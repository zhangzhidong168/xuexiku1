# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import List, Dict
# import requests

# app = FastAPI()

# # API Key 只在这里写一次
# API_KEY = "18a7ef4a92244c4883dee5ce4fb5a79a.iHeTi1cEW7STPK6E"

# ZHIPU_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

# # 定义请求格式
# class ChatRequest(BaseModel):
#     messages: List[Dict[str, str]]
#     model: str = "glm-4-flash"

# @app.post("/chat")
# def chat(req: ChatRequest):
#     """本地 API，转发给智谱"""
    
#     headers = {
#         "Authorization": "Bearer " + API_KEY,
#         "Content-Type": "application/json"
#     }
    
#     data = {
#         "model": req.model,
#         "messages": req.messages
#     }
    
#     try:
#         response = requests.post(ZHIPU_URL, headers=headers, json=data)
#         result = response.json()
#         return result
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.get("/health")
# def health():
#     """检查服务是否正常"""
#     return {"status": "ok"}


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import requests
from fastapi.responses import StreamingResponse

app = FastAPI()

API_KEY = "18a7ef4a92244c4883dee5ce4fb5a79a.iHeTi1cEW7STPK6E"
ZHIPU_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

class ChatRequest(BaseModel):
    messages: List[Dict[str, str]]
    model: str = "glm-4-flash"
    stream: bool = False

@app.post("/chat")
def chat(req: ChatRequest):
    headers = {
        "Authorization": "Bearer " + API_KEY,
        "Content-Type": "application/json"
    }
    
    data = {
        "model": req.model,
        "messages": req.messages,
        "stream": req.stream
    }
    
    # 流式模式
    if req.stream:
        def generate():
            resp = requests.post(ZHIPU_URL, headers=headers, json=data, stream=True)
            for chunk in resp.iter_lines():
                if chunk:
                    yield chunk.decode("utf-8") + "\n"
        return StreamingResponse(generate(), media_type="text/event-stream")
    
    # 普通模式
    try:
        response = requests.post(ZHIPU_URL, headers=headers, json=data)
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok"}
