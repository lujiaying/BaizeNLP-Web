# -*- coding: utf-8 -*-

from gevent import monkey
monkey.patch_all()

import os

import leancloud

from app import app
from cloud import engine

APP_ID = "RmotWpAsflj29RiNlWb0nzX7-gzGzoHsz"
APP_KEY = "bErLivRY9osBC4PlrY93sv1I"
MASTER_KEY = "mPDiCfM9EvKbkPSm3T3myHcQ"
PORT = 8080

leancloud.init(APP_ID, app_key=APP_KEY, master_key=MASTER_KEY)
# 如果需要使用 master key 权限访问 LeanCLoud 服务，请将这里设置为 True
leancloud.use_master_key(False)

application = engine


if __name__ == '__main__':
    # 只在本地开发环境执行的代码
    from gevent.pywsgi import WSGIServer
    from werkzeug.serving import run_with_reloader
    from werkzeug.debug import DebuggedApplication

    @run_with_reloader
    def run():
        global application
        app.debug = True
        application = DebuggedApplication(application, evalex=True)
        server = WSGIServer(('0.0.0.0', PORT), application)
        server.serve_forever()

    run()
