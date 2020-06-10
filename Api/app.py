import os

from flask import Flask, request, render_template, redirect,url_for

from Api.getyaml.json_to_yaml import json_to_yaml, make_locustfile, make_apifile
from Api.public.WriteJson import write_json
from Api.public.start import start_project
from Api.settings import CASE_DIR,HOST,PROJECT_NAME
from Api.public.msg import Msg

app = Flask(__name__)



@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html',PROJECT_NAME = PROJECT_NAME)
    elif request.method == 'POST':
        # 获取表单内容
        url = request.form.get('url')
        if HOST in url:
            url = url.split(HOST)[1]
        meth = request.form.get('meth')
        name = request.form.get('name')
        if request.form.get('isauto'):  # 判断是否勾选自动填写
            name = (url + '_' + meth.upper()).replace('/', '_')
        remark = request.form.get('remark')
        json_data = request.form.get('json_data')
        menu = request.form.get('menu')

        if name == '':
            context = Msg([{'2': '如果未现在自动生成接口名为必填项'}])
            return render_template('index.html',**context,PROJECT_NAME = PROJECT_NAME)

        elif url == '':
            context = Msg([{'2':'接口地址为必填项'}])
            return render_template('index.html',**context,PROJECT_NAME = PROJECT_NAME)

        elif remark == '':
            context = Msg([{'2': '备注为必填项'}])
            return render_template('index.html',**context,PROJECT_NAME = PROJECT_NAME)
        # 写入json文件
        write_json(json_data=json_data)
        # yaml输出路径
        case_path = os.path.join(CASE_DIR, name) + '.yaml'
        if os.path.isfile(case_path):
            #已存在
            context = Msg([{'1': f'该测试用例已存在，如需再次生成请手动将{case_path}删除或者重命名后再操作'}])
            return render_template('index.html', **context,PROJECT_NAME = PROJECT_NAME)
        else:
            # 执行操作
            L = list()
            a = json_to_yaml(remark=remark,
                             name=name,
                             url=url,
                             meth=meth,
                             case_path=case_path)
            if '2' not in a.keys():
                L.append(a)
                if menu == '1':
                    b = make_locustfile(name=name, remark=remark)
                    c = make_apifile(name=name, remark=remark)
                    L.append(b)
                    L.append(c)
                if menu == '2':
                    b = make_locustfile(name=name, remark=remark)
                    L.append(b)
                if menu == '3':
                    c = make_apifile(name=name, remark=remark)
                    L.append(c)
                context = Msg(L)
                return render_template('index.html',**context,PROJECT_NAME = PROJECT_NAME)
            else:
                L.append(a)
                context = Msg(L)
                return render_template('index.html',**context,PROJECT_NAME = PROJECT_NAME)


@app.route('/start', methods=['POST', 'GET'])
def start():
    if request.method == 'GET':
        return render_template('start.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        a = start_project(name)
        context = Msg(a)
        return render_template('start.html',**context)