# AI News Hub - 人工智能资讯中心

一个自动抓取 AI 相关新闻的网站，每 5 分钟更新一次，展示最近三天的新闻。

## 🌟 特性

- ✅ **自动抓取**：从多个知名 AI 新闻源自动抓取新闻
- ✅ **实时更新**：每 5 分钟自动更新一次
- ✅ **分类展示**：按 AI 技术、科技动态等分类展示
- ✅ **赛博朋克风格**：活泼中带一点赛博感的视觉设计
- ✅ **三天资讯**：只展示最近三天的最新新闻
- ✅ **一键部署**：自动发布到 GitHub Pages

## 📁 项目结构

```
ai-news-site/
├── backend/
│   ├── main.py           # FastAPI 主程序
│   ├── scraper.py        # 新闻抓取模块
│   ├── requirements.txt  # Python 依赖
│   └── news_data.json    # 新闻数据存储
├── frontend/
│   ├── index.html        # 主页面
│   ├── style.css         # 赛博朋克风格样式
│   └── app.js            # 前端逻辑
├── scripts/
│   └── deploy.sh         # 部署脚本
└── README.md
```

## 🚀 快速开始

### 1. 安装后端依赖

```bash
cd backend
pip install -r requirements.txt
```

### 2. 启动后端服务

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

后端服务将在 http://localhost:8000 启动

### 3. 访问前端

直接在浏览器打开 `frontend/index.html` 文件，或部署到 GitHub Pages

## 📡 支持的新闻源

- TechCrunch AI
- The Verge AI
- MIT Technology Review
- AI News (PetaPilot)
- 机器之心
- 量子位

## 🎨 设计特色

- **赛博朋克配色**：霓虹蓝、紫、粉的经典组合
- **动态网格背景**：营造科技感
- **故障效果**：标题采用 glitch 动画
- **响应式设计**：完美适配桌面和移动端
- **实时状态**：显示最后更新时间、下次更新倒计时

## 🔧 API 接口

### 获取所有新闻
```
GET /api/news
```

### 按分类获取新闻
```
GET /api/news/category/{category}
```

### 获取新闻源列表
```
GET /api/sources
```

### 手动刷新新闻
```
POST /api/refresh
```

## 🌐 部署到 GitHub Pages

```bash
cd scripts
chmod +x deploy.sh
./deploy.sh
```

部署完成后，访问：`https://<你的用户名>.github.io/ai-news-hub/`

## 📝 注意事项

1. **后端服务**：前端需要后端服务支持，可以将后端部署到 Heroku、Vercel 或任何支持 Python 的平台
2. **CORS**：如果前后端分离部署，需要配置 CORS
3. **更新频率**：默认每 5 分钟更新一次，可在 `backend/main.py` 中调整
4. **数据存储**：当前使用 JSON 文件存储，生产环境建议使用数据库

## 🛠️ 技术栈

- **后端**：Python + FastAPI
- **前端**：HTML/CSS/JavaScript
- **抓取**：requests + BeautifulSoup + feedparser
- **部署**：GitHub Pages

## 📄 License

MIT License

---

🤖 由 AI 驱动 · 为 AI 爱好者打造
