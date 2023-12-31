# coding: utf-8
import sys
import os
import yaml
from datetime import datetime
from flask_babel import Babel
import leancloud
from flask import Flask, jsonify, request, redirect
from flask import render_template
from leancloud import LeanCloudError

app = Flask(__name__)
babel = Babel(app)
app.config['BABEL_LANGUAGES'] = ['en', 'zh-CN', 'zh-TW', 'ja-JP']
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
leancloud.init(os.environ.get('LEANCLOUD_APP_ID', '404'), os.environ.get('LEANCLOUD_APP_KEY', '404'))
previous = None
@app.route('/')
def index():
    global previous
    if request.args.get('lang'):
        if request.args.get('lang') in app.config['BABEL_LANGUAGES']:
            lang = request.args.get('lang')
        elif request.accept_languages.best_match(app.config['BABEL_LANGUAGES']):
            lang = str(request.accept_languages.best_match(
                app.config['BABEL_LANGUAGES']))
        else:
            lang = 'en'
    elif request.accept_languages.best_match(app.config['BABEL_LANGUAGES']):
        lang = str(request.accept_languages.best_match(
            app.config['BABEL_LANGUAGES']))
    else:
        lang = 'en'
    with open(f'lang/{lang}.yml', encoding='utf8') as f:
        transtable = f.read()
    if not previous:
        Announcement: leancloud.Object = leancloud.Object.extend('announcement')
        query = Announcement.query
        query.limit(1)  # 限制只获取一条数据
        query.descending('createdAt')  # 按照 createdAt 降序排列，即获取最新的一条数据
        query.not_equal_to('en', '')
        try:
            result = query.first()
            previous = {
            'code': 200,
            'msg': 'success',
            'id': result.id,
            'announcement': {
                'en': result.get('en'),
                'zh-CN': result.get('zh_CN'),
                'zh-TW': result.get('zh_TW'),
                'ja-JP': result.get('ja_JP')
                }
            }
        except LeanCloudError:
            pass
    return render_template('index.html', lang=yaml.load(transtable, Loader=yaml.FullLoader), prev_ann = previous)

@app.route('/api/time')
def time():
    return str(datetime.now())

@app.route('/add')
def add_panel():
    render_template('add.html')

@app.route('/api/add', methods=['POST'])
def add_api():
    global previous
    en, zh_CN, zh_TW, ja_JP = request.form.get('en'), request.form.get('zh_CN'), request.form.get('zh_TW'), request.form.get('ja_JP')
    if en == '' or zh_CN == '' or zh_TW == '' or ja_JP == '':
        Announcement: leancloud.Object = leancloud.Object.extend('announcement')
        query = Announcement.query
        query.limit(1)  # 限制只获取一条数据
        query.descending('createdAt')  # 按照 createdAt 降序排列，即获取最新的一条数据
        query.not_equal_to('en', '')
        try:
            no_previous_ann = False
            result = query.first()
        except LeanCloudError:
            no_previous_ann = True
        if not no_previous_ann:
            if en == '':
                en = result.get('en')
            if zh_CN == '':
                zh_CN = result.get('zh_CN')
            if zh_TW == '':
                zh_TW = result.get('zh_TW')
            if ja_JP == '':
                ja_JP = result.get('ja_JP')
    token = request.form.get('token')
    if token == os.environ.get('TOKEN', 'VAMS'):
        try:
            Announcement = leancloud.Object.extend('announcement')
            announcement = Announcement()
            announcement.set('en', en)
            announcement.set('zh_CN', zh_CN)
            announcement.set('zh_TW', zh_TW)
            announcement.set('ja_JP', ja_JP)
            announcement.save()
            Announcement: leancloud.Object = leancloud.Object.extend('announcement')
            query = Announcement.query
            query.limit(1)  # 限制只获取一条数据
            query.descending('createdAt')  # 按照 createdAt 降序排列，即获取最新的一条数据
            query.not_equal_to('en', '')
            result = query.first()
            previous = {
                'code': 200,
                'msg': 'success',
                'id': result.id,
                'announcement': {
                    'en': result.get('en'),
                    'zh-CN': result.get('zh_CN'),
                    'zh-TW': result.get('zh_TW'),
                    'ja-JP': result.get('ja_JP')
                }
            }        
            return redirect('/?success')
        except Exception as e:
            print(e)
            return redirect('/?failed')
    else:
        return redirect('/?badtoken')

@app.route('/api/get')
def get_api():
    global previous
    if not previous:
        Announcement: leancloud.Object = leancloud.Object.extend('announcement')
        query = Announcement.query
        query.limit(1)  # 限制只获取一条数据
        query.descending('createdAt')  # 按照 createdAt 降序排列，即获取最新的一条数据
        query.not_equal_to('en', '')
        try:
            result = query.first()
        except LeanCloudError:
            return {"code": 500, "msg": "no announcement found", "id": None, "announcement": None}
        if result:
            previous = data = {
                'code': 200,
                'msg': 'success',
                'id': result.id,
                'announcement': {
                    'en': result.get('en'),
                    'zh-CN': result.get('zh_CN'),
                    'zh-TW': result.get('zh_TW'),
                    'ja-JP': result.get('ja_JP')
                }
            }        
            return data
    else: 
        return previous
    return {'code': 500, 'msg': 'no announcement found', 'id': None, 'announcement': None}

@app.route('/api/noarchive')
def query_to_keep_unarchive():
    Announcement: leancloud.Object = leancloud.Object.extend('announcement')
    query = Announcement.query
    query.limit(1)  # 限制只获取一条数据
    query.descending('createdAt')  # 按照 createdAt 降序排列，即获取最新的一条数据
    query.not_equal_to('en', '')
    result = query.first()
    return "200"



@ app.route('/assets/<path:filename>')
def serve_static(filename):
    return send_from_directory('assets', filename)

# REST API example

@app.route('/api/python-version', methods=['GET'])
def python_version():
    return jsonify({"python-version": sys.version})

if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=0)
