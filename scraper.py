# -*- coding: utf-8 -*-
"""
新闻抓取模块
支持多个新闻源的 RSS 和 HTML 抓取
"""

import requests
import feedparser
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from typing import List, Dict
import re


class NewsScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        # 新闻源配置
        self.sources = {
            'techcrunch': {
                'name': 'TechCrunch AI',
                'url': 'https://techcrunch.com/category/artificial-intelligence/feed/',
                'type': 'rss',
                'category': '技术'
            },
            'theverge': {
                'name': 'The Verge AI',
                'url': 'https://www.theverge.com/rss/ai-artificial-intelligence',
                'type': 'rss',
                'category': '技术'
            },
            'mit-tech': {
                'name': 'MIT Technology Review',
                'url': 'https://www.technologyreview.com/feed/',
                'type': 'rss',
                'category': '技术'
            },
            'ainews': {
                'name': 'AI News',
                'url': 'https://www.ainews.com/rss',
                'type': 'rss',
                'category': 'AI'
            },
            'jiqizhixin': {
                'name': '机器之心',
                'url': 'https://www.jiqizhixin.com/feed',
                'type': 'rss',
                'category': 'AI'
            },
            'qingliuwei': {
                'name': '量子位',
                'url': 'https://www.qbitai.com/feed',
                'type': 'rss',
                'category': 'AI'
            }
        }

    def fetch_rss(self, url: str) -> List[Dict]:
        """抓取 RSS 源"""
        try:
            feed = feedparser.parse(url)
            news_list = []
            
            for entry in feed.entries[:10]:  # 每个源最多取 10 条
                news = {
                    'title': entry.get('title', ''),
                    'url': entry.get('link', ''),
                    'summary': entry.get('summary', '')[:200],
                    'source': feed.feed.get('title', 'Unknown'),
                    'published': entry.get('published', datetime.now().isoformat()),
                    'category': 'AI',
                    'image': ''
                }
                
                # 尝试获取图片
                if 'media_thumbnail' in entry:
                    news['image'] = entry['media_thumbnail'][0]['url']
                elif 'links' in entry and entry['links']:
                    for link in entry['links']:
                        if 'image' in link.get('type', ''):
                            news['image'] = link['href']
                            break
                
                news_list.append(news)
            
            return news_list
        except Exception as e:
            print(f"Error fetching RSS {url}: {e}")
            return []

    def fetch_all(self) -> List[Dict]:
        """抓取所有新闻源"""
        all_news = []
        
        for source_id, source_info in self.sources.items():
            print(f"Fetching from {source_info['name']}...")
            news_list = self.fetch_rss(source_info['url'])
            
            for news in news_list:
                news['category'] = source_info['category']
                news['source'] = source_info['name']
            
            all_news.extend(news_list)
        
        # 按时间排序
        all_news.sort(key=lambda x: x.get('published', ''), reverse=True)
        
        # 只保留最近 3 天的新闻
        three_days_ago = datetime.now() - timedelta(days=3)
        recent_news = []
        
        for news in all_news:
            try:
                pub_date = datetime.fromisoformat(news['published'].replace('Z', '+00:00'))
                if pub_date >= three_days_ago:
                    recent_news.append(news)
            except:
                recent_news.append(news)
        
        return recent_news


if __name__ == '__main__':
    scraper = NewsScraper()
    news = scraper.fetch_all()
    print(f"Fetched {len(news)} news items")
    for n in news[:5]:
        print(f"- {n['title']}")
