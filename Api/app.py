#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao

@Contact :   qyzhg@163.com

@File    :   main.py

@Time    :   2020/6/11 8:43 上午
'''

import os
import sys
import csv

try:
    from flask import Flask, request, render_template, redirect, url_for
except ImportError:
    os.system('pip install flask')
    from flask import Flask, request, render_template, redirect, url_for
# sys.path.append(os.path.abspath('../'))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Api.getyaml.json_to_yaml import json_to_yaml, make_locustfile, make_apifile
from Api.public.WriteJson import write_json
from Api.public.start import start_project
from Api.settings import BASE_DIR,CASE_DIR, HOST, PROJECT_NAME,EMAIL_ADDRESS
from Api.public.msg import Msg
from Api.public.create_script import create_script
from Api.public.RunTest import Runtest,runLOCUST
from Api.public.update import Update
from concurrent.futures import ThreadPoolExecutor


executor = ThreadPoolExecutor(2)
app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR,'templates'),
            static_folder=os.path.join(BASE_DIR,'static')
            )


@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html', PROJECT_NAME=PROJECT_NAME)
    elif request.method == 'POST':
        # 获取表单内容
        url = request.form.get('url')
        if HOST in url:
            url = url.split(HOST)[1]
        meth = request.form.get('meth')
        name = request.form.get('name')
        if request.form.get('isauto'):  # 判断是否勾选自动填写
            name = (url + '_' + meth.upper()).replace('/', '_').replace('-', '_')
        remark = request.form.get('remark')
        json_data = request.form.get('json_data')
        menu = request.form.get('menu')
        if name == '':
            context = Msg([{'2': '如果未现在自动生成接口名为必填项'}])
            return render_template('index.html', **context, PROJECT_NAME=PROJECT_NAME)
        elif url == '':
            context = Msg([{'2': '接口地址为必填项'}])
            return render_template('index.html', **context, PROJECT_NAME=PROJECT_NAME)
        elif remark == '':
            context = Msg([{'2': '备注为必填项'}])
            return render_template('index.html', **context, PROJECT_NAME=PROJECT_NAME)
        # 写入json文件
        write_json(json_data=json_data)
        # yaml输出路径
        case_path = os.path.join(CASE_DIR, name) + '.yaml'
        if os.path.isfile(case_path):
            # 已存在
            context = Msg([{'1': f'该测试用例已存在，如需再次生成请手动将{case_path}删除或者重命名后再操作'}])
            return render_template('index.html', **context, PROJECT_NAME=PROJECT_NAME)
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
                return render_template('index.html', **context, PROJECT_NAME=PROJECT_NAME)
            else:
                L.append(a)
                context = Msg(L)
                return render_template('index.html', **context, PROJECT_NAME=PROJECT_NAME)


@app.route('/start', methods=['POST', 'GET'])
def start():
    if request.method == 'GET':
        return render_template('start.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        if name == '':
            danger = ['请输入项目名!']
            return render_template('start.html', danger=danger)
        a = start_project(name)
        context = Msg(a)
        return render_template('start.html', **context)


@app.route('/cs', methods=['POST', 'GET'])
def cs():
    if request.method == 'GET':
        return render_template('cs.html', PROJECT_NAME=PROJECT_NAME)
    elif request.method == 'POST':
        menu = request.form.get('menu')
        a = create_script(PROJECT_NAME, menu)
        # print(a)
        context = Msg(a)
        return render_template('cs.html', PROJECT_NAME=PROJECT_NAME, **context)


@app.route('/runtest',methods=['POST','GET'])
def runtest():
    email_list = list()
    with open(EMAIL_ADDRESS, "r", encoding='utf-8') as f:
        csv_read = csv.reader(f)
        for line in csv_read:
            d = {
                'email': line[0],
                'name': line[1],
                'duty': line[2],
                'state': line[3]
            }
            email_list.append(d)
    if request.method == 'GET':
        return render_template('runtest.html',PROJECT_NAME = PROJECT_NAME,email_list=email_list[1:])

    elif request.method == 'POST':
        issend = request.form.get('issend')
        if issend:
            a = Runtest(True)
        else:
            a = Runtest()
        context = Msg(a)
        return render_template('runtest.html',PROJECT_NAME = PROJECT_NAME,email_list=email_list[1:],**context)


@app.route('/runlocust',methods=['POST','GET'])
def runlocust():
    if request.method == 'GET':
        return render_template('runlocust.html', PROJECT_NAME=PROJECT_NAME)
    elif request.method == 'POST':
        executor.submit(runlocust_task) #添加异步方法启动locust
        context = Msg([{'0': 'locust服务启动成功'},{'0': '请访问 http://127.0.0.1:8089/ 进行操作'}])
        return render_template('runlocust.html', PROJECT_NAME=PROJECT_NAME,**context)

def runlocust_task():
    runLOCUST()


@app.route('/update',methods=['POST','GET'])
def update():
    if request.method == 'GET':
        return render_template('update.html')
    elif request.method == 'POST':
        context = Msg(Update())
    return render_template('update.html',**context)


if __name__ == '__main__':
    app.run()
