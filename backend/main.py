# -*- coding: utf-8 -*-
"""
FastAPI 主程序
提供新闻 API 和定时抓取任务
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime
import json
import os
import threading
import time
from scraper import NewsScraper

app = FastAPI(title="AI News API")

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 数据文件路径
DATA_FILE = os.path.join(os.path.dirname(__file__), 'news_data.json')

# 全局新闻数据
news_data = {"news": [], "last_updated": None}


def load_news():
    """加载新闻数据"""
    global news_data
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                news_data = json.load(f)
    except:
        news_data = {"news": [], "last_updated": None}


def save_news():
    """保存新闻数据"""
    global news_data
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(news_data, f, ensure_ascii=False, indent=2)


def fetch_news_task():
    """定时抓取新闻任务"""
    global news_data
    scraper = NewsScraper()
    
    while True:
        try:
            print(f"Fetching news at {datetime.now()}")
            news_list = scraper.fetch_all()
            news_data["news"] = news_list
            news_data["last_updated"] = datetime.now().isoformat()
            save_news()
            print(f"Fetched {len(news_list)} news items")
        except Exception as e:
            print(f"Error fetching news: {e}")
        
        # 每 5 分钟执行一次
        time.sleep(300)


@app.on_event("startup")
async def startup_event():
    """应用启动时加载数据并启动定时任务"""
    load_news()
    
    # 如果数据为空，立即抓取一次
    if not news_data["news"]:
        fetch_news_task()
    
    # 启动后台定时任务
    thread = threading.Thread(target=fetch_news_task, daemon=True)
    thread.start()


@app.get("/")
async def root():
    return {"message": "AI News API", "status": "running"}


@app.get("/api/news")
async def get_news():
    """获取所有新闻"""
    return news_data


@app.get("/api/news/category/{category}")
async def get_news_by_category(category: str):
    """按分类获取新闻"""
    filtered_news = [
        n for n in news_data.get("news", [])
        if category.lower() in n.get('category', '').lower()
    ]
    return {"news": filtered_news, "last_updated": news_data.get("last_updated")}


@app.get("/api/sources")
async def get_sources():
    """获取新闻源列表"""
    from scraper import NewsScraper
    scraper = NewsScraper()
    sources = [
        {"id": k, "name": v['name'], "category": v['category']}
        for k, v in scraper.sources.items()
    ]
    return {"sources": sources}


@app.post("/api/refresh")
async def refresh_news():
    """手动刷新新闻"""
    global news_data
    scraper = NewsScraper()
    news_list = scraper.fetch_all()
    news_data["news"] = news_list
    news_data["last_updated"] = datetime.now().isoformat()
    save_news()
    return {"message": "News refreshed", "count": len(news_list)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
