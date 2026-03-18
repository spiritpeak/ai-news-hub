# -*- coding: utf-8 -*-
"""
WSGI 入口文件
Render 默认会导入 your_application.wsgi 并查找 application 对象
"""

# 延迟导入，避免类型推断问题
def get_app():
    import main
    return main.app

# 直接赋值
application = get_app()
app = application
