#!/bin/bash

echo "🚀 AI News Hub 启动脚本"
echo "======================"
echo ""

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 未检测到 Python3，请先安装 Python3"
    exit 1
fi

echo "✅ Python3 版本：$(python3 --version)"
echo ""

# 进入后端目录
cd backend

# 检查依赖
if [ ! -d "venv" ]; then
    echo "📦 创建虚拟环境..."
    python3 -m venv venv
fi

# 激活虚拟环境
source venv/bin/activate

# 安装依赖
echo "📦 安装依赖..."
pip install -r requirements.txt -q

# 启动后端服务
echo ""
echo "🌐 启动后端服务..."
echo "   API 地址：http://localhost:8000"
echo "   API 文档：http://localhost:8000/docs"
echo ""
echo "按 Ctrl+C 停止服务"
echo ""

# 启动服务
uvicorn main:app --reload --host 0.0.0.0 --port 8000
