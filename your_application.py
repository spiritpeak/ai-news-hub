# -*- coding: utf-8 -*-
"""
your_application.py - Render 默认入口
Render 默认执行 gunicorn your_application.wsgi
这个文件提供 wsgi 应用
"""

# 延迟导入 main 模块
def get_app():
    import main
    return main.app

# 导出 application 对象
application = get_app()
app = application
