# -*- coding: utf-8 -*-

from gevent import monkey
monkey.patch_all()

import os

import leancloud

from app import app

APP_ID = os.environ['LEANCLOUD_APP_ID']
APP_KEY = os.environ['LEANCLOUD_APP_KEY']
MASTER_KEY = os.environ['LEANCLOUD_APP_MASTER_KEY']
PORT = int(os.environ.get('LEANCLOUD_APP_PORT', 443))
TOKEN = os.environ.get('TOKEN', 'HelloWorld')

leancloud.init(APP_ID, app_key=APP_KEY, master_key=MASTER_KEY)
# Set this to be True if you need to access LeanCloud services with Master Key.
leancloud.use_master_key(False)

# Uncomment the following line to redirect HTTP requests to HTTPS.
# app = leancloud.HttpsRedirectMiddleware(app)
application = app

if __name__ == '__main__':
    from gevent.pywsgi import WSGIServer
    from geventwebsocket.handler import WebSocketHandler

    env = os.environ['LEANCLOUD_APP_ENV']
    if env == 'production':
        Announcement = leancloud.Object.extend('announcement')
        query = Announcement.query
        query.limit(1)  # 限制只获取一条数据
        query.descending('createdAt')  # 按照 createdAt 降序排列，即获取最新的一条数据
        result = query.find()
        if not result:
            announcement = Announcement()
            announcement.set('en', 'When you see this message, it means that your Valora has successfully integrated the announcement system! The announcement system GitHub repository link: <u><a href="https://github.com/GamerNoTitle/Valora-Announcement">Valora-Announcement</a></u>')
            announcement.set('zh_CN', '当你看到这个提示，说明你的Valora已经成功接入了公告系统！公告系统Github仓库链接：<u><a href="https://github.com/GamerNoTitle/Valora-Announcement">Valora-Announcement</a></u>')
            announcement.set('zh_TW', '當你看到這個提示，說明你的 Valora 已經成功接入了公告系統！公告系統 Github 倉庫連結：<u><a href="https://github.com/GamerNoTitle/Valora-Announcement">Valora-Announcement</a></u>')
            announcement.set('ja_JP', 'このメッセージを見ると、Valora が公告システムを正常に統合したことを意味します！公告システムの GitHub リポジトリのリンク：<u><a href="https://github.com/GamerNoTitle/Valora-Announcement">Valora-Announcement</a></u>')
            announcement.save()

        server = WSGIServer(('0.0.0.0', PORT), application, log=None, handler_class=WebSocketHandler)
        server.serve_forever()
    else:
        from werkzeug.serving import run_with_reloader
        from werkzeug.debug import DebuggedApplication

        app.debug = True
        application = DebuggedApplication(application, evalex=True)
        address = 'localhost' if env == 'development' else '0.0.0.0'
        server = WSGIServer((address, PORT), application, handler_class=WebSocketHandler)
        run_with_reloader(server.serve_forever)
