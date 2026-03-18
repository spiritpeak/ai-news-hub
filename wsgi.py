# -*- coding: utf-8 -*-
"""
WSGI 入口点
Render 默认会查找 your_application.wsgi 或 wsgi.py
这个文件让 gunicorn 可以直接导入并运行 FastAPI 应用
"""

from backend.main import app

# 导出 app 对象，让 gunicorn 可以找到
application = app
