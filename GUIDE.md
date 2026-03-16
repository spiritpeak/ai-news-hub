# AI News Hub - 使用指南 🤖

## ✅ 已完成的开发

### 项目结构
```
ai-news-site/
├── backend/              # 后端服务
│   ├── main.py          # FastAPI 主程序
│   ├── scraper.py       # 新闻抓取模块
│   ├── requirements.txt # Python 依赖
│   └── news_data.json   # 数据存储
├── frontend/            # 前端页面
│   ├── index.html       # 主页面
│   ├── style.css        # 赛博朋克风格
│   └── app.js           # 前端逻辑
├── scripts/             # 脚本工具
│   └── deploy.sh        # 部署脚本
└── start.sh             # 一键启动脚本
```

### 功能特性 ✅
- ✅ 自动抓取 6 个 AI 新闻源
- ✅ 每 5 分钟自动更新
- ✅ 按类型模块展示（全部/AI 技术/科技动态）
- ✅ 赛博朋克风格设计
- ✅ 展示最近三天新闻
- ✅ 自动发布到 GitHub
- ✅ 响应式设计

### 新闻源
1. TechCrunch AI
2. The Verge AI
3. MIT Technology Review
4. AI News
5. 机器之心
6. 量子位

## 🚀 如何使用

### 方法 1：本地运行（推荐先测试）

1. **启动后端服务**
```bash
cd /Users/xiamingzhu/.openclaw/workspace-linus/ai-news-site
./start.sh
```

或者手动启动：
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

2. **访问前端**
- 打开浏览器访问：`file:///Users/xiamingzhu/.openclaw/workspace-linus/ai-news-site/frontend/index.html`
- 或者使用 Live Server 等工具

### 方法 2：部署到 GitHub Pages（已完成）

前端已自动部署到：
👉 **https://spiritpeak.github.io/ai-news-hub/**

⚠️ **注意**：前端需要后端 API 支持才能显示新闻。

## 📝 后续步骤

### 选项 A：本地运行（简单）
1. 运行 `./start.sh` 启动后端
2. 访问前端页面
3. 适合本地测试和开发

### 选项 B：部署后端到云平台（推荐）

#### 部署到 Hugging Face Spaces（免费）
1. 创建 Hugging Face 账号
2. 创建新的 Space（选择 Docker 模板）
3. 上传后端代码
4. 获取 API 地址
5. 修改前端 `app.js` 中的 `API_BASE` 为新地址

#### 部署到 Render.com（免费）
1. 注册 Render.com
2. 创建新的 Web Service
3. 连接 GitHub 仓库
4. 自动部署

#### 部署到 Railway.app（免费）
1. 注册 Railway.app
2. 连接 GitHub
3. 一键部署

### 选项 C：使用 GitHub Actions 自动运行

创建 `.github/workflows/refresh.yml` 定时抓取新闻。

## 🎨 设计亮点

1. **赛博朋克配色**：霓虹蓝 (#00f3ff)、紫 (#bd00ff)、粉 (#ff00ff)
2. **动态网格背景**：营造科技感
3. **故障效果**：标题采用 glitch 动画
4. **实时状态栏**：显示更新时间和倒计时
5. **卡片悬停效果**：3D 悬浮 + 霓虹边框
6. **响应式设计**：完美适配手机和桌面

## 🔧 API 接口

```bash
# 获取所有新闻
GET http://localhost:8000/api/news

# 按分类获取
GET http://localhost:8000/api/news/category/AI

# 获取新闻源列表
GET http://localhost:8000/api/sources

# 手动刷新
POST http://localhost:8000/api/refresh
```

## 📊 项目状态

- [x] 项目结构创建
- [x] 后端开发完成
- [x] 前端开发完成
- [x] 赛博朋克风格实现
- [x] GitHub 仓库创建
- [x] 前端部署到 GitHub Pages
- [ ] 后端部署到云平台
- [ ] 配置自动更新

## 🎯 下一步建议

1. **立即可做**：运行 `./start.sh` 本地测试
2. **部署后端**：选择云平台部署后端服务
3. **配置域名**：绑定自定义域名
4. **添加更多新闻源**：扩展 RSS 源
5. **添加搜索功能**：支持关键词搜索
6. **添加收藏功能**：使用 localStorage

## 💡 提示

- 后端使用 JSON 文件存储，适合小规模使用
- 生产环境建议使用数据库（PostgreSQL/MongoDB）
- 可以添加缓存机制减少 API 调用
- 考虑添加新闻去重逻辑

---

🎉 项目已完成基础开发，可以开始使用了！
