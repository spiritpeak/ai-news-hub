# -*- coding: utf-8 -*-
"""
WSGI 入口文件 - 简单版本
直接导入 main 模块，避免任何复杂的导入逻辑
"""

# 直接导入 app 对象
import main
application = main.app
app = application
