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
leancloud.init(os.environ.get('LEANCLOUD_APP_ID'), os.environ.get('LEANCLOUD_APP_KEY'))

@app.route('/')
def index():
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

    return render_template('index.html', lang=yaml.load(transtable, Loader=yaml.FullLoader))

@app.route('/api/time')
def time():
    return str(datetime.now())

@app.route('/add')
def add_panel():
    render_template('add.html')

@app.route('/api/add', methods=['POST'])
def add_api():
    en, zh_CN, zh_TW, ja_JP = request.form.get('en'), request.form.get('zh_CN'), request.form.get('zh_TW'), request.form.get('ja_JP')
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
            return redirect('/?success')
        except Exception as e:
            print(e)
            return redirect('/?failed')
    else:
        return redirect('/?badtoken')

@app.route('/api/get')
def get_api():
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
        data = {
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
    return {'code': 500, 'msg': 'no announcement found', 'id': None, 'announcement': None}


@ app.route('/assets/<path:filename>')
def serve_static(filename):
    return send_from_directory('assets', filename)

# REST API example

@app.route('/api/python-version', methods=['GET'])
def python_version():
    return jsonify({"python-version": sys.version})
