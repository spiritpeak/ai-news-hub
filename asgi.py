# -*- coding: utf-8 -*-
"""
ASGI 入口文件
Render 和现代 Python 服务器都支持 ASGI
"""

# 直接在这里创建 FastAPI 应用，避免导入问题
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="AI News API")

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "AI News API", "status": "running"}

@app.get("/api/news")
async def get_news():
    return {"news": [], "last_updated": None}

# 导出 ASGI 应用
application = app
