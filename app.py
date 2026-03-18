# -*- coding: utf-8 -*-
"""
Render 启动入口
Render 默认会查找并运行 app.py 或 main.py
这个文件确保 uvicorn 能正确启动 FastAPI 应用
"""

import uvicorn
import os

# 从环境变量获取端口（Render 会设置 PORT 环境变量）
port = int(os.environ.get("PORT", 8000))

if __name__ == "__main__":
    # 启动 uvicorn
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=port,
        reload=False,
        workers=1
    )
