# -*- coding: utf-8 -*-
"""
WSGI 入口文件
Render 默认会导入 your_application.wsgi 并查找 application 对象
"""

import sys
import os

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 从 backend.main 导入 FastAPI 应用
from backend.main import app as application

# 同时导出 app 以便兼容
app = application
