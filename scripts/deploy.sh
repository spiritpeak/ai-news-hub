#!/bin/bash
# GitHub 部署脚本

echo "🚀 开始部署到 GitHub..."

# 检查 GITHUB_TOKEN 是否已设置
if [ -z "$GITHUB_TOKEN" ]; then
    echo "❌ 请先设置 GITHUB_TOKEN 环境变量"
    echo "export GITHUB_TOKEN=\"your_token_here\""
    exit 1
fi

REPO_NAME="ai-news-hub"
BRANCH_NAME="gh-pages"

# 检查是否在正确的目录
if [ ! -d "frontend" ]; then
    echo "❌ 请在项目根目录下运行此脚本"
    exit 1
fi

# 获取用户名
USERNAME=$(curl -s -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user | grep -o '"login":"[^"]*"' | cut -d'"' -f4)

# 初始化 Git
cd frontend
git init
git remote add origin "https://${GITHUB_TOKEN}@github.com/${USERNAME}/${REPO_NAME}.git" || true
git checkout -b $BRANCH_NAME || git checkout $BRANCH_NAME

# 添加所有文件
git add -A
git commit -m "Deploy AI News Hub - $(date '+%Y-%m-%d %H:%M:%S')"

# 推送到 GitHub
git push -f origin $BRANCH_NAME

echo ""
echo "✅ 部署完成!"
echo "🌐 访问地址：https://${USERNAME}.github.io/${REPO_NAME}/"
echo ""
echo "📝 后端服务启动说明:"
echo "  cd backend"
echo "  pip install -r requirements.txt"
echo "  uvicorn main:app --reload --host 0.0.0.0 --port 8000"
echo ""
