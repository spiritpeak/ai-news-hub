# -*- coding: utf-8 -*-
"""
WSGI 入口文件
Render 默认会导入 your_application.wsgi 并查找 application 对象
代码文件在主目录下，直接导入 main 即可
"""

from main import app as application

# 同时导出 app 以便兼容
app = application
